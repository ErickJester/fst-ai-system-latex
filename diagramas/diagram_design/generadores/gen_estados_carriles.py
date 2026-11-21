"""Estados del análisis en carriles (swimlanes), para la diapositiva 14.
Fuente: diagramas/estados_analisis.puml. Uso: gen_estados_carriles.py salida.html"""
import html, sys
esc = html.escape
W, H = 1800, 900
INK = '#1f2430'
o = []

CSS = """
.n{font:600 25px Geist,'Segoe UI',sans-serif;fill:#1f2430}
.l{font:400 18px Geist,'Segoe UI',sans-serif;fill:#1f2430}
.c{font:600 21px Geist,'Segoe UI',sans-serif;fill:#fff}
.g{font:400 18px Geist,'Segoe UI',sans-serif;fill:#1f2430}
"""

def carril(y0, y1, titulo, bg, bd, lab):
    o.append(f'<rect x="20" y="{y0}" width="{W-40}" height="{y1-y0}" rx="10" fill="{bg}" stroke="{bd}"/>')
    o.append(f'<rect x="20" y="{y0}" width="52" height="{y1-y0}" rx="10" fill="{lab}"/>')
    cy = (y0 + y1) / 2
    o.append(f'<text transform="translate(52,{cy}) rotate(-90)" text-anchor="middle" class="c">{esc(titulo)}</text>')

def caja(x0, x1, y0, y1, texto, fill, stroke, dash=False):
    o.append(f'<rect x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}" rx="12" fill="{fill}" stroke="{stroke}" stroke-width="2.2"' + (' stroke-dasharray="8,5"' if dash else '') + '/>')
    o.append(f'<text x="{(x0+x1)/2}" y="{(y0+y1)/2+9}" text-anchor="middle" class="n">{esc(texto)}</text>')

