import math, html, sys

CH = 5.5  # ancho aprox. de un caracter mono de 9px
LH = 14

def comp_h(n):
    return n * LH + 12 if n else 0

C = {}
def cls(name, col, y, attrs=(), ops=(), stereo=None, focal=False):
    C[name] = dict(col=col, y=y, attrs=list(attrs), ops=list(ops), stereo=stereo, focal=focal)

# ---- Datos tomados de diagramas/clases.puml ----
cls('Administrador', 0, 40, [], [
    '+ crearCuentaUsuario(datos): Usuario', '+ desactivarCuentaUsuario(id): void',
    '+ listarUsuarios(): List<Usuario>', '+ monitorearSistema(): void'])
cls('Usuario', 1, 40, [
    '- idInstitucional: String', '- nombre: String', '- apellidos: String', '- correo: String',
    '- contrasenaHash: String', '- activo: Boolean', '- cambioRequerido: Boolean'], [
    '+ iniciarSesion(correo, contrasena): String', '+ cerrarSesion(token): void',
    '+ cambiarContrasena(nueva): void', '+ crearExperimento(datos): Experimento',
    '+ subirVideo(idTanda, sesion, archivo): Video', '+ eliminarExperimento(id): void',
    '+ descargarReporte(idExperimento, formato): Reporte'])
cls('Experimento', 2, 40, ['- id: Integer', '- nombre: String', '- fecha: Date', '- notas: String'],
    ['+ validarNombreUnico(): Boolean', '+ consultarEstado(): String'])
cls('Grupo', 3, 40, ['- id: Integer', '- etiqueta: String', '- tipo: String', '- tratamiento: String'])
cls('Tanda', 4, 40, ['- id: Integer', '- ordinal: Integer', '- nCilindros: Integer'])
cls('Especimen', 4, 240, ['- id: Integer', '- numeroCilindro: Integer'])
cls('Video', 3, 200, ['- id: Integer', '- sesion: String', '- archivo: String', '- duracion: Float',
    '- fechaCarga: DateTime'], ['+ validarFormatoMp4(): Boolean', '+ validarReproducible(): Boolean',
    '+ estaProximaEliminacion(dias): Boolean'])
cls('Analisis', 2, 240, ['- id: Integer', '- estado: String', '- etapa: String', '- nivelClasif: String',
    '- fechaAnalisis: DateTime'])
cls('Worker', 2, 400, [], ['+ procesarCola(): void', '+ borrarVideosExpirados(): void'], stereo='control')
cls('PipelineAnalisis', 2, 520, [], [
    '+ preprocesarVideo(video): void', '+ detectarCilindros(): List<ROI>',
    '+ clasificarConducta(especimen, roi, segundo): String', '+ generarReporte(experimento, tipo): Reporte',
    '+ actualizarProgreso(idAnalisis, pct, etapa): void', '+ marcarError(idAnalisis, mensaje): void'],
    stereo='control')
cls('ROI', 5, 240, ['- numeroCilindro: Integer', '- x: Integer', '- y: Integer', '- w: Integer', '- h: Integer', '- yAgua: Integer', '- yFondo: Integer'])
cls('Notificacion', 1, 330, ['- id: Integer', '- tipo: String', '- mensaje: String', '- leido: Boolean',
    '- fechaCreacion: DateTime'], ['+ marcarComoLeida(): void'])
cls('Reporte', 1, 500, ['- id: Integer', '- formato: String', '- ruta: String', '- fechaGeneracion: DateTime'],
    ['+ generar(experimento, formato): void', '+ descargar(): File'])
cls('Observacion', 3, 450, [], ['+ calcularBloques(): List<String>'])
cls('Intervalo', 4, 460, ['- minuto: Integer'])
cls('Conducta', 4, 620, ['- nombre: String'])
cls('PRESENTA', 5, 540, ['- segundos: Float'])
cls('Segundo', 3, 580, ['- segundo: Integer', '- conducta: String', '- origen: String'],
    ['+ corregir(conducta, origen): void'])

