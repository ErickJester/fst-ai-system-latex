import html, sys
esc = html.escape
out = []
FS = 18
LH = 24
W, H = 1680, 1040

def node(x, y, w, title, lines, focal=False):
    h = 44 + len(lines) * LH + 16
    f, s, sw = ('#fbe9e2', '#d9532c', 1.5) if focal else ('#faf9f5', '#1a1a1a', 1)
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{f}" stroke="{s}" stroke-width="{sw}"/>')
    out.append(f'<text x="{x+w/2}" y="{y+28}" text-anchor="middle" class="nm">{esc(title)}</text>')
    for i, t in enumerate(lines):
        out.append(f'<text x="{x+w/2}" y="{y+52+i*LH}" text-anchor="middle" class="a">{esc(t)}</text>')
    return dict(x=x, y=y, w=w, h=h, b=y+h, cx=x+w/2, cy=y+h/2)

def frame(x, y, w, h, title, bottom=False):
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="#f1eee5" stroke="#6b6b6b" stroke-dasharray="6,4"/>')
    out.append(f'<text x="{x+w-16}" y="{y+26}" text-anchor="end" class="st">{esc(title)}</text>')

def arrow(pts, dashed=False):
    d = 'M' + ' L'.join(f'{x},{y}' for x, y in pts)
    out.append(f'<path d="{d}" fill="none" stroke="{"#6b6b6b" if dashed else "#1a1a1a"}" stroke-width="1.4"' + (' stroke-dasharray="6,4"' if dashed else '') + ' marker-end="url(#f-arr)"/>')

def label(x, y, t, anchor='start'):
    out.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="r">{esc(t)}</text>')

# ---- Entrenamiento (fuera de línea) ----
frame(20, 14, 1640, 176, 'ENTRENAMIENTO Y EVALUACIÓN · FUERA DE LÍNEA · NO ES PARTE DEL FLUJO POR VIDEO')
t1 = node(40, 56, 290, 'Videos', ['sin las anotaciones', 'manuales'])
t2 = node(370, 56, 290, 'Etiquetado', ['el equipo revisa', 'las conductas'])
t3 = node(700, 56, 290, 'Entrenamiento', ['con los segundos', 'etiquetados'])
t4 = node(1030, 56, 290, 'Modelo', ['en el volumen', 'de modelos'])
t5 = node(1360, 56, 280, 'Evaluación', ['F1 por conducta', '(provisional)'])
arrow([(330, t1['cy']), (370, t1['cy'])])
arrow([(660, t2['cy']), (700, t2['cy'])])
arrow([(990, t3['cy']), (1030, t3['cy'])])
arrow([(1320, t4['cy']), (1360, t4['cy'])])

# ---- Flujo por video (fila principal) ----
Y = 260
a1 = node(40, Y, 330, 'Investigador', ['sube el video', 'del experimento'])
a2 = node(410, Y, 330, 'Backend', ['valida formato', 'y guarda el video'])
a3 = node(780, Y, 330, 'Cola de análisis', ['estado «en cola»;', 'Día 1: solo se guarda'])
a4 = node(1150, Y, 330, 'Worker', ['toma el más antiguo;', 'un video a la vez'])
arrow([(370, a1['cy']), (410, a1['cy'])])
arrow([(740, a2['cy']), (780, a2['cy'])])
arrow([(1110, a3['cy']), (1150, a3['cy'])])

# ---- Pipeline ----
frame(40, 430, 1600, 230, 'PIPELINE DE ANÁLISIS · DENTRO DEL WORKER')
p1 = node(70, 470, 330, 'Preprocesamiento', ['registro de cámara', 'y modelo de fondo'])
p2 = node(440, 470, 330, 'Cilindros', ['localiza de 2 a 4', 'tubos por video'])
p3 = node(810, 470, 330, 'Clasificación', ['conducta de cada', 'segundo (modelo)'], focal=True)
pz = node(1180, 470, 440, 'En pausa', ['3 s seguidos sin ver:', 'guarda imagen y avisa;', 'el usuario ajusta o cancela;', 'sin respuesta en 72 h, cancela'])
arrow([(1310, a4['b']), (1310, 404), (235, 404), (235, p1['y'])])
arrow([(400, p1['cy']), (440, p2['cy'])])
arrow([(770, p2['cy']), (810, p3['cy'])])
arrow([(1140, p3['cy']), (1180, pz['cy'])], dashed=True)

