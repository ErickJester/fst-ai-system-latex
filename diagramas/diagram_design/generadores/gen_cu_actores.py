import html, math, os, sys

# Casos de uso por actor (cap. 5, "Diseño de casos de uso"): un diagrama por actor, con las relaciones
# <<include>> y <<extend>> y el límite del sistema. Uso:
#   python gen_cu_actores.py CARPETA_SALIDA
# Escribe un .html por diagrama (SVG en línea); los PNG se sacan con el navegador (ver LEEME del cap. 5).
esc = html.escape
OW, OH = 224, 60          # óvalo
FONT = 13

# nodo: id -> (texto, col, fila). col y fila son coordenadas de cuadrícula (admiten decimales).
# arista: (origen, destino, tipo) con tipo: 'a' asociación, 'ext' <<extend>>, 'inc' <<include>>, 'gen' generalización
DIAGRAMAS = {}

DIAGRAMAS['cu_actor_general'] = dict(
    titulo='Plataforma Web FST — visión general por actor',
    ancho=900, alto=720, caja=(230, 20, 670, 690),
    actores=[('V', 'Usuario sin sesión', 70, 140, ''), ('I', 'Investigador', 70, 330, ''),
             ('A', 'Administrador', 70, 540, ''), ('W', 'Worker', 840, 430, 'system')],
    grupos=[('g1', 'Recuperar contraseña\n(CU-01)', 480, 100),
            ('g2', 'Sesión y cuenta propia\n(CU-02, 03, 04 y 05)', 480, 180),
            ('g3', 'Experimentos y carga de video\n(CU-06, 07, 08, 09, 10 y 11)', 480, 260),
            ('g4', 'Seguimiento del análisis\n(CU-12, 13 y pausa)', 480, 340),
            ('g5', 'Resultados, revisión y reportes\n(CU-14, 15, 16, 17 y 18)', 480, 420),
            ('g6', 'Administración de cuentas\n(CU-20, 21 y 22)', 480, 500),
            ('g7', 'Estado del sistema y experimentos\nglobales (CU-23 y 24)', 480, 580),
            ('g8', 'Procesos automáticos\n(pipeline y CU-25)', 480, 650)],
    ngrupo=(280, 56),
    aristas=[('V', 'g1', 'a'), ('I', 'g2', 'a'), ('I', 'g3', 'a'), ('I', 'g4', 'a'), ('I', 'g5', 'a'),
             ('A', 'g6', 'a'), ('A', 'g7', 'a'), ('W', 'g8', 'a'), ('W', 'g4', 'a'), ('A', 'I', 'gen')],
)

DIAGRAMAS['cu_actor_visitante'] = dict(
    titulo='Usuario sin sesión',
    ancho=640, alto=250, caja=(200, 20, 410, 210),
    actores=[('V', 'Usuario\nsin sesión', 80, 120, '')],
    nodos={'CU03': ('CU-01\nRecuperar contraseña', 420, 100)},
    aristas=[('V', 'CU03', 'a')],
    nota=(215, 190, 'Al iniciar sesión (CU-02) pasa a ser Investigador o Administrador.'),
)

DIAGRAMAS['cu_actor_investigador_1'] = dict(
    titulo='Investigador — sesión y cuenta propia',
    ancho=820, alto=460, caja=(190, 20, 600, 420),
    actores=[('I', 'Investigador', 70, 230, '')],
    nodos={'CU01': ('CU-02\nIniciar sesión', 360, 90),
           'CU16': ('CU-04\nCambiar contraseña\nal primer acceso', 650, 90),
           'CU02': ('CU-03\nCerrar sesión', 360, 230),
           'CU18': ('CU-05\nActualizar perfil propio', 360, 370)},
    aristas=[('I', 'CU01', 'a'), ('I', 'CU02', 'a'), ('I', 'CU18', 'a'), ('CU16', 'CU01', 'ext')],
    nota=(205, 410, 'El Administrador hereda estos casos de uso.'),
)

DIAGRAMAS['cu_actor_investigador_2'] = dict(
    titulo='Investigador — experimentos y carga de video',
    ancho=820, alto=790, caja=(190, 20, 600, 750),
    actores=[('I', 'Investigador', 70, 380, '')],
    nodos={'CU04': ('CU-06\nRegistrar experimento', 350, 80),
           'CU05': ('CU-07\nSubir video', 350, 200),
           'CU19': ('CU-08\nEncolar análisis\nautomático', 650, 160),
           'CU20': ('CU-09\nNotificar rechazo\nde video', 650, 250),
           'CU22': ('CU-10\nConsultar lista de\nexperimentos', 350, 400),
           'FIL': ('Filtrar experimentos', 650, 360),
           'AVI': ('Avisar expiración\nde video', 650, 450),
           'CU23': ('CU-11\nEliminar experimento', 350, 620),
           'CON': ('Confirmar eliminación', 650, 620)},
    aristas=[('I', 'CU04', 'a'), ('I', 'CU05', 'a'), ('I', 'CU22', 'a'), ('I', 'CU23', 'a'),
             ('CU19', 'CU05', 'ext'), ('CU20', 'CU05', 'ext'), ('FIL', 'CU22', 'ext'),
             ('AVI', 'CU22', 'ext'), ('CU23', 'CON', 'inc')],
)

