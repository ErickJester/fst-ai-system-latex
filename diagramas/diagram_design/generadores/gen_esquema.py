import math, html, sys

# Esquema de la base de datos pensado para una hoja carta en vertical (3 columnas, sin cuadro de
# dominios): ancho y alto caben en el area de texto del documento con espacio para el pie de figura.
CH = 5.3   # ancho aprox. de un caracter mono de 9px
LH = 14
GAPV = 46  # espacio vertical entre tablas de una misma columna
esc = html.escape

# ---- Datos tomados de diagramas/esquema_fisico.puml (12 tablas, 13 FK; D-52 quita INTERVALO y PRESENTA y D-102 quita CONDUCTA) ----
# columna: (marca, nombre, tipo)   marca: PK, FK, 'PK FK', UK, 'FK UK' o ''
T = {}
COLS = [[], [], []]
def tab(name, col, cols, cons=(), soporte=False):
    T[name] = dict(col=col, cols=list(cols), cons=list(cons), soporte=soporte, y=0)
    COLS[col].append(name)

# columna 0: usuarios y soporte del sistema
tab('USUARIO', 0, [
    ('PK', 'idInstitucional', 'varchar(10)'), ('', 'nombre', 'varchar(n)'), ('', 'apellidos', 'varchar(n)'),
    ('UK', 'correo', 'varchar(n)'), ('', 'contrasenaHash', 'varchar(n)'), ('', 'activo', 'boolean'),
    ('', 'cambioRequerido', 'boolean')])
tab('ADMINISTRADOR', 0, [('PK FK', 'idInstitucional', 'varchar(10)')])
tab('NOTIFICACION', 0, [
    ('PK', 'idNotificacion', 'integer'), ('FK', 'idInstitucional', 'varchar(10)'),
    ('FK', 'idExperimento', 'integer · nulo'), ('', 'tipo', 'tipo_notificacion'), ('', 'mensaje', 'text'),
    ('', 'leido', 'boolean'), ('', 'fechaCreacion', 'timestamptz')], soporte=True)
tab('REPORTE', 0, [
    ('PK', 'idReporte', 'integer'), ('FK', 'idExperimento', 'integer'), ('', 'formato', 'formato_reporte'),
    ('UK', 'ruta', 'text'), ('', 'fechaGeneracion', 'timestamptz')], soporte=True)
# columna 1: experimento, espécimen, observación, conducta
tab('EXPERIMENTO', 1, [
    ('PK', 'idExperimento', 'integer'), ('FK', 'idInstitucional', 'varchar(10)'), ('UK', 'nombre', 'varchar(n)'),
    ('', 'fecha', 'date'), ('', 'notas', 'text · nulo')])
tab('ESPECIMEN', 1, [
    ('PK', 'idEspecimen', 'integer'), ('FK', 'idTanda', 'integer'), ('', 'numeroCilindro', 'smallint')],
    ['UK (idTanda, numeroCilindro)'])
tab('OBSERVACION', 1, [
    ('PK', 'idObservacion', 'integer'), ('FK', 'idEspecimen', 'integer'), ('FK', 'idVideo', 'integer')],
    ['UK (idEspecimen, idVideo)'])
# columna 2: grupo, tanda, video, analisis, segundo
tab('GRUPO', 2, [
    ('PK', 'idGrupo', 'integer'), ('FK', 'idExperimento', 'integer'), ('', 'etiqueta', 'varchar(n)'),
    ('', 'tipo', 'tipo_grupo'), ('', 'tratamiento', 'text')], ['UK (idExperimento, etiqueta)'])
tab('TANDA', 2, [
    ('PK', 'idTanda', 'integer'), ('FK', 'idGrupo', 'integer'), ('', 'ordinal', 'smallint'),
    ('', 'nCilindros', 'smallint')], ['UK (idGrupo, ordinal)'])
tab('VIDEO', 2, [
    ('PK', 'idVideo', 'integer'), ('FK', 'idTanda', 'integer'), ('', 'sesion', 'sesion_video'),
    ('', 'archivo', 'text · nulo'), ('', 'nombreOriginal', 'varchar(255) · nulo'), ('', 'duracion', 'numeric(p,s)'), ('', 'fechaCarga', 'timestamptz')],
    ['UK (idTanda, sesion)'])
