"""
Genera Reunion_Sandino_2026-09-03.pdf en la raíz del repositorio.

Material para la reunión de verificación con el Dr. Sandino: los dos diagramas
de base de datos (el conceptual entidad-relación y el grafo relacional final,
ya normalizado) y el guion para recorrerlos preguntando si el modelo coincide
con el protocolo real del laboratorio.

Carta horizontal. Los diagramas se dibujan en vectores, no se importan como
imagen, para que se vean nítidos en pantalla compartida y al imprimir.

Ejecutar desde la raíz del repositorio:
    python scripts/gen_reunion_pdf.py
"""
from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "Reunion_Sandino_2026-09-03.pdf"

PAGE_W, PAGE_H = landscape(letter)          # 792 x 612
M = 40                                       # margen
CONTENT_W = PAGE_W - 2 * M                   # 712

INK = HexColor("#0D1F21")
SOFT = HexColor("#3A4E4E")
MUTED = HexColor("#677978")
RULE = HexColor("#D3DBD8")
RULE_S = HexColor("#E8EDEB")
ACCENT = HexColor("#0F6F70")
ACCENT_D = HexColor("#DCEBEA")
WARN = HexColor("#A65D2E")
SURF = HexColor("#FFFFFF")

BODY = "Helvetica"
BOLD = "Helvetica-Bold"
ITAL = "Helvetica-Oblique"
DISP = "Times-Bold"
MONO = "Courier"


# ───────────────────────────── utilidades ─────────────────────────────

