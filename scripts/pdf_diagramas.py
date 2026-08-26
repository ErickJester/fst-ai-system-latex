"""
Construcción de PDFs de diagramas a página completa, sin LaTeX.

Módulo compartido por gen_casos_uso_pdf.py y gen_diagramas_pdf.py. Define el
formato común: carta horizontal, un diagrama por página, encabezado con el
nombre del diagrama y pie con la numeración.
"""
from pathlib import Path

from PIL import Image, ImageChops
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.units import cm
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

AZUL_IPN = HexColor("#2F5496")
GRIS_REGLA = HexColor("#B4BCC6")
GRIS_TEXTO = HexColor("#6C7885")

PAGE_W, PAGE_H = landscape(letter)  # 792 x 612 pt

MARGEN_X = 1.5 * cm
MARGEN_SUP = 1.5 * cm
MARGEN_INF = 1.2 * cm

BANDA_ENCABEZADO = 16  # alto del encabezado más su regla
BANDA_PIE = 14         # franja reservada al pie; la imagen nunca la invade

DPI_MAXIMO = 300  # por encima de esto no se gana calidad visible y el PDF crece


def recortar_margen_blanco(ruta: Path) -> Image.Image:
    """Recorta el margen blanco que PlantUML y Mermaid dejan alrededor del
    diagrama. Gana entre 6 y 10 % de área útil según el diagrama."""
    img = Image.open(ruta).convert("RGB")
    fondo = Image.new("RGB", img.size, (255, 255, 255))
    caja = ImageChops.difference(img, fondo).getbbox()
    return img.crop(caja) if caja else img


def _ajustar_titulo(c: canvas.Canvas, titulo: str, disponible: float) -> tuple[str, float]:
    """Reduce el cuerpo del título hasta que quepa; si aun así no cabe, lo corta."""
    for cuerpo in (8.5, 8.0, 7.5, 7.0):
        if c.stringWidth(titulo, "Helvetica-Bold", cuerpo) <= disponible:
            return titulo, cuerpo
    cuerpo = 7.0
    recortado = titulo
    while recortado and c.stringWidth(recortado + "…", "Helvetica-Bold", cuerpo) > disponible:
        recortado = recortado[:-1]
    return recortado + "…", cuerpo


def _marco(c: canvas.Canvas, subtitulo: str, titulo: str,
           pagina: int, total: int) -> None:
    """Encabezado, regla y pie. Se dibuja DESPUÉS de la imagen para que el
    fondo blanco del PNG no lo tape."""
    y = PAGE_H - MARGEN_SUP

    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(AZUL_IPN)
    c.drawString(MARGEN_X, y, "TT 2026-B066")

    ancho_tt = c.stringWidth("TT 2026-B066", "Helvetica-Bold", 8.5)
    c.setFont("Helvetica", 8.5)
    c.setFillColor(GRIS_TEXTO)
    c.drawString(MARGEN_X + ancho_tt + 5, y, f"|  {subtitulo}")

    # Nombre del diagrama, alineado a la derecha y sin invadir el texto izquierdo
    ocupado = MARGEN_X + ancho_tt + 5 + c.stringWidth(f"|  {subtitulo}", "Helvetica", 8.5)
    disponible = (PAGE_W - MARGEN_X) - ocupado - 18
    texto, cuerpo = _ajustar_titulo(c, titulo, disponible)
    c.setFont("Helvetica-Bold", cuerpo)
    c.setFillColor(AZUL_IPN)
    c.drawRightString(PAGE_W - MARGEN_X, y, texto)

    c.setStrokeColor(GRIS_REGLA)
    c.setLineWidth(0.5)
    c.line(MARGEN_X, y - 5, PAGE_W - MARGEN_X, y - 5)

    c.setFont("Helvetica", 8.5)
    c.setFillColor(GRIS_TEXTO)
    c.drawCentredString(PAGE_W / 2, MARGEN_INF, f"{pagina} / {total}")
    c.setFillColor(GRIS_REGLA)
    c.drawRightString(PAGE_W - MARGEN_X, MARGEN_INF, "ESCOM-IPN")


def _pagina(c: canvas.Canvas, ruta: Path, subtitulo: str, titulo: str,
            pagina: int, total: int) -> tuple[float, float]:
    """Dibuja una página. Devuelve el porcentaje de ancho y alto que ocupa
    la imagen, para poder verificar el resultado."""
    tope = PAGE_H - MARGEN_SUP - BANDA_ENCABEZADO
    base = MARGEN_INF + BANDA_PIE
    disp_w = PAGE_W - 2 * MARGEN_X
    disp_h = tope - base

    img = recortar_margen_blanco(ruta)
    img_w, img_h = img.size

    # Escala al máximo respetando la proporción: manda la restricción más
    # estricta. Un diagrama muy alargado llena el ancho y deja espacio
    # vertical libre; es inevitable sin deformarlo.
    escala = min(disp_w / img_w, disp_h / img_h)
    final_w, final_h = img_w * escala, img_h * escala

    # Reduce la resolución si excede DPI_MAXIMO: no aporta nitidez y engorda el PDF
    px_max = int(final_w / 72 * DPI_MAXIMO)
    if img_w > px_max:
        img = img.resize((px_max, int(img_h * px_max / img_w)), Image.LANCZOS)

    x = (PAGE_W - final_w) / 2
    y = base + (disp_h - final_h) / 2

    c.drawImage(ImageReader(img), x, y, width=final_w, height=final_h,
                preserveAspectRatio=True, anchor="c", mask="auto")

    _marco(c, subtitulo, titulo, pagina, total)
    return final_w / PAGE_W * 100, final_h / PAGE_H * 100


def construir(salida: Path, diagramas: list[tuple[Path, str]],
              subtitulo: str, titulo_pdf: str) -> None:
    """Genera el PDF. `diagramas` es una lista de (ruta de imagen, título)."""
    faltantes = [str(r) for r, _ in diagramas if not r.exists()]
    if faltantes:
        raise SystemExit("Faltan imágenes:\n  " + "\n  ".join(faltantes))

    salida.parent.mkdir(parents=True, exist_ok=True)

    c = canvas.Canvas(str(salida), pagesize=(PAGE_W, PAGE_H))
    c.setTitle(titulo_pdf)
    c.setAuthor("Frausto Robles Ángel Ali · Rodríguez Verdín Sandoval Vanesa")
    c.setSubject("Prototipo de sistema web de análisis conductual del FST")

    total = len(diagramas)
    for i, (ruta, titulo) in enumerate(diagramas, start=1):
        cob_w, cob_h = _pagina(c, ruta, subtitulo, titulo, i, total)
        aviso = "  <- proporción muy alargada" if min(cob_w, cob_h) < 40 else ""
        print(f"  [{i:2}/{total}] {ruta.stem:22} {cob_w:3.0f}% x {cob_h:3.0f}%  {titulo}{aviso}")
        c.showPage()

    c.save()
    kb = salida.stat().st_size / 1024
    print(f"\nListo: {salida}  ({kb:,.0f} KB, {total} páginas)")
