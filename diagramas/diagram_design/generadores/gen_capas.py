import html, sys
LH = 14
out = []
esc = html.escape

def hop_path(pts, hops):
    """pts: lista de puntos; hops: lista de (x,y) donde un tramo horizontal salta sobre una vertical."""
    d = f'M{pts[0][0]},{pts[0][1]}'
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        if y0 == y1:
            for hx, hy in sorted([h for h in hops if h[1] == y0], key=lambda h: -h[0] if x1 < x0 else h[0]):
                if min(x0, x1) < hx < max(x0, x1):
                    s = -1 if x1 < x0 else 1
                    d += f' L{hx - 6*s},{y0} A6,6 0 0 {1 if s > 0 else 0} {hx + 6*s},{y0}'
        d += f' L{x1},{y1}'
    return d

def plain(x, y, w, lines, title, stereo, fill='#faf9f5', stroke='#1a1a1a', sw=1):
    h = 44 + len(lines) * LH + 14
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
    out.append(f'<text x="{x+w/2}" y="{y+14}" text-anchor="middle" class="st">«{stereo}»</text>')
    out.append(f'<text x="{x+w/2}" y="{y+30}" text-anchor="middle" class="nm">{esc(title)}</text>')
    out.append(f'<line x1="{x}" y1="{y+40}" x2="{x+w}" y2="{y+40}" stroke="{stroke}"/>')
    for i, t in enumerate(lines):
        out.append(f'<text x="{x+12}" y="{y+58+i*LH}" class="a">{esc(t)}</text>')
    return y + h

W, H = 1400, 880
bands = [
    ('CAPA 1', 'Presentación', 104, 240, '#f4f2ea'),
    ('CAPA 2', 'Lógica de negocio', 262, 412, '#efede4'),
    ('CAPA 3', 'Procesamiento asíncrono', 434, 620, '#f4f2ea'),
    ('CAPA 4', 'Datos', 666, 826, '#efede4'),
]
for tag, name, y0, y1, fill in bands:
    out.append(f'<rect x="20" y="{y0}" width="{W-40}" height="{y1-y0}" rx="8" fill="{fill}" stroke="#d8d5cc"/>')
    out.append(f'<text x="38" y="{y0+24}" class="st">{tag}</text>')
    out.append(f'<text x="38" y="{y0+42}" class="nm" text-anchor="start">{esc(name)}</text>')

# ---- Componentes ----
# Actor
out.append('<rect x="230" y="22" width="300" height="52" rx="6" fill="#faf9f5" stroke="#1a1a1a" stroke-dasharray="6,4"/>')
out.append('<text x="380" y="40" text-anchor="middle" class="st">«actor»</text>')
out.append('<text x="380" y="58" text-anchor="middle" class="nm">Investigador (navegador web)</text>')

# Capa 1
plain(230, 118, 300, ['React.js + Vite', 'Formularios de experimento', 'Visualización de resultados', 'Descarga de reportes (PDF, CSV, XLSX)'], 'frontend', 'contenedor')
# Capa 2
plain(230, 276, 420, ['Flask + SQLAlchemy + Flask-JWT-Extended', 'API REST (JSON)', 'Autenticación con JWT', 'Validación de los archivos de video', 'Encolado de las tareas de análisis'], 'backend', 'contenedor')
# Capa 3: worker (pieza clave)
wx, wy, ww = 800, 456, 560
rows = [('OpenCV', 'Preprocesamiento y localización de cilindros'),
        ('scikit-learn', 'Clasificador sobre rasgos'),
        ('PyTorch', 'R(2+1)D-18 (en evaluación)'),
        ('Python', 'Consulta la cola · borra videos a los 30 días')]
wh = 44 + len(rows) * 18 + 10
out.append(f'<rect x="{wx}" y="{wy}" width="{ww}" height="{wh}" rx="6" fill="#fbe9e2" stroke="#d9532c" stroke-width="1.5"/>')
out.append(f'<text x="{wx+ww/2}" y="{wy+14}" text-anchor="middle" class="st">«contenedor»</text>')
out.append(f'<text x="{wx+ww/2}" y="{wy+30}" text-anchor="middle" class="nm">worker</text>')
out.append(f'<line x1="{wx}" y1="{wy+40}" x2="{wx+ww}" y2="{wy+40}" stroke="#d9532c"/>')
for i, (a, b) in enumerate(rows):
    yy = wy + 58 + i * 18
    out.append(f'<text x="{wx+14}" y="{yy}" class="a" style="font-weight:600">{esc(a)}</text>')
    out.append(f'<text x="{wx+130}" y="{yy}" class="a">{esc(b)}</text>')
