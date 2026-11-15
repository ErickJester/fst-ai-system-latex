import html, sys

# Contenedores del sistema (TT2), versión para diapositiva: poco texto y letra grande.
# Mismo lenguaje visual que contenedores.html. Uso: python gen_contenedores_s.py SALIDA.html
esc = html.escape
W, H = 1360, 640
LH, TOP = 22, 54
B = {}


def box(n, ster, titulo, lineas, x, y, w, kind='cont'):
    B[n] = dict(ster=ster, t=titulo, ls=lineas, x=x, y=y, w=w, h=TOP + len(lineas) * LH + 14, kind=kind)


box('nav', 'dispositivo', 'Equipo del investigador', ['Navegador web'], 20, 250, 250, 'ext')
box('mail', 'servicio externo', 'Cuenta de correo', ['Cuenta configurable', '(avisos, RF-33)'], 20, 440, 250, 'ext')
box('web', 'contenedor', 'web', ['React.js + Vite · nginx', 'Interfaz del investigador'], 380, 80, 320)
box('api', 'contenedor', 'api', ['Spring Boot · Java 21', 'API REST con JWT', 'Encola los análisis'], 380, 250, 320)
box('db', 'contenedor', 'db', ['PostgreSQL 16', 'Cola de tareas y resultados', '12 tablas'], 800, 80, 320)
box('wk', 'contenedor', 'worker', ['Python · OpenCV · PyTorch', 'Pipeline de análisis', 'Un video a la vez', 'Tareas diarias'], 800, 250, 340)
box('vc', 'volumen', 'Volumen compartido', ['Videos y copia H.264', 'Datos de pausa', 'Reportes PDF, CSV, XLSX'], 560, 450, 340, 'vol')
box('vm', 'volumen', 'Volumen de modelos', ['Solo lectura', 'Clasificador de conducta'], 960, 450, 330, 'vol')

out = []
out.append('<rect x="330" y="24" width="1010" height="596" rx="10" fill="#f1eee5" stroke="#6b6b6b" stroke-width="1.4" stroke-dasharray="7,5"/>')
out.append('<text x="356" y="48" class="st">«docker compose»</text>')

edges = []


def edge(pts, label='', seg=0, lado='der'):
    edges.append((pts, label, seg, lado))


def Rr(n, dy): b = B[n]; return (b['x'] + b['w'], b['y'] + dy)
def Ll(n, dy): b = B[n]; return (b['x'], b['y'] + dy)
def Tt(n, dx): b = B[n]; return (b['x'] + dx, b['y'])
def Bb(n, dx): b = B[n]; return (b['x'] + dx, b['y'] + b['h'])


edge([Rr('nav', 30), (320, B['nav']['y'] + 30), (320, B['web']['y'] + 40), Ll('web', 40)], 'carga la app', 1)
edge([Rr('nav', 70), Ll('api', 70)], 'API REST + JWT', 0)
edge([Rr('api', 40), (750, B['api']['y'] + 40), (750, B['db']['y'] + 40), Ll('db', 40)], 'encola', 1, 'izq')
edge([Tt('wk', 90), Bb('db', 90)], 'consulta la cola', 0)
edge([Bb('api', 240), Tt('vc', 60)], 'lee y sirve archivos', 0, 'izq')
edge([Bb('wk', 40), Tt('vc', 280)], 'guarda resultados', 0, 'izq')
edge([Bb('wk', 250), Tt('vm', 90)], 'carga el modelo', 0)
edge([(330, B['mail']['y'] + 30), Rr('mail', 30)], 'envía correo', 0)

for pts, label, seg, lado in edges:
    d = 'M' + ' L'.join(f'{x},{y}' for x, y in pts)
    out.append(f'<path d="{d}" fill="none" stroke="#1a1a1a" stroke-width="1.5"/>')
    (x1, y1), (x2, y2) = pts[-2], pts[-1]
    if abs(y2 - y1) >= abs(x2 - x1):
        s = 1 if y2 > y1 else -1
        out.append(f'<path d="M{x2 - 5},{y2 - 9 * s} L{x2},{y2} L{x2 + 5},{y2 - 9 * s}" fill="none" stroke="#1a1a1a" stroke-width="1.5"/>')
    else:
        s = 1 if x2 > x1 else -1
        out.append(f'<path d="M{x2 - 9 * s},{y2 - 5} L{x2},{y2} L{x2 - 9 * s},{y2 + 5}" fill="none" stroke="#1a1a1a" stroke-width="1.5"/>')
for n, b in B.items():
    x, y, w, h = b['x'], b['y'], b['w'], b['h']
    fill = {'cont': '#faf9f5', 'vol': '#ece7d8', 'ext': '#faf9f5'}[b['kind']]
    stroke, sw, dash = '#1a1a1a', 1.5, ''
    if n == 'wk':
        fill, stroke, sw = '#fbe9e2', '#d9532c', 2
    if b['kind'] == 'ext':
        dash = ' stroke-dasharray="7,5"'
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{dash}/>')
    out.append(f'<text x="{x + w / 2}" y="{y + 17}" text-anchor="middle" class="st">«{b["ster"]}»</text>')
    out.append(f'<text x="{x + w / 2}" y="{y + 38}" text-anchor="middle" class="nm">{esc(b["t"])}</text>')
    out.append(f'<line x1="{x}" y1="{y + 46}" x2="{x + w}" y2="{y + 46}" stroke="{stroke}"/>')
    for i, t in enumerate(b['ls']):
        out.append(f'<text x="{x + 14}" y="{y + TOP + 14 + i * LH}" class="a">{esc(t)}</text>')

for pts, label, seg, lado in edges:
    if not label:
        continue
    a, b = pts[seg], pts[seg + 1]
    mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
    w = len(label) * 7.2 + 10
    if abs(b[0] - a[0]) >= abs(b[1] - a[1]):
        out.append(f'<rect x="{mx - w / 2:.0f}" y="{my - 22:.0f}" width="{w:.0f}" height="18" fill="#faf9f5"/>'
                   f'<text x="{mx:.0f}" y="{my - 8:.0f}" text-anchor="middle" class="r">{esc(label)}</text>')
    else:
        x0 = mx + 8 if lado == 'der' else mx - 8 - w
        out.append(f'<rect x="{x0:.0f}" y="{my - 9:.0f}" width="{w:.0f}" height="18" fill="#f1eee5"/>'
                   f'<text x="{x0 + 5:.0f}" y="{my + 5:.0f}" class="r">{esc(label)}</text>')

css = (".a{font:400 15px 'Geist Mono',monospace;fill:#1a1a1a}"
       ".nm{font:600 18px Geist,Arial,sans-serif;fill:#1a1a1a}"
       ".st{font:400 12px 'Geist Mono',monospace;fill:#6b6b6b}"
       ".r{font:400 12.5px 'Geist Mono',monospace;fill:#555;letter-spacing:.04em}")
svg = (f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" xmlns="http://www.w3.org/2000/svg">'
       f'<title>Contenedores del sistema</title><style>{css}</style><rect width="{W}" height="{H}" fill="#faf9f5"/>'
       + '\n'.join(out) + '</svg>')
page = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Contenedores del sistema</title>'
        '<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;600&family=Geist+Mono:wght@400&display=swap" rel="stylesheet">'
        '<style>html,body{margin:0;background:#faf9f5}svg{display:block}</style></head><body>' + svg + '</body></html>')
open(sys.argv[1], 'w', encoding='utf-8').write(page)
print('ok', W, H)
