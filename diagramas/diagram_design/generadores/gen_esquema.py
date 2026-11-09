import math, html, sys

# Esquema físico en UNA hoja vertical para carta (ancho de \textwidth = 15.6 cm).
# Letra de 15 px CSS. Cardinalidad en notación de pata de gallo (crow's foot).
# Uso: python gen_esquema_v4.py SALIDA.html [GAPV]

esc = html.escape
CH = 9.0     # ancho de carácter de Geist Mono a 15 px (0.6 em)
LH = 28      # interlínea de filas
HEAD = 38    # alto del encabezado de tabla
NX = 56      # sangría del nombre de columna
GAPV = int(sys.argv[2]) if len(sys.argv) > 2 else 60   # separación vertical entre tablas
GAPC = 60    # separación horizontal entre columnas
Y0 = 26
X0 = 28

OUT = sys.argv[1]

# (marca, nombre, tipo) ; restricciones ; soporte del sistema
# Datos de diagramas/esquema_fisico.puml (12 tablas, 13 FK, dominios).
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

COLS = [['USUARIO', 'ADMINISTRADOR', 'NOTIFICACION', 'REPORTE'],
        ['EXPERIMENTO', 'GRUPO', 'TANDA', 'ESPECIMEN', 'OBSERVACION'],
        ['VIDEO', 'ANALISIS', 'SEGUNDO']]

def tw(n):
    cols, cons, _ = DATA[n]
    w = len(n) * 11 + 24
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
edge([Lr('EXPERIMENTO', 'idInstitucional'), (gap01 - 12, ry('EXPERIMENTO', 'idInstitucional')),
      (gap01 - 12, ry('USUARIO', 'idInstitucional')), Rr('USUARIO', 'idInstitucional')], 'zm', 'one')
edge([Lr('NOTIFICACION', 'idInstitucional'), (lx, ry('NOTIFICACION', 'idInstitucional')),
      (lx, ry('USUARIO', 'idInstitucional')), Lr('USUARIO', 'idInstitucional')], 'zm', 'one')
edge([Tc('ADMINISTRADOR'), Bc('USUARIO')], 'zo', 'one')
edge([Rr('REPORTE', 'idExperimento'), (gap01 + 10, ry('REPORTE', 'idExperimento')),
      (gap01 + 10, ry('EXPERIMENTO', 'idExperimento')), Lr('EXPERIMENTO', 'idExperimento')], 'zm', 'one')
edge([Rr('NOTIFICACION', 'idExperimento'), (gap01 - 4, ry('NOTIFICACION', 'idExperimento')),
      (gap01 - 4, ry('EXPERIMENTO', 'idExperimento')), Lr('EXPERIMENTO', 'idExperimento')], 'zm', 'zo')
edge([Tc('GRUPO'), Bc('EXPERIMENTO')], 'zm', 'one')
edge([Tc('TANDA'), Bc('GRUPO')], 'om', 'one')
edge([Tc('ESPECIMEN'), Bc('TANDA')], 'om', 'one', '2..4')
edge([Tc('OBSERVACION'), Bc('ESPECIMEN')], 'zo', 'one')
edge([Rr('OBSERVACION', 'idVideo'), (gap12 - 22, ry('OBSERVACION', 'idVideo')),
      (gap12 - 22, ry('VIDEO', 'idVideo')), Lr('VIDEO', 'idVideo')], 'zm', 'one', '0..4')
edge([Lr('VIDEO', 'idTanda'), (gap12 - 10, ry('VIDEO', 'idTanda')),
      (gap12 - 10, ry('TANDA', 'idTanda')), Rr('TANDA', 'idTanda')], 'om', 'one', '1..2')
edge([Tc('ANALISIS'), Bc('VIDEO')], 'zo', 'one')
edge([Lr('SEGUNDO', 'idObservacion'), (gap12 - 16, ry('SEGUNDO', 'idObservacion')),
      (gap12 - 16, ry('OBSERVACION', 'idObservacion')), Rr('OBSERVACION', 'idObservacion')], 'om', 'one', '1..300')