# ---- Desenlaces ----
e1 = node(70, 720, 470, 'Si falla', ['no se abre el video o no hay', 'cilindros (o un fallo imprevisto):', 'estado «error» y diagnóstico;', 'el worker sigue con el siguiente'])
arrow([(235, p1['b']), (235, e1['y'])], dashed=True)
label(250, p1['b'] + 60, 'FALLA')
r1 = node(600, 720, 470, 'Resultados', ['conducta de cada segundo;', 'tiempos por minuto;', 'copia H.264 para revisión'])
arrow([(975, p3['b']), (975, r1['y'])])
label(990, p3['b'] + 60, 'ÉXITO')
r2 = node(1130, 720, 490, 'Investigador', ['revisa cada segundo;', 'los totales se recalculan;', 'puede reiniciar el análisis'])
arrow([(1070, r1['cy']), (1130, r2['cy'])])
r3 = node(600, 890, 470, 'Reportes', ['descarga en PDF, CSV o XLSX'])
arrow([(835, r1['b']), (835, r3['y'])])

legend = f'''<g transform="translate(40,{H-24})" class="lg">
<line x1="0" y1="0" x2="34" y2="0" stroke="#1a1a1a"/><path d="M28,-5 L34,0 L28,5" fill="none" stroke="#1a1a1a"/><text x="46" y="6">FLUJO NORMAL</text>
<line x1="230" y1="0" x2="264" y2="0" stroke="#6b6b6b" stroke-dasharray="6,4"/><path d="M258,-5 L264,0 L258,5" fill="none" stroke="#6b6b6b"/><text x="276" y="6">FLUJO DE FALLA</text>
<rect x="480" y="-10" width="26" height="18" rx="3" fill="#fbe9e2" stroke="#d9532c" stroke-width="1.5"/><text x="520" y="6">CLASIFICACIÓN: LA ÚNICA ETAPA QUE USA EL MODELO</text>
</g>'''

svg = f'''<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="fl-title fl-desc" xmlns="http://www.w3.org/2000/svg">
<title id="fl-title">Flujo general del sistema</title>
<desc id="fl-desc">Del video subido por el investigador a la cola de análisis, las tres etapas del pipeline, los resultados y los reportes, con el entrenamiento del modelo fuera de línea.</desc>
<defs><marker id="f-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1,1 L9,5 L1,9" fill="none" stroke="#444" stroke-width="1.2"/></marker></defs>
<style>
.a{{font:400 {FS}px 'Geist Mono',monospace;fill:#1a1a1a}}
.nm{{font:600 {FS}px Geist,sans-serif;fill:#1a1a1a}}
.st{{font:400 {FS}px 'Geist Mono',monospace;fill:#6b6b6b}}
.r{{font:400 {FS}px 'Geist Mono',monospace;fill:#6b6b6b}}
.lg text{{font:400 {FS}px 'Geist Mono',monospace;fill:#6b6b6b}}
</style>
{chr(10).join(out)}
{legend}
</svg>'''
page = f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Flujo del sistema</title>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;600&family=Geist+Mono:wght@400&display=swap" rel="stylesheet">
<style>
html,body{{height:100%;margin:0;background:#faf9f5}}
body{{overflow-x:auto;overflow-y:hidden}}
svg{{display:block;height:100vh;width:auto}}
</style></head><body>{svg}</body></html>'''
open(sys.argv[1], 'w', encoding='utf-8').write(page)
print('ok', W, H)
