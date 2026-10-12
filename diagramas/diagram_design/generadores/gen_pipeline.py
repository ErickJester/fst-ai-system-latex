import html, sys
esc = html.escape
out = []
LH = 14
W_NODE = 230
X0, STEP = 250, 260
def cxl(c): return X0 + c * STEP           # borde izquierdo de la columna c
def cxc(c): return cxl(c) + W_NODE // 2    # centro de la columna c
def cxr(c): return cxl(c) + W_NODE         # borde derecho

N = {}
def box(key, c, cy, title, lines, focal=False, pill=False, dash=False, fill='#faf9f5'):
    h = 30 + len(lines) * LH + 10
    x, y = cxl(c), cy - h // 2
    f, s, sw = ('#fbe9e2', '#d9532c', 1.5) if focal else (fill, '#1a1a1a', 1)
    rx = h // 2 if pill else 6
    out.append(f'<rect x="{x}" y="{y}" width="{W_NODE}" height="{h}" rx="{rx}" fill="{f}" stroke="{s}" stroke-width="{sw}"' + (' stroke-dasharray="5,4"' if dash else '') + '/>')
    out.append(f'<text x="{x+W_NODE/2}" y="{y+20}" text-anchor="middle" class="nm">{esc(title)}</text>')
    for i, t in enumerate(lines):
        out.append(f'<text x="{x+W_NODE/2}" y="{y+38+i*LH}" text-anchor="middle" class="a">{esc(t)}</text>')
    N[key] = dict(c=c, cy=cy, h=h, x=x, y=y)

