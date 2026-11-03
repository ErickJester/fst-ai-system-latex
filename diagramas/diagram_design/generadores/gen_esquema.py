import math, html, sys

# Esquema físico en UNA hoja vertical para carta (ancho de \textwidth = 15.6 cm).
# Letra de 15 px CSS: alto impreso de letra = 15 x 15.6 / W.
# Uso: python gen_esquema_v3.py SALIDA.html

esc = html.escape
CH = 9.0     # ancho de carácter de Geist Mono a 15 px (0.6 em)
LH = 22      # interlínea de filas
HEAD = 38    # alto del encabezado de tabla
NX = 52      # sangría del nombre de columna
GAPV = int(sys.argv[2]) if len(sys.argv) > 2 else 44   # separación vertical entre tablas
GAPC = 40    # separación horizontal entre columnas
Y0 = 26
X0 = 28

OUT = sys.argv[1]

# (marca, nombre, tipo) ; restricciones ; soporte del sistema
# Datos de diagramas/esquema_fisico.puml (12 tablas, 13 FK, 9 dominios).
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
def edge(pts, m_hijo, m_padre):
    edges.append(dict(pts=pts, mh=m_hijo, mp=m_padre, color=PALETA[len(edges) % len(PALETA)]))

# Las 13 FK: de la lado hijo (FK) al lado padre (PK).
edge([Lr('EXPERIMENTO', 'idInstitucional'), (gap01 - 24, ry('EXPERIMENTO', 'idInstitucional')),
      (gap01 - 24, ry('USUARIO', 'idInstitucional')), Rr('USUARIO', 'idInstitucional')], '0..*', '1')
edge([Lr('NOTIFICACION', 'idInstitucional'), (lx, ry('NOTIFICACION', 'idInstitucional')),
      (lx, ry('USUARIO', 'idInstitucional')), Lr('USUARIO', 'idInstitucional')], '0..*', '1')
edge([Tc('ADMINISTRADOR'), Bc('USUARIO')], '0..1', '1')
edge([Rr('REPORTE', 'idExperimento'), (gap01 + 10, ry('REPORTE', 'idExperimento')),
      (gap01 + 10, ry('EXPERIMENTO', 'idExperimento')), Lr('EXPERIMENTO', 'idExperimento')], '0..*', '1')
edge([Rr('NOTIFICACION', 'idExperimento'), (gap01 - 10, ry('NOTIFICACION', 'idExperimento')),
      (gap01 - 10, ry('EXPERIMENTO', 'idExperimento')), Lr('EXPERIMENTO', 'idExperimento')], '0..*', '0..1')
edge([Tc('GRUPO'), Bc('EXPERIMENTO')], '0..*', '1')
edge([Tc('TANDA'), Bc('GRUPO')], '1..*', '1')
edge([Tc('ESPECIMEN'), Bc('TANDA')], '2..4', '1')
edge([Tc('OBSERVACION'), Bc('ESPECIMEN')], '0..1', '1')
edge([Rr('OBSERVACION', 'idVideo'), (gap12 - 8, ry('OBSERVACION', 'idVideo')),
      (gap12 - 8, ry('VIDEO', 'idVideo')), Lr('VIDEO', 'idVideo')], '0..4', '1')
edge([Lr('VIDEO', 'idTanda'), (gap12 + 8, ry('VIDEO', 'idTanda')),
      (gap12 + 8, ry('TANDA', 'idTanda')), Rr('TANDA', 'idTanda')], '1..2', '1')
edge([Tc('ANALISIS'), Bc('VIDEO')], '0..1', '1')
edge([Lr('SEGUNDO', 'idObservacion'), (gap12 - 24, ry('SEGUNDO', 'idObservacion')),
      (gap12 - 24, ry('OBSERVACION', 'idObservacion')), Rr('OBSERVACION', 'idObservacion')], '1..300', '1')

out = []

def unit(a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]; n = math.hypot(dx, dy) or 1
    return dx / n, dy / n

def mult(p, q, text, d, color):
    if not text:
        return
    ux, uy = unit(p, q)
    if abs(ux) > abs(uy):
        x = p[0] + ux * d; y = p[1] - 6
        anch = 'start' if ux > 0 else 'end'
    else:
        x = p[0] + 8; y = p[1] + uy * d + (4 if uy > 0 else 0); anch = 'start'
    out.append(f'<text x="{x:.0f}" y="{y:.0f}" text-anchor="{anch}" class="m">{esc(text)}</text>')

for e in edges:
    d = 'M' + ' L'.join(f'{x},{y}' for x, y in e['pts'])
    out.append(f'<path d="{d}" fill="none" stroke="{e["color"]}" stroke-width="1.4" '
               f'marker-end="url(#es-arr-{PALETA.index(e["color"])})"/>')
