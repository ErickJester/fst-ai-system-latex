import html, math, sys

# Esquema conceptual (diagramas/esquema_conceptual.tex): modelo entidad-relacion extendido, notacion
# de Chen con cardinalidades (minimo,maximo). 10 entidades y 11 interrelaciones (D-52: sin Intervalo ni
# 'presenta'); los atributos no se dibujan. Las posiciones son las del .tex.
# 'agrupa' (Grupo-Espécimen) es una interrelacion derivada (D-92): va punteada, no se guarda en la base.
esc = html.escape
SX, SY, OX, OY = 56, 47, 60, 62        # px por cm del .tex y desplazamiento

# nombre: (x, y, tipo, etiqueta)   tipo: ent, rel, att   (coordenadas del .tex)
P = {
    'usuario': (0.7, -0.9, 'ent', 'Usuario'), 'registra': (3.75, -0.9, 'rel', 'registra'),
    'experim': (7.4, -0.9, 'ent', 'Experimento'), 'compone': (7.4, -2.3, 'rel', 'compone'),
    'grupo': (7.4, -3.7, 'ent', 'Grupo'),
    'agrupa': (3.6, -5.1, 'rel', 'agrupa'), 'grabaen': (11.1, -5.1, 'rel', 'se graba en'),
    'especimen': (3.6, -6.5, 'ent', 'Espécimen'), 'aloja': (7.4, -6.5, 'rel', 'aloja'),
    'tanda': (11.1, -6.5, 'ent', 'Tanda'), 'produce': (11.1, -7.9, 'rel', 'produce'),
    'video': (11.1, -9.3, 'ent', 'Video'), 'procesa': (14.5, -9.3, 'rel', 'procesa'),
    'analisis': (17.6, -9.3, 'ent', 'Análisis'),
    'aparece': (3.6, -10.6, 'rel', 'aparece en'), 'contiene': (11.1, -10.6, 'rel', 'contiene'),
    'observ': (7.4, -12.0, 'ent', 'Observación'),
    'conducta': (11.1, -14.8, 'ent', 'Conducta'),
    'etiqueta': (3.6, -13.4, 'rel', 'se etiqueta en'), 'segundo': (3.6, -14.8, 'ent', 'Segundo'),
    'clasifica': (7.4, -14.8, 'rel', 'se clasifica como'),
}
DIM = {'ent': (150, 38), 'rel': (112, 50), 'att': (104, 32)}
N = {k: dict(cx=OX + x * SX, cy=OY - y * SY, t=t, lab=l, w=DIM[t][0], h=DIM[t][1]) for k, (x, y, t, l) in P.items()}
# las interrelaciones con etiqueta de dos lineas son un poco mas grandes
for k in ('etiqueta', 'clasifica', 'grabaen', 'aparece'):
    N[k]['w'] = 124

def a(n, lado):
    d = N[n]; x, y = d['cx'], d['cy']
    if lado == 'e': return (x + d['w'] / 2, y)
    if lado == 'w': return (x - d['w'] / 2, y)
    if lado == 'n': return (x, y - d['h'] / 2)
    if lado == 's': return (x, y + d['h'] / 2)

out = []
cards = []

def linea(pts, dash=False):
    d = 'M' + ' L'.join(f'{x:.0f},{y:.0f}' for x, y in pts)
    out.append(f'<path d="{d}" fill="none" stroke="#1a1a1a" stroke-width="1.2"' + (' stroke-dasharray="4,3"' if dash else '') + '/>')

def card(texto, p, q, pos, lado):
    """Etiqueta (min,max) sobre el segmento p->q a la fraccion pos; lado: arriba/abajo/izq/der."""
    x = p[0] + (q[0] - p[0]) * pos; y = p[1] + (q[1] - p[1]) * pos
    if lado == 'arriba': cards.append((texto, x, y - 6, 'middle'))
    elif lado == 'abajo': cards.append((texto, x, y + 13, 'middle'))
    elif lado == 'der': cards.append((texto, x + 6, y + 3, 'start'))
    elif lado == 'izq': cards.append((texto, x - 6, y + 3, 'end'))

