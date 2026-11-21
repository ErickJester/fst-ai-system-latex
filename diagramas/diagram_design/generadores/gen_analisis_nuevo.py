"""Estados del análisis y flujo (pipeline) del análisis, rediseñados en HTML/SVG.
Fuente de verdad: diagramas/estados_analisis.puml y diagramas/pipeline.puml (y los cap. 5 y 6).
Uso: gen_analisis_nuevo.py estados salida.html | pipeline salida.html
"""
import html, sys, os
DIAPO = os.environ.get('DIAPO') == '1'
KX, KY, F = (1.32, 1.17, 1.3) if DIAPO else (1, 1, 1)
PITCH = 16 * F

esc = html.escape
FONT = '''<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;600&family=Geist+Mono:wght@400&display=swap" rel="stylesheet">'''
CSS = f'''
.t{{font:600 {15*F:.1f}px Geist,'Segoe UI',sans-serif;fill:#1a1a1a}}
.b{{font:400 {12.5*F:.1f}px Geist,'Segoe UI',sans-serif;fill:#3a3a3a}}
.l{{font:400 {12.5*F:.1f}px Geist,'Segoe UI',sans-serif;fill:#1a1a1a}}
.tag{{font:400 {11*F:.1f}px 'Geist Mono',monospace;fill:#6b6b6b;letter-spacing:.08em}}
.mod{{font:600 {17*F:.1f}px Geist,'Segoe UI',sans-serif;fill:#1a1a1a}}
.lg text{{font:400 {12*F:.1f}px 'Geist Mono',monospace;fill:#6b6b6b}}
'''
INK, MUTE, PAPER = '#1a1a1a', '#6b6b6b', '#faf9f5'