for e in edges:
    pts = e['pts']
    mult(pts[0], pts[1], e['mh'], 10, e['color'])
    mult(pts[-1], pts[-2], e['mp'], 10, e['color'])

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
            out.append(f'<text x="{x+8}" y="{by}" class="b" fill="{BADGE[m]}">{m}</text>')
        out.append(f'<text x="{x+NX}" y="{by}" class="a">{esc(nm)}</text>')
        out.append(f'<text x="{x+w-10}" y="{by}" text-anchor="end" class="ty">{esc(ty)}</text>')
    if t['cons']:
        cy = y + HEAD + len(t['cols']) * LH + 4
        out.append(f'<line x1="{x+8}" y1="{cy}" x2="{x+w-8}" y2="{cy}" stroke="#6b6b6b" stroke-dasharray="3,3"/>')
        for k, c in enumerate(t['cons']):
            out.append(f'<text x="{x+10}" y="{cy+16+k*LH}" class="ty">{esc(c)}</text>')

def legend(x, y, w):
    items = [('b', 'PK', '#d9532c', 'llave primaria'), ('b', 'FK', '#1a1a1a', 'llave foránea'),
             ('b', 'UK', '#6b6b6b', 'valor único'), ('b', 'CK', '#6b6b6b', 'restricción de valores'),
             ('arrow', 'hijo → padre'), ('swatch', 'soporte del sistema'),
             ('t', 'Dominios (CHECK o tipo enumerado):'),
             ('t', 'tipo_notificacion, formato_reporte,'),
             ('t', 'tipo_grupo, sesion_video,'),
             ('t', 'estado_analisis, etapa_analisis,'),
             ('t', 'nivel_clasif_analisis,'),
             ('t', 'tipo_conducta, origen_segundo')]
    h = 52 + len(items) * LH + 14
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="#faf9f5" stroke="#6b6b6b" stroke-dasharray="4,3"/>')
    out.append(f'<text x="{x+12}" y="{y+28}" class="nm">Leyenda</text>')
    for i, it in enumerate(items):
        by = y + 52 + i * LH
        kind = it[0]
        if kind == 'b':
            out.append(f'<text x="{x+12}" y="{by}" class="b" fill="{it[2]}">{it[1]}</text>')
            out.append(f'<text x="{x+56}" y="{by}" class="ty">{esc(it[3])}</text>')
        elif kind == 'arrow':
            ly = by - 5
            out.append(f'<line x1="{x+12}" y1="{ly}" x2="{x+38}" y2="{ly}" stroke="#6b6b6b" stroke-width="1.4"/>')
            out.append(f'<path d="M{x+32},{ly-4} L{x+38},{ly} L{x+32},{ly+4}" fill="none" stroke="#6b6b6b" stroke-width="1.4"/>')
            out.append(f'<text x="{x+56}" y="{by}" class="ty">{esc(it[1])}</text>')
        elif kind == 'swatch':
            out.append(f'<rect x="{x+12}" y="{by-12}" width="26" height="14" rx="3" fill="#ece7d8" stroke="#1a1a1a"/>')
            out.append(f'<text x="{x+56}" y="{by}" class="ty">{esc(it[1])}</text>')
        else:
            out.append(f'<text x="{x+12}" y="{by}" class="ty">{esc(it[1])}</text>')
    return y + h

lg_bottom = legend(colx[2], colbot[2] + GAPV, colw[2])
H = int(max(max(colbot), lg_bottom) + 22)
W = int(colx[2] + colw[2] + X0)
MARCADORES = ''.join(
    f'<marker id="es-arr-{i}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" '
    f'markerUnits="userSpaceOnUse" orient="auto"><path d="M1,1 L9,5 L1,9" fill="none" stroke="{c}" stroke-width="1.5"/></marker>'
    for i, c in enumerate(PALETA))
CSS = (".a{font:400 15px 'Geist Mono',monospace;fill:#1a1a1a}"
       ".ty{font:400 15px 'Geist Mono',monospace;fill:#6b6b6b}"
       ".b{font:600 15px 'Geist Mono',monospace}"
       ".m{font:600 15px 'Geist Mono',monospace;fill:#000}"
       ".nm{font:600 18px Geist,sans-serif;fill:#1a1a1a}")
svg = (f'<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="es-title es-desc" xmlns="http://www.w3.org/2000/svg">\n'
       f'<title id="es-title">Esquema físico de la base de datos</title>\n'
       f'<desc id="es-desc">Las 12 tablas de la base de datos PostgreSQL con sus columnas, tipos, llaves, restricciones y las 13 llaves foráneas con su cardinalidad.</desc>\n'
       f'<defs>{MARCADORES}</defs>\n<style>{CSS}</style>\n' + chr(10).join(out) + '\n</svg>')
page = ('<!doctype html>\n<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<title>Esquema de la base de datos</title>\n'
        '<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;600&family=Geist+Mono:wght@400;600&display=swap" rel="stylesheet">\n'
        '<style>html,body{margin:0;background:#faf9f5}svg{display:block;width:' + str(W) + 'px;height:' + str(H) + 'px}</style>\n'
        '</head><body>' + svg + '</body></html>')
open(OUT, 'w', encoding='utf-8').write(page)
print('W', W, 'H', H, 'letra_cm', round(15 * 15.6 / W, 3), 'alto_cm', round(H * 15.6 / W, 2), 'ratio_W/H', round(W / H, 3))