tab('ANALISIS', 2, [
    ('PK', 'idAnalisis', 'integer'), ('FK UK', 'idVideo', 'integer'), ('', 'estado', 'estado_analisis'),
    ('', 'etapa', 'etapa_analisis'), ('', 'nivelClasif', 'nivel_clasif_analisis'),
    ('', 'fechaAnalisis', 'timestamptz'), ('', 'rutaDiagnostico', 'text · nulo')])
tab('SEGUNDO', 2, [
    ('PK FK', 'idObservacion', 'integer'), ('PK', 'segundo', 'smallint'),
    ('', 'conducta', 'tipo_conducta · nulo'), ('', 'origen', 'origen_segundo')],
    ['CK segundo entre 1 y 300'])

# ---- Anchos y alturas ----
colw = [0, 0, 0]
for n, t in T.items():
    w = len(n) * 7 + 40
    for m, nm, ty in t['cols']:
        w = max(w, 8 + 34 + len(nm) * CH + 8 + len(ty) * CH + 10)
    for c in t['cons']:
        w = max(w, len(c) * CH + 28)
    colw[t['col']] = max(colw[t['col']], math.ceil(w / 10) * 10)
GAP = [84, 100]
X0 = 70
colx = [X0, X0 + colw[0] + GAP[0], X0 + colw[0] + GAP[0] + colw[1] + GAP[1]]
for n, t in T.items():
    t['x'] = colx[t['col']]; t['w'] = colw[t['col']]
    t['h'] = 32 + len(t['cols']) * LH + 12 + (len(t['cons']) * LH + 4 if t['cons'] else 0)

def rowy(n, name):
    t = T[n]
    i = [c[1] for c in t['cols']].index(name)
    return t['y'] + 34 + i * LH + 7

# ---- Posiciones verticales ----
Y0 = 40
def stack(names, y=Y0):
    for n in names:
        T[n]['y'] = y; y += T[n]['h'] + GAPV
    return y
stack(COLS[0])
stack(['EXPERIMENTO'])
T['ESPECIMEN']['y'] = T['EXPERIMENTO']['y'] + T['EXPERIMENTO']['h'] + GAPV
T['OBSERVACION']['y'] = T['ESPECIMEN']['y'] + T['ESPECIMEN']['h'] + GAPV
# columna 2: la PK de TANDA a la altura del idTanda de ESPECIMEN y la de VIDEO a la del idVideo de OBSERVACION
T['GRUPO']['y'] = Y0
T['TANDA']['y'] = T['ESPECIMEN']['y'] + 14
T['VIDEO']['y'] = T['OBSERVACION']['y'] + 28
T['ANALISIS']['y'] = T['VIDEO']['y'] + T['VIDEO']['h'] + GAPV
seg_min = T['ANALISIS']['y'] + T['ANALISIS']['h'] + GAPV
T['SEGUNDO']['y'] = seg_min