DIAGRAMAS['cu_actor_investigador_3'] = dict(
    titulo='Investigador — seguimiento del análisis',
    ancho=900, alto=640, caja=(190, 20, 600, 600),
    actores=[('I', 'Investigador', 70, 300, ''), ('W', 'Worker', 840, 110, 'system')],
    nodos={'CU07': ('CU-12\nMonitorear progreso\ndel análisis', 350, 110),
           'CU08': ('CU-13\nDescargar reporte\nde diagnóstico', 640, 210),
           'P37': ('Pausar el análisis', 640, 360),
           'P38': ('Ajustar el recuadro\ndel cilindro y continuar', 350, 380),
           'P39': ('Cancelar el análisis\nen pausa', 350, 500)},
    aristas=[('I', 'CU07', 'a'), ('I', 'CU08', 'a'), ('I', 'P38', 'a'), ('I', 'P39', 'a'),
             ('W', 'CU07', 'a'), ('W', 'P37', 'a'), ('CU08', 'CU07', 'ext'),
             ('P38', 'P37', 'ext'), ('P39', 'P37', 'ext')],
)

DIAGRAMAS['cu_actor_investigador_4'] = dict(
    titulo='Investigador — resultados, revisión y reportes',
    ancho=820, alto=760, caja=(190, 20, 600, 720),
    actores=[('I', 'Investigador', 70, 360, '')],
    nodos={'CU09': ('CU-14\nConsultar resultados\ndel análisis', 350, 80),
           'CU27': ('CU-16\nConsultar estadísticas\nde grupo o tanda', 650, 70),
           'CU10': ('CU-15\nDescargar reporte\n(PDF, CSV o XLSX)', 350, 230),
           'GEN': ('Generar archivo\nde reporte', 650, 230),
           'CU25': ('CU-17\nRevisar segundo\na segundo', 350, 430),
           'CU26': ('CU-18\nCorregir etiqueta\nde un segundo', 650, 400),
           'REI': ('Reiniciar el análisis', 650, 520)},
    aristas=[('I', 'CU09', 'a'), ('I', 'CU10', 'a'), ('I', 'CU25', 'a'),
             ('CU27', 'CU09', 'ext'), ('CU10', 'GEN', 'inc'), ('CU26', 'CU25', 'ext'),
             ('REI', 'CU25', 'ext')],
    nota=(205, 690, 'Reiniciar: solo el creador del experimento o un Administrador.'),
)

DIAGRAMAS['cu_actor_administrador_1'] = dict(
    titulo='Administrador — gestión de cuentas de usuario',
    ancho=960, alto=840, caja=(190, 20, 760, 800), ow=190,
    actores=[('I', 'Investigador', 70, 120, ''), ('A', 'Administrador', 70, 470, '')],
    nodos={'CU11': ('CU-20\nGestionar cuenta\nde usuario', 320, 430),
           'LIS': ('Listar usuarios', 320, 90),
           'CU12': ('CU-21\nCrear cuenta\nde usuario', 580, 150),
           'EDI': ('Editar datos\nde la cuenta', 580, 260),
           'ROL': ('Dar o quitar el rol\nde Administrador', 580, 370),
           'CU17': ('CU-22\nDesactivar cuenta\nde usuario', 580, 480),
           'REA': ('Reactivar cuenta', 580, 590),
           'TMP': ('Generar contraseña\ntemporal nueva', 580, 700),
           'SEL': ('Seleccionar cuenta\nde la lista', 810, 480)},
    aristas=[('A', 'CU11', 'a'), ('A', 'I', 'gen'), ('CU11', 'LIS', 'inc'),
             ('CU12', 'CU11', 'ext'), ('EDI', 'CU11', 'ext'), ('ROL', 'CU11', 'ext'),
             ('CU17', 'CU11', 'ext'), ('REA', 'CU11', 'ext'), ('TMP', 'CU11', 'ext'),
             ('EDI', 'SEL', 'inc'), ('ROL', 'SEL', 'inc'), ('CU17', 'SEL', 'inc'),
             ('REA', 'SEL', 'inc'), ('TMP', 'SEL', 'inc')],
    nota=(205, 780, 'El Administrador hereda todos los casos de uso del Investigador.'),
)

