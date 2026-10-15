"""
Genera docs/todos_los_diagramas.pdf: todos los diagramas que el capítulo 5 incluye
hoy, en el orden en que aparecen en el documento, uno por página (carta horizontal).

La lista sale de los \\includegraphics de chapters/*.tex, así que se mantiene al día
sola. Quedan fuera las capturas de pantalla de la interfaz (figures/mockups/) y los
logos. Los títulos son los pies de figura del documento.

Ejecutar desde la raíz del repositorio:
    python scripts/gen_todos_diagramas_pdf.py
"""
import re
import tempfile
from pathlib import Path

import fitz

from pdf_diagramas import construir

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "docs" / "todos_los_diagramas.pdf"

RE_IMG = re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}")
RE_CAP = re.compile(r"\\caption\{(.+?)\}", re.S)
EXCLUIR = ("figures/mockups/", "figures/logos/")


def limpiar(cap: str) -> str:
    cap = cap.replace("[autoría propia]", "")
    cap = re.sub(r"\\textit\{([^}]*)\}", r"\1", cap)
    cap = re.sub(r"\\texttt\{([^}]*)\}", r"\1", cap)
    cap = cap.replace("---", "—").replace("~", " ").replace("\\ ", " ")
    return re.sub(r"\s+", " ", cap).strip().rstrip(".")


def figuras() -> list[tuple[str, str]]:
    salida = []
    for tex in sorted((REPO / "chapters").glob("*.tex")):
        src = tex.read_text(encoding="utf-8")
        for m in RE_IMG.finditer(src):
            inicio = src.rfind("\n", 0, m.start()) + 1
            if src[inicio:m.start()].lstrip().startswith("%"):
                continue
            img = m.group(1)
            if img.startswith(EXCLUIR):
                continue
            c = RE_CAP.search(src[m.end():m.end() + 700])
            salida.append((img, limpiar(c.group(1)) if c else Path(img).name))
    return salida


def resolver(img: str, tmp: Path) -> Path:
    """Devuelve la ruta de una imagen raster; si la fuente es PDF, la rasteriza."""
    for ext in ("", ".png", ".jpg", ".pdf"):
        ruta = REPO / (img + ext)
        if ruta.is_file():
            break
    else:
        raise SystemExit(f"No existe el archivo de la figura: {img}")
    if ruta.suffix.lower() != ".pdf":
        return ruta
    png = tmp / (ruta.stem + ".png")
    fitz.open(ruta)[0].get_pixmap(dpi=250).save(png)
    return png


def main() -> None:
    lista = figuras()
    with tempfile.TemporaryDirectory() as t:
        diagramas = [(resolver(img, Path(t)), titulo) for img, titulo in lista]
        construir(
            salida=OUT,
            diagramas=diagramas,
            subtitulo="Diagramas del documento",
            titulo_pdf="Todos los diagramas — TT 2026-B066",
        )


if __name__ == "__main__":
    main()