def tramo(p, q, texto, pos, lado):
    linea([p, q]); card(texto, p, q, pos, lado)

# -- Usuario registra Experimento
tramo(a('usuario', 'e'), a('registra', 'w'), '(0,N)', .35, 'arriba')
tramo(a('registra', 'e'), a('experim', 'w'), '(1,1)', .65, 'arriba')
# -- Experimento se compone de Grupos (minimo tres: control, referencia y tratamiento)
tramo(a('experim', 's'), a('compone', 'n'), '(3,N)', .5, 'der')
tramo(a('compone', 's'), a('grupo', 'n'), '(1,1)', .5, 'der')
# -- Grupo: bus hacia 'agrupa' (espécimen) y 'se graba en' (tanda)
g = a('grupo', 's'); bus_y = g[1] + 16
linea([g, (g[0], bus_y)])
linea([(g[0], bus_y), (a('agrupa', 'n')[0], bus_y), a('agrupa', 'n')], dash=True)   # derivada (D-92)
linea([(g[0], bus_y), (a('grabaen', 'n')[0], bus_y), a('grabaen', 'n')])
cards.append(('(2,N)', a('agrupa', 'n')[0] - 6, a('agrupa', 'n')[1] - 8, 'end'))
cards.append(('(1,N)', a('grabaen', 'n')[0] + 6, a('grabaen', 'n')[1] - 8, 'start'))
linea([a('agrupa', 's'), a('especimen', 'n')], dash=True)
card('(1,1)', a('agrupa', 's'), a('especimen', 'n'), .5, 'der')
tramo(a('grabaen', 's'), a('tanda', 'n'), '(1,1)', .5, 'der')
# -- Tanda aloja Espécimenes (2,4)
tramo(a('especimen', 'e'), a('aloja', 'w'), '(1,1)', .3, 'arriba')
tramo(a('aloja', 'e'), a('tanda', 'w'), '(2,4)', .7, 'arriba')
# -- Tanda produce Videos (1,2): el Día 1 es opcional
tramo(a('tanda', 's'), a('produce', 'n'), '(1,2)', .5, 'der')
tramo(a('produce', 's'), a('video', 'n'), '(1,1)', .5, 'der')
# -- Video se procesa en Análisis (0,1): el Día 1 no se analiza
tramo(a('video', 'e'), a('procesa', 'w'), '(0,1)', .35, 'arriba')
tramo(a('procesa', 'e'), a('analisis', 'w'), '(1,1)', .65, 'arriba')
# -- Espécimen aparece en Observaciones (0,1)
tramo(a('especimen', 's'), a('aparece', 'n'), '(0,1)', .6, 'der')
ap = a('aparece', 's'); ow = a('observ', 'w')
linea([ap, (ap[0], ow[1]), ow]); card('(1,1)', (ap[0], ow[1]), ow, .72, 'arriba')
# -- Video contiene Observaciones (0,4)
tramo(a('video', 's'), a('contiene', 'n'), '(0,4)', .6, 'der')
co = a('contiene', 's'); oe = a('observ', 'e')
linea([co, (co[0], oe[1]), oe]); card('(1,1)', (co[0], oe[1]), oe, .72, 'arriba')
# -- Observación se etiqueta en Segundos (1,300) y cada segundo se clasifica como Conducta
o_sw = (N['observ']['cx'] - 50, N['observ']['cy'] + N['observ']['h'] / 2)
linea([o_sw, a('etiqueta', 'e')]); card('(1,300)', o_sw, a('etiqueta', 'e'), .5, 'der')
tramo(a('etiqueta', 's'), a('segundo', 'n'), '(1,1)', .5, 'der')
tramo(a('segundo', 'e'), a('clasifica', 'w'), '(0,1)', .5, 'arriba')
tramo(a('clasifica', 'e'), a('conducta', 'w'), '(0,N)', .5, 'arriba')