def Lr(n, name): return (T[n]['x'], rowy(n, name))
def Rr(n, name): return (T[n]['x'] + T[n]['w'], rowy(n, name))
def Tc(n, dx=None): return (T[n]['x'] + (T[n]['w'] // 2 if dx is None else dx), T[n]['y'])
def Bc(n, dx=None): return (T[n]['x'] + (T[n]['w'] // 2 if dx is None else dx), T[n]['y'] + T[n]['h'])
def gap(i, off): return colx[i] + colw[i] + off   # a la derecha de la columna i

PALETA = ['#1b6fb0', '#2e8b57', '#8e44ad', '#c0392b', '#b8860b', '#16a085', '#d35400', '#e84393', '#34495e',
          '#6c8e00', '#0097a7', '#a0522d', '#5e35b1', '#c2185b', '#00796b', '#f57c00', '#455a64']
edges = []
def edge(pts, m_hijo, m_padre):
    if len(pts) == 2 and abs(pts[0][1] - pts[1][1]) > 2 and abs(pts[0][0] - pts[1][0]) > 30:
        mx = (pts[0][0] + pts[1][0]) // 2
        pts = [pts[0], (mx, pts[0][1]), (mx, pts[1][1]), pts[1]]
    edges.append(dict(pts=pts, mh=m_hijo, mp=m_padre, color=PALETA[len(edges) % len(PALETA)]))

# Cada arista va del lado hijo (la FK) al lado padre (la PK). Cardinalidades del .puml.
edge([Lr('EXPERIMENTO', 'idInstitucional'), (gap(0, 40), rowy('EXPERIMENTO', 'idInstitucional')),
      (gap(0, 40), rowy('USUARIO', 'idInstitucional')), Rr('USUARIO', 'idInstitucional')], '0..*', '1')
edge([Lr('NOTIFICACION', 'idInstitucional'), (X0 - 34, rowy('NOTIFICACION', 'idInstitucional')),
      (X0 - 34, rowy('USUARIO', 'cambioRequerido')), Lr('USUARIO', 'cambioRequerido')], '0..*', '1')
edge([Tc('ADMINISTRADOR'), Bc('USUARIO', T['ADMINISTRADOR']['w'] // 2)], '0..1', '1')
edge([Rr('REPORTE', 'idExperimento'), (gap(0, 40), rowy('REPORTE', 'idExperimento')),
      (gap(0, 40), rowy('EXPERIMENTO', 'fecha')), Lr('EXPERIMENTO', 'fecha')], '0..*', '1')
edge([Rr('NOTIFICACION', 'idExperimento'), (gap(0, 62), rowy('NOTIFICACION', 'idExperimento')),
      (gap(0, 62), rowy('EXPERIMENTO', 'notas')), Lr('EXPERIMENTO', 'notas')], '0..*', '0..1')
edge([Lr('GRUPO', 'idExperimento'), Rr('EXPERIMENTO', 'idExperimento')], '3..*', '1')
edge([Tc('TANDA'), Bc('GRUPO')], '1..*', '1')
edge([Rr('ESPECIMEN', 'idTanda'), Lr('TANDA', 'idTanda')], '2..4', '1')
edge([Tc('VIDEO'), Bc('TANDA')], '1..2', '1')
edge([Tc('ANALISIS'), Bc('VIDEO')], '0..1', '1')
edge([Rr('OBSERVACION', 'idVideo'), Lr('VIDEO', 'idVideo')], '0..4', '1')
edge([Tc('OBSERVACION'), Bc('ESPECIMEN')], '0..1', '1')
edge([Lr('SEGUNDO', 'idObservacion'), (gap(1, 45), rowy('SEGUNDO', 'idObservacion')),
      (gap(1, 45), rowy('OBSERVACION', 'idObservacion')), Rr('OBSERVACION', 'idObservacion')], '1..300', '1')

# ---- SVG ----
out = []

def unit(a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]; n = math.hypot(dx, dy) or 1
    return dx / n, dy / n

def mult(p, q, text, d, color):
    if not text: return
    ux, uy = unit(p, q)
    if abs(ux) > abs(uy):
        x = p[0] + ux * d; y = p[1] - 5
        anch = 'start' if ux > 0 else 'end'
    else:
        x = p[0] + 6; y = p[1] + uy * d + (3 if uy > 0 else 0); anch = 'start'
    out.append(f'<text x="{x:.0f}" y="{y:.0f}" text-anchor="{anch}" class="m">{esc(text)}</text>')

for e in edges:
    d = 'M' + ' L'.join(f'{x},{y}' for x, y in e['pts'])
    out.append(f'<path d="{d}" fill="none" stroke="{e["color"]}" stroke-width="1.4" marker-end="url(#es-arr-{PALETA.index(e["color"])})"/>')
for e in edges:
    pts = e['pts']
    mult(pts[0], pts[1], e['mh'], 8, e['color'])
    mult(pts[-1], pts[-2], e['mp'], 8, e['color'])

BADGE = {'PK': '#d9532c', 'PK FK': '#d9532c', 'FK': '#1a1a1a', 'FK UK': '#1a1a1a', 'UK': '#6b6b6b'}
for n, t in T.items():
    x, y, w, h = t['x'], t['y'], t['w'], t['h']
    fill = '#ece7d8' if t['soporte'] else '#faf9f5'
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="#1a1a1a" stroke-width="1"/>')
    out.append(f'<text x="{x + w/2}" y="{y + 21}" text-anchor="middle" class="nm">{n}</text>')
    out.append(f'<line x1="{x}" y1="{y+32}" x2="{x+w}" y2="{y+32}" stroke="#1a1a1a"/>')
    yy = y + 32 + 14
    for m, nm, ty in t['cols']:
        if m:
            out.append(f'<text x="{x+8}" y="{yy}" class="b" fill="{BADGE[m]}">{m}</text>')
        out.append(f'<text x="{x+42}" y="{yy}" class="a">{esc(nm)}</text>')
        out.append(f'<text x="{x+w-10}" y="{yy}" text-anchor="end" class="ty">{esc(ty)}</text>')
        yy += LH
    if t['cons']:
        sy = y + 32 + len(t['cols']) * LH + 12
        out.append(f'<line x1="{x+8}" y1="{sy-2}" x2="{x+w-8}" y2="{sy-2}" stroke="#6b6b6b" stroke-dasharray="3,3"/>')
        yy = sy + 10
        for c in t['cons']:
            out.append(f'<text x="{x+10}" y="{yy}" class="ty">{esc(c)}</text>'); yy += LH

# Leyenda en el hueco de la columna 0
lx = colx[0]
ly = T['REPORTE']['y'] + T['REPORTE']['h'] + GAPV
lw = colw[0]
items = [
    ('PK', '#d9532c', 'llave primaria'), ('FK', '#1a1a1a', 'llave foránea'), ('UK', '#6b6b6b', 'valor único'),
    ('CK', '#6b6b6b', 'restricción de valores')]
lh = 24 + len(items) * LH + 2 * LH
out.append(f'<rect x="{lx}" y="{ly}" width="{lw}" height="{lh}" rx="6" fill="#faf9f5" stroke="#6b6b6b" stroke-dasharray="4,3"/>')
for i, (k, c, v) in enumerate(items):
    yy = ly + 18 + i * LH
    out.append(f'<text x="{lx+10}" y="{yy}" class="b" fill="{c}">{k}</text><text x="{lx+40}" y="{yy}" class="ty">{v}</text>')
yy = ly + 18 + len(items) * LH + 4
out.append(f'<line x1="{lx+10}" y1="{yy-4}" x2="{lx+34}" y2="{yy-4}" stroke="#6b6b6b" stroke-width="1.2"/><path d="M28,0" fill="none"/>'
           f'<path d="M{lx+29},{yy-8} L{lx+34},{yy-4} L{lx+29},{yy}" fill="none" stroke="#6b6b6b" stroke-width="1.4"/>'
           f'<text x="{lx+40}" y="{yy-1}" class="ty">hijo → padre</text>')
out.append(f'<rect x="{lx+lw-30}" y="{ly+8}" width="20" height="12" rx="3" fill="#ece7d8" stroke="#1a1a1a"/>')
out.append(f'<text x="{lx+lw-10}" y="{ly+32}" text-anchor="end" class="ty">soporte</text>')

maxx = colx[2] + colw[2] + 30
maxy = max(max(t['y'] + t['h'] for t in T.values()), ly + lh) + 30
W, H = int(maxx), int(maxy)
MARCADORES = ''.join(f'<marker id="es-arr-{i}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1,1 L9,5 L1,9" fill="none" stroke="{c}" stroke-width="1.5"/></marker>' for i, c in enumerate(PALETA))
svg = f'''<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="es-title es-desc" xmlns="http://www.w3.org/2000/svg">
<title id="es-title">Esquema de la base de datos</title>
<desc id="es-desc">Las 12 tablas de la base de datos PostgreSQL con sus columnas, tipos, llaves primarias, foráneas y únicas, y las 13 llaves foráneas con su cardinalidad.</desc>
<defs>
{MARCADORES}
</defs>
<style>
.a{{font:400 9px 'Geist Mono',monospace;fill:#1a1a1a}}
.ty{{font:400 9px 'Geist Mono',monospace;fill:#6b6b6b}}
.b{{font:600 8px 'Geist Mono',monospace}}
.nm{{font:600 12px Geist,sans-serif;fill:#1a1a1a}}
.m{{font:600 10px 'Geist Mono',monospace;fill:#000}}
</style>
{chr(10).join(out)}
</svg>'''

page = f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Esquema de la base de datos</title>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;600&family=Geist+Mono:wght@400&display=swap" rel="stylesheet">
<style>
html,body{{margin:0;background:#faf9f5}}
svg{{display:block;width:{W}px;height:{H}px}}
</style></head><body>{svg}</body></html>'''
open(sys.argv[1], 'w', encoding='utf-8').write(page)
print('ok', W, 'x', H, 'proporcion ancho/alto', round(W / H, 3), 'tablas', len(T), 'aristas', len(edges))