def diamond(key, c, cy, lines):
    h = 92
    x = cxl(c); mx = x + W_NODE / 2
    pts = f'{mx},{cy-h/2} {x+W_NODE},{cy} {mx},{cy+h/2} {x},{cy}'
    out.append(f'<polygon points="{pts}" fill="#faf9f5" stroke="#1a1a1a"/>')
    for i, t in enumerate(lines):
        out.append(f'<text x="{mx}" y="{cy - (len(lines)-1)*7 + i*14 + 3}" text-anchor="middle" class="a" style="font-weight:600">{esc(t)}</text>')
    N[key] = dict(c=c, cy=cy, h=h, x=x, y=cy - h // 2)

def L(k): return (N[k]['x'], N[k]['cy'])
def R(k): return (N[k]['x'] + W_NODE, N[k]['cy'])
def T(k): return (N[k]['x'] + W_NODE // 2, N[k]['y'])
def B(k): return (N[k]['x'] + W_NODE // 2, N[k]['y'] + N[k]['h'])

def arrow(pts, dashed=False, head=True, color='#1a1a1a'):
    d = 'M' + ' L'.join(f'{x},{y}' for x, y in pts)
    out.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="1"' + (' stroke-dasharray="4,3"' if dashed else '') + (' marker-end="url(#p-arr)"' if head else '') + '/>')

def label(x, y, t, anchor='middle'):
    tw = len(t) * 5.2 + 8
    x0 = x - tw / 2 if anchor == 'middle' else (x - 4 if anchor == 'start' else x - tw + 4)
    out.append(f'<rect x="{x0:.0f}" y="{y-9}" width="{tw:.0f}" height="11" fill="#faf9f5"/><text x="{x}" y="{y}" text-anchor="{anchor}" class="r">{esc(t)}</text>')

W, H = 1640, 1000
# ---- Franjas de modulo ----
bands = [('MÓDULO 1', 'Preprocesamiento', 36, 186), ('MÓDULO 2', 'Localización de los cilindros', 290, 440),
         ('MÓDULO 3', 'Clasificación de conducta', 460, 790), ('MÓDULO 4', 'Resultados', 810, 950)]
for i, (tag, name, y0, y1) in enumerate(bands):
    out.append(f'<rect x="20" y="{y0}" width="{W-40}" height="{y1-y0}" rx="8" fill="{"#f4f2ea" if i % 2 == 0 else "#efede4"}" stroke="#d8d5cc"/>')
    out.append(f'<text x="36" y="{y0+24}" class="st">{tag}</text>')
    out.append(f'<text x="36" y="{y0+42}" class="nm" style="text-anchor:start">{esc(name)}</text>')

# ---- Modulo 1 (izquierda a derecha) ----
cy1 = 118
box('start', 0, cy1, 'Video subido', ['por el investigador'], pill=True)
box('m1a', 1, cy1, 'Lee los cuadros', ['del video (OpenCV)'])
diamond('m1d', 2, cy1, ['¿Se pudo abrir', 'el video?'])
box('m1b', 3, cy1, 'Registro de cámara', ['alinea cada cuadro', 'contra uno de referencia'])
box('m1c', 4, cy1, 'Modelo de fondo', ['percentil 10 de cada píxel', 'y mapa de ocupación'])
arrow([R('start'), L('m1a')]); arrow([R('m1a'), L('m1d')])
arrow([R('m1d'), L('m1b')]); label(R('m1d')[0] + 22, cy1 - 6, 'SÍ')
arrow([R('m1b'), L('m1c')])
# ---- Falla (entre modulos 1 y 2) ----
ey = 232
box('err', 2, ey, 'Falla', ['reporte de diagnóstico', 'y análisis en «error»'], dash=True)
arrow([B('m1d'), T('err')], dashed=True, color='#6b6b6b'); label(B('m1d')[0] + 20, 196, 'NO', 'start')
# ---- Modulo 2 (derecha a izquierda) ----
cy2 = 366
box('m2a', 4, cy2, 'Línea de agua y suelo', ['rebordes del recipiente'])
box('m2b', 3, cy2, 'Separa los cilindros', ['por dónde hubo movimiento', 'dentro del agua'])
diamond('m2d', 2, cy2, ['¿Se hallaron', 'los cilindros?'])
box('m2c', 1, cy2, 'Región de interés', ['de cada cilindro', '(de 2 a 4 por video)'])
arrow([B('m1c'), T('m2a')])
arrow([L('m2a'), R('m2b')]); arrow([L('m2b'), R('m2d')])
arrow([L('m2d'), R('m2c')]); label(L('m2d')[0] - 22, cy2 - 6, 'SÍ')
arrow([T('m2d'), B('err')], dashed=True, color='#6b6b6b'); label(T('m2d')[0] + 20, 322, 'NO', 'start')
# ---- Modulo 3 (CNN de fusion: dos ramas que se juntan) ----
r1, r2, rc = 540, 700, 620
box('v1', 0, r1, 'Recorta el tubo', ['usa la región de interés', 'de cada cilindro'])
box('v2', 1, r1, 'Arma el clip de cada segundo', ['16 cuadros de una ventana de 4 s'])
box('s1', 0, r2, 'Separa al espécimen', ['del fondo, en su cilindro', '(diferencia y brillo)'])
box('s2', 1, r2, 'Mide 15 rasgos', ['movimiento, postura y trayectoria', 'en una ventana de 4 s', 'centrada en cada segundo'])
box('s3', 2, r2, 'Mide 7 reglas', ['pataleo bajo el agua y cambio', 'sobre la línea de agua', 'se mide en el mismo clip'])
box('cnn', 3, rc, 'CNN 3D con medidas de apoyo', ['red R(2+1)D-18 sobre el clip,', 'más las 22 medidas'], focal=True)
box('cond', 4, rc, 'Conducta del segundo', ['inmovilidad, nado o escalamiento'])
# modulo 2 -> modulo 3
ca, cb = B('m2c'), T('v1')
arrow([ca, (ca[0], 450), (cb[0], 450), cb])
arrow([R('v1'), L('v2')])
# 'Separa al espécimen' recibe del módulo 2 (región de interés y fondo), por la izquierda del recorte
arrow([(570, ca[1]), (570, 435), (220, 435), (220, r2), L('s1')])
arrow([R('s1'), L('s2')])
# union de las dos ramas
cnx = N['cnn']['x'] + W_NODE // 2
arrow([R('v2'), (cnx, R('v2')[1]), T('cnn')])
# las 7 reglas salen del clip
s3x = N['s3']['x'] + W_NODE // 2
arrow([R('v2'), (s3x, R('v2')[1]), T('s3')])
out.append(f'<circle cx="{s3x}" cy="{R("v2")[1]}" r="3" fill="#1a1a1a"/>')
# las dos medidas llegan a la red, cada una con su flecha
arrow([R('s3'), (cnx - 40, R('s3')[1]), (cnx - 40, B('cnn')[1])])
arrow([B('s2'), (B('s2')[0], 772), (cnx + 40, 772), (cnx + 40, B('cnn')[1])])
arrow([R('cnn'), L('cond')])
box('pausa', 4, 524, 'En pausa', ['3 s seguidos sin ver al espécimen:', 'aviso al usuario; si ajusta el', 'recuadro, continúa; sin respuesta', 'en 5 min, el análisis se cancela'], dash=True)
arrow([(cnx + 70, N['cnn']['y']), (cnx + 70, 524), L('pausa')], dashed=True, color='#6b6b6b')
# ---- Modulo 4 (resultados) ----
cy4 = 880
box('b2', 4, cy4, 'Guarda', ['conducta de cada segundo', 'segundos por conducta y minuto', 'copia del video para revisión', '(H.264, recortada a lo analizado)'])
arrow([B('cond'), T('b2')])

legend = '''<g transform="translate(40,972)" class="lg">
<line x1="0" y1="0" x2="28" y2="0" stroke="#1a1a1a"/><path d="M22,-4 L28,0 L22,4" fill="none" stroke="#1a1a1a"/><text x="38" y="3">FLUJO NORMAL</text>
<line x1="160" y1="0" x2="188" y2="0" stroke="#6b6b6b" stroke-dasharray="4,3"/><path d="M182,-4 L188,0 L182,4" fill="none" stroke="#6b6b6b"/><text x="198" y="3">FALLA</text>
<polygon points="300,0 312,-7 324,0 312,7" fill="#faf9f5" stroke="#1a1a1a"/><text x="334" y="3">DECISIÓN</text>
<rect x="440" y="-8" width="22" height="14" rx="3" fill="#fbe9e2" stroke="#d9532c" stroke-width="1.5"/><text x="470" y="3">LA RED: DECIDE LA CONDUCTA DE CADA SEGUNDO</text>
</g>'''

svg = f'''<svg viewBox="0 20 {W} {H-20}" role="img" aria-labelledby="pl-title pl-desc" xmlns="http://www.w3.org/2000/svg">
<title id="pl-title">Pipeline de análisis conductual</title>
<desc id="pl-desc">Los cuatro módulos del pipeline: preprocesamiento, localización de los cilindros, clasificación de conducta y resultados, con las dos fallas posibles.</desc>
<defs><marker id="p-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1,1 L9,5 L1,9" fill="none" stroke="#444" stroke-width="1.2"/></marker></defs>
<style>
.a{{font:400 9px 'Geist Mono',monospace;fill:#1a1a1a}}
.nm{{font:600 12px Geist,sans-serif;fill:#1a1a1a}}
.st{{font:400 8px 'Geist Mono',monospace;fill:#6b6b6b;letter-spacing:.06em}}
.r{{font:400 8px 'Geist Mono',monospace;fill:#6b6b6b;letter-spacing:.06em}}
.lg text{{font:400 9px 'Geist Mono',monospace;fill:#6b6b6b}}
</style>
{chr(10).join(out)}
{legend}
</svg>'''
page = f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Pipeline de análisis</title>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;600&family=Geist+Mono:wght@400&display=swap" rel="stylesheet">
<style>
html,body{{height:100%;margin:0;background:#faf9f5}}
body{{overflow-x:auto;overflow-y:hidden}}
svg{{display:block;height:100vh;width:auto}}
</style></head><body>{svg}</body></html>'''
open(sys.argv[1], 'w', encoding='utf-8').write(page)
print('ok')
