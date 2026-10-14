import math, html, sys

# Diagrama de clases (diagramas/clases.puml) partido en dos hojas carta horizontales:
#   hoja 1: usuarios, experimentos, tandas y videos
#   hoja 2: observaciones, resultados y analisis automatico (worker y pipeline)
# Uso: gen_clases_hojas.py 1|2 salida.html
esc = html.escape
CH = 6.8     # ancho aprox. de un caracter mono de 11px
LH = 17

def comp_h(n):
    return n * LH + 12 if n else 0

DATOS = {}
def cls(name, attrs=(), ops=(), stereo=None):
    DATOS[name] = dict(attrs=list(attrs), ops=list(ops), stereo=stereo)

cls('Administrador', [], [
    '+ crearCuentaUsuario(datos): Usuario', '+ desactivarCuentaUsuario(id): void',
    '+ listarUsuarios(): List<Usuario>', '+ monitorearSistema(): void', '+ modificarCuentaUsuario(id, datos): void'])
cls('Usuario', [
    '- idInstitucional: String', '- nombre: String', '- apellidos: String', '- correo: String',
    '- contrasenaHash: String', '- activo: Boolean', '- cambioRequerido: Boolean'], [
    '+ iniciarSesion(correo, contrasena): String', '+ cerrarSesion(token): void',
    '+ cambiarContrasena(nueva): void', '+ crearExperimento(datos): Experimento',
    '+ subirVideo(idTanda, sesion, archivo): Video', '+ eliminarExperimento(id): void',
    '+ descargarReporte(idExperimento, formato): Reporte', '+ reiniciarAnalisis(idAnalisis): void',
    '+ ajustarRecuadro(idAnalisis, cilindro, recuadro): void', '+ cancelarAnalisisEnPausa(idAnalisis): void'])
cls('Experimento', ['- id: Integer', '- nombre: String', '- fecha: Date', '- notas: String'],
    ['+ validarNombreUnico(): Boolean', '+ consultarEstado(): String', '+ compararGrupos(): List<Estadisticas>'])
cls('Grupo', ['- id: Integer', '- etiqueta: String', '- tipo: String', '- tratamiento: String'],
    ['+ calcularEstadisticas(): Estadisticas'])
cls('Tanda', ['- id: Integer', '- ordinal: Integer', '- nCilindros: Integer'])
cls('Especimen', ['- id: Integer', '- numeroCilindro: Integer'])
cls('Video', ['- id: Integer', '- sesion: String', '- archivo: String', '- duracion: Float', '- fechaCarga: DateTime'],
    ['+ validarFormato(): Boolean', '+ validarOrientacion(): Boolean', '+ validarReproducible(): Boolean',
     '+ estaProximaEliminacion(dias): Boolean'])
cls('Analisis', ['- id: Integer', '- estado: String', '- etapa: String', '- nivelClasif: String',
                 '- fechaAnalisis: DateTime'])
cls('Worker', [], ['+ procesarCola(): void', '+ borrarVideosExpirados(): void', '+ avisarVencimientos(): void',
                   '+ vigilarDisco(): void', '+ reencolarHuerfanos(): void', '+ cancelarPausasVencidas(): void'],
    stereo='control')
cls('PipelineAnalisis', [], [
    '+ preprocesarVideo(video): void', '+ detectarCilindros(): List<ROI>',
    '+ clasificarConducta(especimen, roi, segundo): String', '+ generarReporte(experimento, tipo): Reporte',
    '+ actualizarProgreso(idAnalisis, etapa): void', '+ marcarError(idAnalisis, mensaje): void',
    '+ pausarAnalisis(idAnalisis): void', '+ guardarImagenPausa(idAnalisis, cilindro, segundo): void',
    '+ aplicarAjusteRecuadro(idAnalisis): void',
    '+ cancelarAnalisis(idAnalisis): void', '+ generarCopiaRevision(video): void'], stereo='control')
cls('ROI', ['- numeroCilindro: Integer', '- x: Integer', '- y: Integer', '- w: Integer', '- h: Integer',
            '- yAgua: Integer', '- yFondo: Integer'])
