"""Seis diagramas «antes y después» (TT1 / TT2) rehechos para ocupar una diapositiva completa cada uno:
modelo de datos, arquitectura y pipeline. Uso: gen_diapo_antes_despues.py CARPETA"""
import html, math, os, sys
esc = html.escape
INK, PAPEL, CREMA, ROJO, ROJO_F = '#1a1a1a', '#faf9f5', '#ece7d8', '#d9532c', '#fde8e1'
FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;600&family=Geist+Mono:wght@400;600&display=swap" rel="stylesheet">')


def pagina(nombre, W, H, css, cuerpo):
    svg = (f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg"><title>{esc(nombre)}</title>'
           f'<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1,1 L9,5 L1,9" fill="none" stroke="{INK}" stroke-width="1.6"/></marker></defs>'
           f'<style>{css}</style><rect width="{W}" height="{H}" fill="{PAPEL}"/>' + '\n'.join(cuerpo) + '</svg>')
    return (f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{esc(nombre)}</title>{FONTS}'
            f'<style>html,body{{margin:0;background:{PAPEL}}}svg{{display:block}}</style></head><body>{svg}</body></html>')


# ------------------------------------------------------------------ modelo de datos
TT2 = {
    'USUARIO': ([('PK', 'idInstitucional', ''), ('', 'nombre', ''), ('', 'apellidos', ''), ('', 'correo', ''), ('', 'contrasenaHash', ''),
                 ('', 'activo', ''), ('', 'cambioRequerido', '')], False),
    'ADMINISTRADOR': ([('PK FK', 'idInstitucional', '')], False),
    'NOTIFICACION': ([('PK', 'idNotificacion', ''), ('FK', 'idInstitucional', ''), ('FK', 'idExperimento', 'nulo'), ('', 'tipo', ''),
                      ('', 'mensaje', ''), ('', 'leido', ''), ('', 'fechaCreacion', '')], True),
    'REPORTE': ([('PK', 'idReporte', ''), ('FK', 'idExperimento', ''), ('', 'formato', ''), ('', 'ruta', ''), ('', 'fechaGeneracion', '')], True),
    'EXPERIMENTO': ([('PK', 'idExperimento', ''), ('FK', 'idInstitucional', ''), ('', 'nombre', ''), ('', 'fecha', ''), ('', 'notas', 'nulo')], False),
    'GRUPO': ([('PK', 'idGrupo', ''), ('FK', 'idExperimento', ''), ('', 'etiqueta', ''), ('', 'tipo', ''), ('', 'tratamiento', '')], False),
    'TANDA': ([('PK', 'idTanda', ''), ('FK', 'idGrupo', ''), ('', 'ordinal', ''), ('', 'nCilindros', '')], False),
    'ESPECIMEN': ([('PK', 'idEspecimen', ''), ('FK', 'idTanda', ''), ('', 'numeroCilindro', '')], False),
    'OBSERVACION': ([('PK', 'idObservacion', ''), ('FK', 'idEspecimen', ''), ('FK', 'idVideo', '')], False),
    'VIDEO': ([('PK', 'idVideo', ''), ('FK', 'idTanda', ''), ('', 'sesion', ''), ('', 'archivo', 'nulo'), ('', 'nombreOriginal', 'nulo'),
               ('', 'duracion', ''), ('', 'fechaCarga', '')], False),
    'ANALISIS': ([('PK', 'idAnalisis', ''), ('FK', 'idVideo', ''), ('', 'estado', ''), ('', 'etapa', ''), ('', 'nivelClasif', ''),
                  ('', 'fechaAnalisis', ''), ('', 'rutaDiagnostico', 'nulo')], False),
    'SEGUNDO': ([('PK FK', 'idObservacion', ''), ('PK', 'segundo', ''), ('', 'conducta', 'nulo'), ('', 'origen', '')], False),
}
TT2_COLS = [['USUARIO', 'ADMINISTRADOR', 'NOTIFICACION', 'REPORTE'], ['EXPERIMENTO', 'GRUPO', 'TANDA', 'ESPECIMEN'],
            ['OBSERVACION', 'VIDEO', 'ANALISIS'], ['SEGUNDO']]