def flecha(pts, dash=False):
    d = 'M' + ' L'.join(f'{x},{y}' for x, y in pts)
    o.append(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="1.8"' + (' stroke-dasharray="7,5"' if dash else '') + ' marker-end="url(#ar)"/>')

def txt(lineas, x, y, ancla='middle', fondo=None):
    if isinstance(lineas, str):
        lineas = [lineas]
    if fondo:
        w = max(len(l) for l in lineas) * 9.2 + 12
        x0 = x - w / 2 if ancla == 'middle' else (x - 6 if ancla == 'start' else x - w + 6)
        o.append(f'<rect x="{x0:.0f}" y="{y-18}" width="{w:.0f}" height="{len(lineas)*23+4}" fill="{fondo}"/>')
    for i, l in enumerate(lineas):
        o.append(f'<text x="{x}" y="{y+i*23}" text-anchor="{ancla}" class="l">{esc(l)}</text>')

def fin(cx, cy):
    o.append(f'<circle cx="{cx}" cy="{cy}" r="15" fill="#fff" stroke="{INK}" stroke-width="2"/><circle cx="{cx}" cy="{cy}" r="8.5" fill="{INK}"/>')

# carriles
BG1, BG2, BG3, BG4 = '#f3f4f6', '#eef4fc', '#fdf1ec', '#fff7e8'
carril(15, 175, 'Cola', BG1, '#d1d5db', '#6b7280')
carril(190, 430, 'Procesamiento', BG2, '#bfd3ee', '#4a79c4')
carril(445, 605, 'Fallas', BG3, '#f2c9bb', '#d9693f')
carril(620, 820, 'Usuario', BG4, '#f1d9a8', '#c99a2e')

# cola
o.append(f'<circle cx="125" cy="105" r="12" fill="{INK}"/>')
caja(250, 620, 70, 140, 'En cola', '#e5e7eb', '#6b7280')
flecha([(137, 105), (250, 105)])
txt(['se validó', 'el video'], 193, 62)
# procesamiento
caja(330, 680, 270, 340, 'Preprocesamiento', '#dde9f9', '#3b78c4')
caja(790, 1010, 270, 340, 'Cilindros', '#dde9f9', '#3b78c4')
caja(1180, 1440, 270, 340, 'Clasificación', '#dde9f9', '#3b78c4')
caja(1590, 1770, 270, 340, 'Completado', '#dff3e6', '#2f8f55')
flecha([(590, 140), (590, 270)])
txt(['el Worker', 'tomó la tarea'], 602, 190, 'start')
flecha([(680, 305), (790, 305)])
flecha([(1010, 305), (1180, 305)])
txt(['se hallaron', 'los cilindros'], 1095, 262, fondo=BG2)
flecha([(1440, 305), (1590, 305)])
txt(['terminaron', 'las tres etapas'], 1515, 262, fondo=BG2)
# reinicio del análisis y reencolado
flecha([(1680, 270), (1680, 105), (620, 105)])
txt('el investigador reinició el análisis', 1150, 90, fondo=BG1)
flecha([(390, 270), (390, 140)])
txt(['el Worker se apagó', 'a media tarea: al', 'arrancar lo reencola'], 402, 176, 'start')
# fallas
caja(400, 650, 480, 555, 'Error', '#fde2d9', '#d9532c')
flecha([(430, 340), (430, 480)], dash=True)
txt(['no se pudo', 'abrir el video'], 420, 400, 'end')
flecha([(860, 340), (860, 400), (600, 400), (600, 480)], dash=True)
txt(['no se hallaron', 'los cilindros'], 848, 362, 'end')
flecha([(650, 517), (715, 517)])
fin(730, 517)
fin(1680, 520)
flecha([(1680, 340), (1680, 505)])
# atención del usuario
caja(800, 1060, 680, 750, 'En pausa', '#fdf0d0', '#c99a2e', dash=True)
flecha([(950, 340), (950, 680)])
txt(['3 s seguidos sin', 'ver al espécimen'], 962, 520, 'start')
caja(1330, 1580, 680, 750, 'Cancelado', '#fbd5de', '#c0405f')
flecha([(1060, 715), (1330, 715)])
txt(['el usuario cancela', 'o pasan 72 h'], 1195, 668)
flecha([(1580, 715), (1665, 715)])
fin(1680, 715)
flecha([(800, 715), (265, 715), (265, 140)])
txt(['el usuario ajusta', 'o confirma el', 'recuadro'], 255, 640, 'end')

# leyenda
leg = [('#e5e7eb', '#6b7280', False, 'Cola'), ('#dde9f9', '#3b78c4', False, 'Procesamiento'), ('#dff3e6', '#2f8f55', False, 'Cierre exitoso'),
       ('#fde2d9', '#d9532c', False, 'Error'), ('#fdf0d0', '#c99a2e', True, 'En pausa'), ('#fbd5de', '#c0405f', False, 'Cierre por cancelación')]
x = 60
for f, s, d, t in leg:
    o.append(f'<rect x="{x}" y="850" width="30" height="24" rx="5" fill="{f}" stroke="{s}" stroke-width="2"' + (' stroke-dasharray="5,3"' if d else '') + '/>')
    o.append(f'<text x="{x+40}" y="869" class="g">{esc(t)}</text>')
    x += 40 + len(t) * 10 + 50

svg = f'''<svg viewBox="0 0 {W} {H}" role="img" xmlns="http://www.w3.org/2000/svg"><title>Estados de un análisis</title>
<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M1,1 L9,5 L1,9" fill="none" stroke="#1f2430" stroke-width="1.5"/></marker></defs>
<style>{CSS}</style>
<rect width="{W}" height="{H}" fill="#fff"/>
{chr(10).join(o)}</svg>'''
open(sys.argv[1], 'w', encoding='utf-8').write(f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Estados de un análisis</title>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;600&display=swap" rel="stylesheet">
<style>html,body{{margin:0;background:#fff}}svg{{display:block;width:{W}px;height:{H}px}}</style></head><body>{svg}</body></html>''')
print('ok')