cls('Notificacion', ['- id: Integer', '- tipo: String', '- mensaje: String', '- leido: Boolean',
                     '- fechaCreacion: DateTime'], ['+ marcarComoLeida(): void'])
cls('Reporte', ['- id: Integer', '- formato: String', '- ruta: String', '- fechaGeneracion: DateTime'],
    ['+ generar(experimento, formato): void', '+ descargar(): File'])
cls('Observacion', [], ['+ calcularBloques(): List<String>'])
cls('Intervalo', ['- minuto: Integer'])
cls('Conducta', ['- nombre: String'])
cls('PRESENTA', ['- segundos: Float'])
cls('Segundo', ['- segundo: Integer', '- conducta: String', '- origen: String'], ['+ corregir(conducta, origen): void'])

def partir(linea, limite=44):
    """Parte una firma larga en dos renglones, despues de una coma."""
    if len(linea) <= limite:
        return [linea]
    k = linea.rfind(', ', 0, limite)
    if k < 0:
        return [linea]
    return [linea[:k + 1], '    ' + linea[k + 2:]]

UNA = sys.argv[1] == 'U'
for d in DATOS.values():
    if UNA:
        d['ops'] = [r for l in d['ops'] for r in partir(l)]
    a, o = comp_h(len(d['attrs'])), comp_h(len(d['ops']))
    d['ah'], d['oh'] = a, o
    d['h'] = 32 + a + o if (a or o) else 44
    lines = d['attrs'] + d['ops'] + (['«control»'] if d['stereo'] else [])
    d['wmin'] = max([len(t) for t in lines] + [10]) * CH + 28

C = {}                 # clases de la hoja con su posicion
edges = []
PALETA = ['#1b6fb0', '#2e8b57', '#8e44ad', '#c0392b', '#b8860b', '#16a085', '#d35400', '#e84393', '#34495e',
          '#6c8e00', '#0097a7', '#a0522d', '#5e35b1', '#c2185b', '#00796b', '#f57c00', '#455a64', '#8d6e63']
ASSOC, DEP, INH, PLAIN = 'assoc', 'dep', 'inh', 'plain'

def columnas(cols, gaps, x0=70):
    """cols: lista de listas de nombres; devuelve el ancho de cada columna y su x."""
    w = [max(max(math.ceil(DATOS[n]['wmin'] / 20) * 20, 180) for n in col) for col in cols]
    xs = [x0]
    for i in range(1, len(cols)):
        xs.append(xs[-1] + w[i - 1] + gaps[i - 1])
    for i, col in enumerate(cols):
        for n in col:
            C[n] = dict(DATOS[n], x=xs[i], w=w[i], y=0, col=i)
    return xs, w

