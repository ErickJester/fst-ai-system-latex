import html, sys
esc = html.escape
out = []
LH = 14

def node(x, y, w, title, lines, focal=False, fill='#faf9f5'):
    h = 30 + len(lines) * LH + 10
    f, s, sw = ('#fbe9e2', '#d9532c', 1.5) if focal else (fill, '#1a1a1a', 1)
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{f}" stroke="{s}" stroke-width="{sw}"/>')
    out.append(f'<text x="{x+w/2}" y="{y+20}" text-anchor="middle" class="nm">{esc(title)}</text>')
    for i, t in enumerate(lines):
        out.append(f'<text x="{x+w/2}" y="{y+38+i*LH}" text-anchor="middle" class="a">{esc(t)}</text>')
    return dict(x=x, y=y, w=w, h=h)

def frame(x, y, w, h, title, dash=True, fill='#f1eee5'):
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="#6b6b6b"' + (' stroke-dasharray="6,4"' if dash else '') + '/>')
    out.append(f'<text x="{x+14}" y="{y+18}" class="st">{esc(title)}</text>')

def arrow(pts, dashed=False, color='#1a1a1a'):
    d = 'M' + ' L'.join(f'{x},{y}' for x, y in pts)
    out.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="1"' + (' stroke-dasharray="4,3"' if dashed else '') + ' marker-end="url(#f-arr)"/>')

def label(x, y, t, anchor='middle'):
    tw = len(t) * 5.2 + 8
    x0 = x - tw / 2 if anchor == 'middle' else x - 4
    out.append(f'<rect x="{x0:.0f}" y="{y-9}" width="{tw:.0f}" height="11" fill="#faf9f5"/><text x="{x}" y="{y}" text-anchor="{anchor}" class="r">{esc(t)}</text>')

# ---- Entrenamiento (fuera de linea) ----
frame(500, 24, 1160, 136, 'ENTRENAMIENTO Y EVALUACIÓN · FUERA DE LÍNEA, ANTES DE DESPLEGAR · NO ES PARTE DEL FLUJO POR VIDEO')
t1 = node(520, 56, 170, 'Videos del laboratorio', ['sin sus anotaciones', 'manuales'])
t2 = node(730, 56, 200, 'Etiquetado por el equipo', ['el etiquetador propone,', 'el equipo revisa y corrige'])
t3 = node(970, 56, 170, 'Entrenamiento', ['con los bloques', 'etiquetados'])
t4 = node(1255, 56, 150, 'Modelo entrenado', ['en el volumen', 'de modelos'])
t5 = node(1445, 56, 190, 'Evaluación', ['precisión, recall y F1', 'por conducta (provisional)'])
arrow([(690, 86), (730, 86)])
arrow([(930, 86), (970, 86)])
arrow([(1140, 86), (1255, 86)])
arrow([(1405, 86), (1445, 86)])

# ---- Flujo por video ----
Y = 282
a1 = node(40, Y, 170, 'Investigador', ['sube el video', 'del experimento'])
a2 = node(250, Y, 190, 'Backend', ['valida formato y orientación', 'y guarda el video'])
a3 = node(480, Y, 170, 'Se encola el análisis', ['estado «en cola»'])
a4 = node(690, Y, 170, 'Worker', ['toma la tarea', '(consulta periódica)'])
frame(900, 240, 520, 150, 'PIPELINE DE ANÁLISIS · DENTRO DEL WORKER')
p1 = node(915, Y, 150, 'Preprocesamiento', ['registro de cámara', 'y modelo de fondo'])
p2 = node(1085, Y, 150, 'Cilindros', ['localiza de 2 a 4', 'tubos por video'])
p3 = node(1255, Y, 150, 'Clasificación', ['conducta de cada', 'segundo, con el modelo'], focal=True)
mid = lambda n: n['y'] + 44
arrow([(210, mid(a1)), (250, mid(a1))])
arrow([(440, mid(a2)), (480, mid(a2))])
arrow([(650, mid(a3)), (690, mid(a3))])
arrow([(860, mid(a4)), (915, mid(a4))])
arrow([(1065, mid(p1)), (1085, mid(p1))])
arrow([(1235, mid(p2)), (1255, mid(p2))])
# modelo -> clasificacion
arrow([(1330, 56 + t4['h']), (1330, Y)])
label(1330, 200, 'MODELO ENTRENADO')
# falla
e1 = node(915, 440, 290, 'Si falla', ['el video no se abre o no se encuentran', 'los cilindros: el análisis pasa a «error»', 'con reporte de diagnóstico y aviso'], fill='#faf9f5')
arrow([(1065, 390), (1065, 440)], dashed=True, color='#6b6b6b')
label(1100, 420, 'FALLA')
# exito
r1 = node(1235, 440, 190, 'Resultados', ['conducta de cada segundo,', 'tiempos por minuto,', 'video anotado'])
arrow([(1330, 390), (1330, 440)])
label(1370, 420, 'ÉXITO', 'start')
r2 = node(1235, 580, 190, 'Investigador', ['consulta y revisa segundo', 'a segundo; los totales', 'por minuto se recalculan'])
arrow([(1330, 440 + r1['h']), (1330, 580)])
r3 = node(985, 580, 190, 'Reportes', ['descarga en PDF,', 'CSV o XLSX'])
arrow([(1235, 580 + 44), (1175, 580 + 44)])

legend = '''<g transform="translate(40,690)" class="lg">
<line x1="0" y1="0" x2="28" y2="0" stroke="#1a1a1a"/><path d="M22,-4 L28,0 L22,4" fill="none" stroke="#1a1a1a"/><text x="38" y="3">FLUJO NORMAL</text>
<line x1="160" y1="0" x2="188" y2="0" stroke="#6b6b6b" stroke-dasharray="4,3"/><path d="M182,-4 L188,0 L182,4" fill="none" stroke="#6b6b6b"/><text x="198" y="3">FLUJO DE FALLA</text>
<rect x="340" y="-8" width="22" height="14" rx="3" fill="#fbe9e2" stroke="#d9532c" stroke-width="1.5"/><text x="370" y="3">CLASIFICACIÓN: LA ÚNICA ETAPA QUE USA EL MODELO</text>
</g>'''
W, H = 1700, 720
svg = f'''<svg viewBox="0 10 {W} {H-10}" role="img" aria-labelledby="fl-title fl-desc" xmlns="http://www.w3.org/2000/svg">
<title id="fl-title">Flujo general del sistema</title>
<desc id="fl-desc">Del video subido por el investigador al análisis en cola, las tres etapas del pipeline, los resultados y los reportes, con el entrenamiento del modelo fuera de línea.</desc>
<defs><marker id="f-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1,1 L9,5 L1,9" fill="none" stroke="#444" stroke-width="1.2"/></marker></defs>
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
<title>Flujo del sistema</title>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;600&family=Geist+Mono:wght@400&display=swap" rel="stylesheet">
<style>
html,body{{height:100%;margin:0;background:#faf9f5}}
body{{overflow-x:auto;overflow-y:hidden}}
svg{{display:block;height:100vh;width:auto}}
</style></head><body>{svg}</body></html>'''
open(sys.argv[1], 'w', encoding='utf-8').write(page)
print('ok')