DIAGRAMAS['cu_actor_administrador_2'] = dict(
    titulo='Administrador — estado del sistema y experimentos globales',
    ancho=820, alto=420, caja=(190, 20, 600, 380),
    actores=[('A', 'Administrador', 70, 190, '')],
    nodos={'CU13': ('CU-23\nMonitorear estado\ndel sistema', 350, 100),
           'DIS': ('Notificar uso de disco', 650, 100),
           'CU24': ('CU-24\nGestionar experimentos\nglobales', 350, 280)},
    aristas=[('A', 'CU13', 'a'), ('A', 'CU24', 'a'), ('DIS', 'CU13', 'ext')],
    nota=(205, 350, 'Antes de cada acción de administración el sistema aplica CU-19 (verificar el rol).'),
)

DIAGRAMAS['cu_actor_worker'] = dict(
    titulo='Worker (actor del sistema) — procesos automáticos',
    ancho=860, alto=660, caja=(190, 20, 600, 620),
    actores=[('W', 'Worker', 70, 340, 'system')],
    nodos={'U30': ('Ejecutar pipeline\nde análisis', 340, 160),
           'U36': ('Reportar error\ndel pipeline', 640, 110),
           'U37': ('Pausar el análisis', 640, 220),
           'CU07': ('CU-12\nMonitorear progreso\ndel análisis', 340, 350),
           'CU08': ('CU-13\nDescargar reporte\nde diagnóstico', 640, 350),
           'CU14': ('CU-25\nBorrar video\nautomáticamente', 340, 520)},
    aristas=[('W', 'U30', 'a'), ('W', 'CU07', 'a'), ('W', 'CU14', 'a'),
             ('U36', 'U30', 'ext'), ('U37', 'U30', 'ext'), ('CU08', 'CU07', 'ext')],
)

CSS = ("text{font-family:Arial,Helvetica,sans-serif;fill:#1a1a1a}"
       ".t{font-size:%dpx}.s{font-size:11px;fill:#555}.h{font-size:17px;font-weight:700}"
       ".st{font-size:11px;font-style:italic;fill:#444}" % FONT)


def elipse_punto(cx, cy, rx, ry, tx, ty):
    """Punto del borde de la elipse (cx,cy,rx,ry) en la dirección hacia (tx,ty)."""
    dx, dy = tx - cx, ty - cy
    n = math.hypot(dx / rx, dy / ry) or 1
    return cx + dx / n, cy + dy / n