out = []

def unit(a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]; n = math.hypot(dx, dy) or 1
    return dx / n, dy / n

def symbol(p, q, kind, color, rng=None, rpos=None):
    # p: punto sobre el borde de la tabla; q: siguiente punto de la línea. Los símbolos salen hacia la línea.
    ux, uy = unit(p, q)
    vx, vy = -uy, ux
    def P(d): return (p[0] + ux * d, p[1] + uy * d)
    def bar(d):
        a = P(d)
        return (f'<line x1="{a[0]+vx*6:.1f}" y1="{a[1]+vy*6:.1f}" x2="{a[0]-vx*6:.1f}" y2="{a[1]-vy*6:.1f}" '
                f'stroke="{color}" stroke-width="1.6"/>')
    def circ(d):
        a = P(d)
        return (f'<circle cx="{a[0]:.1f}" cy="{a[1]:.1f}" r="3.5" fill="#faf9f5" stroke="{color}" stroke-width="1.6"/>')
    def foot():
        apex = P(9)
        segs = []
        for s in (6, 0, -6):
            e = (p[0] + vx * s, p[1] + vy * s)
            segs.append(f'<line x1="{apex[0]:.1f}" y1="{apex[1]:.1f}" x2="{e[0]:.1f}" y2="{e[1]:.1f}" '
                        f'stroke="{color}" stroke-width="1.6"/>')
        return ''.join(segs)
    if kind == 'one':
        s = bar(5) + bar(9)
    elif kind == 'zo':
        s = bar(5) + circ(13)
    elif kind == 'om':
        s = foot() + bar(13)
    else:  # zm
        s = foot() + circ(15)
    out.append(s)
    if rng:
        tx, ty, anc = rpos
        wr = len(rng) * 6.7 + 4
        out.append(f'<rect x="{tx-1:.0f}" y="{ty-11:.0f}" width="{wr+2:.0f}" height="14" fill="#faf9f5"/>')
        out.append(f'<text x="{tx:.0f}" y="{ty:.0f}" text-anchor="{anc}" class="rl" fill="{color}">{esc(rng)}</text>')

for e in edges:
    d = 'M' + ' L'.join(f'{x},{y}' for x, y in e['pts'])
    out.append(f'<path d="{d}" fill="none" stroke="{e["color"]}" stroke-width="1.4"/>')
OBST = []
def hit(a, b):
    return not (a[2] < b[0] or b[2] < a[0] or a[3] < b[1] or b[3] < a[1])
def add_seg(a, b, pad=1):
    OBST.append((min(a[0], b[0]) - pad, min(a[1], b[1]) - pad, max(a[0], b[0]) + pad, max(a[1], b[1]) + pad))
for e in edges:
    for i in range(len(e['pts']) - 1):
        add_seg(e['pts'][i], e['pts'][i + 1])
    for p_, q_ in ((e['pts'][0], e['pts'][1]), (e['pts'][-1], e['pts'][-2])):
        ux_, uy_ = unit(p_, q_)
        far = (p_[0] + ux_ * 22, p_[1] + uy_ * 22)
        OBST.append((min(p_[0], far[0]) - 9, min(p_[1], far[1]) - 9, max(p_[0], far[0]) + 9, max(p_[1], far[1]) + 9))
for n, t in T.items():
    x, y, w, h = t['x'], t['y'], t['w'], t['h']
    add_seg((x, y), (x + w, y)); add_seg((x, y + h), (x + w, y + h))
    add_seg((x, y), (x, y + h)); add_seg((x + w, y), (x + w, y + h))
