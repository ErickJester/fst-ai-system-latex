import math, html, sys

# Esquema LÓGICO (grafo relacional) en UNA hoja vertical para carta (ancho de \textwidth = 15.6 cm).
# Letra de 15 px CSS. Cardinalidad en notación de pata de gallo (crow's foot).
# Uso: python gen_esquema_v4.py SALIDA.html [GAPV]

esc = html.escape
CH = 9.0     # ancho de carácter de Geist Mono a 15 px (0.6 em)
import os
LH = int(os.environ.get('LH', 28))
HEAD = int(os.environ.get('HEAD', 38))
NX = 56      # sangría del nombre de columna
GAPV = int(sys.argv[2]) if len(sys.argv) > 2 else 130   # separación vertical entre tablas
GAPC = int(os.environ.get('GAPC', 260))
Y0 = 26
X0 = 52

OUT = sys.argv[1]

# (marca, nombre, tipo) ; restricciones ; soporte del sistema
# Datos de diagramas/grafo_relacional_3_vigente.puml (los mismos atributos que el físico, sin tipos) (12 tablas, 13 FK, dominios).
DATA = {
    'USUARIOS': ([('PK', 'id', ''), ('', 'correo', ''), ('', 'contrasena_hash', ''), ('', 'nombre', ''),
                  ('', 'rol', ''), ('', 'activo', ''), ('', 'debe_cambiar_contrasena', ''),
                  ('', 'creado_en', ''), ('', 'ultimo_acceso', '')], [], False),
    'NOTIFICACIONES': ([('PK', 'id', ''), ('FK', 'id_usuario', ''), ('FK', 'id_experimento', ''),
                        ('', 'creado_en', ''), ('', 'tipo', ''), ('', 'mensaje', ''), ('', 'leido', '')], [], True),
    'SUJETOS': ([('PK', 'id', ''), ('FK', 'id_experimento', ''), ('', 'indice_rata', ''),
                 ('', 'etiqueta', '')], [], False),
    'ROIS': ([('PK', 'id', ''), ('FK', 'id_video', ''), ('FK', 'id_sujeto', ''), ('', 'x', ''), ('', 'y', ''),
              ('', 'w', ''), ('', 'h', '')], [], False),
    'EXPERIMENTOS': ([('PK', 'id', ''), ('FK', 'id_usuario', ''), ('', 'creado_en', ''), ('', 'nombre', ''),
                      ('', 'fecha_experimento', ''), ('', 'tratamiento', ''), ('', 'especie', ''),
                      ('', 'disposicion', ''), ('', 'notas', '')], [], False),
    'VIDEOS': ([('PK', 'id', ''), ('FK', 'id_experimento', ''), ('', 'creado_en', ''), ('', 'dia', ''),
                ('', 'nombre_archivo', ''), ('', 'ruta', ''), ('', 'duracion_s', ''),
                ('', 'fecha_eliminacion', '')], [], False),
    'TRABAJOS': ([('PK', 'id', ''), ('FK', 'id_video', ''), ('FK', 'id_config', ''), ('', 'creado_en', ''),
                  ('', 'iniciado_en', ''), ('', 'finalizado_en', ''), ('', 'estado', ''), ('', 'etapa', ''),
                  ('', 'progreso_pct', ''), ('', 'error', '')], [], False),
    'ANIMALES': ([('PK', 'id', ''), ('FK', 'id_trabajo', ''), ('FK', 'id_sujeto', '')], [], False),
    'RESULTADOS_COMPORTAMIENTO': ([('PK', 'id', ''), ('FK', 'id_animal', ''), ('', 'nado_s', ''),
                                   ('', 'inmovil_s', ''), ('', 'escape_s', ''), ('', 'total_analizado_s', '')],
                                  [], False),
    'REPORTES': ([('PK', 'id', ''), ('FK', 'id_experimento', ''), ('', 'creado_en', ''), ('', 'formato', ''),
                  ('', 'ruta', '')], [], True),
    'CONFIGURACIONES_ANALISIS': ([('PK', 'id', ''), ('', 'creado_en', ''), ('', 'nombre_modelo', ''),
                                  ('', 'hash_modelo', ''), ('', 'version_pipeline', ''),
                                  ('', 'umbral_confianza', ''), ('', 'segundos_omitir', ''),
                                  ('', 'umbral_inmovil', ''), ('', 'umbral_desplazamiento', ''),
                                  ('', 'umbral_std_posicion', ''), ('', 'umbral_aspecto_trepada', '')], [], False),
    'COMPORTAMIENTO_POR_MINUTO': ([('PK', 'id', ''), ('FK', 'id_animal', ''), ('', 'minuto', ''),
                                   ('', 'nado_s', ''), ('', 'inmovil_s', ''), ('', 'escape_s', '')], [], False),
}