TT2_FK = [('EXPERIMENTO', 'idInstitucional', 'USUARIO', 'idInstitucional'), ('NOTIFICACION', 'idInstitucional', 'USUARIO', 'idInstitucional'),
          ('ADMINISTRADOR', 'idInstitucional', 'USUARIO', 'idInstitucional'), ('REPORTE', 'idExperimento', 'EXPERIMENTO', 'idExperimento'),
          ('NOTIFICACION', 'idExperimento', 'EXPERIMENTO', 'idExperimento'), ('GRUPO', 'idExperimento', 'EXPERIMENTO', 'idExperimento'),
          ('TANDA', 'idGrupo', 'GRUPO', 'idGrupo'), ('ESPECIMEN', 'idTanda', 'TANDA', 'idTanda'),
          ('OBSERVACION', 'idEspecimen', 'ESPECIMEN', 'idEspecimen'), ('OBSERVACION', 'idVideo', 'VIDEO', 'idVideo'),
          ('VIDEO', 'idTanda', 'TANDA', 'idTanda'), ('ANALISIS', 'idVideo', 'VIDEO', 'idVideo'),
          ('SEGUNDO', 'idObservacion', 'OBSERVACION', 'idObservacion')]

TT1 = {
    'USUARIOS': ([('PK', 'id', ''), ('', 'correo', ''), ('', 'contrasena_hash', ''), ('', 'nombre', ''), ('', 'rol', ''), ('', 'activo', ''),
                  ('', 'debe_cambiar_contrasena', ''), ('', 'creado_en', ''), ('', 'ultimo_acceso', '')], False),
    'NOTIFICACIONES': ([('PK', 'id', ''), ('FK', 'id_usuario', ''), ('FK', 'id_experimento', ''), ('', 'creado_en', ''), ('', 'tipo', ''),
                        ('', 'mensaje', ''), ('', 'leido', '')], True),
    'SUJETOS': ([('PK', 'id', ''), ('FK', 'id_experimento', ''), ('', 'indice_rata', ''), ('', 'etiqueta', '')], False),
    'ROIS': ([('PK', 'id', ''), ('FK', 'id_video', ''), ('FK', 'id_sujeto', ''), ('', 'x', ''), ('', 'y', ''), ('', 'w', ''), ('', 'h', '')], False),
    'EXPERIMENTOS': ([('PK', 'id', ''), ('FK', 'id_usuario', ''), ('', 'creado_en', ''), ('', 'nombre', ''), ('', 'fecha_experimento', ''),
                      ('', 'tratamiento', ''), ('', 'especie', ''), ('', 'disposicion', ''), ('', 'notas', '')], False),
    'VIDEOS': ([('PK', 'id', ''), ('FK', 'id_experimento', ''), ('', 'creado_en', ''), ('', 'dia', ''), ('', 'nombre_archivo', ''), ('', 'ruta', ''),
                ('', 'duracion_s', ''), ('', 'fecha_eliminacion', '')], False),
    'TRABAJOS': ([('PK', 'id', ''), ('FK', 'id_video', ''), ('FK', 'id_config', ''), ('', 'creado_en', ''), ('', 'iniciado_en', ''),
                  ('', 'finalizado_en', ''), ('', 'estado', ''), ('', 'etapa', ''), ('', 'progreso_pct', ''), ('', 'error', '')], False),
    'ANIMALES': ([('PK', 'id', ''), ('FK', 'id_trabajo', ''), ('FK', 'id_sujeto', '')], False),
    'RESULTADOS_COMPORTAMIENTO': ([('PK', 'id', ''), ('FK', 'id_animal', ''), ('', 'nado_s', ''), ('', 'inmovil_s', ''), ('', 'escape_s', ''),
                                   ('', 'total_analizado_s', '')], False),
    'REPORTES': ([('PK', 'id', ''), ('FK', 'id_experimento', ''), ('', 'creado_en', ''), ('', 'formato', ''), ('', 'ruta', '')], True),
    'CONFIGURACIONES_ANALISIS': ([('PK', 'id', ''), ('', 'creado_en', ''), ('', 'nombre_modelo', ''), ('', 'hash_modelo', ''), ('', 'version_pipeline', ''),
                                  ('', 'umbral_confianza', ''), ('', 'segundos_omitir', ''), ('', 'umbral_inmovil', ''), ('', 'umbral_desplazamiento', ''),
                                  ('', 'umbral_std_posicion', ''), ('', 'umbral_aspecto_trepada', '')], False),
    'COMPORTAMIENTO_POR_MINUTO': ([('PK', 'id', ''), ('FK', 'id_animal', ''), ('', 'minuto', ''), ('', 'nado_s', ''), ('', 'inmovil_s', ''),
                                   ('', 'escape_s', '')], False),
}
TT1_COLS = [['USUARIOS', 'NOTIFICACIONES', 'REPORTES'], ['EXPERIMENTOS', 'SUJETOS', 'ROIS'], ['VIDEOS', 'TRABAJOS', 'ANIMALES'],
            ['CONFIGURACIONES_ANALISIS', 'RESULTADOS_COMPORTAMIENTO', 'COMPORTAMIENTO_POR_MINUTO']]