for e in edges:
    if not e['rng']:
        continue
    p, q = e['pts'][0], e['pts'][1]
    w = len(e['rng']) * 6.7 + 4
    cands = []
    if abs(q[1] - p[1]) < 1:
        sg = 1 if q[0] > p[0] else -1
        for d in range(2, 34, 2):
            x0 = p[0] + d if sg > 0 else p[0] - d - w
            for ty in (p[1] - 12, p[1] + 22):
                cands.append((x0, ty))
    else:
        ux_, uy_ = unit(p, q)
        for k in range(12, 44, 4):
            for x0 in (p[0] + 12, p[0] - 12 - w):
                cands.append((x0, p[1] + uy_ * k + 4))
    choice = None
    for x0, ty in cands:
        box = (x0 - 1, ty - 11, x0 + w + 1, ty + 3)
        if not any(hit(box, o) for o in OBST):
            choice = (x0, ty)
            break
    if choice is None:
        choice = cands[0]
        print('FALLBACK', e['rng'])
    e['rpos'] = (choice[0], choice[1], 'start')
    OBST.append((choice[0] - 1, choice[1] - 11, choice[0] + w + 1, choice[1] + 3))

for e in edges:
    pts = e['pts']
    symbol(pts[0], pts[1], e['child'], e['color'], e['rng'], e['rpos'] if e['rng'] else None)
    symbol(pts[-1], pts[-2], e['parent'], e['color'])

BADGE = {'PK': '#d9532c', 'PK FK': '#d9532c', 'FK': '#1a1a1a', 'FK UK': '#1a1a1a', 'UK': '#6b6b6b'}
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
    simbolos = [('one', 'exactamente uno'), ('zo', 'cero o uno'), ('om', 'uno o más'), ('zm', 'cero o más')]
    texto = [('PK', '#d9532c', 'llave primaria'), ('FK', '#1a1a1a', 'llave foránea'),
             ('UK', '#6b6b6b', 'valor único'), ('CK', '#6b6b6b', 'restricción de valores')]
    h = 52 + (len(texto) + len(simbolos) + 1) * LH + 14
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="#faf9f5" stroke="#6b6b6b" stroke-dasharray="4,3"/>')
    out.append(f'<text x="{x+12}" y="{y+28}" class="nm">Leyenda</text>')
    by = y + 52
    for k, c, v in texto:
        out.append(f'<text x="{x+12}" y="{by}" class="b" fill="{c}">{k}</text>')
        out.append(f'<text x="{x+56}" y="{by}" class="ty">{esc(v)}</text>')
        by += LH
    out.append(f'<text x="{x+12}" y="{by}" class="ty">Cardinalidad:</text>')
    by += LH
    for kind, v in simbolos:
        p = (x + 14, by - 5); q = (x + 56, by - 5)
        out.append(f'<line x1="{p[0]}" y1="{p[1]}" x2="{q[0]}" y2="{q[1]}" stroke="#6b6b6b" stroke-width="1.4"/>')
        symbol(p, q, kind, '#1a1a1a')
        out.append(f'<text x="{x+70}" y="{by}" class="ty">{esc(v)}</text>')
        by += LH
    out.append(f'<rect x="{x+12}" y="{by-12}" width="26" height="14" rx="3" fill="#ece7d8" stroke="#1a1a1a"/>')
    out.append(f'<text x="{x+56}" y="{by}" class="ty">soporte del sistema</text>')
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
       f'<title id="es-title">Esquema físico de la base de datos</title>\n'
       f'<desc id="es-desc">Las 12 tablas de la base de datos PostgreSQL con sus columnas, tipos, llaves, restricciones y las 13 llaves foráneas con su cardinalidad en notación de pata de gallo.</desc>\n'
       f'<style>{CSS}</style>\n' + chr(10).join(out) + '\n</svg>')
page = ('<!doctype html>\n<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<title>Esquema de la base de datos</title>\n'
        '<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;600&family=Geist+Mono:wght@400;600&display=swap" rel="stylesheet">\n'
        '<style>html,body{margin:0;background:#faf9f5}svg{display:block;width:' + str(W) + 'px;height:' + str(H) + 'px}</style>\n'
        '</head><body>' + svg + '</body></html>')
open(OUT, 'w', encoding='utf-8').write(page)
print('W', W, 'H', H, 'letra_cm', round(15 * 15.6 / W, 3), 'alto_cm', round(H * 15.6 / W, 2))
