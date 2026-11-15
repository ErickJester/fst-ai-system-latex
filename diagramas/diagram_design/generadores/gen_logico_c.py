import math, html, sys, os

# Esquema LÓGICO (grafo relacional) en UNA hoja vertical para carta (ancho de \textwidth = 15.6 cm).
# Letra de 15 px CSS. Cardinalidad en notación de pata de gallo (crow's foot).
# Uso: python gen_esquema_v4.py SALIDA.html [GAPV]

esc = html.escape
CH = 9.0     # ancho de carácter de Geist Mono a 15 px (0.6 em)
LH = int(os.environ.get('LH', 28))
HEAD = int(os.environ.get('HEAD', 38))
NX = int(os.environ.get('NX', 56))
GAPV = int(os.environ.get('GAPV', 60))
GAPC = int(os.environ.get('GAPC', 150))
Y0 = int(os.environ.get('Y0', 26))
X0 = int(os.environ.get('X0', 52))

OUT = sys.argv[1]
ES = float(os.environ.get('ES', 1))

# (marca, nombre, tipo) ; restricciones ; soporte del sistema
# Datos de diagramas/grafo_relacional_3_vigente.puml (los mismos atributos que el físico, sin tipos) (12 tablas, 13 FK, dominios).
DATA = {
    'USUARIO': ([('PK', 'idInstitucional', 'varchar(10)'), ('', 'nombre', 'varchar(100)'),
                 ('', 'apellidos', 'varchar(100)'), ('UK', 'correo', 'varchar(254)'),
                 ('', 'contrasenaHash', 'varchar(255)'), ('', 'activo', 'boolean'),
                 ('', 'cambioRequerido', 'boolean')], [], False),
    'ADMINISTRADOR': ([('PK FK', 'idInstitucional', 'varchar(10)')], [], False),
    'NOTIFICACION': ([('PK', 'idNotificacion', 'integer'), ('FK', 'idInstitucional', 'varchar(10)'),
                      ('FK', 'idExperimento', 'integer · nulo'), ('', 'tipo', 'tipo_notificacion'),
                      ('', 'mensaje', 'text'), ('', 'leido', 'boolean'),
                      ('', 'fechaCreacion', 'timestamptz')], [], True),
    'REPORTE': ([('PK', 'idReporte', 'integer'), ('FK', 'idExperimento', 'integer'),
                 ('', 'formato', 'formato_reporte'), ('UK', 'ruta', 'text'),
                 ('', 'fechaGeneracion', 'timestamptz')], [], True),
    'EXPERIMENTO': ([('PK', 'idExperimento', 'integer'), ('FK', 'idInstitucional', 'varchar(10)'),
                     ('UK', 'nombre', 'varchar(150)'), ('', 'fecha', 'date'),
                     ('', 'notas', 'text · nulo')], [], False),
    'GRUPO': ([('PK', 'idGrupo', 'integer'), ('FK', 'idExperimento', 'integer'),
               ('', 'etiqueta', 'varchar(100)'), ('', 'tipo', 'tipo_grupo'),
               ('', 'tratamiento', 'text')], ['UK (idExperimento, etiqueta)'], False),
    'TANDA': ([('PK', 'idTanda', 'integer'), ('FK', 'idGrupo', 'integer'),
               ('', 'ordinal', 'smallint'), ('', 'nCilindros', 'smallint')],
              ['UK (idGrupo, ordinal)'], False),
    'ESPECIMEN': ([('PK', 'idEspecimen', 'integer'), ('FK', 'idTanda', 'integer'),
                   ('', 'numeroCilindro', 'smallint')], ['UK (idTanda, numeroCilindro)'], False),
    'OBSERVACION': ([('PK', 'idObservacion', 'integer'), ('FK', 'idEspecimen', 'integer'),
                     ('FK', 'idVideo', 'integer')], ['UK (idEspecimen, idVideo)'], False),
    'VIDEO': ([('PK', 'idVideo', 'integer'), ('FK', 'idTanda', 'integer'),
               ('', 'sesion', 'sesion_video'), ('', 'archivo', 'text · nulo'),
               ('', 'nombreOriginal', 'varchar(255) · nulo'), ('', 'duracion', 'numeric(8,2)'),
               ('', 'fechaCarga', 'timestamptz')], ['UK (idTanda, sesion)'], False),
    'ANALISIS': ([('PK', 'idAnalisis', 'integer'), ('FK UK', 'idVideo', 'integer'),
                  ('', 'estado', 'estado_analisis'), ('', 'etapa', 'etapa_analisis'),
                  ('', 'nivelClasif', 'nivel_clasif_analisis'), ('', 'fechaAnalisis', 'timestamptz'),
                  ('', 'rutaDiagnostico', 'text · nulo')], [], False),
    'SEGUNDO': ([('PK FK', 'idObservacion', 'integer'), ('PK', 'segundo', 'smallint'),
                 ('', 'conducta', 'tipo_conducta · nulo'), ('', 'origen', 'origen_segundo')],
                ['CK segundo entre 1 y 300'], False),
}


