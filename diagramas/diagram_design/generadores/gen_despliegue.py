import html, sys, math
CH = 5.5; LH = 14
B = {}
def box(name, stereo, title, lines, x, y, w, kind='cont'):
    h = 44 + len(lines) * LH + 14
    B[name] = dict(stereo=stereo, title=title, lines=lines, x=x, y=y, w=w, h=h, kind=kind)

# ---- Contenido tomado de los capitulos 1-5 (ver notas en el mensaje) ----
box('nav', 'dispositivo', 'Equipo del investigador', ['Navegador web:', 'Chrome · Firefox · Edge'], 40, 300, 200, 'ext')
box('fe', 'contenedor', 'frontend', ['React.js + Vite', 'Interfaz del investigador', 'Descarga de reportes (PDF, CSV, XLSX)'], 410, 120, 260)
box('be', 'contenedor', 'backend', ['Flask + SQLAlchemy + JWT', 'API REST (JSON)', 'Valida los archivos de video', 'Encola las tareas de análisis'], 410, 300, 260)
box('db', 'contenedor', 'db', ['PostgreSQL', 'Cola de tareas: tabla ANALISIS', 'Esquema relacional (15 tablas)'], 750, 120, 230)
box('wk', 'contenedor', 'worker', ['Python · OpenCV · scikit-learn · PyTorch', 'Pipeline de análisis conductual', 'Consulta la cola periódicamente', 'Borra videos a los 30 días (tarea diaria)', 'Clasificador sobre rasgos: sin GPU'], 1060, 300, 280)
box('vc', 'volumen', 'Volumen compartido', ['Videos originales', 'Videos anotados', 'Reportes PDF / CSV / XLSX', 'Reportes de diagnóstico'], 750, 500, 230, 'vol')
box('vm', 'volumen', 'Volumen de modelos', ['Solo lectura para el worker', 'Archivo del clasificador de conducta'], 1060, 500, 280, 'vol')
box('mail', 'servicio externo', 'Cuenta de correo', ['Configurable en el servidor', '(avisos, RF-33)'], 1450, 120, 200, 'ext')

SX, SY, SW, SH = 380, 40, 990, 640
W = 1690; H = 740

def L(n, dy): b = B[n]; return (b['x'], b['y'] + dy)
def R(n, dy): b = B[n]; return (b['x'] + b['w'], b['y'] + dy)
def T(n, dx): b = B[n]; return (b['x'] + dx, b['y'])
def Bt(n, dx): b = B[n]; return (b['x'] + dx, b['y'] + b['h'])

edges = []
def edge(pts, label='', seg=None, lab_dy=-6):
    edges.append((pts, label, seg, lab_dy))

dbx = B['db']['x'] + B['db']['w'] // 2
edge([R('nav', 20), (300, B['nav']['y'] + 20), (300, B['fe']['y'] + 50), L('fe', 50)], 'CARGA LA APP', seg=1)
edge([R('nav', 70), L('be', 70)], 'API REST + JWT', seg=0)
edge([R('be', 30), (dbx - 40, B['be']['y'] + 30), (dbx - 40, B['db']['y'] + B['db']['h'])], 'ENCOLA ANÁLISIS', seg=0)
edge([L('wk', 30), (dbx + 40, B['wk']['y'] + 30), (dbx + 40, B['db']['y'] + B['db']['h'])], 'POLLING Y RESULTADOS', seg=0)
edge([R('be', 90), (dbx - 40, B['be']['y'] + 90), (dbx - 40, B['vc']['y'])], 'LEE Y SIRVE ARCHIVOS', seg=0)
edge([L('wk', 90), (dbx + 40, B['wk']['y'] + 90), (dbx + 40, B['vc']['y'])], 'GUARDA RESULTADOS', seg=0)
wkcx = B['wk']['x'] + 40
edge([Bt('wk', 40), T('vm', 40)], '', seg=0)
edge([(SX + SW, B['mail']['y'] + 50), L('mail', 50)], 'ENVÍA CORREO', seg=0)

out = []
# Servidor
out.append(f'<rect x="{SX}" y="{SY}" width="{SW}" height="{SH}" rx="8" fill="#f1eee5" stroke="#6b6b6b" stroke-dasharray="6,4"/>')
out.append(f'<text x="{SX+16}" y="{SY+22}" class="st">«servidor»</text>')
out.append(f'<text x="{SX+16}" y="{SY+40}" class="nm" text-anchor="start">Servidor institucional ESCOM · Docker Compose</text>')
out.append(f'<text x="{SX+16}" y="{SY+56}" class="st">o cualquier equipo con Docker (RNF-10)</text>')