def construir(nombre, d):
    W, H = d['ancho'], d['alto']
    o = []
    bx, by, bw, bh = d['caja']
    o.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="10" fill="#faf9f5" stroke="#1a1a1a" stroke-width="1.6"/>')
    o.append(f'<text x="{bx+16}" y="{by+22}" class="h">{esc(d["titulo"])}</text>')
    pos = {}   # id -> (cx, cy, rx, ry)
    ow = d.get('ow', OW)
    for k, (t, x, y) in d.get('nodos', {}).items():
        pos[k] = (x, y, ow / 2, OH / 2, t)
    for k, (t, x, y) in [(g[0], (g[1], g[2], g[3])) for g in d.get('grupos', [])]:
        gw, gh = d['ngrupo']
        pos[k] = (x, y, gw / 2, gh / 2, t)
    actores = {}
    for k, nom, x, y, tipo in d['actores']:
        actores[k] = (x, y, nom, tipo)
        pos[k] = (x, y - 8, 26, 34, nom)

    defs = ('<defs>'
            '<marker id="ab" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">'
            '<path d="M1 1 L9 5 L1 9" fill="none" stroke="#1a1a1a" stroke-width="1.4"/></marker>'
            '<marker id="gn" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="12" markerHeight="12" orient="auto">'
            '<path d="M1 1 L11 6 L1 11 Z" fill="#fff" stroke="#1a1a1a" stroke-width="1.3"/></marker></defs>')

    # aristas
    lbl = []
    for a, b, tipo in d['aristas']:
        ax, ay, arx, ary, _ = pos[a]
        bx2, by2, brx, bry, _ = pos[b]
        p1 = elipse_punto(ax, ay, arx, ary, bx2, by2) if a not in actores else (ax + (26 if bx2 > ax else -26), ay)
        p2 = elipse_punto(bx2, by2, brx, bry, ax, ay) if b not in actores else (bx2 + (26 if ax > bx2 else -26), by2)
        if a in actores and b in actores:   # generalización vertical entre actores
            p1 = (ax, ay - 36 if by2 < ay else ay + 36)
            nl = actores[b][2].count(chr(10))
            # la punta de la flecha queda debajo del nombre del actor padre, no encima
            p2 = (bx2, by2 + 66 + 15 * nl if by2 < ay else by2 - 40)
        if tipo == 'a':
            o.append(f'<line x1="{p1[0]:.1f}" y1="{p1[1]:.1f}" x2="{p2[0]:.1f}" y2="{p2[1]:.1f}" stroke="#1a1a1a" stroke-width="1.3"/>')
        elif tipo == 'gen':
            o.append(f'<line x1="{p1[0]:.1f}" y1="{p1[1]:.1f}" x2="{p2[0]:.1f}" y2="{p2[1]:.1f}" stroke="#1a1a1a" stroke-width="1.3" marker-end="url(#gn)"/>')
        else:
            o.append(f'<line x1="{p1[0]:.1f}" y1="{p1[1]:.1f}" x2="{p2[0]:.1f}" y2="{p2[1]:.1f}" stroke="#1a1a1a" stroke-width="1.2" stroke-dasharray="6,4" marker-end="url(#ab)"/>')
            mx, my = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
            txt = '«extend»' if tipo == 'ext' else '«include»'
            w = len(txt) * 6.4 + 8
            lbl.append(f'<rect x="{mx-w/2:.1f}" y="{my-9:.1f}" width="{w:.1f}" height="15" fill="#faf9f5"/>'
                       f'<text x="{mx:.1f}" y="{my+3:.1f}" text-anchor="middle" class="st">{txt}</text>')

    # nodos
    for k, (cx, cy, rx, ry, t) in pos.items():
        if k in actores:
            continue
        if k in dict((g[0], 1) for g in d.get('grupos', [])):
            o.append(f'<rect x="{cx-rx}" y="{cy-ry}" width="{2*rx}" height="{2*ry}" rx="12" fill="#f1eee5" stroke="#1a1a1a" stroke-width="1.3"/>')
        else:
            o.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#ffffff" stroke="#1a1a1a" stroke-width="1.4"/>')
        lineas = t.split('\n')
        y0 = cy - (len(lineas) - 1) * 8 + 4
        for i, l in enumerate(lineas):
            o.append(f'<text x="{cx}" y="{y0 + i*16}" text-anchor="middle" class="t">{esc(l)}</text>')
    # actores (monigote)
    for k, (x, y, nom, tipo) in actores.items():
        fill = '#fff6c9' if tipo == 'system' else '#ffffff'
        o.append(f'<circle cx="{x}" cy="{y-30}" r="10" fill="{fill}" stroke="#1a1a1a" stroke-width="1.4"/>')
        o.append(f'<line x1="{x}" y1="{y-20}" x2="{x}" y2="{y+10}" stroke="#1a1a1a" stroke-width="1.4"/>')
        o.append(f'<line x1="{x-16}" y1="{y-10}" x2="{x+16}" y2="{y-10}" stroke="#1a1a1a" stroke-width="1.4"/>')
        o.append(f'<line x1="{x}" y1="{y+10}" x2="{x-13}" y2="{y+32}" stroke="#1a1a1a" stroke-width="1.4"/>')
        o.append(f'<line x1="{x}" y1="{y+10}" x2="{x+13}" y2="{y+32}" stroke="#1a1a1a" stroke-width="1.4"/>')
        ls = nom.split('\n')
        for i, l in enumerate(ls):
            o.append(f'<text x="{x}" y="{y+52+i*15}" text-anchor="middle" class="t" style="font-weight:700">{esc(l)}</text>')
        if tipo == 'system':
            o.append(f'<text x="{x}" y="{y+52+len(ls)*15}" text-anchor="middle" class="st">«system»</text>')
    o.extend(lbl)
    if d.get('nota'):
        nx, ny, nt = d['nota']
        o.append(f'<text x="{nx}" y="{ny}" class="s">{esc(nt)}</text>')
    svg = (f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" '
           f'aria-label="{esc(d["titulo"])}">{defs}<style>{CSS}</style>' + ''.join(o) + '</svg>')
    page = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><title>' + esc(d['titulo']) +
            '</title><style>html,body{margin:0;background:#fff}svg{display:block}</style></head><body>' + svg + '</body></html>')
    return page, W, H


if __name__ == '__main__':
    out_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
    os.makedirs(out_dir, exist_ok=True)
    for nombre, d in DIAGRAMAS.items():
        page, W, H = construir(nombre, d)
        open(os.path.join(out_dir, nombre + '.html'), 'w', encoding='utf-8').write(page)
        print(nombre, W, H)
