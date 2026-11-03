import html, sys
esc = html.escape
out = []
LH = 19          # interlinea (px CSS) para letra de 15 px
FS = 15          # letra de cuerpo (px CSS)
W, H = 1400, 900

def box(x, y, w, lines, title=None, stereo=None, fill='#faf9f5', stroke='#1a1a1a', sw=1, dash=False):
    head = 58 if (title and stereo) else 44
    h = head + len(lines) * LH + 14
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"' + (' stroke-dasharray="6,4"' if dash else '') + '/>')
    ty = y + 20
    if stereo:
        out.append(f'<text x="{x+w/2}" y="{ty}" text-anchor="middle" class="st">«{esc(stereo)}»</text>')
        ty += 18
    if title:
        out.append(f'<text x="{x+w/2}" y="{ty}" text-anchor="middle" class="nm">{esc(title)}</text>')
    out.append(f'<line x1="{x}" y1="{y+head}" x2="{x+w}" y2="{y+head}" stroke="{stroke}"/>')
    for i, t in enumerate(lines):
        out.append(f'<text x="{x+14}" y="{y+head+21+i*LH}" class="a">{esc(t)}</text>')
    return dict(x=x, y=y, w=w, h=h, bottom=y+h)

def band(tag, name, y0, y1, fill):
    out.append(f'<rect x="20" y="{y0}" width="{W-40}" height="{y1-y0}" rx="8" fill="{fill}" stroke="#d8d5cc"/>')
    out.append(f'<text x="36" y="{y0+22}" class="st">{tag}</text>')
    out.append(f'<text x="36" y="{y0+42}" class="nm">{esc(name)}</text>')

def lab(x, y, t, anchor='start'):
    out.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="r">{esc(t)}</text>')

def arrow(pts):
    d = 'M' + ' L'.join(f'{x},{y}' for x, y in pts)
    out.append(f'<path d="{d}" fill="none" stroke="#1a1a1a" stroke-width="1.2" marker-end="url(#c-arr)"/>')

# Actor
out.append('<rect x="480" y="16" width="440" height="62" rx="6" fill="#faf9f5" stroke="#1a1a1a" stroke-dasharray="6,4"/>')
out.append('<text x="700" y="38" text-anchor="middle" class="st">«actor»</text>')
out.append('<text x="700" y="62" text-anchor="middle" class="nm">Investigador (navegador)</text>')

# Bandas
band('CAPA 1', 'Presentación', 96, 250, '#f4f2ea')
band('CAPA 2', 'Lógica de negocio', 266, 432, '#efede4')
band('CAPA 3', 'Procesamiento asíncrono', 452, 650, '#f4f2ea')
band('CAPA 4', 'Datos', 666, 860, '#efede4')

fe = box(420, 124, 560, ['React + Vite', 'Formularios, resultados y reportes'], 'frontend', 'contenedor')
be = box(420, 294, 560, ['Spring Boot (Java 21)', 'API REST (JSON) con JWT', 'Valida videos y encola análisis'], 'backend', 'contenedor')
# Worker (pieza clave)
wk = box(260, 480, 880, ['OpenCV: preprocesamiento y cilindros', 'PyTorch: red de fusión R(2+1)D-18',
                         'Python: un análisis a la vez; reencola al arrancar',
                         'Python: tareas diarias (borrado, aviso, disco)'],
         'worker', 'contenedor', fill='#fbe9e2', stroke='#d9532c', sw=1.5)
db = box(40, 716, 430, ['PostgreSQL 16', 'Tabla ANALISIS = cola de análisis', '12 tablas del esquema'], 'Base de datos', 'contenedor')
vid = box(500, 716, 440, ['videos, copias de revisión,', 'recuadros, pausas, reportes'], 'Volumen compartido', 'volumen', fill='#ece7d8')
mod = box(970, 716, 390, ['solo lectura para el worker', 'archivo del clasificador'], 'Volumen de modelos', 'volumen', fill='#ece7d8')

# Flechas
arrow([(700, fe['bottom']), (700, be['y'])])
lab(712, (fe['bottom'] + be['y']) / 2 + 5, 'API REST (JSON + JWT)')
arrow([(700, be['bottom']), (700, wk['y'])])
lab(712, (be['bottom'] + wk['y']) / 2 + 5, 'ENCOLA ANÁLISIS')
arrow([(420, be['y'] + 40), (250, be['y'] + 40), (250, db['y'])])
lab(240, 580, 'LEE Y ESCRIBE ANÁLISIS', 'end')
arrow([(400, wk['bottom']), (400, db['y'])])
lab(412, wk['bottom'] + 30, 'TOMA TAREAS Y GUARDA')
arrow([(660, wk['bottom']), (660, vid['y'])])
lab(672, wk['bottom'] + 30, 'GUARDA ARCHIVOS')
arrow([(1080, mod['y']), (1080, wk['bottom'])])
lab(1092, wk['bottom'] + 30, 'CARGA AL INICIAR')

legend = '''<g transform="translate(40,884)" class="lg">
<rect x="0" y="-12" width="24" height="16" rx="3" fill="#faf9f5" stroke="#1a1a1a"/><text x="34" y="2">CONTENEDOR</text>
<rect x="200" y="-12" width="24" height="16" rx="3" fill="#ece7d8" stroke="#1a1a1a"/><text x="234" y="2">VOLUMEN</text>
<line x1="380" y1="-4" x2="412" y2="-4" stroke="#1a1a1a"/><path d="M406,-8 L412,-4 L406,0" fill="none" stroke="#1a1a1a"/><text x="422" y="2">COMUNICACIÓN</text>
<rect x="650" y="-12" width="24" height="16" rx="3" fill="#fbe9e2" stroke="#d9532c" stroke-width="1.5"/><text x="684" y="2">PIEZA CLAVE: WORKER SEPARADO DEL BACKEND</text>
</g>'''

svg = f'''<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="ca-title ca-desc" xmlns="http://www.w3.org/2000/svg">
<title id="ca-title">Arquitectura de software por capas</title>
<desc id="ca-desc">Cuatro capas: presentación (React), lógica de negocio (Spring Boot), procesamiento asíncrono (worker con OpenCV y PyTorch) y datos (PostgreSQL y dos volúmenes).</desc>
<defs><marker id="c-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1,1 L9,5 L1,9" fill="none" stroke="#1a1a1a" stroke-width="1.2"/></marker></defs>
<style>
.a{{font:400 {FS}px 'Geist Mono',monospace;fill:#1a1a1a}}
.nm{{font:600 18px Geist,sans-serif;fill:#1a1a1a}}
.st{{font:400 {FS}px 'Geist Mono',monospace;fill:#6b6b6b}}
.r{{font:400 {FS}px 'Geist Mono',monospace;fill:#6b6b6b}}
.lg text{{font:400 {FS}px 'Geist Mono',monospace;fill:#6b6b6b}}
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
print('ok', W, H)