wbot = wy + wh
# Capa 4
dbb = plain(230, 686, 240, ['PostgreSQL', 'Cola de tareas: tabla ANALISIS', 'Esquema relacional (15 tablas)'], 'Base de datos', 'contenedor')
plain(830, 686, 240, ['Videos originales y anotados', 'Reportes PDF / CSV / XLSX', 'Reportes de diagnóstico'], 'Volumen compartido', 'volumen', fill='#ece7d8')
plain(1110, 686, 250, ['Solo lectura para el worker', 'Archivo del clasificador', 'de conducta'], 'Volumen de modelos', 'volumen', fill='#ece7d8')

# ---- Flechas ----
def arrow(pts, hops=()):
    out.append(f'<path d="{hop_path(pts, list(hops))}" fill="none" stroke="#1a1a1a" stroke-width="1" marker-end="url(#c-arr)"/>')
def lab_h(x, y, t):
    tw = len(t) * 5.2 + 8
    out.append(f'<rect x="{x-tw/2:.0f}" y="{y-9}" width="{tw:.0f}" height="11" fill="#efede4"/><text x="{x}" y="{y}" text-anchor="middle" class="r">{esc(t)}</text>')
def lab_v(x, y, t):
    out.append(f'<text x="{x}" y="{y}" class="r">{esc(t)}</text>')

arrow([(380, 74), (380, 118)])
arrow([(380, 218), (380, 276)])
lab_v(390, 252, 'API REST (JSON + JWT)')
arrow([(350, 276 + 44 + 5*LH + 14), (350, 686)])
lab_v(360, 560, 'ENCOLA ANÁLISIS')
by = 276 + 44 + 5 * LH + 14
arrow([(600, by), (600, 650), (880, 650), (880, 686)])
lab_h(740, 644, 'LEE Y SIRVE ARCHIVOS')
arrow([(840, wbot), (840, 630), (410, 630), (410, 686)], hops=[(600, 630)])
lab_h(735, 624, 'TOMA TAREAS Y GUARDA RESULTADOS')
arrow([(1020, wbot), (1020, 686)])
lab_v(1028, (wbot + 686) / 2 + 3, 'GUARDA ARCHIVOS')
arrow([(1230, wbot), (1230, 686)])
lab_v(1238, (wbot + 686) / 2 + 3, 'CARGA AL INICIAR')

legend = '''<g transform="translate(40,850)" class="lg">
<rect x="0" y="-8" width="22" height="14" rx="3" fill="#faf9f5" stroke="#1a1a1a"/><text x="30" y="3">CONTENEDOR DOCKER</text>
<rect x="170" y="-8" width="22" height="14" rx="3" fill="#ece7d8" stroke="#1a1a1a"/><text x="200" y="3">VOLUMEN</text>
<line x1="290" y1="0" x2="318" y2="0" stroke="#1a1a1a"/><path d="M312,-4 L318,0 L312,4" fill="none" stroke="#1a1a1a"/><text x="328" y="3">COMUNICACIÓN</text>
<rect x="450" y="-8" width="22" height="14" rx="3" fill="#fbe9e2" stroke="#d9532c" stroke-width="1.5"/><text x="480" y="3">PIEZA CLAVE: WORKER SEPARADO DEL BACKEND</text>
</g>'''

svg = f'''<svg viewBox="0 6 {W} {H-6}" role="img" aria-labelledby="ca-title ca-desc" xmlns="http://www.w3.org/2000/svg">
<title id="ca-title">Arquitectura de software por capas</title>
<desc id="ca-desc">Cuatro capas: presentación (React), lógica de negocio (Flask), procesamiento asíncrono (worker con OpenCV, scikit-learn y PyTorch) y datos (PostgreSQL y dos volúmenes).</desc>
<defs><marker id="c-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1,1 L9,5 L1,9" fill="none" stroke="#1a1a1a" stroke-width="1.2"/></marker></defs>
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
<title>Arquitectura por capas</title>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;600&family=Geist+Mono:wght@400&display=swap" rel="stylesheet">
<style>
html,body{{height:100%;margin:0;background:#faf9f5}}
body{{overflow-x:auto;overflow-y:hidden}}
svg{{display:block;height:100vh;width:auto}}
</style></head><body>{svg}</body></html>'''
open(sys.argv[1], 'w', encoding='utf-8').write(page)
print('ok')