TT1_FK = [('EXPERIMENTOS', 'id_usuario', 'USUARIOS', 'id'), ('NOTIFICACIONES', 'id_usuario', 'USUARIOS', 'id'),
          ('NOTIFICACIONES', 'id_experimento', 'EXPERIMENTOS', 'id'), ('SUJETOS', 'id_experimento', 'EXPERIMENTOS', 'id'),
          ('REPORTES', 'id_experimento', 'EXPERIMENTOS', 'id'), ('VIDEOS', 'id_experimento', 'EXPERIMENTOS', 'id'),
          ('ROIS', 'id_sujeto', 'SUJETOS', 'id'), ('ROIS', 'id_video', 'VIDEOS', 'id'), ('TRABAJOS', 'id_video', 'VIDEOS', 'id'),
          ('TRABAJOS', 'id_config', 'CONFIGURACIONES_ANALISIS', 'id'), ('ANIMALES', 'id_trabajo', 'TRABAJOS', 'id'),
          ('ANIMALES', 'id_sujeto', 'SUJETOS', 'id'), ('RESULTADOS_COMPORTAMIENTO', 'id_animal', 'ANIMALES', 'id'),
          ('COMPORTAMIENTO_POR_MINUTO', 'id_animal', 'ANIMALES', 'id')]

PALETA = ['#1b6fb0', '#2e8b57', '#8e44ad', '#c0392b', '#b8860b', '#16a085', '#d35400', '#e84393', '#34495e', '#6c8e00', '#0097a7', '#a0522d', '#5e35b1', '#7f8c8d']
BADGE = {'PK': '#d9532c', 'PK FK': '#d9532c', 'FK': '#1a1a1a'}


