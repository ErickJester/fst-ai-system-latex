import html, sys

# Dos maquinas de estados (diagramas/estados_analisis.puml y diagramas/estados_experimento.puml)
# en el estilo de diagram_design. Uso: gen_estados.py analisis|experimento salida.html
esc = html.escape
LH = 11

class Dib:
    def __init__(self):
        self.out = []

    def estado(self, x, y, w, h, nombre, tipo='normal'):
        fill, stroke, sw, dash = '#faf9f5', '#1a1a1a', 1, ''
        if tipo == 'error':
            fill, stroke, sw = '#fbe9e2', '#d9532c', 1.5
        elif tipo == 'pausa':
            dash = ' stroke-dasharray="5,4"'
        self.out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h//2 if tipo == "inicio" else 8}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{dash}/>')
        self.out.append(f'<text x="{x + w/2}" y="{y + h/2 + 4}" text-anchor="middle" class="nm">{esc(nombre)}</text>')

    def marco(self, x, y, w, h, titulo):
        self.out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#f1eee5" stroke="#6b6b6b" stroke-dasharray="6,4"/>')
        self.out.append(f'<text x="{x+14}" y="{y+20}" class="st">{esc(titulo)}</text>')

    def inicio(self, cx, cy):
        self.out.append(f'<circle cx="{cx}" cy="{cy}" r="7" fill="#1a1a1a"/>')

    def fin(self, cx, cy):
        self.out.append(f'<circle cx="{cx}" cy="{cy}" r="9" fill="#faf9f5" stroke="#1a1a1a"/><circle cx="{cx}" cy="{cy}" r="5" fill="#1a1a1a"/>')

    def flecha(self, pts, falla=False):
        d = 'M' + ' L'.join(f'{x},{y}' for x, y in pts)
        col = '#6b6b6b' if falla else '#1a1a1a'
        self.out.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="1.1"' + (' stroke-dasharray="4,3"' if falla else '') + ' marker-end="url(#es-arr)"/>')

    def etiqueta(self, lineas, x, y, ancla='middle'):
        if isinstance(lineas, str):
            lineas = [lineas]
        w = max(len(l) for l in lineas) * 5.3 + 8
        x0 = x - w / 2 if ancla == 'middle' else (x - 4 if ancla == 'start' else x - w + 4)
        self.out.append(f'<rect x="{x0:.0f}" y="{y-9}" width="{w:.0f}" height="{len(lineas)*LH+1}" fill="#faf9f5"/>')
        for i, l in enumerate(lineas):
            self.out.append(f'<text x="{x}" y="{y + i*LH}" text-anchor="{ancla}" class="a">{esc(l)}</text>')

    def nota(self, x, y, w, lineas, desde=None):
        h = 14 + len(lineas) * 12 + 6
        if desde:
            self.out.append(f'<line x1="{desde[0]}" y1="{desde[1]}" x2="{desde[0]}" y2="{y}" stroke="#6b6b6b" stroke-dasharray="2,3"/>')
        self.out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="#faf9f5" stroke="#6b6b6b" stroke-dasharray="4,3"/>')
        for i, l in enumerate(lineas):
            self.out.append(f'<text x="{x+10}" y="{y+17+i*12}" class="a">{esc(l)}</text>')


def pagina(d, W, H, titulo, desc, leyenda):
    svg = f'''<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="es-title es-desc" xmlns="http://www.w3.org/2000/svg">
<title id="es-title">{esc(titulo)}</title>
<desc id="es-desc">{esc(desc)}</desc>
<defs><marker id="es-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1,1 L9,5 L1,9" fill="none" stroke="#444" stroke-width="1.2"/></marker></defs>
<style>
.a{{font:400 9px 'Geist Mono',monospace;fill:#1a1a1a}}
.nm{{font:600 12px Geist,sans-serif;fill:#1a1a1a}}
.st{{font:400 8px 'Geist Mono',monospace;fill:#6b6b6b;letter-spacing:.06em}}
.lg text{{font:400 9px 'Geist Mono',monospace;fill:#6b6b6b}}
</style>
{chr(10).join(d.out)}
{leyenda}
</svg>'''
    return f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(titulo)}</title>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;600&family=Geist+Mono:wght@400&display=swap" rel="stylesheet">