def wrap(text, font, size, width):
    """Parte `text` en las líneas que caben en `width`."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        probe = w if not cur else cur + " " + w
        if stringWidth(probe, font, size) <= width:
            cur = probe
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(c, text, x, y, width, font=BODY, size=8.5, leading=11.5, color=SOFT):
    """Dibuja un párrafo con salto de línea automático. Devuelve la y final."""
    c.setFont(font, size)
    c.setFillColor(color)
    for line in wrap(text, font, size, width):
        c.drawString(x, y, line)
        y -= leading
    return y


def page_header(c, kicker, title):
    c.setFont(MONO, 7)
    c.setFillColor(ACCENT)
    c.drawString(M, PAGE_H - M - 4, kicker.upper())

    c.setFont(DISP, 17)
    c.setFillColor(INK)
    c.drawString(M, PAGE_H - M - 26, title)

    c.setStrokeColor(INK)
    c.setLineWidth(1.1)
    c.line(M, PAGE_H - M - 36, PAGE_W - M, PAGE_H - M - 36)
    return PAGE_H - M - 54          # y donde empieza el contenido


def page_footer(c, n, total):
    c.setStrokeColor(RULE)
    c.setLineWidth(0.6)
    c.line(M, M - 8, PAGE_W - M, M - 8)
    c.setFont(MONO, 6.5)
    c.setFillColor(MUTED)
    c.drawString(M, M - 20, "TT 2026-B066  ·  ESCOM-IPN  ·  REUNION 3 SEP 2026")
    c.drawRightString(PAGE_W - M, M - 20, "%d / %d" % (n, total))


def box(c, x, y, w, h, label, fill=SURF, size=8):
    """Rectángulo de entidad, con `y` como borde superior."""
    c.setFillColor(fill)
    c.setStrokeColor(INK)
    c.setLineWidth(1.1)
    c.rect(x, y - h, w, h, stroke=1, fill=1)
    c.setFillColor(INK)
    c.setFont(BODY, size)
    c.drawCentredString(x + w / 2, y - h / 2 - size * 0.36, label)


def diamond(c, cx, cy, label, w=60, h=26, size=6.6):
    c.setFillColor(SURF)
    c.setStrokeColor(INK)
    c.setLineWidth(1.1)
    p = c.beginPath()
    p.moveTo(cx - w / 2, cy)
    p.lineTo(cx, cy + h / 2)
    p.lineTo(cx + w / 2, cy)
    p.lineTo(cx, cy - h / 2)
    p.close()
    c.drawPath(p, stroke=1, fill=1)
    c.setFillColor(INK)
    c.setFont(BODY, size)
    c.drawCentredString(cx, cy - size * 0.36, label)


def card(c, x, y, txt, size=5.8):
    """Etiqueta de cardinalidad (mín,máx)."""
    c.setFont(MONO, size)
    c.setFillColor(ACCENT)
    c.drawString(x, y, txt)


def seg(c, pts, width=1.0, color=INK, dash=None):
    c.setStrokeColor(color)
    c.setLineWidth(width)
    if dash:
        c.setDash(dash)
    p = c.beginPath()
    p.moveTo(*pts[0])
    for pt in pts[1:]:
        p.lineTo(*pt)
    c.drawPath(p)
    if dash:
        c.setDash([])


def arrow(c, pts, color=INK, width=1.0):
    """Polilínea con punta de flecha en el último punto."""
    seg(c, pts, width=width, color=color)
    (x0, y0), (x1, y1) = pts[-2], pts[-1]
    dx, dy = x1 - x0, y1 - y0
    n = (dx * dx + dy * dy) ** 0.5 or 1
    ux, uy = dx / n, dy / n
    px, py = -uy, ux
    s, wdt = 6.0, 2.6
    c.setFillColor(color)
    p = c.beginPath()
    p.moveTo(x1, y1)
    p.lineTo(x1 - ux * s + px * wdt, y1 - uy * s + py * wdt)
    p.lineTo(x1 - ux * s - px * wdt, y1 - uy * s - py * wdt)
    p.close()
    c.drawPath(p, stroke=0, fill=1)


def tabla(c, x, y, cols, rows, size=8, leading=10.5, pad=6, head_size=6.5):
    """Tabla simple. `cols` = [(ancho, encabezado), ...]. Devuelve y final."""
    total = sum(w for w, _ in cols)

    c.setFillColor(HexColor("#F2F5F4"))
    c.rect(x, y - 15, total, 15, stroke=0, fill=1)
    c.setFont(MONO, head_size)
    c.setFillColor(MUTED)
    cx = x
    for w, head in cols:
        c.drawString(cx + pad, y - 10.5, head.upper())
        cx += w
    c.setStrokeColor(RULE)
    c.setLineWidth(0.8)
    c.line(x, y - 15, x + total, y - 15)
    y -= 15

    for row in rows:
        wrapped, height = [], 0
        for (w, _), cell in zip(cols, row):
            font = BOLD if cell.startswith("*") else BODY
            text = cell[1:] if cell.startswith("*") else cell
            lines = wrap(text, font, size, w - 2 * pad)
            wrapped.append((font, lines))
            height = max(height, len(lines) * leading)
        height += 2 * pad

        cx = x
        for (w, _), (font, lines) in zip(cols, wrapped):
            ly = y - pad - size
            for line in lines:
                c.setFont(font, size)
                c.setFillColor(INK if font == BOLD else SOFT)
                c.drawString(cx + pad, ly, line)
                ly -= leading
            cx += w

        y -= height
        c.setStrokeColor(RULE_S)
        c.setLineWidth(0.6)
        c.line(x, y, x + total, y)

    return y


# ───────────────────────── página 1 · portada ─────────────────────────

def pagina_portada(c):
    y = PAGE_H - M - 60

    c.setFont(MONO, 7.5)
    c.setFillColor(ACCENT)
    c.drawString(M, y, "TT 2026-B066  ·  ESCOM-IPN  ·  3 DE SEPTIEMBRE DE 2026")

    c.setFont(DISP, 30)
    c.setFillColor(INK)
    c.drawString(M, y - 40, "Revisión del modelo de datos")
    c.setFont(DISP, 30)
    c.drawString(M, y - 74, "con el laboratorio")

    c.setFillColor(ACCENT)
    c.rect(M, y - 96, 70, 3, stroke=0, fill=1)

    yy = para(
        c,
        "El modelo de base de datos se rehízo por completo siguiendo la metodología de diseño en "
        "tres etapas. El propósito de esta sesión es recorrer los dos diagramas resultantes y "
        "confirmar, paso por paso, que la estructura corresponde al protocolo real del laboratorio.",
        M, y - 124, 430, size=9.5, leading=13.5, color=SOFT,
    )

    para(
        c,
        "No hace falta conocer notación de bases de datos para revisarlo: cada nivel del diagrama "
        "corresponde a algo concreto del experimento, y el guion de las páginas 3 y 5 traduce cada "
        "uno a una pregunta directa.",
        M, yy - 6, 430, size=9.5, leading=13.5, color=SOFT,
    )

    # ficha lateral
    bx, bw = M + 470, CONTENT_W - 470
    by = y - 6
    c.setStrokeColor(RULE)
    c.setLineWidth(0.8)
    c.setFillColor(HexColor("#F7F9F8"))
    c.rect(bx, by - 214, bw, 214, stroke=1, fill=1)

    ficha = [
        ("Laboratorio", "Bioquímica Estructural, Sección de Posgrado, ENMyH-IPN"),
        ("Investigador", "Dr. César Augusto Sandino Reyes López"),
        ("Directores", "Dr. Israel Salas Ramírez\nDra. Martha Rosa Cordero López"),
        ("Equipo", "Frausto Robles Á. A.\nRodríguez Verdín S. V."),
        ("Contenido", "2 diagramas · 14 puntos de verificación · 5 preguntas abiertas"),
    ]
    fy = by - 18
    for etiqueta, valor in ficha:
        c.setFont(MONO, 6)
        c.setFillColor(MUTED)
        c.drawString(bx + 12, fy, etiqueta.upper())
        fy -= 11
        for parte in valor.split("\n"):
            for line in wrap(parte, BODY, 8, bw - 24):
                c.setFont(BODY, 8)
                c.setFillColor(INK)
                c.drawString(bx + 12, fy, line)
                fy -= 10.5
        fy -= 8

    # índice
    iy = M + 120
    c.setStrokeColor(RULE)
    c.line(M, iy + 16, M + 430, iy + 16)
    indice = [
        ("2", "Diagrama entidad-relación (conceptual)"),
        ("3", "Guion para recorrerlo — 10 puntos de verificación"),
        ("4", "Grafo relacional final (normalizado)"),
        ("5", "Guion del esquema lógico — qué cambió y por qué"),
        ("6", "Lo que falta confirmar"),
    ]
    for num, txt in indice:
        c.setFont(MONO, 7.5)
        c.setFillColor(ACCENT)
        c.drawString(M, iy, num)
        c.setFont(BODY, 9)
        c.setFillColor(INK)
        c.drawString(M + 22, iy, txt)
        iy -= 15


# ─────────────────── página 2 · diagrama conceptual ───────────────────

def pagina_conceptual(c):
    page_header(c, "Etapa conceptual · resultado", "Diagrama entidad-relación")

    TOP = PAGE_H - M - 66

    def Y(v):
        return TOP - v

    EW, EH = 84, 30                       # entidad
    BX = [26, 218, 410, 602]              # cuatro columnas de entidades
    DX = [164, 356, 548]                  # rombos entre columnas contiguas
    T1, T2, T3, T4 = 0, 90, 252, 348      # borde superior de cada hilera

    def cx(i):
        return M + BX[i] + EW / 2

    def hrel(i, fila, nombre, c_izq, c_der):
        """Interrelación horizontal entre las columnas i e i+1 de una hilera."""
        y = Y(fila + EH / 2)
        x0, x1 = M + BX[i] + EW, M + DX[i] - 28
        x2, x3 = M + DX[i] + 28, M + BX[i + 1]
        seg(c, [(x0, y), (x1, y)])
        diamond(c, M + DX[i], y, nombre)
        seg(c, [(x2, y), (x3, y)])
        c.setFont(MONO, 5.5)
        c.setFillColor(ACCENT)
        c.drawCentredString((x0 + x1) / 2, y + 5, c_izq)
        c.drawCentredString((x2 + x3) / 2, y + 5, c_der)

    def vrel(x, y_arriba, y_abajo, nombre, c_sup, c_inf):
        """Interrelación vertical entre dos hileras."""
        cy = (Y(y_arriba) + Y(y_abajo)) / 2
        seg(c, [(x, Y(y_arriba)), (x, cy + 12)])
        diamond(c, x, cy, nombre)
        seg(c, [(x, cy - 12), (x, Y(y_abajo))])
        c.setFont(MONO, 5.5)
        c.setFillColor(ACCENT)
        c.drawString(x + 5, Y(y_arriba) - 11, c_sup)
        c.drawString(x + 5, Y(y_abajo) + 6, c_inf)

    def codo(x_desde, y_fila, x_hasta, y_codo, nombre, c_sup, c_inf, dx_dia):
        """Baja de una hilera, corre en horizontal con su rombo y baja a la siguiente."""
        yc = Y(y_codo)
        seg(c, [(x_desde, Y(y_fila + EH)), (x_desde, yc), (M + dx_dia + 28, yc)])
        diamond(c, M + dx_dia, yc, nombre)
        seg(c, [(M + dx_dia - 28, yc), (x_hasta, yc), (x_hasta, Y(T3))])
        c.setFont(MONO, 5.5)
        c.setFillColor(ACCENT)
        c.drawString(x_desde + 5, Y(y_fila + EH) - 11, c_sup)
        c.drawString(x_hasta + 5, Y(T3) + 6, c_inf)

    # ── hilera 1 ──
    box(c, M + BX[0], Y(T1), EW, EH, "Usuario")
    box(c, M + BX[1], Y(T1), EW, EH, "Experimento")
    box(c, M + BX[3], Y(T1), EW, EH, "Análisis")
    hrel(0, T1, "registra", "(0,N)", "(1,1)")

    # ── hilera 2 ──
    box(c, M + BX[1], Y(T2), EW, EH, "Grupo")
    box(c, M + BX[2], Y(T2), EW, EH, "Tanda")
    box(c, M + BX[3], Y(T2), EW, EH, "Video")
    hrel(1, T2, "se graba en", "(2,N)", "(1,1)")
    hrel(2, T2, "produce", "(1,2)", "(1,1)")

    # ── hilera 3 ──
    box(c, M + BX[1], Y(T3), EW, EH, "Espécimen")
    box(c, M + BX[2], Y(T3), EW, EH, "Observación", fill=ACCENT_D)
    box(c, M + BX[3], Y(T3), EW, EH, "Intervalo")
    hrel(1, T3, "aparece en", "(1,2)", "(1,1)")
    hrel(2, T3, "se divide en", "(5,5)", "(1,1)")

    # ── hilera 4 ──
    box(c, M + BX[3], Y(T4), EW, EH, "Conducta")

    # ── interrelaciones verticales ──
    vrel(cx(1), T1 + EH, T2, "compone", "(3,N)", "(1,1)")
    vrel(cx(3), T1 + EH, T2, "procesa", "(1,1)", "(1,N)")
    vrel(M + BX[1] + 22, T2 + EH, T3, "agrupa", "(6,8)", "(1,1)")
    vrel(cx(3), T3 + EH, T4, "presenta", "(2,3)", "(0,N)")

    # ── los dos codos que unen grabación y medición ──
    codo(M + BX[2] + 30, T2, M + BX[1] + 68, 218, "aloja", "(3,4)", "(1,1)", 363)
    codo(M + BX[3] + 58, T2, M + BX[2] + 60, 195, "contiene", "(3,4)", "(1,1)", 565)

    # ── atributo de la interrelación presenta ──
    cyp = (Y(T3 + EH) + Y(T4)) / 2
    seg(c, [(cx(3) - 28, cyp), (cx(3) - 56, cyp)], dash=[2, 2])
    c.setStrokeColor(INK)
    c.setFillColor(SURF)
    c.setLineWidth(1.1)
    c.ellipse(cx(3) - 120, cyp - 12, cx(3) - 56, cyp + 12, stroke=1, fill=1)
    c.setFont(ITAL, 7)
    c.setFillColor(INK)
    c.drawCentredString(cx(3) - 88, cyp - 2.5, "segundos")

    # ── leyenda ──
    ly = M + 44
    c.setStrokeColor(RULE)
    c.setLineWidth(0.6)
    c.line(M, ly + 14, PAGE_W - M, ly + 14)
    leyenda = [
        "Rectángulo = entidad",
        "Rombo = interrelación",
        "Óvalo = atributo de la interrelación",
        "(mín,máx) = cardinalidad",
        "Sombreado = entidad asociativa",
    ]
    lx = M
    for item in leyenda:
        c.setFont(MONO, 6.5)
        c.setFillColor(MUTED)
        c.drawString(lx, ly, item)
        lx += stringWidth(item, MONO, 6.5) + 20

    para(
        c,
        "Las diez entidades son fuertes: ninguna necesita a otra para identificarse. Las dos hileras "
        "de arriba llevan la logística de grabación —el estudio, los grupos, las grabaciones, los "
        "videos y sus análisis—; la de abajo lleva la medición —la rata, su aparición en un video, el "
        "minuto y la conducta—. Las dos ramas se reencuentran en Observación.",
        M, ly - 14, CONTENT_W, size=7.5, leading=10, color=SOFT,
    )


# ────────────────── página 3 · guion del conceptual ──────────────────

def pagina_guion_conceptual(c):
    y = page_header(c, "Guion · página 2", "Cómo recorrer el diagrama, nivel por nivel")

    y = para(
        c,
        "Cada renglón es un nivel del diagrama. La columna del centro se dice en voz alta; la de la "
        "derecha es lo que hay que confirmar con el laboratorio. Si algo no coincide con el protocolo "
        "real, es exactamente lo que se busca en esta sesión.",
        M, y, 560, size=8.5, leading=11.5,
    ) - 10

    cols = [(96, "Nivel"), (300, "Lo que dice el diagrama"), (316, "Lo que hay que confirmar")]
    rows = [
        ["*Experimento",
         "Un estudio completo: alrededor de cuatro grupos, entre 32 y 48 ratas y unos ocho videos del Día 2.",
         "¿Es así como ustedes llaman «experimento»? Antes lo teníamos modelado como una sola grabación."],
        ["*Grupo",
         "Cada estudio se divide en tres o más grupos: control, referencia con fluoxetina y tratamiento experimental.",
         "¿Siempre son mínimo tres? ¿Puede haber dos grupos de tratamiento en el mismo estudio?"],
        ["*Tanda",
         "Como en el encuadre caben máximo cuatro cilindros, un grupo de seis a ocho ratas se graba en dos veces.",
         "¿Cómo le dicen ustedes a ese conjunto de ratas que se graban juntas? «Tanda» es un nombre que pusimos nosotros."],
        ["*Espécimen",
         "Cada rata pertenece a un grupo —eso dice qué tratamiento recibió— y aparece en una grabación —eso dice en qué video sale.",
         "¿Una misma grabación puede mezclar ratas de dos grupos distintos, o siempre son del mismo?"],
        ["*Identidad de la rata",
         "Cada rata tiene un identificador propio, además del cilindro que ocupa en el encuadre.",
         "¿Con qué la identifican: arete, número de jaula, marca, código de bitácora? ¿Es único en todo el laboratorio o solo dentro de un estudio?"],
        ["*Cilindro",
         "El número de cilindro cuelga de la rata: es el puesto que le tocó dentro del encuadre.",
         "¿La misma rata vuelve al mismo cilindro el Día 2, o se reacomodan?"],
        ["*Video",
         "Cada grabación produce uno o dos videos: el del Día 1, de veinte minutos, y el del Día 2, de cinco.",
         "¿Siempre se graban los dos días? Del Día 1 entendimos que solo se analizan los primeros cinco minutos del grupo control."],
        ["*Análisis",
         "Un mismo video puede analizarse más de una vez.",
         "Si se vuelve a analizar y da un resultado distinto, ¿prefiere conservar los dos para compararlos, o que el nuevo reemplace al anterior?"],
        ["*Observación",
         "Es la aparición de una rata concreta en un video concreto. De ahí cuelga todo lo que se mide.",
         "Confirmar que la unidad de análisis es siempre «una rata en un video», y no el video completo."],
        ["*Intervalo y conducta",
         "Cada observación se divide en los cinco minutos, y en cada minuto se reparten los segundos entre las tres conductas.",
         "¿El desglose por minuto es lo que necesitan, en segundos? ¿La suma de las tres conductas debe dar siempre sesenta segundos?"],
    ]
    tabla(c, M, y, cols, rows, size=7.6, leading=9.6, pad=5)


# ─────────────────── página 4 · grafo relacional ───────────────────

def pagina_logico(c):
    page_header(c, "Etapa lógica · resultado final", "Grafo relacional, ya normalizado")

    TOP = PAGE_H - M - 66

    def Y(v):
        return TOP - v

    BW = 120
    COL = {0: 0, 1: 148, 2: 296, 3: 444, 4: 592}

    tablas = {
        "USUARIO":     (0, 6,   [("idBoleta", "pk"), ("nombre", ""), ("apellidos", ""),
                                 ("correo", ""), ("contrasena", "")]),
        "EXPERIMENTO": (0, 92,  [("idExperimento", "pk"), ("idBoleta", "fk"), ("nombre", ""),
                                 ("fecha", ""), ("notas", "")]),
        "GRUPO":       (0, 178, [("idGrupo", "pk"), ("idExperimento", "fk"), ("etiqueta", ""),
                                 ("tipo", ""), ("tratamiento", "")]),
        "TANDA":       (1, 178, [("idTanda", "pk"), ("idGrupo", "fk"), ("ordinal", ""),
                                 ("nCilindros", "")]),
        "VIDEO":       (2, 80,  [("idVideo", "pk"), ("idTanda", "fk"), ("sesion", ""),
                                 ("archivo", ""), ("duracion", ""), ("fechaCarga", "")]),
        "ESPECIMEN":   (2, 224, [("idEspecimen", "pk"), ("idTanda", "fk"),
                                 ("idLaboratorio", ""), ("numeroCilindro", "")]),
        "ANALISIS":    (3, 70,  [("idAnalisis", "pk"), ("idVideo", "fk"), ("estado", ""),
                                 ("etapa", ""), ("confianza", ""), ("nivelClasif", ""),
                                 ("fechaAnalisis", "")]),
        "OBSERVACION": (3, 216, [("idObservacion", "pk"), ("idEspecimen", "fk"), ("idVideo", "fk")]),
        "INTERVALO":   (4, 216, [("idIntervalo", "pk"), ("idObservacion", "fk"), ("minuto", "")]),
        "PRESENTA":    (4, 292, [("idIntervalo", "pkfk"), ("conducta", "pkfk"), ("segundos", "")]),
        "CONDUCTA":    (4, 368, [("nombre", "pk")]),
    }

    geo = {}
    for nombre, (col, top, attrs) in tablas.items():
        x = M + COL[col]
        h = 14 + len(attrs) * 9.6 + 5
        yt = Y(top)
        geo[nombre] = (x, yt, BW, h)

        c.setFillColor(SURF)
        c.setStrokeColor(INK)
        c.setLineWidth(1.1)
        c.rect(x, yt - h, BW, h, stroke=1, fill=1)

        c.setFillColor(HexColor("#F2F5F4"))
        c.rect(x, yt - 14, BW, 14, stroke=0, fill=1)
        c.setStrokeColor(INK)
        c.setLineWidth(1.1)
        c.line(x, yt - 14, x + BW, yt - 14)
        c.setFont(BOLD, 7.2)
        c.setFillColor(INK)
        c.drawString(x + 5, yt - 10, nombre)

        ay = yt - 23
        for attr, tipo in attrs:
            c.setFont(MONO, 6.4)
            c.setFillColor(ACCENT if "fk" in tipo else INK)
            c.drawString(x + 5, ay, attr)
            if "pk" in tipo:
                c.setStrokeColor(INK)
                c.setLineWidth(0.6)
                w = stringWidth(attr, MONO, 6.4)
                c.line(x + 5, ay - 1.6, x + 5 + w, ay - 1.6)
            ay -= 9.6

    def right(n):
        x, y, w, h = geo[n]
        return x + w, y - h / 2

    def left(n):
        x, y, w, h = geo[n]
        return x, y - h / 2

    def bottom(n, frac=0.5):
        x, y, w, h = geo[n]
        return x + w * frac, y - h

    def top_of(n, frac=0.5):
        x, y, w, h = geo[n]
        return x + w * frac, y

    # llaves foráneas: la flecha apunta a la relación referenciada.
    # Todo el ruteo es ortogonal y por fuera de las cajas.
    arrow(c, [top_of("EXPERIMENTO"), bottom("USUARIO")])
    arrow(c, [top_of("GRUPO"), bottom("EXPERIMENTO")])
    arrow(c, [left("TANDA"), (geo["GRUPO"][0] + BW, left("TANDA")[1])])

    xv, yv = left("VIDEO")
    arrow(c, [(xv, yv), (geo["TANDA"][0] + 90, yv), (geo["TANDA"][0] + 90, geo["TANDA"][1])])

    xe, ye = left("ESPECIMEN")
    arrow(c, [(xe, ye), (geo["TANDA"][0] + 30, ye),
              (geo["TANDA"][0] + 30, geo["TANDA"][1] - geo["TANDA"][3])])

    arrow(c, [left("ANALISIS"), (geo["VIDEO"][0] + BW, left("ANALISIS")[1])])
    arrow(c, [left("OBSERVACION"), (geo["ESPECIMEN"][0] + BW, left("OBSERVACION")[1])])

    xo, yo = top_of("OBSERVACION", 0.78)
    arrow(c, [(xo, yo), (xo, yo + 26), (geo["VIDEO"][0] + 90, yo + 26),
              (geo["VIDEO"][0] + 90, geo["VIDEO"][1] - geo["VIDEO"][3])])

    arrow(c, [left("INTERVALO"), (geo["OBSERVACION"][0] + BW, left("INTERVALO")[1])])
    arrow(c, [top_of("PRESENTA"), bottom("INTERVALO")])
    arrow(c, [bottom("PRESENTA"), top_of("CONDUCTA")])

    # leyenda
    ly = M + 44
    c.setStrokeColor(RULE)
    c.setLineWidth(0.6)
    c.line(M, ly + 14, PAGE_W - M, ly + 14)
    lx = M
    for item in ["Subrayado = llave primaria", "Color = llave foránea",
                 "Flecha = apunta a la tabla referenciada",
                 "11 relaciones · 11 llaves foráneas · forma normal de Boyce-Codd"]:
        c.setFont(MONO, 6.5)
        c.setFillColor(MUTED)
        c.drawString(lx, ly, item)
        lx += stringWidth(item, MONO, 6.5) + 22

    para(
        c,
        "Es el mismo modelo de la página 2, ya convertido a tablas y validado con las formas normales. "
        "Cada tabla tiene una llave de una sola columna, salvo PRESENTA, que lleva las dos de sus "
        "participantes. Todas las referencias entre tablas son de una columna.",
        M, ly - 14, CONTENT_W, size=7.5, leading=10, color=SOFT,
    )


# ──────────────────── página 5 · guion del lógico ────────────────────

def pagina_guion_logico(c):
    y = page_header(c, "Guion · página 4", "Qué se ve en el grafo y qué cambió al validarlo")

    y = para(
        c,
        "Este diagrama no aporta información nueva sobre el protocolo: es el de la página 2 traducido "
        "a tablas. Lo que sí conviene explicar es qué encontró la validación, porque el esquema "
        "definitivo no quedó igual al que salió de la conversión.",
        M, y, 560, size=8.5, leading=11.5,
    ) - 10

    c.setFont(BOLD, 9)
    c.setFillColor(INK)
    c.drawString(M, y, "Cómo se lee")
    y -= 14

    cols = [(150, "Punto"), (562, "Qué decir")]
    rows = [
        ["*Una tabla por entidad",
         "Las diez entidades del diagrama anterior se volvieron diez tablas, más una undécima para la relación entre intervalo y conducta, que es la que guarda los segundos."],
        ["*El único dato medido",
         "Todo el sistema mide una sola cosa: los segundos que una rata dedicó a una conducta en un minuto. Está en la última tabla, PRESENTA. Las otras cuarenta y tantas columnas existen para ubicar ese dato."],
        ["*Las flechas",
         "Cada flecha dice «esta tabla se apoya en aquella». Se sigue la cadena hacia atrás y se llega del dato medido hasta el estudio completo."],
    ]
    y = tabla(c, M, y, cols, rows, size=7.8, leading=9.8, pad=5) - 18

    c.setFont(BOLD, 9)
    c.setFillColor(INK)
    c.drawString(M, y, "Los tres defectos que encontró la validación")
    y -= 14

    cols2 = [(90, "Dónde"), (300, "Qué estaba mal"), (322, "Cómo quedó")]
    rows2 = [
        ["*Usuario",
         "El nombre completo guardaba dos datos en una sola columna: nombre de pila y apellidos.",
         "Se partió en dos columnas. Es lo que permite ordenar y buscar personal por apellido."],
        ["*Espécimen",
         "Se guardaba el grupo de la rata además de su grabación. Como una grabación pertenece a un solo grupo, el dato estaba dos veces y las dos copias podían contradecirse.",
         "Se eliminó la columna duplicada. El grupo de una rata se obtiene a través de su grabación. Esto depende de que una grabación no mezcle grupos: es la pregunta P-04."],
        ["*Video",
         "La duración se guardaba como el valor nominal de la sesión: veinte minutos el Día 1, cinco el Día 2. Ese dato se repetía idéntico en todas las filas.",
         "Ahora se guarda la duración real del archivo. Sirve además para detectar que alguien subió el video del Día 1 marcándolo como Día 2."],
    ]
    tabla(c, M, y, cols2, rows2, size=7.6, leading=9.6, pad=5)


# ──────────────────── página 6 · preguntas abiertas ────────────────────

def pagina_preguntas(c):
    y = page_header(c, "Cierre", "Lo que falta confirmar")

    y = para(
        c,
        "Cinco puntos que no se pueden cerrar sin el laboratorio, ordenados por lo que cambian en el "
        "modelo. Los tres primeros modifican la estructura; los dos últimos, la planeación.",
        M, y, 560, size=8.5, leading=11.5,
    ) - 12

    preguntas = [
        ("P-03", "¿Con qué se identifica físicamente a cada rata: arete, número de jaula, marca, código?",
         "Es el único dato del diccionario que sigue declarado como «por confirmar». Falta saber también si ese identificador es único en todo el laboratorio o solo dentro de un estudio."),
        ("P-04", "¿Una misma grabación puede mezclar ratas de dos grupos distintos?",
         "Sostiene la corrección de la página 5: si una grabación no mezcla grupos, el grupo de una rata se deduce de su grabación. Si pudiera mezclar, hay que rehacer esa parte."),
        ("P-02", "¿La misma rata vuelve al mismo cilindro el Día 2, o se reacomodan?",
         "Decide si el número de cilindro se queda colgando de la rata o se mueve a cada aparición en video."),
        ("P-05", "¿Cómo le dicen ustedes al conjunto de ratas que se graban juntas?",
         "«Tanda» es un nombre provisional que pusimos nosotros. Va a aparecer en el documento escrito, en el diagrama y en la interfaz del sistema."),
        ("P-08", "Si un video se reanaliza y da un resultado distinto, ¿se conservan los dos o se reemplaza?",
         "Conservar los dos permitiría medir la repetibilidad del sistema, que es el criterio que usted puso por encima de la velocidad."),
    ]

    for ref, pregunta, nota in preguntas:
        c.setFont(MONO, 7)
        c.setFillColor(ACCENT)
        c.drawString(M, y, ref)
        c.setFont(BOLD, 9.5)
        c.setFillColor(INK)
        for line in wrap(pregunta, BOLD, 9.5, 600):
            c.drawString(M + 44, y, line)
            y -= 12
        y = para(c, nota, M + 44, y - 1, 600, size=7.8, leading=10, color=MUTED) - 4

        c.setStrokeColor(RULE_S)
        c.setLineWidth(0.6)
        c.line(M + 44, y, PAGE_W - M, y)
        y -= 16

    # compromisos del laboratorio
    y -= 4
    c.setStrokeColor(ACCENT)
    c.setLineWidth(2)
    c.line(M, y + 12, M, y - 34)
    c.setFont(BOLD, 9)
    c.setFillColor(INK)
    c.drawString(M + 10, y + 2, "Antes de terminar, recordar los dos entregables pendientes")
    para(
        c,
        "Los archivos de Excel con los análisis manuales de los videos ya compartidos —que servirán "
        "como conjunto de prueba, no para entrenar— y la guía de cómo identificar las conductas.",
        M + 10, y - 12, 600, size=8, leading=10.5,
    )


# ────────────────────────────── ensamble ──────────────────────────────

def main():
    c = canvas.Canvas(str(OUT), pagesize=landscape(letter))
    c.setTitle("Revisión del modelo de datos con el laboratorio — TT 2026-B066")
    c.setAuthor("Frausto Robles Á. A. · Rodríguez Verdín S. V.")

    paginas = [
        pagina_portada,
        pagina_conceptual,
        pagina_guion_conceptual,
        pagina_logico,
        pagina_guion_logico,
        pagina_preguntas,
    ]
    total = len(paginas)
    for n, dibujar in enumerate(paginas, start=1):
        dibujar(c)
        page_footer(c, n, total)
        c.showPage()

    c.save()
    print("Generado: %s" % OUT)


if __name__ == "__main__":
    main()