labs = []
for pts, label, seg, dy in edges:
    d = 'M' + ' L'.join(f'{x},{y}' for x, y in pts)
    out.append(f'<path d="{d}" fill="none" stroke="#1a1a1a" stroke-width="1" marker-end="url(#d-arr)"/>')
    if label:
        a, b = pts[seg], pts[seg + 1]
        mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
        tw = len(label) * 5.2 + 8
        if abs(b[0] - a[0]) >= abs(b[1] - a[1]):
            labs.append(f'<rect x="{mx-tw/2:.0f}" y="{my-15:.0f}" width="{tw:.0f}" height="11" fill="#f1eee5"/><text x="{mx:.0f}" y="{my-6:.0f}" text-anchor="middle" class="r">{html.escape(label)}</text>')
        else:
            labs.append(f'<text x="{mx-6:.0f}" y="{my:.0f}" text-anchor="end" class="r">{html.escape(label)}</text>')
out += labs
# vm edge label (vertical, text a la derecha)
vx = B['wk']['x'] + 40; vy = (B['wk']['y'] + B['wk']['h'] + B['vm']['y']) / 2
out.append(f'<text x="{vx+8}" y="{vy+3:.0f}" class="r">CARGA AL INICIAR (SOLO LECTURA)</text>')

for n, b in B.items():
    x, y, w, h = b['x'], b['y'], b['w'], b['h']
    focal = n == 'wk'
    fill = {'cont': '#faf9f5', 'vol': '#ece7d8', 'ext': '#faf9f5'}[b['kind']]
    stroke = '#1a1a1a'; sw = 1; dash = ''
    if focal: fill, stroke, sw = '#fbe9e2', '#d9532c', 1.5
    if b['kind'] == 'ext': dash = ' stroke-dasharray="6,4"'
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{dash}/>')
    out.append(f'<text x="{x+w/2}" y="{y+14}" text-anchor="middle" class="st">«{b["stereo"]}»</text>')
    out.append(f'<text x="{x+w/2}" y="{y+30}" text-anchor="middle" class="nm">{html.escape(b["title"])}</text>')
    out.append(f'<line x1="{x}" y1="{y+40}" x2="{x+w}" y2="{y+40}" stroke="{stroke}"/>')
    for i, t in enumerate(b['lines']):
        out.append(f'<text x="{x+12}" y="{y+40+18+i*LH}" class="a">{html.escape(t)}</text>')

ly = 710
legend = f'''<g transform="translate(40,{ly})" class="lg">
<rect x="0" y="-8" width="22" height="14" rx="3" fill="#faf9f5" stroke="#1a1a1a"/><text x="30" y="3">CONTENEDOR</text>
<rect x="130" y="-8" width="22" height="14" rx="3" fill="#ece7d8" stroke="#1a1a1a"/><text x="160" y="3">VOLUMEN</text>
<rect x="250" y="-8" width="22" height="14" rx="3" fill="#faf9f5" stroke="#1a1a1a" stroke-dasharray="4,3"/><text x="280" y="3">FUERA DEL SERVIDOR</text>
<line x1="440" y1="0" x2="468" y2="0" stroke="#1a1a1a"/><path d="M462,-4 L468,0 L462,4" fill="none" stroke="#1a1a1a"/><text x="478" y="3">COMUNICACIÓN</text>
<rect x="600" y="-8" width="22" height="14" rx="3" fill="#fbe9e2" stroke="#d9532c" stroke-width="1.5"/><text x="630" y="3">PIEZA CLAVE: WORKER SEPARADO DEL BACKEND</text>
</g>'''

svg = f'''<svg viewBox="0 10 {W} {H-10}" role="img" aria-labelledby="dp-title dp-desc" xmlns="http://www.w3.org/2000/svg">
<title id="dp-title">Diagrama de despliegue del sistema</title>
<desc id="dp-desc">Cuatro contenedores Docker (frontend, backend, worker y base de datos) y dos volúmenes en un servidor, con el navegador del investigador y una cuenta de correo fuera de él.</desc>
<defs><marker id="d-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1,1 L9,5 L1,9" fill="none" stroke="#1a1a1a" stroke-width="1.2"/></marker></defs>
<style>
.a{{font:400 9px 'Geist Mono',monospace;fill:#1a1a1a}}
.nm{{font:600 12px Geist,sans-serif;fill:#1a1a1a}}
.st{{font:400 8px 'Geist Mono',monospace;fill:#6b6b6b}}
.r{{font:400 8px 'Geist Mono',monospace;fill:#6b6b6b;letter-spacing:.06em}}
.lg text{{font:400 9px 'Geist Mono',monospace;fill:#6b6b6b}}
</style>
{chr(10).join(out)}
{legend}
</svg>'''

page = f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Diagrama de despliegue</title>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;600&family=Geist+Mono:wght@400&display=swap" rel="stylesheet">
<style>
html,body{{height:100%;margin:0;background:#faf9f5}}
body{{overflow-x:auto;overflow-y:hidden}}
svg{{display:block;height:100vh;width:auto}}
</style></head><body>{svg}</body></html>'''
open(sys.argv[1], 'w', encoding='utf-8').write(page)
print('ok')