# Grafo lógico: sin tipos de dato. Solo se anota «nulo»; UK pasa a AK (llave alterna); se quitan las restricciones CK.
for _n, (_cols, _cons, _sop) in list(DATA.items()):
    _c2 = [(m.replace('UK', 'AK'), nm, 'nulo' if 'nulo' in ty else '') for m, nm, ty in _cols]
    _k2 = [c.replace('UK', 'AK') for c in _cons if not c.startswith('CK')]
    DATA[_n] = (_c2, _k2, _sop)

COLS = [['USUARIOS', 'NOTIFICACIONES', 'SUJETOS', 'ROIS'],
        ['EXPERIMENTOS', 'VIDEOS', 'TRABAJOS', 'ANIMALES', 'RESULTADOS_COMPORTAMIENTO'],
        ['REPORTES', 'CONFIGURACIONES_ANALISIS', 'COMPORTAMIENTO_POR_MINUTO']]

def tw(n):
    cols, cons, _ = DATA[n]
    w = max(len(n) * 13.5 + 30, 190)
    for m, nm, ty in cols:
        w = max(w, NX + (len(nm) + len(ty)) * CH + 16)
    for c in cons:
        w = max(w, len(c) * CH + 24)
    return math.ceil(w)

def th(n):
    cols, cons, _ = DATA[n]
    h = HEAD + len(cols) * LH + 8
    if cons:
        h += len(cons) * LH + 6
    return h

T = {}
colx, colw, colbot = [], [], []
x = X0
for names in COLS:
    colx.append(x)
    colw.append(max(tw(n) for n in names))
    x += colw[-1] + GAPC
for ci, names in enumerate(COLS):
    y = Y0
    for n in names:
        cols, cons, soporte = DATA[n]
        T[n] = dict(x=colx[ci], y=y, w=colw[ci], h=th(n), cols=cols, cons=cons, soporte=soporte)
        y += th(n) + GAPV
    colbot.append(y - GAPV)

def ry(n, field):
    i = [c[1] for c in T[n]['cols']].index(field)
    return T[n]['y'] + HEAD + i * LH + 11