def h(n): return C[n]['h']
def L(n, dy): return (C[n]['x'], C[n]['y'] + dy)
def R(n, dy): return (C[n]['x'] + C[n]['w'], C[n]['y'] + dy)
def T(n, dx=None): return (C[n]['x'] + (C[n]['w'] // 2 if dx is None else dx), C[n]['y'])
def B(n, dx=None): return (C[n]['x'] + (C[n]['w'] // 2 if dx is None else dx), C[n]['y'] + C[n]['h'])

def edge(pts, kind=ASSOC, m1='', m2='', role='', start='', end='arrow', role_seg=None):
    edges.append(dict(pts=pts, kind=kind, m1=m1, m2=m2, role=role, start=start, end=end, role_seg=role_seg,
                      color=PALETA[len(edges) % len(PALETA)], i=len(edges)))

extra = []   # figuras sueltas (notas, conectores)
chips = []   # (clase, texto): marcas de "continua en la otra hoja"
notas_hoja = []   # lineas explicativas de esas marcas, debajo de la leyenda

# ---------------------------------------------------------------- hoja 1
def hoja1():
    xs, w = columnas([['Administrador', 'Usuario', 'Notificacion', 'Reporte'], ['Experimento', 'Grupo', 'Tanda'],
                      ['Especimen', 'Video', 'Analisis']], [150, 150])
    C['Administrador']['y'] = 40
    C['Usuario']['y'] = 40 + h('Administrador') + 70
    C['Notificacion']['y'] = C['Usuario']['y'] + h('Usuario') + 80
    C['Reporte']['y'] = C['Notificacion']['y'] + h('Notificacion') + 80
    C['Experimento']['y'] = 40
    C['Grupo']['y'] = C['Experimento']['y'] + h('Experimento') + 80
    C['Tanda']['y'] = C['Grupo']['y'] + h('Grupo') + 130
    C['Especimen']['y'] = C['Tanda']['y']
    C['Video']['y'] = C['Especimen']['y'] + h('Especimen') + 70
    C['Analisis']['y'] = C['Video']['y'] + h('Video') + 84
    gx = lambda i, off: xs[i] + w[i] + off
    cx = C['Usuario']['w'] // 2
    edge([B('Administrador', cx), T('Usuario', cx)], INH, end='tri')
    edge([R('Usuario', 16), (gx(0, 40), C['Usuario']['y'] + 16), (gx(0, 40), C['Experimento']['y'] + 16),
          L('Experimento', 16)], ASSOC, '1', '0..*', 'REGISTRA')
    edge([B('Usuario'), T('Notificacion')], ASSOC, '1', '0..*', 'RECIBE')
    edge([B('Experimento'), T('Grupo')], ASSOC, '1', '3..*', 'COMPONE', start='dia', end='')
    edge([B('Grupo'), T('Tanda')], ASSOC, '1', '1..*', 'SE GRABA EN', start='dia', end='')
    edge([R('Tanda', 16), L('Especimen', 16)], ASSOC, '1', '2..4', 'ALOJA', start='dia', end='')
    edge([R('Tanda', 60), (gx(1, 70), C['Tanda']['y'] + 60), (gx(1, 70), C['Video']['y'] + 16), L('Video', 16)],
         ASSOC, '1', '1..2', 'PRODUCE', start='dia', end='', role_seg=1)
    edge([T('Analisis'), B('Video')], ASSOC, '0..1', '1', 'PROCESA')
    edge([L('Experimento', 60), (gx(0, 55), C['Experimento']['y'] + 60), (gx(0, 55), C['Notificacion']['y'] + 16),
          R('Notificacion', 16)], ASSOC, '0..1', '0..*', 'ORIGINA', role_seg=1)
    edge([L('Experimento', 100), (gx(0, 100), C['Experimento']['y'] + 100), (gx(0, 100), C['Reporte']['y'] + 16),
          R('Reporte', 16)], ASSOC, '1', '0..*', 'ORIGINA', role_seg=1)
    chips.extend([('Especimen', '→ hoja 2'), ('Video', '→ hoja 2'), ('Analisis', '→ hoja 2')])
    notas_hoja.extend([
        '→ hoja 2 en Especimen: sigue allí (aparece en una Observacion y se delimita con un ROI).',
        '→ hoja 2 en Video: sigue allí (contiene Observaciones; lo procesa y lo elimina el Worker y el Pipeline).',
        '→ hoja 2 en Analisis: sigue allí (lo procesa el Worker y el Pipeline).'])
    return ('Diagrama de clases (hoja 1): usuarios, experimentos y videos',
            'Clases de usuarios, experimentos, grupos, tandas, espécimen, video y análisis, con sus relaciones.')

# ---------------------------------------------------------------- hoja 2
def hoja2():
    xs, w = columnas([['Analisis', 'Worker', 'PipelineAnalisis'], ['Video', 'Observacion', 'Segundo'],
                      ['Especimen', 'Intervalo'], ['ROI', 'Conducta']], [170, 150, 160])
    C['Analisis']['y'] = 40
    C['Worker']['y'] = 40 + h('Analisis') + 76
    C['PipelineAnalisis']['y'] = C['Worker']['y'] + h('Worker') + 76
    C['Video']['y'] = C['Worker']['y'] + 4
    C['Observacion']['y'] = C['Video']['y'] + h('Video') + 84
    C['Especimen']['y'] = C['Observacion']['y']
    C['ROI']['y'] = C['Especimen']['y']
    C['Intervalo']['y'] = C['Observacion']['y'] + h('ROI') + 70
    C['Conducta']['y'] = C['Intervalo']['y']
    C['Segundo']['y'] = C['Observacion']['y'] + h('Observacion') + 136
    # PRESENTA (clase asociativa) debajo de la linea Intervalo-Conducta
    mid = (xs[2] + w[2] + xs[3]) // 2
    C['PRESENTA'] = dict(DATOS['PRESENTA'], x=mid - 100, w=200, y=C['Intervalo']['y'] + h('Intervalo') + 84, col=9)
    BM = max(c['y'] + c['h'] for c in C.values())
    R1, R2 = BM + 22, BM + 48
    gx = lambda i, off: xs[i] + w[i] + off
    px = xs[0] - 34
    # control
    edge([T('Worker'), B('Analisis')], DEP, role='PROCESA')
    edge([B('Worker'), T('PipelineAnalisis')], DEP, role='INVOCA')
    edge([R('Worker', 20), L('Video', 16)], DEP, role='ELIMINA')
    pip = C['PipelineAnalisis']['y']
    edge([L('PipelineAnalisis', 20), (px, pip + 20), (px, C['Analisis']['y'] + 90), L('Analisis', 90)], DEP)
    edge([R('PipelineAnalisis', 25), (gx(0, 40), pip + 25), (gx(0, 40), C['Video']['y'] + 120), L('Video', 120)],
         DEP, role='PROCESA', role_seg=1)
    edge([R('PipelineAnalisis', 60), (gx(0, 110), pip + 60), (gx(0, 110), C['Observacion']['y'] + 22),
          L('Observacion', 22)], DEP, role='ORIGINA', role_seg=1)
    edge([R('PipelineAnalisis', 90), (gx(0, 75), pip + 90), (gx(0, 75), R1),
          (C['PRESENTA']['x'] + C['PRESENTA']['w'] // 2, R1),
          (C['PRESENTA']['x'] + C['PRESENTA']['w'] // 2, C['PRESENTA']['y'] + C['PRESENTA']['h'])],
         DEP, role='GENERA', role_seg=2)
    roi = C['ROI']; rx = roi['x'] + roi['w']
    edge([R('PipelineAnalisis', 120), (gx(0, 45), pip + 120), (gx(0, 45), R2), (rx + 30, R2),
          (rx + 30, roi['y'] + 60), (rx, roi['y'] + 60)], DEP, m2='2..4', role='CREA', role_seg=2)
    # datos
    edge([B('Video'), T('Observacion')], ASSOC, '1', '0..4', 'CONTIENE')
    edge([L('Especimen', 16), R('Observacion', 16)], ASSOC, '1', '0..1', 'APARECE EN')
    gm = gx(1, 70)
    edge([R('Observacion', 46), (gm, C['Observacion']['y'] + 46), (gm, C['Intervalo']['y'] + 16), L('Intervalo', 16)],
         ASSOC, '1', '5', 'SE DIVIDE EN', start='dia', end='', role_seg=1)
    edge([B('Observacion'), T('Segundo')], ASSOC, '1', '1..300', 'SE ETIQUETA EN', start='dia', end='')
    edge([R('Intervalo', 16), L('Conducta', 16)], PLAIN, '0..*', '4', '', end='')
    edge([R('Especimen', 16), L('ROI', 16)], ASSOC, '1', '0..*', 'SE DELIMITA CON')
    # conector punteado de la clase asociativa
    extra.append(f'<line x1="{mid}" y1="{C["Intervalo"]["y"] + 16}" x2="{mid}" y2="{C["PRESENTA"]["y"]}" stroke="#6b6b6b" stroke-dasharray="2,3"/>')
    chips.extend([('Especimen', '← hoja 1'), ('Video', '← hoja 1'), ('Analisis', '← hoja 1')])
    notas_hoja.extend([
        '← hoja 1 en Especimen: viene de allí (lo aloja una Tanda).',
        '← hoja 1 en Video: viene de allí (lo produce una Tanda y Analisis lo procesa).',
        '← hoja 1 en Analisis: viene de allí (procesa a un Video).'])
    return ('Diagrama de clases (hoja 2): observaciones, resultados y análisis automático',
            'Clases de worker, pipeline, análisis, video, observación, intervalo, conducta, segundo y ROI, con sus relaciones.')

def hojaU():
    xs, w = columnas([['Administrador', 'Usuario', 'Notificacion', 'Reporte'],
                      ['Experimento', 'Grupo', 'Tanda', 'Analisis', 'Worker', 'PipelineAnalisis'],
                      ['Especimen', 'Video', 'Observacion', 'Segundo'], ['Intervalo'], ['ROI', 'Conducta']],
                     [150, 230, 170, 100])
    Y = lambda n, v: C[n].__setitem__('y', v)
    Y('Administrador', 40)
    Y('Usuario', 40 + h('Administrador') + 70)
    Y('Notificacion', C['Usuario']['y'] + h('Usuario') + 80)
    Y('Reporte', C['Notificacion']['y'] + h('Notificacion') + 80)
    Y('Experimento', 40)
    Y('Grupo', 40 + h('Experimento') + 80)
    Y('Tanda', C['Grupo']['y'] + h('Grupo') + 130)
    Y('Especimen', C['Tanda']['y'])
    Y('Video', C['Especimen']['y'] + h('Especimen') + 70)
    Y('Observacion', C['Video']['y'] + h('Video') + 84)
    Y('Segundo', C['Observacion']['y'] + h('Observacion') + 136)
    Y('Analisis', C['Video']['y'] + 104)
    Y('Worker', C['Analisis']['y'] + h('Analisis') + 76)
    Y('PipelineAnalisis', C['Worker']['y'] + h('Worker') + 76)
    Y('Intervalo', C['Observacion']['y'])
    Y('ROI', C['Especimen']['y'])
    Y('Conducta', C['Observacion']['y'])
    mid = (xs[3] + w[3] + xs[4]) // 2
    C['PRESENTA'] = dict(DATOS['PRESENTA'], x=mid - 100, w=200, y=C['Intervalo']['y'] + h('Intervalo') + 84, col=9)
    BM = max(c['y'] + c['h'] for c in C.values())
    R1, R2 = BM + 22, BM + 48
    gA = lambda off: xs[0] + w[0] + off
    gB = lambda off: xs[1] + w[1] + off
    gC = lambda off: xs[2] + w[2] + off
    y = lambda n: C[n]['y']
    cx = C['Usuario']['w'] // 2
    # usuarios y soporte
    edge([B('Administrador', cx), T('Usuario', cx)], INH, end='tri')
    edge([R('Usuario', 16), (gA(40), y('Usuario') + 16), (gA(40), y('Experimento') + 16), L('Experimento', 16)],
         ASSOC, '1', '0..*', 'REGISTRA')
    edge([B('Usuario'), T('Notificacion')], ASSOC, '1', '0..*', 'RECIBE')
    edge([L('Experimento', 60), (gA(70), y('Experimento') + 60), (gA(70), y('Notificacion') + 16),
          R('Notificacion', 16)], ASSOC, '0..1', '0..*', 'ORIGINA', role_seg=1)
    edge([L('Experimento', 100), (gA(115), y('Experimento') + 100), (gA(115), y('Reporte') + 16),
          R('Reporte', 16)], ASSOC, '1', '0..*', 'ORIGINA', role_seg=1)
    # estructura del experimento
    edge([B('Experimento'), T('Grupo')], ASSOC, '1', '3..*', 'COMPONE', start='dia', end='')
    edge([B('Grupo'), T('Tanda')], ASSOC, '1', '1..*', 'SE GRABA EN', start='dia', end='')
    edge([R('Tanda', 16), L('Especimen', 16)], ASSOC, '1', '2..4', 'ALOJA', start='dia', end='')
    edge([R('Tanda', 60), (gB(30), y('Tanda') + 60), (gB(30), y('Video') + 16), L('Video', 16)],
         ASSOC, '1', '1..2', 'PRODUCE', start='dia', end='', role_seg=1)
    # analisis automatico
    edge([R('Analisis', 16), L('Video', 120)], ASSOC, '0..1', '1', 'PROCESA')
    edge([T('Worker'), B('Analisis')], DEP, role='PROCESA')
    edge([B('Worker'), T('PipelineAnalisis')], DEP, role='INVOCA')
    edge([R('Worker', 20), (gB(60), y('Worker') + 20), (gB(60), y('Video') + 150), L('Video', 150)],
         DEP, role='ELIMINA')
    edge([R('PipelineAnalisis', 25), (gB(90), y('PipelineAnalisis') + 25), (gB(90), y('Video') + 185),
          L('Video', 185)], DEP, role='PROCESA')
    edge([R('PipelineAnalisis', 55), (gB(120), y('PipelineAnalisis') + 55), (gB(120), y('Analisis') + 100),
          R('Analisis', 100)], DEP)
    edge([R('PipelineAnalisis', 85), (gB(150), y('PipelineAnalisis') + 85), (gB(150), y('Observacion') + 22),
          L('Observacion', 22)], DEP, role='ORIGINA')
    pres = C['PRESENTA']
    edge([R('PipelineAnalisis', 100), (gB(205), y('PipelineAnalisis') + 100), (gB(205), R1),
          (pres['x'] + pres['w'] // 2, R1), (pres['x'] + pres['w'] // 2, pres['y'] + pres['h'])],
         DEP, role='GENERA', role_seg=2)
    roi = C['ROI']; rx = roi['x'] + roi['w']
    edge([R('PipelineAnalisis', 150), (gB(180), y('PipelineAnalisis') + 150), (gB(180), R2), (rx + 30, R2),
          (rx + 30, roi['y'] + 60), (rx, roi['y'] + 60)], DEP, m2='2..4', role='CREA', role_seg=2)
    # observaciones y resultados
    edge([B('Video'), T('Observacion')], ASSOC, '1', '0..4', 'CONTIENE')
    edge([R('Especimen', 55), (gC(60), y('Especimen') + 55), (gC(60), y('Observacion') + 22),
          R('Observacion', 22)], ASSOC, '1', '0..1', 'APARECE EN', role_seg=1)
    edge([R('Observacion', 46), L('Intervalo', 46)], ASSOC, '1', '5', 'SE DIVIDE EN', start='dia', end='')
    edge([B('Observacion'), T('Segundo')], ASSOC, '1', '1..300', 'SE ETIQUETA EN', start='dia', end='')
    edge([R('Intervalo', 16), L('Conducta', 16)], PLAIN, '0..*', '4', '', end='')
    edge([R('Especimen', 16), L('ROI', 16)], ASSOC, '1', '0..*', 'SE DELIMITA CON')
    extra.append(f'<line x1="{mid}" y1="{y("Intervalo") + 16}" x2="{mid}" y2="{pres["y"]}" stroke="#6b6b6b" stroke-dasharray="2,3"/>')
    return ('Diagrama de clases del sistema',
            'Las 18 clases del sistema con sus relaciones: usuarios, experimentos, video, pipeline de análisis y resultados.')

hoja = sys.argv[1]
titulo, desc = {'1': hoja1, '2': hoja2, 'U': hojaU}[hoja]()

# ---------------------------------------------------------------- SVG
out = []
def unit(a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]; n = math.hypot(dx, dy) or 1
    return dx / n, dy / n

for e in edges:
    pts = e['pts']; k = e['kind']; c = e['color']; i = e['i']
    d = 'M' + ' L'.join(f'{x},{y}' for x, y in pts)
    attrs = f'fill="none" stroke-width="1.4" stroke="{c}"'
    if k == DEP: attrs += ' stroke-dasharray="4,3"'
    if e['start'] == 'dia': attrs += f' marker-start="url(#cl-dia-{i})"'
    if e['end'] == 'arrow': attrs += f' marker-end="url(#cl-arr-{i})"'
    if e['end'] == 'tri': attrs += f' marker-end="url(#cl-tri-{i})"'
    out.append(f'<path d="{d}" {attrs}/>')

def mult(p, q, text, d, color):
    if not text: return
    ux, uy = unit(p, q)
    if abs(ux) > abs(uy):
        x = p[0] + ux * d; y = p[1] - 6
        anch = 'start' if ux > 0 else 'end'
    else:
        x = p[0] + 8; y = p[1] + uy * d + (3 if uy > 0 else 0); anch = 'start'
    out.append(f'<text x="{x:.0f}" y="{y:.0f}" text-anchor="{anch}" class="m" fill="{color}">{esc(text)}</text>')

labels = []
for e in edges:
    pts = e['pts']
    mult(pts[0], pts[1], e['m1'], 24 if e['start'] == 'dia' else 10, e['color'])
    mult(pts[-1], pts[-2], e['m2'], 14, e['color'])
    if e['role']:
        segs = list(range(len(pts) - 1))
        i = e['role_seg'] if e['role_seg'] is not None else max(
            segs, key=lambda s: math.hypot(pts[s + 1][0] - pts[s][0], pts[s + 1][1] - pts[s][1]))
        a, b = pts[i], pts[i + 1]
        mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
        tw = len(e['role']) * 7.4 + 8
        if abs(b[0] - a[0]) >= abs(b[1] - a[1]):
            labels.append(f'<rect x="{mx - tw/2:.0f}" y="{my + 3:.0f}" width="{tw:.0f}" height="15" fill="#faf9f5"/>'
                          f'<text x="{mx:.0f}" y="{my + 15:.0f}" text-anchor="middle" class="r" fill="{e["color"]}">{esc(e["role"])}</text>')
        else:
            labels.append(f'<g transform="rotate(-90 {mx:.0f} {my:.0f})">'
                          f'<rect x="{mx - tw/2:.0f}" y="{my - 18:.0f}" width="{tw:.0f}" height="15" fill="#faf9f5"/>'
                          f'<text x="{mx:.0f}" y="{my - 6:.0f}" text-anchor="middle" class="r" fill="{e["color"]}">{esc(e["role"])}</text></g>')
out += labels

for n, c in C.items():
    x, y, w, hh = c['x'], c['y'], c['w'], c['h']
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{hh}" rx="6" fill="#faf9f5" stroke="#1a1a1a" stroke-width="1"/>')
    if c['stereo']:
        out.append(f'<text x="{x + w/2}" y="{y + 13}" text-anchor="middle" class="st">«{c["stereo"]}»</text>')
        out.append(f'<text x="{x + w/2}" y="{y + 28}" text-anchor="middle" class="nm">{esc(n)}</text>')
    else:
        out.append(f'<text x="{x + w/2}" y="{y + 22}" text-anchor="middle" class="nm">{esc(n)}</text>')
    if c['attrs'] or c['ops']:
        out.append(f'<line x1="{x}" y1="{y+32}" x2="{x+w}" y2="{y+32}" stroke="#1a1a1a"/>')
    yy = y + 32 + 17
    for t in c['attrs']:
        out.append(f'<text x="{x+12}" y="{yy}" class="a">{esc(t)}</text>'); yy += LH
    if c['attrs'] and c['ops']:
        sy = y + 32 + c['ah']
        out.append(f'<line x1="{x}" y1="{sy}" x2="{x+w}" y2="{sy}" stroke="#1a1a1a"/>')
        yy = sy + 17
    elif c['ops']:
        yy = y + 32 + 17
    for t in c['ops']:
        out.append(f'<text x="{x+12}" y="{yy}" class="a">{esc(t)}</text>'); yy += LH
out += extra
for nombre, texto in chips:
    c = C[nombre]
    wch = len(texto) * 6.8 + 18
    out.append(f'<rect x="{c["x"] + 10}" y="{c["y"] - 28}" width="{wch:.0f}" height="20" rx="10" fill="#fbe9e2" stroke="#d9532c" stroke-width="1.3"/>')
    out.append(f'<text x="{c["x"] + 10 + wch/2:.0f}" y="{c["y"] - 14}" text-anchor="middle" class="a" style="font-weight:600">{esc(texto)}</text>')

maxx = max(c['x'] + c['w'] for c in C.values()) + 70
BM = max(c['y'] + c['h'] for c in C.values())
if hoja in ('2', 'U'):
    BM += 52
leg_y = BM + 50
W, H = int(maxx), int(leg_y + 30 + len(notas_hoja) * 18 + 6)
legend = f'''<g transform="translate(40,{leg_y})" class="lg">
<path d="M0,0 L8,-6 L16,0 L8,6 Z" fill="#1a1a1a"/><line x1="16" y1="0" x2="44" y2="0" stroke="#1a1a1a"/><text x="54" y="3">COMPOSICIÓN</text>
<line x1="190" y1="0" x2="218" y2="0" stroke="#6b6b6b"/><path d="M212,-4 L218,0 L212,4" fill="none" stroke="#6b6b6b"/><text x="228" y="3">ASOCIACIÓN</text>
<line x1="350" y1="0" x2="378" y2="0" stroke="#6b6b6b" stroke-dasharray="4,3"/><path d="M372,-4 L378,0 L372,4" fill="none" stroke="#6b6b6b"/><text x="388" y="3">DEPENDENCIA</text>
<path d="M520,0 L532,-6 L532,6 Z" fill="#faf9f5" stroke="#1a1a1a"/><line x1="510" y1="0" x2="520" y2="0" stroke="#1a1a1a"/><text x="542" y="3">HERENCIA</text>
<text x="640" y="3" style="fill:#6b6b6b">CADA FLECHA TIENE SU PROPIO COLOR</text>
</g>'''
MARC = ''.join(
    f'<marker id="cl-dia-{e["i"]}" viewBox="0 0 16 12" refX="0" refY="6" markerWidth="16" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M0,6 L8,0 L16,6 L8,12 Z" fill="{e["color"]}" stroke="{e["color"]}"/></marker>'
    f'<marker id="cl-arr-{e["i"]}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M1,1 L9,5 L1,9" fill="none" stroke="{e["color"]}" stroke-width="1.5"/></marker>'
    f'<marker id="cl-tri-{e["i"]}" viewBox="0 0 14 14" refX="13" refY="7" markerWidth="14" markerHeight="14" markerUnits="userSpaceOnUse" orient="auto"><path d="M1,1 L13,7 L1,13 Z" fill="#faf9f5" stroke="{e["color"]}" stroke-width="1.4"/></marker>'
    for e in edges)
NOTAS = ''.join(f'<text x="40" y="{leg_y + 28 + i * 18}" class="a">{esc(n)}</text>' for i, n in enumerate(notas_hoja))
svg = f'''<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="cl-title cl-desc" xmlns="http://www.w3.org/2000/svg">
<title id="cl-title">{esc(titulo)}</title>
<desc id="cl-desc">{esc(desc)}</desc>
<defs>{MARC}</defs>
<style>
.a{{font:400 11px 'Geist Mono',monospace;fill:#1a1a1a}}
.nm{{font:600 14px Geist,sans-serif;fill:#1a1a1a}}
.st{{font:400 10px 'Geist Mono',monospace;fill:#6b6b6b}}
.m{{font:600 10px 'Geist Mono',monospace}}
.r{{font:600 11px 'Geist Mono',monospace;letter-spacing:.04em}}
.lg text{{font:400 9px 'Geist Mono',monospace;fill:#6b6b6b}}
</style>
{chr(10).join(out)}
{legend}
{NOTAS}
</svg>'''
page = f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(titulo)}</title>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;600&family=Geist+Mono:wght@400&display=swap" rel="stylesheet">
<style>
html,body{{margin:0;background:#faf9f5}}
svg{{display:block;width:{W}px;height:{H}px}}
</style></head><body>{svg}</body></html>'''
open(sys.argv[2], 'w', encoding='utf-8').write(page)
print('ok hoja', hoja, W, 'x', H, 'proporcion', round(W / H, 2), 'aristas', len(edges))