def er(titulo, DATA, COLS, FK, FS, GAPC, coloffs=None):
    CH = FS * 0.6
    LH, HEAD = round(FS * 1.5), round(FS * 2.2)
    NX = round(FS * 3.7)
    GAPV = round(FS * 1.7)
    X0, Y0 = 24, 20
    coloffs = coloffs or [0] * len(COLS)
    T, colx, colw = {}, [], []
    x = X0
    for names in COLS:
        w = 0
        for n in names:
            cols, _ = DATA[n]
            w = max(w, len(n) * FS * 0.78 + 28)
            for m, nm, ty in cols:
                w = max(w, NX + (len(nm) + (len(ty) + 2 if ty else 0)) * CH + 14)
        colx.append(x); colw.append(math.ceil(w)); x += math.ceil(w) + GAPC
    colbot = []
    for ci, names in enumerate(COLS):
        y = Y0 + coloffs[ci]
        for n in names:
            cols, sop = DATA[n]
            h = HEAD + len(cols) * LH + 8
            T[n] = dict(x=colx[ci], y=y, w=colw[ci], h=h, cols=cols, sop=sop, ci=ci, pos=names.index(n))
            y += h + GAPV
        colbot.append(y - GAPV)
    W = colx[-1] + colw[-1] + X0
    ry = lambda n, f: T[n]['y'] + HEAD + [c[1] for c in T[n]['cols']].index(f) * LH + LH // 2 + 2
    nuse = {}
    out = []
    for k, (c, cf, p, pf) in enumerate(FK):
        col = PALETA[k % len(PALETA)]
        tc, tp = T[c], T[p]
        yc, yp = ry(c, cf), ry(p, pf)
        if tc['ci'] == tp['ci'] and abs(tc['pos'] - tp['pos']) == 1:
            cx = tc['x'] + tc['w'] // 2
            if tc['pos'] > tp['pos']:
                pts = [(cx, tc['y']), (cx, tp['y'] + tp['h'])]
            else:
                pts = [(cx, tc['y'] + tc['h']), (cx, tp['y'])]
            out.append(f'<circle cx="{pts[0][0]}" cy="{pts[0][1]}" r="4.5" fill="{col}"/>')
        else:
            if tc['ci'] == tp['ci']:
                gi, sc, sp = tc['ci'], 1, 1
            elif tp['ci'] > tc['ci']:
                gi, sc, sp = tc['ci'], 1, 0
            else:
                gi, sc, sp = tp['ci'], 0, 1
            xs = tc['x'] + (tc['w'] if sc else 0)
            xe = tp['x'] + (tp['w'] if sp else 0)
            gl = colx[gi] + colw[gi]
            idx = nuse.get(gi, 0); nuse[gi] = idx + 1
            chx = gl + 20 + idx * ((GAPC - 40) / 3.0)
            pts = [(xs, yc), (chx, yc), (chx, yp), (xe, yp)]
            out.append(f'<circle cx="{xs}" cy="{yc}" r="4.5" fill="{col}"/>')
        d = 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in pts)
        out.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="2.2"/>')
        (x1, y1), (x2, y2) = pts[-2], pts[-1]
        dx, dy = x2 - x1, y2 - y1
        nrm = math.hypot(dx, dy) or 1
        ux, uy = dx / nrm, dy / nrm
        bx, by = x2 - ux * 13, y2 - uy * 13
        out.append(f'<path d="M{x2:.1f},{y2:.1f} L{bx - uy*6:.1f},{by + ux*6:.1f} L{bx + uy*6:.1f},{by - ux*6:.1f} Z" fill="{col}"/>')
    body = list(out)
    for n, t in T.items():
        x, y, w, h = t['x'], t['y'], t['w'], t['h']
        fill = CREMA if t['sop'] else PAPEL
        body.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="{fill}" stroke="{INK}" stroke-width="1.6"/>')
        body.append(f'<text x="{x + w/2}" y="{y + HEAD - FS*0.55:.0f}" text-anchor="middle" class="nm">{n}</text>')
        body.append(f'<line x1="{x}" y1="{y + HEAD}" x2="{x + w}" y2="{y + HEAD}" stroke="{INK}" stroke-width="1.2"/>')
        for i, (m, nm, ty) in enumerate(t['cols']):
            by = y + HEAD + i * LH + LH * 0.72
            if m:
                body.append(f'<text x="{x + 8}" y="{by:.0f}" class="b" fill="{BADGE[m]}">{m}</text>')
            body.append(f'<text x="{x + NX}" y="{by:.0f}" class="a">{esc(nm)}</text>')
            if ty:
                body.append(f'<text x="{x + w - 10}" y="{by:.0f}" text-anchor="end" class="ty">{ty}</text>')
    H = int(max(colbot) + 30 + 44)
    ly = H - 24
    lx = X0 + 6
    for k, c, v in [('PK', '#d9532c', 'llave primaria'), ('FK', INK, 'llave foránea')]:
        body.append(f'<text x="{lx}" y="{ly}" class="b" fill="{c}">{k}</text><text x="{lx + FS*2.2:.0f}" y="{ly}" class="ty">{v}</text>')
        lx += FS * 2.2 + len(v) * CH + 36
    body.append(f'<text x="{lx}" y="{ly}" class="ty">nulo = puede quedar vacío</text>')
    lx += 25 * CH + 36
    body.append(f'<text x="{lx}" y="{ly}" class="ty">flecha: de la tabla hija a la tabla padre</text>')
    lx += 39 * CH + 36
    body.append(f'<rect x="{lx}" y="{ly - FS*0.8:.0f}" width="{FS*1.7:.0f}" height="{FS*0.9:.0f}" rx="3" fill="{CREMA}" stroke="{INK}"/><text x="{lx + FS*2.2:.0f}" y="{ly}" class="ty">tabla de soporte</text>')
    css = (f".a{{font:400 {FS}px 'Geist Mono',monospace;fill:{INK}}}.ty{{font:400 {FS*0.92:.1f}px 'Geist Mono',monospace;fill:#6b6b6b}}"
           f".b{{font:600 {FS}px 'Geist Mono',monospace}}.nm{{font:600 {FS*1.12:.1f}px Geist,sans-serif;fill:{INK}}}")
    return pagina(titulo, W, H, css, body), W, H