# Grafo lógico: sin tipos de dato. Solo se anota «nulo»; UK pasa a AK (llave alterna); se quitan las restricciones CK.
for _n, (_cols, _cons, _sop) in list(DATA.items()):
    if os.environ.get('NOAK'):
        _c2 = [(m.replace('UK', '').strip(), nm, 'nulo' if 'nulo' in ty else '') for m, nm, ty in _cols]
        _k2 = [c for c in _cons if not c.startswith('CK') and not c.startswith('UK')]
    else:
        _c2 = [(m.replace('UK', 'AK'), nm, 'nulo' if 'nulo' in ty else '') for m, nm, ty in _cols]
        _k2 = [c.replace('UK', 'AK') for c in _cons if not c.startswith('CK')]
    DATA[_n] = (_c2, _k2, _sop)

COLS = [['USUARIO', 'ADMINISTRADOR', 'NOTIFICACION', 'REPORTE'],
        ['EXPERIMENTO', 'GRUPO', 'TANDA', 'ESPECIMEN', 'OBSERVACION'],
        ['VIDEO', 'ANALISIS', 'SEGUNDO']]

import json
if os.environ.get('COLS_JSON'):
    COLS = json.loads(os.environ['COLS_JSON'])

def tw(n):
    cols, cons, _ = DATA[n]
    w = max(len(n) * float(os.environ.get('NM', 11)) + 24, 190)
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
lx = colx[0] - round(14 * ES)

PALETA = ['#1b6fb0', '#2e8b57', '#8e44ad', '#c0392b', '#b8860b', '#16a085', '#d35400', '#e84393',
          '#34495e', '#6c8e00', '#0097a7', '#a0522d', '#5e35b1']
edges = []
def edge(pts, child, parent, rng=None):
    edges.append(dict(pts=pts, child=child, parent=parent, rng=rng, color=PALETA[len(edges) % len(PALETA)]))

# Notación de pata de gallo. child = cardinalidad del lado hijo (muchos), parent = lado padre (uno).
# one = exactamente uno; zo = cero o uno; om = uno o más; zm = cero o más.
# rng = rango que la pata de gallo no expresa; se escribe en letra chica junto al símbolo.
edge([Lr('EXPERIMENTO', 'idInstitucional'), (gap01 - round(24 * ES), ry('EXPERIMENTO', 'idInstitucional')),
      (gap01 - round(24 * ES), ry('USUARIO', 'idInstitucional')), Rr('USUARIO', 'idInstitucional')], 'zm', 'one')
edge([Lr('NOTIFICACION', 'idInstitucional'), (lx, ry('NOTIFICACION', 'idInstitucional')),
      (lx, ry('USUARIO', 'idInstitucional')), Lr('USUARIO', 'idInstitucional')], 'zm', 'one')
edge([Tc('ADMINISTRADOR'), Bc('USUARIO')], 'zo', 'one')
edge([Rr('REPORTE', 'idExperimento'), (gap01 + round(26 * ES), ry('REPORTE', 'idExperimento')),
      (gap01 + round(26 * ES), ry('EXPERIMENTO', 'idExperimento')), Lr('EXPERIMENTO', 'idExperimento')], 'zm', 'one')
edge([Rr('NOTIFICACION', 'idExperimento'), (gap01 + round(1 * ES), ry('NOTIFICACION', 'idExperimento')),
      (gap01 + round(1 * ES), ry('EXPERIMENTO', 'idExperimento')), Lr('EXPERIMENTO', 'idExperimento')], 'zm', 'zo')
edge([Tc('GRUPO'), Bc('EXPERIMENTO')], 'zm', 'one')
edge([Tc('TANDA'), Bc('GRUPO')], 'om', 'one')
edge([Tc('ESPECIMEN'), Bc('TANDA')], 'om', 'one', '2..4')
edge([Tc('OBSERVACION'), Bc('ESPECIMEN')], 'zo', 'one')
edge([Rr('OBSERVACION', 'idVideo'), (gap12 - round(30 * ES), ry('OBSERVACION', 'idVideo')),
      (gap12 - round(30 * ES), ry('VIDEO', 'idVideo')), Lr('VIDEO', 'idVideo')], 'zm', 'one', '0..4')
edge([Lr('VIDEO', 'idTanda'), (gap12 + round(14 * ES), ry('VIDEO', 'idTanda')),
      (gap12 + round(14 * ES), ry('TANDA', 'idTanda')), Rr('TANDA', 'idTanda')], 'om', 'one', '1..2')