# ---- Geometria ----
ncol = 6
colw = [0] * ncol
for c in C.values():
    lines = c['attrs'] + c['ops'] + [n for n in ['«control»'] if c['stereo']]
    w = max([len(t) for t in lines] + [10]) * CH + 28
    colw[c['col']] = max(colw[c['col']], math.ceil(w / 20) * 20, 180)
GAP = [110, 110, 150, 100, 110]
colx = [40]
for i in range(1, ncol):
    colx.append(colx[-1] + colw[i - 1] + GAP[i - 1])

for n, c in C.items():
    c['x'] = colx[c['col']]; c['w'] = colw[c['col']]
    a, o = comp_h(len(c['attrs'])), comp_h(len(c['ops']))
    c['h'] = 32 + a + o if (a or o) else 44
    c['ah'], c['oh'] = a, o

def L(n, dy): c = C[n]; return (c['x'], c['y'] + dy)
def R(n, dy): c = C[n]; return (c['x'] + c['w'], c['y'] + dy)
def T(n, dx): c = C[n]; return (c['x'] + dx, c['y'])
def B(n, dx): c = C[n]; return (c['x'] + dx, c['y'] + c['h'])
def cx(n): return C[n]['w'] // 2
def gapx(i, off): return colx[i] + colw[i] + off  # i = columna a cuya derecha esta el hueco

edges = []
def edge(pts, kind, m1='', m2='', role='', start='', end='', role_seg=None):
    edges.append(dict(pts=pts, kind=kind, m1=m1, m2=m2, role=role, start=start, end=end, role_seg=role_seg))

ASSOC, DEP, INH, PLAIN = 'assoc', 'dep', 'inh', 'plain'

# Herencia
edge([R('Administrador', 16), L('Usuario', 16)], INH, end='tri')
# Usuario
edge([R('Usuario', 16), L('Experimento', 16)], ASSOC, '1', '0..*', 'REGISTRA', end='arrow')
edge([B('Usuario', cx('Usuario')), T('Notificacion', cx('Usuario'))], ASSOC, '1', '0..*', 'RECIBE', end='arrow')
# Jerarquia experimental
edge([R('Experimento', 16), L('Grupo', 16)], ASSOC, '1', '3..*', 'COMPONE', start='dia', end='')
edge([R('Grupo', 16), L('Tanda', 16)], ASSOC, '1', '1..*', 'SE GRABA EN', start='dia')
tx = C['Tanda']['x']
edge([B('Tanda', C['Tanda']['w'] - 60), B('Especimen', C['Tanda']['w'] - 60) if False else (tx + C['Tanda']['w'] - 60, C['Especimen']['y'])],
     ASSOC, '1', '2..4', 'ALOJA', start='dia')
edge([B('Tanda', 60), (tx + 60, C['Video']['y'] + 16), R('Video', 16)], ASSOC, '1', '1..2', 'PRODUCE', start='dia')
# Analisis
edge([R('Analisis', 30), L('Video', 70)], ASSOC, '1', '1', 'PROCESA', end='arrow')
# Dependencias del Worker / Pipeline
edge([T('Worker', cx('Worker')), B('Analisis', cx('Worker'))], DEP, role='PROCESA', end='arrow')
edge([B('Worker', cx('Worker')), T('PipelineAnalisis', cx('Worker'))], DEP, role='INVOCA', end='arrow')
g2 = lambda off: gapx(2, off)
edge([R('Worker', 20), (g2(40), C['Worker']['y'] + 20), (g2(40), C['Video']['y'] + 120), L('Video', 120)],
     DEP, role='ELIMINA', end='arrow', role_seg=2)
edge([R('PipelineAnalisis', 25), (g2(90), C['PipelineAnalisis']['y'] + 25), (g2(90), C['Video']['y'] + 160), L('Video', 160)],
     DEP, role='PROCESA', end='arrow', role_seg=1)
edge([R('PipelineAnalisis', 60), (g2(120), C['PipelineAnalisis']['y'] + 60), (g2(120), C['Observacion']['y'] + 22), L('Observacion', 22)],
     DEP, role='ORIGINA', end='arrow', role_seg=0)