# ------------------------------------------------------------------ arquitectura
CSSA = (f".t{{font:600 38px Geist,Arial,sans-serif;fill:{INK}}}.n{{font:600 30px Geist,Arial,sans-serif;fill:{INK}}}"
        f".s{{font:400 26px 'Geist Mono',monospace;fill:{INK}}}.k{{font:400 19px 'Geist Mono',monospace;fill:#6b6b6b}}"
        f".l{{font:400 21px 'Geist Mono',monospace;fill:#444}}.g{{font:600 28px Geist,Arial,sans-serif;fill:{INK}}}")


def caja(o, x, y, w, h, titulo, lineas, estilo='', etiqueta=None, tam='t'):
    fondo = {'': '#ffffff', 'vol': CREMA, 'clave': ROJO_F, 'ext': '#ffffff'}[estilo]
    borde = ROJO if estilo == 'clave' else INK
    dash = ' stroke-dasharray="9,6"' if estilo == 'ext' else ''
    o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fondo}" stroke="{borde}" stroke-width="2.2"{dash}/>')
    ty = y + 40
    if etiqueta:
        o.append(f'<text x="{x + 18}" y="{y + 28}" class="k">{esc(etiqueta)}</text>')
        ty = y + 66
    o.append(f'<text x="{x + 18}" y="{ty}" class="{tam}">{esc(titulo)}</text>')
    if lineas:
        o.append(f'<line x1="{x}" y1="{ty + 14}" x2="{x + w}" y2="{ty + 14}" stroke="{borde}" stroke-width="1.4"/>')
    for i, l in enumerate(lineas):
        o.append(f'<text x="{x + 18}" y="{ty + 52 + i * 39}" class="s">{esc(l)}</text>')