edge([Tc('ANALISIS'), Bc('VIDEO')], 'zo', 'one')
edge([Lr('SEGUNDO', 'idObservacion'), (gap12 - round(8 * ES), ry('SEGUNDO', 'idObservacion')),
      (gap12 - round(8 * ES), ry('OBSERVACION', 'idObservacion')), Rr('OBSERVACION', 'idObservacion')], 'om', 'one', '1..300')

out = []
LABELS = ['idInstitucional', 'idInstitucional', 'idInstitucional', 'idExperimento', 'idExperimento', 'idExperimento',
          'idGrupo', 'idTanda', 'idEspecimen', 'idVideo', 'idTanda', 'idVideo', 'idObservacion']
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
    rc = e['rng'] or CH_TXT[e['child']]
    extremo(pts[0], pts[1], rc, e['color'])
    extremo(pts[-1], pts[-2], PA_TXT[e['parent']], e['color'])
    tramos = [(math.hypot(pts[i+1][0]-pts[i][0], pts[i+1][1]-pts[i][1]), i) for i in range(len(pts)-1)]
    _, ix = max(tramos)
    etiqueta_fk(pts[ix], pts[ix+1], LABELS[k], e['color'], 0.3 if k == 9 else 0.5)

BADGE = {'PK': '#d9532c', 'PK FK': '#d9532c', 'FK': '#1a1a1a', 'FK UK': '#1a1a1a', 'UK': '#6b6b6b', 'AK': '#6b6b6b', 'FK AK': '#1a1a1a', 'PK FK': '#d9532c'}
for n, t in T.items():
    x, y, w, h = t['x'], t['y'], t['w'], t['h']
    fill = '#ece7d8' if t['soporte'] else '#faf9f5'
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="#1a1a1a" stroke-width="1"/>')
    out.append(f'<text x="{x + w/2}" y="{y + HEAD - 11}" text-anchor="middle" class="nm">{n}</text>')
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
    texto = [('PK', '#d9532c', 'llave primaria'), ('FK', '#1a1a1a', 'llave foránea')] + ([] if os.environ.get('NOAK') else [('AK', '#6b6b6b', 'llave alterna')]) + [('nulo', '#6b6b6b', 'puede ir vacío')]
    h = 52 + (len(texto) + 3) * LH + 14
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="#faf9f5" stroke="#6b6b6b" stroke-dasharray="4,3"/>')
    out.append(f'<text x="{x+12}" y="{y+28}" class="nm">Leyenda</text>')
    by = y + 52
    for k, c, v in texto:
        out.append(f'<text x="{x+12}" y="{by}" class="b" fill="{c}">{k}</text>')
        out.append(f'<text x="{x+62}" y="{by}" class="ty">{esc(v)}</text>')
        by += LH
    out.append(f'<text x="{x+12}" y="{by}" class="ty">Flecha: hijo → padre</text>')
    by += LH
    out.append(f'<text x="{x+12}" y="{by}" class="ty">Rótulo: la FK</text>')
    by += LH
    out.append(f'<rect x="{x+12}" y="{by-12}" width="26" height="14" rx="3" fill="#ece7d8" stroke="#1a1a1a"/>')
    out.append(f'<text x="{x+56}" y="{by}" class="ty">soporte del sistema</text>')
    by += LH
    return y + h

lg_bottom = 0 if os.environ.get('NOLEG') else legend(colx[0], colbot[0] + GAPV, colw[0])
H = int(max(max(colbot), lg_bottom) + 22)
W = int(colx[2] + colw[2] + X0)
MARCADORES = ''
CSS = (".a{font:400 15px 'Geist Mono',monospace;fill:#1a1a1a}"
       ".ty{font:400 15px 'Geist Mono',monospace;fill:#6b6b6b}"
       ".b{font:600 15px 'Geist Mono',monospace}"
       ".rl{font:400 11px 'Geist Mono',monospace}"
       ".nm{font:600 18px Geist,sans-serif;fill:#1a1a1a}")
svg = (f'<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="es-title es-desc" xmlns="http://www.w3.org/2000/svg">\n'
       f'<title id="es-title">Esquema lógico (grafo relacional)</title>\n'
       f'<desc id="es-desc">Las 12 relaciones del esquema lógico con sus atributos, llaves primarias, foráneas y alternas, y las 13 llaves foráneas con su cardinalidad numérica.</desc>\n'
       f'<style>{CSS}</style>\n' + chr(10).join(out) + '\n</svg>')
page = ('<!doctype html>\n<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<title>Esquema lógico</title>\n'
        '<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;600&family=Geist+Mono:wght@400;600&display=swap" rel="stylesheet">\n'
        '<style>html,body{margin:0;background:#faf9f5}svg{display:block;width:' + str(W) + 'px;height:' + str(H) + 'px}</style>\n'
        '</head><body>' + svg + '</body></html>')
open(OUT, 'w', encoding='utf-8').write(page)
print('W', W, 'H', H, 'letra_cm', round(15 * 15.6 / W, 3), 'alto_cm', round(H * 15.6 / W, 2))