edge([R('PipelineAnalisis', 90), (g2(30), C['PipelineAnalisis']['y'] + 90), (g2(30), 760),
      (C['PRESENTA']['x'] + C['PRESENTA']['w'] // 2, 760), (C['PRESENTA']['x'] + C['PRESENTA']['w'] // 2, C['PRESENTA']['y'] + C['PRESENTA']['h'])],
     DEP, role='GENERA', end='arrow', role_seg=2)
g1 = lambda off: gapx(1, off)
edge([L('PipelineAnalisis', 20), (g1(95), C['PipelineAnalisis']['y'] + 20), (g1(95), C['Analisis']['y'] + 90), L('Analisis', 90)],
     DEP, end='arrow')
# Usuario -> Notificacion / Reporte desde Experimento
edge([L('Experimento', 70), (g1(25), C['Experimento']['y'] + 70), (g1(25), C['Notificacion']['y'] + 20), R('Notificacion', 20)],
     ASSOC, '0..1', '0..*', 'ORIGINA', end='arrow', role_seg=1)
edge([L('Experimento', 100), (g1(60), C['Experimento']['y'] + 100), (g1(60), C['Reporte']['y'] + 20), R('Reporte', 20)],
     ASSOC, '1', '0..*', 'ORIGINA', end='arrow', role_seg=1)
# Resultados
g3 = lambda off: gapx(3, off)
edge([L('Especimen', 36), (g3(50), C['Especimen']['y'] + 36), (g3(50), C['Observacion']['y'] + 16), R('Observacion', 16)],
     ASSOC, '1', '1..2', 'APARECE EN', end='arrow', role_seg=1)
edge([B('Video', cx('Video')), T('Observacion', cx('Video'))], ASSOC, '1', '2..4', 'CONTIENE', end='arrow')
edge([R('Observacion', 36), L('Intervalo', 26)], ASSOC, '1', '5', 'SE DIVIDE EN', start='dia')
edge([B('Observacion', cx('Video')), T('Segundo', cx('Video'))], ASSOC, '1', '1..300', 'SE ETIQUETA EN', start='dia')
edge([B('Intervalo', cx('Intervalo')), T('Conducta', cx('Intervalo'))], PLAIN, '2..4', '0..*', '')

# ROI: creado por el pipeline (2..4) y delimita a cada especimen
roi = C['ROI']; rx = roi['x'] + roi['w']
edge([R('PipelineAnalisis', 110), (g2(20), C['PipelineAnalisis']['y'] + 110), (g2(20), 780),
      (rx + 30, 780), (rx + 30, roi['y'] + 60), (rx, roi['y'] + 60)],
     DEP, m2='2..4', role='CREA', end='arrow', role_seg=2)
edge([R('Especimen', 36), L('ROI', 36)], ASSOC, '1', '0..*', 'SE DELIMITA CON', end='arrow')
midy = (C['Intervalo']['y'] + C['Intervalo']['h'] + C['Conducta']['y']) // 2
edge([(C['Intervalo']['x'] + cx('Intervalo'), midy), L('PRESENTA', C['PRESENTA']['h'] // 2 + (midy - (C['PRESENTA']['y'] + C['PRESENTA']['h'] // 2)))],
     'dot')

# ---- SVG ----
out = []
def esc(s): return html.escape(s)
maxx = max(c['x'] + c['w'] for c in C.values()) + 70
maxy = 900
for e in edges:
    pts = e['pts']; k = e['kind']
    d = 'M' + ' L'.join(f'{x},{y}' for x, y in pts)
    attrs = 'fill="none" stroke-width="1"'
    if k == DEP: attrs += ' stroke="#6b6b6b" stroke-dasharray="4,3"'
    elif k == 'dot': attrs += ' stroke="#6b6b6b" stroke-dasharray="2,3"'
    elif k == INH: attrs += ' stroke="#1a1a1a"'
    else: attrs += ' stroke="#1a1a1a"' if e['start'] == 'dia' else ' stroke="#6b6b6b"'
    if e['start'] == 'dia': attrs += ' marker-start="url(#cl-dia)"'
    if e['end'] == 'arrow': attrs += ' marker-end="url(#cl-arr)"'
    if e['end'] == 'tri': attrs += ' marker-end="url(#cl-tri)"'
    out.append(f'<path d="{d}" {attrs}/>')

def unit(a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]; n = math.hypot(dx, dy) or 1
    return dx / n, dy / n

def mult(p, q, text, d):
    if not text: return
    ux, uy = unit(p, q)
    if abs(ux) > abs(uy):
        x = p[0] + ux * d; y = p[1] - 6
        anch = 'start' if ux > 0 else 'end'
    else:
        x = p[0] + 8; y = p[1] + uy * d + (3 if uy > 0 else 0); anch = 'start'
    out.append(f'<text x="{x:.0f}" y="{y:.0f}" text-anchor="{anch}" class="m">{esc(text)}</text>')

labels = []
for e in edges:
    pts = e['pts']
    d1 = 22 if e['start'] == 'dia' else 10
    mult(pts[0], pts[1], e['m1'], d1)
    mult(pts[-1], pts[-2], e['m2'], 14)
    if e['role']:
        segs = list(range(len(pts) - 1))
        i = e['role_seg'] if e['role_seg'] is not None else max(segs, key=lambda s: math.hypot(pts[s+1][0]-pts[s][0], pts[s+1][1]-pts[s][1]))
        a, b = pts[i], pts[i + 1]
        mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
        tw = len(e['role']) * 5.2 + 6
        if abs(b[0] - a[0]) >= abs(b[1] - a[1]):
            labels.append(f'<rect x="{mx - tw/2:.0f}" y="{my + 4:.0f}" width="{tw:.0f}" height="11" fill="#faf9f5"/>'
                          f'<text x="{mx:.0f}" y="{my + 13:.0f}" text-anchor="middle" class="r">{esc(e["role"])}</text>')
        else:
            labels.append(f'<rect x="{mx + 5:.0f}" y="{my - 6:.0f}" width="{tw:.0f}" height="11" fill="#faf9f5"/>'
                          f'<text x="{mx + 8:.0f}" y="{my + 3:.0f}" class="r">{esc(e["role"])}</text>')
out += labels

for n, c in C.items():
    x, y, w, h = c['x'], c['y'], c['w'], c['h']
    fill, stroke, sw = ('#fbe9e2', '#d9532c', 1.5) if c['focal'] else ('#faf9f5', '#1a1a1a', 1)
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
    if c['stereo']:
        out.append(f'<text x="{x + w/2}" y="{y + 12}" text-anchor="middle" class="st">«{c["stereo"]}»</text>')
        out.append(f'<text x="{x + w/2}" y="{y + 26}" text-anchor="middle" class="nm">{esc(n)}</text>')
    else:
        out.append(f'<text x="{x + w/2}" y="{y + 21}" text-anchor="middle" class="nm">{esc(n)}</text>')
    if c['attrs'] or c['ops']:
        out.append(f'<line x1="{x}" y1="{y+32}" x2="{x+w}" y2="{y+32}" stroke="{stroke}"/>')
    yy = y + 32 + 18
    for t in c['attrs']:
        out.append(f'<text x="{x+12}" y="{yy}" class="a">{esc(t)}</text>'); yy += LH
    if c['attrs'] and c['ops']:
        sy = y + 32 + c['ah']
        out.append(f'<line x1="{x}" y1="{sy}" x2="{x+w}" y2="{sy}" stroke="{stroke}"/>')
        yy = sy + 18
    elif c['ops']:
        yy = y + 32 + 14 + 4
    for t in c['ops']:
        out.append(f'<text x="{x+12}" y="{yy}" class="a">{esc(t)}</text>'); yy += LH


# Nota del ROI
nx, ny, nw, nh = roi['x'], roi['y'] + roi['h'] + 24, roi['w'], 58
out.append(f'<line x1="{nx+nw/2}" y1="{roi["y"]+roi["h"]}" x2="{nx+nw/2}" y2="{ny}" stroke="#6b6b6b" stroke-dasharray="2,3"/>')
out.append(f'<rect x="{nx}" y="{ny}" width="{nw}" height="{nh}" rx="3" fill="#faf9f5" stroke="#6b6b6b" stroke-dasharray="4,3"/>')
for i, t in enumerate(['Coordenadas del video', 'ya estabilizado. No se', 'guarda en la base de datos.']):
    out.append(f'<text x="{nx+10}" y="{ny+18+i*14}" class="a">{t}</text>')
# Paquetes (etiquetas de zona, solo texto)
leg_y = 850
legend = f'''<g transform="translate(40,{leg_y})" class="lg">
<path d="M0,0 L8,-6 L16,0 L8,6 Z" fill="#1a1a1a"/><line x1="16" y1="0" x2="44" y2="0" stroke="#1a1a1a"/><text x="54" y="3">COMPOSICIÓN</text>
<line x1="170" y1="0" x2="198" y2="0" stroke="#6b6b6b"/><path d="M192,-4 L198,0 L192,4" fill="none" stroke="#6b6b6b"/><text x="208" y="3">ASOCIACIÓN</text>
<line x1="320" y1="0" x2="348" y2="0" stroke="#6b6b6b" stroke-dasharray="4,3"/><path d="M342,-4 L348,0 L342,4" fill="none" stroke="#6b6b6b"/><text x="358" y="3">DEPENDENCIA</text>
<path d="M480,0 L492,-6 L492,6 Z" fill="#faf9f5" stroke="#1a1a1a"/><line x1="470" y1="0" x2="480" y2="0" stroke="#1a1a1a"/><text x="502" y="3">HERENCIA</text>
<line x1="600" y1="0" x2="628" y2="0" stroke="#6b6b6b" stroke-dasharray="2,3"/><text x="638" y="3">CLASE ASOCIATIVA</text>
</g>'''

svg = f'''<svg viewBox="10 20 {maxx-20} 855" role="img" aria-labelledby="cl-title cl-desc" xmlns="http://www.w3.org/2000/svg">
<title id="cl-title">Diagrama de clases completo del sistema</title>
<desc id="cl-desc">Las 18 clases del sistema con sus relaciones: usuarios, experimentos, video, pipeline de analisis y resultados.</desc>
<defs>
<marker id="cl-dia" viewBox="0 0 16 12" refX="0" refY="6" markerWidth="16" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M0,6 L8,0 L16,6 L8,12 Z" fill="#1a1a1a" stroke="#1a1a1a"/></marker>
<marker id="cl-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1,1 L9,5 L1,9" fill="none" stroke="#444" stroke-width="1.2"/></marker>
<marker id="cl-tri" viewBox="0 0 14 14" refX="13" refY="7" markerWidth="14" markerHeight="14" markerUnits="userSpaceOnUse" orient="auto"><path d="M1,1 L13,7 L1,13 Z" fill="#faf9f5" stroke="#1a1a1a"/></marker>
</defs>
<style>
.a{{font:400 9px 'Geist Mono',monospace;fill:#1a1a1a}}
.nm{{font:600 12px Geist,sans-serif;fill:#1a1a1a}}
.st{{font:400 8px 'Geist Mono',monospace;fill:#6b6b6b}}
.m{{font:400 8px 'Geist Mono',monospace;fill:#1a1a1a}}
.r{{font:400 8px 'Geist Mono',monospace;fill:#6b6b6b;letter-spacing:.06em}}
.lg text{{font:400 9px 'Geist Mono',monospace;fill:#6b6b6b}}
</style>
{chr(10).join(out)}
{legend}
</svg>'''

page = f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Clases: sistema completo</title>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;600&family=Geist+Mono:wght@400&family=Instrument+Serif&display=swap" rel="stylesheet">
<style>
:root{{--paper:#faf9f5;--ink:#1a1a1a;--muted:#6b6b6b;--rule:#d8d5cc}}
body{{margin:0;background:var(--paper);color:var(--ink);font-family:Geist,system-ui,sans-serif}}
html,body{{height:100%}}
body{{overflow-x:auto;overflow-y:hidden}}
svg{{display:block;height:100vh;width:auto}}
</style></head><body>{svg}</body></html>'''

open(sys.argv[1], 'w', encoding='utf-8').write(page)
print('ok', maxx, 'x', maxy, 'clases', len(C), 'aristas', len(edges))