def flecha(o, pts, etiqueta=None, pos=None, ancla='start'):
    d = 'M' + ' L'.join(f'{x},{y}' for x, y in pts)
    o.append(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="2.2" marker-end="url(#ar)"/>')
    if etiqueta:
        lines = etiqueta if isinstance(etiqueta, list) else [etiqueta]
        x, y = pos
        for i, l in enumerate(lines):
            o.append(f'<text x="{x}" y="{y + i*26}" text-anchor="{ancla}" class="l">{esc(l)}</text>')


def arquitectura(tt2):
    W, H = 1820, 900
    o = []
    CW, GAP = 500, 130
    X = [30, 30 + CW + GAP, 30 + 2 * (CW + GAP)]
    caja(o, X[0], 24, CW, 76, 'Navegador del investigador', [], 'ext', tam='n')
    ry0, ry1 = 190, 455
    if tt2:
        caja(o, X[0], ry0, CW, ry1 - ry0, 'web', ['React.js + Vite · nginx', 'Interfaz del investigador'], '', '«contenedor»')
        caja(o, X[1], ry0, CW, ry1 - ry0, 'api', ['Spring Boot · Java 21', 'API REST con JWT', 'Encola los análisis'], '', '«contenedor»')
        caja(o, X[2], ry0, CW, ry1 - ry0, 'worker', ['Python · PyTorch · OpenCV', 'Pipeline de 3 etapas', 'Red R(2+1)D-18', 'Un video a la vez'], 'clave', '«contenedor»')
    else:
        caja(o, X[0], ry0, CW, ry1 - ry0, 'frontend', ['React.js + Vite', 'Interfaz del investigador'], '', '«contenedor»')
        caja(o, X[1], ry0, CW, ry1 - ry0, 'backend', ['Flask + Gunicorn', 'API REST con JWT', 'Encola los análisis'], '', '«contenedor»')
        caja(o, X[2], ry0, CW, ry1 - ry0, 'worker', ['Python · OpenCV · PyTorch', 'Pipeline de 5 módulos', 'YOLOv8 + ByteTrack', 'ResNet-18 y ResNet-50'], 'clave', '«contenedor»')
    c0, c1, c2 = (x + CW // 2 for x in X)
    flecha(o, [(c0, 100), (c0, ry0)], 'navegador', (c0 + 14, 152))
    flecha(o, [(X[0] + CW, 315), (X[1], 315)], ['API REST', '+ JWT'], ((X[0] + CW + X[1]) / 2, 270), 'middle')
    yb0 = 585
    o.append(f'<rect x="30" y="{yb0}" width="{W-60}" height="290" rx="10" fill="#f3f1ea" stroke="{INK}" stroke-width="2" stroke-dasharray="9,6"/>')
    o.append(f'<text x="50" y="{yb0 + 38}" class="g">Capa de datos</text>')
    by0, by1 = yb0 + 58, yb0 + 270
    if tt2:
        caja(o, X[0] + 20, by0, CW - 40, by1 - by0, 'Volumen', ['Videos y reportes', 'compartido'], 'vol')
        caja(o, X[1] + 20, by0, CW - 40, by1 - by0, 'db', ['PostgreSQL', 'Cuentas, resultados', 'y cola de análisis'], '', '«contenedor»')
        caja(o, X[2] + 20, by0, CW - 40, by1 - by0, 'Modelos', ['Clasificador entrenado', '(solo lectura)'], 'vol')
    else:
        caja(o, X[1] + 20, by0, CW - 40, by1 - by0, 'db', ['PostgreSQL', 'Cuentas, resultados', 'y cola de análisis'], '', '«contenedor»')
        caja(o, X[2] + 20, by0, CW - 40, by1 - by0, 'Archivos', ['Videos originales', 'y reportes'], 'vol')
    flecha(o, [(c1, ry1), (c1, by0)], 'encola y sirve', (c1 + 14, 535))
    flecha(o, [(c2, ry1), (c2, by0)], ['toma la cola', 'y guarda'], (c2 + 14, 520))
    return pagina('Arquitectura del TT2' if tt2 else 'Arquitectura del TT1', W, H, CSSA, o), W, H


# ------------------------------------------------------------------ pipeline
def ajusta(t, n):
    pal, lin, cur = t.split(), [], ''
    for p in pal:
        if cur and len(cur) + len(p) + 1 > n:
            lin.append(cur)
            cur = p
        else:
            cur = (cur + ' ' + p).strip()
    return lin + [cur]


def pipeline(tt2):
    W, H = 1840, 740
    if tt2:
        tars = [('1', 'Preprocesamiento', 'Comprueba que el video abra, corrige su rotación y confirma que el modelo esté disponible', ''),
                ('2', 'Localización de cilindros', 'Modelo de fondo y línea de agua; separa los cilindros y calcula la región de cada uno (de 2 a 4)', ''),
                ('3', 'Clasificación de conducta', '15 rasgos y 7 reglas; clip de 16 cuadros. Red R(2+1)D-18 con 22 medidas: una conducta por segundo', 'clave'),
                ('4', 'Resultados', 'Conducta de cada segundo, tiempos por minuto y copia del video para revisión', '')]
    else:
        tars = [('1', 'Preprocesamiento', 'Lectura de cuadros, ecualización adaptativa (CLAHE) y estabilización de la cámara (ECC + ORB)', ''),
                ('2', 'Detección de regiones', 'Distribución de los cilindros (1×4, 2×2 o 1×3), región de cada cilindro y línea de agua', ''),
                ('3', 'Seguimiento', 'YOLOv8 + ByteTrack: asignación por IoU, validación física y recuperación de estado', 'baja'),
                ('4', 'Clasificación', 'ResNet-18, con ResNet-50 y heurística de respaldo; voto mayoritario por ventana de un segundo', ''),
                ('5', 'Resultados', 'Tiempos por conducta y desglose por minuto, video anotado y datos de seguimiento', '')]
    n = len(tars)
    gap = 70
    cw = (W - 60 - (n - 1) * gap) / n
    y0, h = 40, 660
    TS, BS = (38, 34) if tt2 else (30, 27)
    cpl = int((cw - 40) / (0.6 * BS))
    tw = int((cw - 36) / (0.56 * TS))
    o = []
    for i, (num, t, cuerpo, est) in enumerate(tars):
        x = 30 + i * (cw + gap)
        fondo = ROJO_F if est == 'clave' else ('#f3f1ea' if est == 'baja' else '#fff')
        borde = ROJO if est in ('clave', 'baja') else INK
        dash = ' stroke-dasharray="10,6"' if est == 'baja' else ''
        o.append(f'<rect x="{x:.0f}" y="{y0}" width="{cw:.0f}" height="{h}" rx="12" fill="{fondo}" stroke="{borde}" stroke-width="2.4"{dash}/>')
        o.append(f'<circle cx="{x + 44:.0f}" cy="{y0 + 54}" r="28" fill="{INK}"/><text x="{x + 44:.0f}" y="{y0 + 65}" text-anchor="middle" class="num">{num}</text>')
        tl = ajusta(t, tw)
        ty = y0 + 130
        for k, l in enumerate(tl):
            o.append(f'<text x="{x + 20:.0f}" y="{ty + k * TS * 1.25:.0f}" class="tt">{esc(l)}</text>')
        ty += (len(tl) - 1) * TS * 1.25 + 52
        if est == 'baja':
            o.append(f'<text x="{x + 20:.0f}" y="{ty:.0f}" class="rj">se eliminó en TT2</text>')
            ty += 48
        for k, l in enumerate(ajusta(cuerpo, cpl)):
            o.append(f'<text x="{x + 20:.0f}" y="{ty + k * BS * 1.5:.0f}" class="bd">{esc(l)}</text>')
        if i < n - 1:
            yy = y0 + h / 2
            o.append(f'<path d="M{x + cw + 6:.0f},{yy:.0f} L{x + cw + gap - 6:.0f},{yy:.0f}" stroke="{INK}" stroke-width="2.6" marker-end="url(#ar)"/>')
    css = (f".tt{{font:600 {TS}px Geist,Arial,sans-serif;fill:{INK}}}.num{{font:600 30px Geist,Arial,sans-serif;fill:#fff}}"
           f".bd{{font:400 {BS}px 'Geist Mono',monospace;fill:{INK}}}.rj{{font:400 {BS-3}px 'Geist Mono',monospace;fill:{ROJO}}}")
    return pagina('Pipeline del TT2' if tt2 else 'Pipeline del TT1', W, H, css, o), W, H


if __name__ == '__main__':
    d = sys.argv[1]
    os.makedirs(d, exist_ok=True)
    FS = float(os.environ.get('FS', 18))
    for nombre, f in (('datos_tt1', lambda: er('Modelo de datos TT1', TT1, TT1_COLS, TT1_FK, FS, 120)),
                      ('datos_tt2', lambda: er('Modelo de datos TT2', TT2, TT2_COLS, TT2_FK, FS, 120, [0, 0, 0, 280])),
                      ('arquitectura_tt1', lambda: arquitectura(False)), ('arquitectura_tt2', lambda: arquitectura(True)),
                      ('pipeline_tt1', lambda: pipeline(False)), ('pipeline_tt2', lambda: pipeline(True))):
        s, W, H = f()
        open(os.path.join(d, nombre + '.html'), 'w', encoding='utf-8').write(s)
        print(nombre, W, H)