def Lr(n, f): return (T[n]['x'], ry(n, f))
def Rr(n, f): return (T[n]['x'] + T[n]['w'], ry(n, f))
def Tc(n): return (T[n]['x'] + T[n]['w'] // 2, T[n]['y'])
def Bc(n): return (T[n]['x'] + T[n]['w'] // 2, T[n]['y'] + T[n]['h'])

gap01 = colx[1] - GAPC // 2
gap12 = colx[2] - GAPC // 2
lx = colx[0] - 14

PALETA = ['#1b6fb0', '#2e8b57', '#8e44ad', '#c0392b', '#b8860b', '#16a085', '#d35400', '#e84393',
          '#34495e', '#6c8e00', '#0097a7', '#a0522d', '#5e35b1']
edges = []
def edge(pts, child, parent, rng=None):
    edges.append(dict(pts=pts, child=child, parent=parent, rng=rng, color=PALETA[len(edges) % len(PALETA)]))

# Notación de pata de gallo. child = cardinalidad del lado hijo (muchos), parent = lado padre (uno).
# one = exactamente uno; zo = cero o uno; om = uno o más; zm = cero o más.
# rng = rango que la pata de gallo no expresa; se escribe en letra chica junto al símbolo.
edge([Lr('EXPERIMENTOS', 'id_usuario'), (gap01 - 24, ry('EXPERIMENTOS', 'id_usuario')),
      (gap01 - 24, ry('USUARIOS', 'id')), Rr('USUARIOS', 'id')], 'zm', 'one')
edge([Lr('NOTIFICACIONES', 'id_usuario'), (lx, ry('NOTIFICACIONES', 'id_usuario')),
      (lx, ry('USUARIOS', 'id')), Lr('USUARIOS', 'id')], 'zm', 'one')
edge([Rr('NOTIFICACIONES', 'id_experimento'), (gap01 + 1, ry('NOTIFICACIONES', 'id_experimento')),
      (gap01 + 1, ry('EXPERIMENTOS', 'id')), Lr('EXPERIMENTOS', 'id')], 'zm', 'one')
edge([Rr('SUJETOS', 'id_experimento'), (gap01 + 26, ry('SUJETOS', 'id_experimento')),
      (gap01 + 26, ry('EXPERIMENTOS', 'id')), Lr('EXPERIMENTOS', 'id')], 'zm', 'one')
edge([Lr('REPORTES', 'id_experimento'), (gap12 - 20, ry('REPORTES', 'id_experimento')),
      (gap12 - 20, ry('EXPERIMENTOS', 'id')), Rr('EXPERIMENTOS', 'id')], 'zm', 'one')
edge([Tc('VIDEOS'), Bc('EXPERIMENTOS')], 'zm', 'one')
edge([Tc('ROIS'), Bc('SUJETOS')], 'zm', 'one')
edge([Rr('ROIS', 'id_video'), (gap01 - 48, ry('ROIS', 'id_video')),
      (gap01 - 48, ry('VIDEOS', 'id')), Lr('VIDEOS', 'id')], 'zm', 'one')
edge([Tc('TRABAJOS'), Bc('VIDEOS')], 'zm', 'one')
edge([Rr('TRABAJOS', 'id_config'), (gap12 + 14, ry('TRABAJOS', 'id_config')),
      (gap12 + 14, ry('CONFIGURACIONES_ANALISIS', 'id')), Lr('CONFIGURACIONES_ANALISIS', 'id')], 'zm', 'one')
edge([Tc('ANIMALES'), Bc('TRABAJOS')], 'zm', 'one')
edge([Lr('ANIMALES', 'id_sujeto'), (gap01 - 72, ry('ANIMALES', 'id_sujeto')),
      (gap01 - 72, ry('SUJETOS', 'id')), Rr('SUJETOS', 'id')], 'zm', 'one')
edge([Tc('RESULTADOS_COMPORTAMIENTO'), Bc('ANIMALES')], 'zm', 'one')
edge([Lr('COMPORTAMIENTO_POR_MINUTO', 'id_animal'), (gap12 - 44, ry('COMPORTAMIENTO_POR_MINUTO', 'id_animal')),
      (gap12 - 44, ry('ANIMALES', 'id')), Rr('ANIMALES', 'id')], 'zm', 'one')

out = []
LABELS = ['id_usuario', 'id_usuario', 'id_experimento', 'id_experimento', 'id_experimento', 'id_experimento',
          'id_sujeto', 'id_video', 'id_video', 'id_config', 'id_trabajo', 'id_sujeto', 'id_animal', 'id_animal']
CH_TXT = {'zm': '0..*', 'om': '1..*', 'zo': '0..1'}
PA_TXT = {'one': '1', 'zo': '0..1'}

def tag(x, y, txt, color, anchor='middle', bg=True):
    w = len(txt) * 6.9 + 6
    x0 = x - w / 2 if anchor == 'middle' else (x if anchor == 'start' else x - w)
    if bg:
        out.append(f'<rect x="{x0:.1f}" y="{y-11:.1f}" width="{w:.1f}" height="15" fill="#faf9f5"/>')
    out.append(f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" class="rl" fill="{color}">{esc(txt)}</text>')

def punta(p, q, color):
    ux, uy = unit(p, q)
    vx, vy = -uy, ux
    b = (p[0] + ux * 10, p[1] + uy * 10)
    out.append(f'<path d="M{p[0]:.1f},{p[1]:.1f} L{b[0]+vx*5:.1f},{b[1]+vy*5:.1f} L{b[0]-vx*5:.1f},{b[1]-vy*5:.1f} Z" fill="{color}"/>')

def unit(a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]; n = math.hypot(dx, dy) or 1
    return dx / n, dy / n

def extremo(p, q, txt, color):
    ux, uy = unit(p, q)
    if abs(uy) > abs(ux):   # tramo vertical: el número va a la izquierda de la línea
        tag(p[0] - 7, p[1] + uy * 18 + 4, txt, color, 'end')
    else:                   # tramo horizontal: el número va arriba
        tag(p[0] + ux * 22, p[1] - 8, txt, color, 'middle')

def etiqueta_fk(a, b, txt, color, t=0.5):
    mx, my = a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t
    w = len(txt) * 6.9 + 6
    if abs(b[0] - a[0]) < 1:   # vertical
        if abs(b[1] - a[1]) < 90:   # tramo corto entre tablas: a la derecha de la línea
            tag(mx + 8, my + 4, txt, color, 'start')
        else:                        # canal largo: texto girado sobre la línea
            out.append(f'<g transform="rotate(-90 {mx:.1f} {my:.1f})"><rect x="{mx-w/2:.1f}" y="{my-11:.1f}" width="{w:.1f}" height="15" fill="#faf9f5"/>'
                       f'<text x="{mx:.1f}" y="{my+1:.1f}" text-anchor="middle" class="rl" fill="{color}">{esc(txt)}</text></g>')
    else:
        tag(mx, my + 4, txt, color)

for e in edges:
    d = 'M' + ' L'.join(f'{x},{y}' for x, y in e['pts'])
    out.append(f'<path d="{d}" fill="none" stroke="{e["color"]}" stroke-width="1.5"/>')
for k, e in enumerate(edges):
    pts = e['pts']
    punta(pts[-1], pts[-2], e['color'])

BADGE = {'PK': '#d9532c', 'PK FK': '#d9532c', 'FK': '#1a1a1a', 'FK UK': '#1a1a1a', 'UK': '#6b6b6b', 'AK': '#6b6b6b', 'FK AK': '#1a1a1a', 'PK FK': '#d9532c'}
for n, t in T.items():
    x, y, w, h = t['x'], t['y'], t['w'], t['h']
    fill = '#ece7d8' if t['soporte'] else '#faf9f5'
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="#1a1a1a" stroke-width="1"/>')
    out.append(f'<text x="{x + w/2}" y="{y + 26}" text-anchor="middle" class="nm">{n}</text>')
    out.append(f'<line x1="{x}" y1="{y+HEAD}" x2="{x+w}" y2="{y+HEAD}" stroke="#1a1a1a"/>')
    for i, (m, nm, ty) in enumerate(t['cols']):
        by = y + HEAD + 16 + i * LH
        if m:
            out.append(f'<text x="{x+4}" y="{by}" class="b" fill="{BADGE[m]}">{m}</text>')
        out.append(f'<text x="{x+NX}" y="{by}" class="a">{esc(nm)}</text>')
        out.append(f'<text x="{x+w-10}" y="{by}" text-anchor="end" class="ty">{esc(ty)}</text>')
    if t['cons']:
        cy = y + HEAD + len(t['cols']) * LH + 4
        out.append(f'<line x1="{x+8}" y1="{cy}" x2="{x+w-8}" y2="{cy}" stroke="#6b6b6b" stroke-dasharray="3,3"/>')
        for k, c in enumerate(t['cons']):
            out.append(f'<text x="{x+10}" y="{cy+16+k*LH}" class="ty">{esc(c)}</text>')

def legend(x, y, w):
    texto = [('PK', '#d9532c', 'llave primaria'), ('FK', '#1a1a1a', 'llave foránea')]
    h = 52 + (len(texto) + 2) * LH + 14
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="#faf9f5" stroke="#6b6b6b" stroke-dasharray="4,3"/>')
    out.append(f'<text x="{x+12}" y="{y+28}" class="nm">Leyenda</text>')
    by = y + 52
    for k, c, v in texto:
        out.append(f'<text x="{x+12}" y="{by}" class="b" fill="{c}">{k}</text>')
        out.append(f'<text x="{x+62}" y="{by}" class="ty">{esc(v)}</text>')
        by += LH
    out.append(f'<text x="{x+12}" y="{by}" class="ty">Flecha: hijo → padre</text>')
    by += LH
    out.append(f'<rect x="{x+12}" y="{by-12}" width="26" height="14" rx="3" fill="#ece7d8" stroke="#1a1a1a"/>')
    out.append(f'<text x="{x+56}" y="{by}" class="ty">de soporte</text>')
    by += LH
    return y + h

lg_bottom = legend(colx[0], colbot[0] + GAPV, colw[0])
H = int(max(max(colbot), lg_bottom) + 22)
W = int(colx[2] + colw[2] + X0)
MARCADORES = ''
CSS = (".a{font:400 15px 'Geist Mono',monospace;fill:#1a1a1a}"
       ".ty{font:400 15px 'Geist Mono',monospace;fill:#6b6b6b}"
       ".b{font:600 15px 'Geist Mono',monospace}"
       ".rl{font:400 11px 'Geist Mono',monospace}"
       ".nm{font:600 18px Geist,sans-serif;fill:#1a1a1a}")
svg = (f'<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="es-title es-desc" xmlns="http://www.w3.org/2000/svg">\n'
       f'<title id="es-title">Modelo de datos del TT1 (grafo relacional)</title>\n'
       f'<desc id="es-desc">Las 12 relaciones del modelo de datos del TT1 con sus atributos, llaves y cardinalidades.</desc>\n'
       f'<style>{CSS}</style>\n' + chr(10).join(out) + '\n</svg>')
page = ('<!doctype html>\n<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<title>Modelo de datos del TT1</title>\n'
        '<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;600&family=Geist+Mono:wght@400;600&display=swap" rel="stylesheet">\n'
        '<style>html,body{margin:0;background:#faf9f5}svg{display:block;width:' + str(W) + 'px;height:' + str(H) + 'px}</style>\n'
        '</head><body>' + svg + '</body></html>')
open(OUT, 'w', encoding='utf-8').write(page)
print('W', W, 'H', H, 'letra_cm', round(15 * 15.6 / W, 3), 'alto_cm', round(H * 15.6 / W, 2))