<style>
html,body{{margin:0;background:#faf9f5}}
svg{{display:block;width:{W}px;height:{H}px}}
</style></head><body>{svg}</body></html>'''


def leyenda(y, con_pausa=True, con_falla=True):
    x = 40
    s = f'<g transform="translate({x},{y})" class="lg">'
    s += '<line x1="0" y1="0" x2="28" y2="0" stroke="#1a1a1a"/><path d="M22,-4 L28,0 L22,4" fill="none" stroke="#1a1a1a"/><text x="38" y="3">TRANSICIÓN</text>'
    if con_falla:
        s += '<line x1="140" y1="0" x2="168" y2="0" stroke="#6b6b6b" stroke-dasharray="4,3"/><path d="M162,-4 L168,0 L162,4" fill="none" stroke="#6b6b6b"/><text x="178" y="3">FALLA</text>'
    s += '<rect x="250" y="-8" width="22" height="14" rx="3" fill="#fbe9e2" stroke="#d9532c" stroke-width="1.5"/><text x="280" y="3">ERROR</text>'
    s += '<rect x="350" y="-8" width="22" height="14" rx="3" fill="#faf9f5" stroke="#1a1a1a" stroke-dasharray="4,3"/><text x="380" y="3">EN PAUSA</text>'
    s += '<circle cx="480" cy="0" r="6" fill="#1a1a1a"/><text x="494" y="3">INICIO</text>'
    s += '<circle cx="570" cy="0" r="8" fill="#faf9f5" stroke="#1a1a1a"/><circle cx="570" cy="0" r="4" fill="#1a1a1a"/><text x="584" y="3">FIN</text>'
    return s + '</g>'


def analisis():
    d = Dib()
    # estados principales
    d.inicio(30, 215)
    d.estado(190, 193, 160, 44, 'en cola')
    d.marco(500, 140, 860, 150, 'PROCESANDO')
    d.estado(530, 193, 160, 44, 'preprocesamiento')
    d.estado(840, 193, 160, 44, 'cilindros')
    d.estado(1150, 193, 160, 44, 'clasificación')
    d.estado(1470, 193, 160, 44, 'completado')
    d.estado(700, 440, 160, 50, 'error', 'error')
    d.estado(1150, 440, 160, 50, 'en pausa', 'pausa')
    d.estado(1470, 440, 160, 50, 'cancelado')
    d.fin(1550, 305); d.fin(780, 560); d.fin(1550, 565)
    # flechas
    d.flecha([(37, 215), (190, 215)])
    d.etiqueta(['se validó y almacenó', 'el video (CU-05, RF-12)'], 113, 197)
    d.flecha([(350, 215), (530, 215)])
    d.etiqueta(['el Worker tomó la', 'tarea (polling, CU-07)'], 440, 197)
    d.flecha([(690, 215), (840, 215)])
    d.flecha([(1000, 215), (1150, 215)])
    d.etiqueta(['[se hallaron', 'los cilindros]'], 1075, 195)
    d.flecha([(1310, 215), (1470, 215)])
    d.etiqueta(['se completaron las', 'tres etapas'], 1415, 197)
    d.flecha([(610, 237), (610, 465), (700, 465)], falla=True)
    d.etiqueta(['[no se pudo abrir', 'el video] (RN-11)'], 600, 370, 'end')
    d.flecha([(920, 237), (920, 465), (860, 465)], falla=True)
    d.etiqueta(['[no se hallaron los cilindros] (RN-11)', 'se generó el reporte de diagnóstico'], 932, 370, 'start')
    d.flecha([(1230, 237), (1230, 440)])
    d.etiqueta(['[3 s seguidos sin ver al espécimen]', 'se avisó al usuario (RN-17)'], 1242, 350, 'start')
    d.flecha([(1310, 465), (1470, 465)])
    d.etiqueta(['el usuario canceló o no', 'respondió en 5 min (RN-17)'], 1390, 440)
    d.flecha([(1230, 490), (1230, 620), (270, 620), (270, 237)])
    d.etiqueta(['el usuario ajustó el recuadro', 'vuelve al frente de la cola y continúa desde la pausa'], 750, 640)
    d.flecha([(900, 140), (900, 92), (310, 92), (310, 193)])
    d.etiqueta('el Worker se apagó a media análisis; al arrancar lo reencola', 600, 84)
    d.flecha([(1550, 193), (1550, 50), (230, 50), (230, 193)])
    d.etiqueta('el investigador reinició el análisis (RN-04)', 900, 42)
    d.flecha([(1550, 237), (1550, 296)])
    d.flecha([(780, 490), (780, 551)])
    d.flecha([(1550, 490), (1550, 556)])
    W, H = 1700, 700
    return pagina(d, W, H, 'Estados del análisis',
                  'Estados de un análisis: en cola, procesando con sus tres etapas, en pausa, completado, error y cancelado.',
                  leyenda(680))


def experimento():
    d = Dib()
    d.inicio(170, 118)
    d.estado(90, 178, 160, 44, 'sin_videos')
    d.estado(440, 178, 190, 44, 'en_espera_dia2')
    d.estado(830, 178, 160, 44, 'en_cola')
    d.estado(1160, 178, 160, 44, 'procesando')
    d.estado(1500, 178, 160, 44, 'error', 'error')
    d.estado(1160, 38, 160, 44, 'completado')
    d.estado(830, 358, 160, 44, 'en_pausa', 'pausa')
    d.estado(520, 358, 160, 44, 'cancelado')
    d.flecha([(170, 125), (170, 178)])
    d.etiqueta('se creó el experimento (CU-04)', 182, 154, 'start')
    d.flecha([(250, 200), (440, 200)])
    d.etiqueta(['solo se subió video', 'del Día 1 (CU-05)'], 345, 182)
    d.flecha([(630, 200), (830, 200)])
    d.etiqueta(['se subió y encoló un', 'video del Día 2 (CU-05)'], 730, 182)
    d.flecha([(170, 222), (170, 290), (850, 290), (850, 222)])
    d.etiqueta('se subió y encoló un video del Día 2 (CU-05)', 510, 308)
    d.flecha([(990, 200), (1160, 200)])
    d.etiqueta(['el Worker empezó a', 'procesar alguna tanda'], 1075, 182)
    d.flecha([(1320, 200), (1500, 200)], falla=True)
    d.etiqueta(['alguna tanda', 'terminó en error'], 1410, 182)
    d.flecha([(1240, 178), (1240, 82)])
    d.etiqueta(['todas las tandas', 'terminaron sin error'], 1252, 130, 'start')
    d.flecha([(1160, 60), (910, 60), (910, 178)])
    d.etiqueta('se agregó una tanda nueva (CU-05)', 1035, 52)
    d.flecha([(960, 358), (960, 222)])
    d.etiqueta(['el usuario ajustó', 'el recuadro'], 972, 262, 'start')
    d.flecha([(1240, 222), (1240, 380), (990, 380)])
    d.etiqueta(['alguna tanda quedó', 'en pausa (RN-17)'], 1252, 320, 'start')
    d.flecha([(830, 380), (680, 380)])
    d.etiqueta(['el usuario canceló o', '5 min sin respuesta'], 755, 362)
    d.nota(1440, 270, 250, ['error tiene precedencia: mientras',
                            'alguna tanda siga en error, el',
                            'experimento sigue en error',
                            '(error > cancelado > en pausa >',
                            'procesando > en cola > completado)'], desde=(1580, 222))
    W, H = 1740, 480
    return pagina(d, W, H, 'Estados del experimento',
                  'Estados de un experimento: sin videos, en espera del Día 2, en cola, procesando, en pausa, completado, error y cancelado.',
                  leyenda(455))


quien, salida = sys.argv[1], sys.argv[2]
page = {'analisis': analisis, 'experimento': experimento}[quien]()
open(salida, 'w', encoding='utf-8').write(page)
print('ok', quien)
