"""
Genera build/casos_uso.pdf: los seis diagramas de casos de uso del capítulo 5,
cada uno en una página completa en orientación horizontal (carta apaisada).

Alternativa a casos_uso.tex para cuando no hay una distribución de TeX instalada.
El resultado es equivalente: mismo contenido, mismo orden, mismo criterio de escalado.

Ejecutar desde la raíz del repositorio:
    python scripts/gen_casos_uso_pdf.py
"""
from pathlib import Path

from PIL import Image, ImageChops
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.units import cm
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

REPO = Path(__file__).resolve().parent.parent
FIGS = REPO / "figures" / "mermaid"
OUT = REPO / "build" / "casos_uso.pdf"

# (archivo de imagen, título de la página)
DIAGRAMAS = [
    ("cu_vision_general", "Visión general del sistema"),
    ("cu_paquete1", "Paquete 1 — Autenticación y gestión de usuarios"),
    ("cu_paquete2", "Paquete 2 — Gestión de experimentos y carga de video"),
    ("cu_paquete3", "Paquete 3 — Análisis conductual"),
    ("cu_paquete4", "Paquete 4 — Resultados y reportes"),
    ("cu_paquete5", "Paquete 5 — Dashboard, notificaciones y administración"),
]

AZUL_IPN = HexColor("#2F5496")
GRIS_REGLA = HexColor("#B4BCC6")
GRIS_TEXTO = HexColor("#6C7885")

PAGE_W, PAGE_H = landscape(letter)  # 792 x 612 pt

MARGEN_X = 1.5 * cm
MARGEN_SUP = 1.5 * cm
MARGEN_INF = 1.2 * cm

BANDA_ENCABEZADO = 16  # alto del encabezado más su regla
BANDA_PIE = 14         # franja reservada al pie; la imagen nunca la invade

# Las imágenes ya traen su propio título embebido ("Figura 5.4 - ..."), así que
# el nombre del diagrama va en el encabezado y no repetido sobre la imagen.


def marco(c: canvas.Canvas, titulo: str, pagina: int, total: int) -> None:
    """Encabezado, regla y pie. Se dibuja DESPUÉS de la imagen para que el
    fondo blanco del PNG no lo tape."""
    y = PAGE_H - MARGEN_SUP

    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(AZUL_IPN)
    c.drawString(MARGEN_X, y, "TT 2026-B066")

    ancho_tt = c.stringWidth("TT 2026-B066", "Helvetica-Bold", 8.5)
    c.setFont("Helvetica", 8.5)
    c.setFillColor(GRIS_TEXTO)
    c.drawString(MARGEN_X + ancho_tt + 5, y, "|  Diagramas de casos de uso")

    # Nombre del diagrama, alineado a la derecha
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(AZUL_IPN)
    c.drawRightString(PAGE_W - MARGEN_X, y, titulo)

    c.setStrokeColor(GRIS_REGLA)
    c.setLineWidth(0.5)
    c.line(MARGEN_X, y - 5, PAGE_W - MARGEN_X, y - 5)

    c.setFont("Helvetica", 8.5)
    c.setFillColor(GRIS_TEXTO)
    c.drawCentredString(PAGE_W / 2, MARGEN_INF, f"{pagina} / {total}")
    c.setFillColor(GRIS_REGLA)
    c.drawRightString(PAGE_W - MARGEN_X, MARGEN_INF, "ESCOM-IPN")


def recortar_margen_blanco(ruta: Path) -> Image.Image:
    """Recorta el margen blanco que PlantUML deja alrededor del diagrama.
    Gana entre 6 y 10 % de área útil según el diagrama."""
    img = Image.open(ruta).convert("RGB")
    fondo = Image.new("RGB", img.size, (255, 255, 255))
    caja = ImageChops.difference(img, fondo).getbbox()
    return img.crop(caja) if caja else img


def pagina_diagrama(c: canvas.Canvas, ruta: Path, titulo: str,
                    pagina: int, total: int) -> None:
    """Una página: la imagen ocupa todo el espacio entre encabezado y pie."""
    # Área disponible para la imagen
    tope = PAGE_H - MARGEN_SUP - BANDA_ENCABEZADO
    base = MARGEN_INF + BANDA_PIE
    disp_w = PAGE_W - 2 * MARGEN_X
    disp_h = tope - base

    img = recortar_margen_blanco(ruta)
    img_w, img_h = img.size

    # Escala al máximo respetando la proporción: manda la restricción más estricta.
    # Los diagramas muy alargados (p. ej. Paquete 2, 3.7:1) llenan el ancho y
    # dejan espacio vertical libre; es inevitable sin deformarlos.
    escala = min(disp_w / img_w, disp_h / img_h)
    final_w, final_h = img_w * escala, img_h * escala

    x = (PAGE_W - final_w) / 2
    y = base + (disp_h - final_h) / 2

    c.drawImage(ImageReader(img), x, y, width=final_w, height=final_h,
                preserveAspectRatio=True, anchor="c", mask="auto")

    # El marco va encima para que nada quede cubierto por el fondo del PNG
    marco(c, titulo, pagina, total)


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)

    faltantes = [n for n, _ in DIAGRAMAS if not (FIGS / f"{n}.png").exists()]
    if faltantes:
        raise SystemExit(f"Faltan imágenes en {FIGS}: {', '.join(faltantes)}")

    c = canvas.Canvas(str(OUT), pagesize=(PAGE_W, PAGE_H))
    c.setTitle("Diagramas de casos de uso — TT 2026-B066")
    c.setAuthor("Frausto Robles Ángel Ali · Rodríguez Verdín Sandoval Vanesa")
    c.setSubject("Prototipo de sistema web de análisis conductual del FST")

    total = len(DIAGRAMAS)
    for i, (nombre, titulo) in enumerate(DIAGRAMAS, start=1):
        ruta = FIGS / f"{nombre}.png"
        with Image.open(ruta) as img:
            w, h = img.size
        cw, ch = recortar_margen_blanco(ruta).size
        print(f"  [{i}/{total}] {nombre:20} {w}x{h} -> {cw}x{ch}  ({cw/ch:.2f}:1)  {titulo}")
        pagina_diagrama(c, ruta, titulo, i, total)
        c.showPage()

    c.save()
    print(f"\nListo: {OUT}  ({OUT.stat().st_size / 1024:.0f} KB, {total} páginas)")


if __name__ == "__main__":
    main()