# ---- figuras ----
def partir(t):
    if t in ('se etiqueta en', 'se clasifica como'):
        i = t.rfind(' ')
        return [t[:i], t[i + 1:]]
    return [t]

for k, d in N.items():
    x, y, w, h = d['cx'], d['cy'], d['w'], d['h']
    lines = partir(d['lab'])
    if d['t'] == 'ent':
        out.append(f'<rect x="{x-w/2:.0f}" y="{y-h/2:.0f}" width="{w}" height="{h}" rx="3" fill="#faf9f5" stroke="#1a1a1a" stroke-width="1.4"/>')
    elif d['t'] == 'rel':
        out.append(f'<polygon points="{x:.0f},{y-h/2:.0f} {x+w/2:.0f},{y:.0f} {x:.0f},{y+h/2:.0f} {x-w/2:.0f},{y:.0f}" fill="#ece7d8" stroke="#1a1a1a" stroke-width="1.2"' + (' stroke-dasharray="4,3"' if k == 'agrupa' else '') + '/>')
    else:
        out.append(f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{w/2}" ry="{h/2}" fill="#faf9f5" stroke="#1a1a1a" stroke-dasharray="4,3" stroke-width="1.2"/>')
    cls = 'nm' if d['t'] == 'ent' else 'rl'
    for i, l in enumerate(lines):
        yy = y + 4 - (len(lines) - 1) * 5.5 + i * 11
        out.append(f'<text x="{x:.0f}" y="{yy:.0f}" text-anchor="middle" class="{cls}">{esc(l)}</text>')

ag = N['agrupa']
out.append(f'<text x="{ag["cx"] - ag["w"] / 2 - 8:.0f}" y="{ag["cy"] + 3:.0f}" text-anchor="end" class="rl" style="font-style:italic">derivada de Tanda</text>')
for texto, x, y, anc in cards:
    out.append(f'<text x="{x:.0f}" y="{y:.0f}" text-anchor="{anc}" class="m">{texto}</text>')

W = int(OX + 17.6 * SX + 110)
H = int(OY + 14.8 * SY + 142)
ly = H - 60
leg = f'''<g transform="translate(40,{ly})" class="lg">
<rect x="0" y="-8" width="26" height="16" rx="2" fill="#faf9f5" stroke="#1a1a1a" stroke-width="1.4"/><text x="36" y="3">ENTIDAD</text>
<polygon points="150,0 163,-8 176,0 163,8" fill="#ece7d8" stroke="#1a1a1a"/><text x="186" y="3">INTERRELACIÓN</text>
<text x="340" y="3" style="font-weight:600;fill:#000">(mín,máx)</text><text x="410" y="3">CARDINALIDAD</text>
<polygon points="540,0 553,-8 566,0 553,8" fill="#ece7d8" stroke="#1a1a1a" stroke-dasharray="3,2"/><text x="576" y="3">INTERRELACIÓN DERIVADA</text>
</g>'''
svg = f'''<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="co-title co-desc" xmlns="http://www.w3.org/2000/svg">
<title id="co-title">Esquema conceptual</title>
<desc id="co-desc">Modelo entidad-relación con las 10 entidades del sistema y sus 11 interrelaciones, con cardinalidades mínima y máxima.</desc>
<style>
.nm{{font:600 12px Geist,sans-serif;fill:#1a1a1a}}
.rl{{font:400 9px 'Geist Mono',monospace;fill:#1a1a1a}}
.m{{font:600 10px 'Geist Mono',monospace;fill:#000}}
.lg text{{font:400 9px 'Geist Mono',monospace;fill:#6b6b6b}}
</style>
{chr(10).join(out)}
{leg}
</svg>'''
page = f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Esquema conceptual</title>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;600&family=Geist+Mono:wght@400&display=swap" rel="stylesheet">
<style>
html,body{{margin:0;background:#faf9f5}}
svg{{display:block;width:{W}px;height:{H}px}}
</style></head><body>{svg}</body></html>'''
open(sys.argv[1], 'w', encoding='utf-8').write(page)
print('ok', W, 'x', H)
