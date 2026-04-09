"""
Convierte bloques mermaid a PNG y actualiza el .tex.
Preserva caption y label originales de cada figura.
Usa mermaid.ink para la mayoría; kroki.io como fallback.
"""
import re
import zlib
import base64
import time
import requests
from pathlib import Path
from mermaid import Mermaid

TEX_FILE = Path(__file__).parent / "chapters" / "05_diseno.tex"
OUT_DIR  = Path(__file__).parent / "figures" / "mermaid"
OUT_DIR.mkdir(parents=True, exist_ok=True)

def render_mermaid_ink(code: str, out: Path) -> bool:
    try:
        d = Mermaid(code, width=1200)
        if d.img_response.status_code == 200:
            d.to_png(out)
            return True
        return False
    except Exception:
        return False

def render_kroki(code: str, out: Path) -> bool:
    compressed = zlib.compress(code.encode("utf-8"), 9)
    encoded = base64.urlsafe_b64encode(compressed).decode("ascii")
    url = f"https://kroki.io/mermaid/png/{encoded}"
    try:
        r = requests.get(url, timeout=30)
        if r.status_code == 200:
            out.write_bytes(r.content)
            return True
        return False
    except Exception:
        return False

def render(code: str, out: Path) -> bool:
    if render_mermaid_ink(code, out):
        return True
    time.sleep(2)
    return render_kroki(code, out)

# Parse y replace
text = TEX_FILE.read_text(encoding="utf-8")

FIGURE_RE = re.compile(
    r"\\begin\{figure\}(\[[^\]]*\])?"
    r"((?:(?!\\end\{figure\}|\\begin\{mermaid\}).)*)"
    r"\\begin\{mermaid\}(.*?)\\end\{mermaid\}"
    r"((?:(?!\\end\{figure\}).)*)"
    r"\\end\{figure\}",
    re.DOTALL,
)

matches = list(FIGURE_RE.finditer(text))
print(f"Found {len(matches)} mermaid figures.\n")

result = text

for m in matches:
    opts         = m.group(1) or "[ht]"
    before       = m.group(2)
    diagram_code = m.group(3).strip()
    after        = m.group(4)

    label_match = re.search(r"\\label\{(fig:[^}]+)\}", after)
    if not label_match:
        print(f"  WARNING: no label found, skipping")
        continue

    label    = label_match.group(1)
    name     = label.replace("fig:", "")
    png_path = OUT_DIR / f"{name}.png"
    rel_path = f"figures/mermaid/{name}"

    print(f"  Rendering {label} ...", end=" ", flush=True)
    ok = render(diagram_code, png_path)
    if ok:
        print("OK")
    else:
        print("FAILED")
        continue

    new_block = (
        f"\\begin{{figure}}{opts}\n"
        f"\\centering\n"
        f"\\includegraphics[width=\\textwidth]{{{rel_path}}}\n"
        f"{after.strip()}\n"
        f"\\end{{figure}}"
    )

    original = m.group(0)
    result = result.replace(original, new_block, 1)

TEX_FILE.write_text(result, encoding="utf-8")
print(f"\nDone. Updated: {TEX_FILE}")
print(f"PNGs saved in: {OUT_DIR}")