def pagina(titulo, desc, W, H, cuerpo, marker):
    svg = f'''<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="t1 d1" xmlns="http://www.w3.org/2000/svg">
<title id="t1">{esc(titulo)}</title><desc id="d1">{esc(desc)}</desc>
<defs><marker id="{marker}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1,1 L9,5 L1,9" fill="none" stroke="#444" stroke-width="1.3"/></marker></defs>
<style>{CSS}</style>
{chr(10).join(cuerpo)}
</svg>'''
    return f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(titulo)}</title>
{FONT}
<style>html,body{{margin:0;background:{PAPER}}}svg{{display:block;width:{W}px;height:{H}px}}</style></head><body>{svg}</body></html>'''


class Lienzo:
    def __init__(self, marker):
        self.o, self.m = [], marker

    def caja(self, x, y, w, h, lineas, tipo='normal', pill=False):
        x, y, w, h = x * KX, y * KY, w * KX, h * KY
        fill, stroke, sw, dash = PAPER, INK, 1.2, ''
        if tipo == 'error':
            fill, stroke, sw = '#fbe9e2', '#d9532c', 1.8
        elif tipo == 'falla':
            dash, stroke = ' stroke-dasharray="6,4"', MUTE
        elif tipo == 'pausa':
            dash = ' stroke-dasharray="6,4"'
        elif tipo == 'foco':
            fill, stroke, sw = '#fbe9e2', '#d9532c', 1.8
        rx = h // 2 if pill else 9
        self.o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{dash}/>')
        n = len(lineas)
        y0 = y + h / 2 - (n - 1) * 9 * F + 5 * F
        for i, t in enumerate(lineas):
            self.o.append(f'<text x="{x + w/2}" y="{y0 + i*18*F:.0f}" text-anchor="middle" class="{"t" if (i == 0 or (tipo == "normal" and not pill)) else "b"}">{esc(t)}</text>')

    def rombo(self, x, y, w, h, lineas):
        x, y, w, h = x * KX, y * KY, w * KX, h * KY
        mx, my = x + w / 2, y + h / 2
        self.o.append(f'<polygon points="{mx},{y} {x+w},{my} {mx},{y+h} {x},{my}" fill="{PAPER}" stroke="{INK}" stroke-width="1.2"/>')
        n = len(lineas)
        y0 = my - (n - 1) * 8 * F + 5 * F
        for i, t in enumerate(lineas):
            self.o.append(f'<text x="{mx}" y="{y0 + i*PITCH:.0f}" text-anchor="middle" class="b" style="font-weight:600;fill:#1a1a1a">{esc(t)}</text>')

    def flecha(self, pts, falla=False, punto=False):
        d = 'M' + ' L'.join(f'{x*KX:.1f},{y*KY:.1f}' for x, y in pts)
        col = MUTE if falla else INK
        self.o.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="1.3"' + (' stroke-dasharray="5,4"' if falla else '') + f' marker-end="url(#{self.m})"/>')

    def etiqueta(self, lineas, x, y, ancla='middle'):
        if isinstance(lineas, str):
            lineas = [lineas]
        x, y = x * KX, y * KY
        w = max(len(l) for l in lineas) * 6.4 * F + 10
        x0 = x - w / 2 if ancla == 'middle' else (x - 5 if ancla == 'start' else x - w + 5)
        self.o.append(f'<rect x="{x0:.0f}" y="{y-13*F}" width="{w:.0f}" height="{len(lineas)*PITCH+3}" fill="{PAPER}"/>')
        for i, l in enumerate(lineas):
            self.o.append(f'<text x="{x}" y="{y + i*PITCH}" text-anchor="{ancla}" class="l">{esc(l)}</text>')

    def inicio(self, cx, cy):
        cx, cy = cx * KX, cy * KY
        self.o.append(f'<circle cx="{cx}" cy="{cy}" r="9" fill="{INK}"/>')

    def fin(self, cx, cy):
        cx, cy = cx * KX, cy * KY
        self.o.append(f'<circle cx="{cx}" cy="{cy}" r="12" fill="{PAPER}" stroke="{INK}" stroke-width="1.3"/><circle cx="{cx}" cy="{cy}" r="6.5" fill="{INK}"/>')

    def marco(self, x, y, w, h, titulo):
        x, y, w, h = x * KX, y * KY, w * KX, h * KY
        self.o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#f1eee5" stroke="{MUTE}" stroke-dasharray="7,5"/>')
        self.o.append(f'<text x="{x+16}" y="{y+24*F}" class="tag">{esc(titulo)}</text>')


def leyenda(x, y, items):
    s = f'<g transform="translate({x},{y})" class="lg">'
    cx = 0
    for tipo, txt in items:
        if tipo == 'flecha':
            s += f'<line x1="{cx}" y1="0" x2="{cx+32}" y2="0" stroke="{INK}" stroke-width="1.3"/><path d="M{cx+25},-4 L{cx+32},0 L{cx+25},4" fill="none" stroke="{INK}"/>'
            w = 40
        elif tipo == 'falla':
            s += f'<line x1="{cx}" y1="0" x2="{cx+32}" y2="0" stroke="{MUTE}" stroke-dasharray="5,4"/><path d="M{cx+25},-4 L{cx+32},0 L{cx+25},4" fill="none" stroke="{MUTE}"/>'
            w = 40
        elif tipo == 'error':
            s += f'<rect x="{cx}" y="-8" width="26" height="16" rx="4" fill="#fbe9e2" stroke="#d9532c" stroke-width="1.6"/>'
            w = 34
        elif tipo == 'pausa':
            s += f'<rect x="{cx}" y="-8" width="26" height="16" rx="4" fill="{PAPER}" stroke="{INK}" stroke-dasharray="5,3"/>'
            w = 34
        elif tipo == 'inicio':
            s += f'<circle cx="{cx+8}" cy="0" r="7" fill="{INK}"/>'
            w = 24
        elif tipo == 'fin':
            s += f'<circle cx="{cx+10}" cy="0" r="10" fill="{PAPER}" stroke="{INK}"/><circle cx="{cx+10}" cy="0" r="5.5" fill="{INK}"/>'
            w = 28
        elif tipo == 'rombo':
            s += f'<polygon points="{cx},0 {cx+13},-8 {cx+26},0 {cx+13},8" fill="{PAPER}" stroke="{INK}"/>'
            w = 34
        s += f'<text x="{cx+w}" y="4">{esc(txt)}</text>'
        cx += w + len(txt) * 7.6 * F + 34
    return s + '</g>'


# ---------------------------------------------------------------- estados del análisis
def estados():
    global KX, KY
    if DIAPO:
        KX, KY = 1.1, 1.3
    d = Lienzo('ea')
    W, H = 1700, 800
    W, H = int(W * KX), int(H * KY)
    # estados
    d.inicio(32, 235)
    d.caja(190, 210, 160, 50, ['en cola'])
    d.marco(480, 150, 900, 170, 'PROCESANDO')
    d.caja(510, 210, 190, 50, ['preprocesamiento'])
    d.caja(820, 210, 160, 50, ['cilindros'])
    d.caja(1120, 210, 170, 50, ['clasificación'])
    d.caja(1470, 210, 170, 50, ['completado'])
    d.caja(560, 500, 160, 54, ['error'], 'error')
    d.caja(1000, 500, 160, 54, ['en pausa'], 'pausa')
    d.caja(1330, 500, 160, 54, ['cancelado'])
    d.fin(640, 640); d.fin(1410, 640); d.fin(1555, 340)
    # flechas principales
    d.flecha([(41, 235), (190, 235)])
    d.etiqueta(['se validó', 'el video'], 112, 205)
    d.flecha([(350, 235), (510, 235)])
    d.etiqueta(['el Worker', 'tomó la tarea'], 430, 205)
    d.flecha([(700, 235), (820, 235)])
    d.flecha([(980, 235), (1120, 235)])
    d.etiqueta(['se hallaron', 'los cilindros'], 1050, 205)
    d.flecha([(1290, 235), (1470, 235)])
    d.etiqueta(['terminaron', 'las tres etapas'], 1380, 205)
    d.flecha([(1555, 260), (1555, 328)])
    # fallas
    d.flecha([(605, 260), (605, 400), (640, 400), (640, 500)], falla=True)
    d.etiqueta(['no se pudo', 'abrir el video'], 590, 395, 'end')
    d.flecha([(860, 260), (860, 420), (690, 420), (690, 500)], falla=True)
    d.etiqueta(['no se hallaron', 'los cilindros'], 850, 400, 'end')
    d.flecha([(640, 554), (640, 628)])
    # pausa
    d.flecha([(940, 260), (940, 380), (1080, 380), (1080, 500)])
    d.etiqueta(['3 s seguidos sin', 'ver al espécimen'], 1092, 440, 'start')
    d.flecha([(1160, 527), (1330, 527)])
    d.etiqueta(['el usuario cancela', 'o pasan 72 h'], 1245, 497)
    d.flecha([(1410, 554), (1410, 628)])
    # regresos a en cola
    d.flecha([(1080, 554), (1080, 720), (270, 720), (270, 260)])
    d.etiqueta(['el usuario ajusta o confirma el recuadro', 'vuelve al frente de la cola'], 680, 700)
    d.flecha([(700, 150), (700, 100), (310, 100), (310, 210)])
    d.etiqueta('el Worker se apagó a media tarea: al arrancar lo reencola', 520, 92)
    d.flecha([(1555, 210), (1555, 52), (230, 52), (230, 210)])
    d.etiqueta('el investigador reinició el análisis', 900, 44)
    cuerpo = d.o + [leyenda(40 * KX, 780 * KY, [('flecha', 'transición'), ('falla', 'falla'), ('error', 'error'), ('pausa', 'en pausa'), ('inicio', 'inicio'), ('fin', 'fin')])]
    return pagina('Estados del análisis',
                  'Estados de un análisis: en cola, procesando con sus tres etapas, en pausa, completado, error y cancelado.',
                  W, H, cuerpo, 'ea')


# ---------------------------------------------------------------- flujo del pipeline
def pipeline():
    d = Lienzo('pf')
    W, H = 1700, 1035
    W0, W, H = W, int(W * KX), int(H * KY)
    NW = 230
    X = lambda c: 40 + c * 270
    cx = lambda c: X(c) + NW // 2
    bandas = [('MÓDULO 1', 'Preprocesamiento', 20, 300), ('MÓDULO 2', 'Localización de los cilindros', 315, 640),
              ('MÓDULO 3', 'Clasificación de conducta', 655, 832), ('MÓDULO 4', 'Resultados', 847, 970)]
    for i, (tag, nombre, y0, y1) in enumerate(bandas):
        y0, y1 = y0 * KY, y1 * KY
        d.o.append(f'<rect x="20" y="{y0}" width="{W-40}" height="{y1-y0}" rx="12" fill="{"#f4f2ea" if i % 2 == 0 else "#efede4"}" stroke="#d8d5cc"/>')
        lado = i >= 2
        tx, an = (38, 'start') if lado else (W - 38, 'end')
        d.o.append(f'<text x="{tx}" y="{y0+24*F}" text-anchor="{an}" class="tag">{tag}</text><text x="{tx}" y="{y0+46*F}" text-anchor="{an}" class="mod">{esc(nombre)}</text>')
    # módulo 1
    y1c = 130
    d.caja(X(0), y1c - 32, NW, 64, ['Video subido', 'por el usuario'], pill=True)
    d.rombo(X(1), y1c - 55, NW, 110, ['¿Se pudo abrir', 'el video?'])
    d.caja(X(2), y1c - 34, NW, 68, ['Verifica los archivos', 'del análisis'])
    d.caja(X(3), y1c - 34, NW, 68, ['Lee ancho, alto', 'y duración'])
    d.flecha([(X(0) + NW, y1c), (X(1), y1c)])
    d.flecha([(X(1) + NW, y1c), (X(2), y1c)]); d.etiqueta('sí', X(1) + NW + 20, y1c - 10)
    d.flecha([(X(2) + NW, y1c), (X(3), y1c)])
    d.caja(X(1), 215, NW, 70, ['Falla', 'reporte de diagnóstico', 'y análisis en error'], 'falla')
    d.flecha([(cx(1), y1c + 55), (cx(1), 215)], falla=True); d.etiqueta('no', cx(1) + 16, 192, 'start')
    # módulo 2, fila a (izq → der)
    ya = 420
    d.caja(X(0), ya - 36, NW, 72, ['Alinea la cámara con', 'un cuadro de referencia'])
    d.caja(X(1), ya - 34, NW, 68, ['Construye el fondo', 'del video'])
    d.caja(X(2), ya - 34, NW, 68, ['Ubica la línea de agua', 'y el suelo'])
    d.caja(X(3), ya - 34, NW, 68, ['Separa los cilindros'])
    d.rombo(X(4), ya - 55, NW, 110, ['¿Se hallaron', 'los cilindros?'])
    d.caja(X(5), ya - 38, NW, 76, ['Falla', 'reporte de diagnóstico', 'y análisis en error'], 'falla')
    # Lee ancho → Alinea
    d.flecha([(cx(3), y1c + 34), (cx(3), 302), (cx(0), 302), (cx(0), ya - 36)])
    for c in range(3):
        d.flecha([(X(c) + NW, ya), (X(c + 1), ya)])
    d.flecha([(X(4) + NW, ya), (X(5), ya)], falla=True); d.etiqueta('no', X(4) + NW + 22, ya - 10)
    # fila b (der → izq)
    yb = 572
    d.caja(X(4), yb - 36, NW, 72, ['Calcula la región', 'de cada cilindro'])
    d.caja(X(3), yb - 34, NW, 68, ['Mide al espécimen', 'en cada cilindro'])
    d.caja(X(2), yb - 40, NW, 80, ['Separa al espécimen', 'del fondo, segundo', 'a segundo'])
    d.rombo(X(1), yb - 62, NW, 124, ['¿Tres segundos', 'seguidos sin ver', 'al espécimen?'])
    d.caja(X(0), yb - 46, NW, 92, ['Pausa', 'guarda imagen fija y datos;', 'espera al usuario (72 h)'], 'pausa')
    d.flecha([(cx(4), ya + 55), (cx(4), yb - 36)]); d.etiqueta('sí', cx(4) + 16, ya + 82, 'start')
    d.flecha([(X(4), yb), (X(3) + NW, yb)])
    d.flecha([(X(3), yb), (X(2) + NW, yb)])
    d.flecha([(X(2), yb), (X(1) + NW, yb)])
    d.flecha([(X(1), yb), (X(0) + NW, yb)]); d.etiqueta('sí', X(1) - 20, yb - 10)
    # módulo 3 (izq → der)
    y3 = 768
    d.caja(X(0), y3 - 38, NW, 76, ['Mide 15 rasgos y', '7 reglas de observación'])
    d.caja(X(1), y3 - 38, NW, 76, ['Conserva los últimos', '300 s de cada espécimen'])
    d.caja(X(2), y3 - 38, NW, 76, ['Arma, por cada segundo,', 'un clip de 4 s'])
    d.caja(X(3), y3 - 42, NW, 84, ['La red de fusión', 'R(2+1)D-18 da tres salidas:', 'nado, inmovilidad, escalamiento'], 'foco')
    d.caja(X(4), y3 - 38, NW, 76, ['Asigna la conducta con', 'la regla del umbral 0.80'])
    d.caja(X(5), y3 - 42, NW, 84, ['Guarda la copia para', 'revisión, los recuadros', 'y los segundos'])
    d.flecha([(cx(1), yb + 62), (cx(1), 640), (262, 640), (262, y3 - 38)]); d.etiqueta('no', cx(1) + 16, yb + 86, 'start')
    for c in range(5):
        d.flecha([(X(c) + NW, y3), (X(c + 1), y3)])
    # módulo 4
    d.caja(X(5), 886, NW, 76, ['Calcula totales y', 'bloques de 5 s al mostrarse', '(no se guardan)'])
    d.flecha([(cx(5), y3 + 42), (cx(5), 886)])
    d.fin(X(4) + 40, 924)
    d.flecha([(X(5), 924), (X(4) + 52, 924)])
    cuerpo = d.o + [leyenda(40 * KX, 1008 * KY, [('flecha', 'flujo normal'), ('falla', 'falla'), ('rombo', 'decisión'), ('pausa', 'pausa'), ('error', 'la red decide la conducta de cada segundo'), ('fin', 'fin')])]
    return pagina('Flujo del análisis',
                  'Los cuatro módulos del pipeline de análisis: preprocesamiento, localización de los cilindros, clasificación de conducta y resultados, con sus fallas y la pausa.',
                  W, H, cuerpo, 'pf')


if __name__ == '__main__':
    quien, salida = sys.argv[1], sys.argv[2]
    open(salida, 'w', encoding='utf-8').write({'estados': estados, 'pipeline': pipeline}[quien]())
    print('ok', quien)
