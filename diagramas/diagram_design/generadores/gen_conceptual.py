import html, sys

# Diagrama entidad-relacion del sistema con la notacion de Elmasri y Navathe, «Fundamentos de sistemas de
# bases de datos» (D-108): resumen de la figura 3.14, notacion (min,max) de la figura 3.15 y
# especializacion con una sola subclase de la figura 4.1.
#  - La pareja (min,max) va junto a la entidad que participa: cuantas veces participa cada ejemplar.
#  - Atributos en ovalos; clave subrayada; clave parcial con subrayado discontinuo; derivado en ovalo
#    punteado. Las llaves foraneas no se dibujan: son las relaciones.
#  - Entidad debil y relacion identificativa con borde doble. Sin linea doble de participacion total: el
#    minimo 1 de la pareja (min,max) ya la indica (D-109).
#  - Subclase unica: linea sin circulo, con el simbolo de subconjunto abierto hacia la superclase.
#  - Nombres de entidad y de relacion en mayusculas; las relaciones se leen de izquierda a derecha o de
#    arriba abajo.
# Corresponde uno a uno con el grafo relacional vigente: 12 entidades = 12 relaciones; 45 atributos mas
# las 13 llaves foraneas (12 relaciones y la especializacion) = 58 atributos.
#
# Uso: py -I -X utf8 gen_conceptual.py salida.html [salida.tex]
esc = html.escape
W, SYF = 2040, 0.93
ENT_W, ENT_H = 190, 46
REL_W, REL_H = 200, 62


def Y(y):
    return round(y * SYF + 5)


# clave: (x, y, nombre, debil)
ENT = {
    'usuario': (360, 360, 'USUARIO', False), 'admin': (360, 580, 'ADMINISTRADOR', False),
    'notif': (720, 150, 'NOTIFICACIÓN', False), 'experim': (1000, 360, 'EXPERIMENTO', False),
    'reporte': (1575, 360, 'REPORTE', False), 'grupo': (1000, 590, 'GRUPO', False),
    'especimen': (640, 820, 'ESPÉCIMEN', False), 'tanda': (1400, 820, 'TANDA', False),
    'video': (1400, 1050, 'VIDEO', False), 'analisis': (1910, 1050, 'ANÁLISIS', False),
    'observ': (1000, 1280, 'OBSERVACIÓN', False), 'segundo': (1350, 1390, 'SEGUNDO', True),
}
# clave: (x, y, nombre, identificativa, ancho)
REL = {
    'recibe': (360, 150, 'RECIBE', False, REL_W), 'origina': (1000, 150, 'SE_ORIGINA_EN', False, 210),
    'registra': (680, 360, 'REGISTRA', False, REL_W), 'genera': (1290, 360, 'GENERA', False, REL_W),
    'compone': (1000, 475, 'SE_COMPONE_DE', False, 210), 'graba': (1400, 695, 'SE_GRABA_EN', False, REL_W),
    'aloja': (1000, 820, 'SE_ALOJA_EN', False, REL_W), 'produce': (1400, 935, 'PRODUCE', False, REL_W),
    'procesa': (1665, 1050, 'SE_PROCESA_EN', False, 210), 'aparece': (640, 1060, 'APARECE_EN', False, REL_W),
    'contiene': (1400, 1175, 'CONTIENE', False, REL_W), 'etiqueta': (1000, 1390, 'SE_ETIQUETA_EN', True, 224),
}
# entidad: [(texto, x, y, tipo, lado)]
#   tipo: 'a' simple, 'k' clave, 'p' clave parcial, 'd' derivado
#   lado: 'w' (x es el borde derecho del ovalo), 'e' y 'ner' (x es su borde izquierdo), 'n' y 's' (x es su centro)
ATR = {
    'usuario': [('Id institucional', 215, 195, 'k', 'w'), ('Correo', 215, 240, 'k', 'w'),
                ('Nombre', 215, 285, 'a', 'w'), ('Apellidos', 215, 330, 'a', 'w'),
                ('Contraseña cifrada', 215, 375, 'a', 'w'), ('Activo', 215, 420, 'a', 'w'),
                ('Cambio requerido', 215, 465, 'a', 'w')],
    'notif': [('Id', 480, 45, 'k', 'n'), ('Tipo', 556, 45, 'a', 'n'), ('Mensaje', 656, 45, 'a', 'n'),
              ('Leído', 762, 45, 'a', 'n'), ('Fecha de creación', 910, 45, 'a', 'n')],
    'experim': [('Id', 1155, 140, 'k', 'ner'), ('Nombre', 1155, 185, 'k', 'ner'),
                ('Fecha', 1155, 230, 'a', 'ner'), ('Notas', 1155, 275, 'a', 'ner')],
    'reporte': [('Id', 1720, 285, 'k', 'e'), ('Formato', 1720, 335, 'a', 'e'), ('Ruta', 1720, 385, 'k', 'e'),
                ('Fecha de generación', 1720, 435, 'a', 'e')],
    'grupo': [('Id', 855, 530, 'k', 'w'), ('Etiqueta', 855, 575, 'a', 'w'), ('Tipo', 855, 620, 'a', 'w'),
              ('Tratamiento', 855, 665, 'a', 'w')],
    'especimen': [('Id', 495, 795, 'k', 'w'), ('Número de cilindro', 495, 845, 'a', 'w')],
    'tanda': [('Id', 1545, 765, 'k', 'e'), ('Orden', 1545, 815, 'a', 'e'),
              ('Número de\ncilindros', 1545, 875, 'd', 'e')],
    'video': [('Id', 1240, 915, 'k', 'w'), ('Sesión', 1240, 960, 'a', 'w'), ('Archivo', 1240, 1005, 'a', 'w'),
              ('Nombre original', 1240, 1050, 'a', 'w'), ('Duración', 1240, 1095, 'a', 'w'),
              ('Fecha de carga', 1240, 1140, 'a', 'w')],
    'analisis': [('Id', 1795, 965, 'k', 'n'), ('Estado', 1885, 965, 'a', 'n'), ('Etapa', 1985, 965, 'a', 'n'),
                 ('Nivel de\nclasificación', 1765, 1140, 'd', 's'), ('Fecha de análisis', 1932, 1200, 'a', 's'),
                 ('Ruta de diagnóstico', 1785, 1260, 'a', 's')],
    'observ': [('Id', 1000, 1195, 'k', 'n')],
    'segundo': [('Número de segundo', 1500, 1340, 'p', 'e'), ('Conducta', 1500, 1390, 'a', 'e'),
                ('Origen', 1500, 1440, 'a', 'e')],
}
# (entidad, lado, relacion, lado, quiebre, (min,max), linea doble)
EDGES = [
    ('usuario', 'n', 'recibe', 's', None, '(0,N)', False), ('notif', 'w', 'recibe', 'e', None, '(1,1)', False),
    ('notif', 'e', 'origina', 'w', None, '(0,1)', False), ('experim', 'n', 'origina', 's', None, '(0,N)', False),
    ('usuario', 'e', 'registra', 'w', None, '(0,N)', False), ('experim', 'w', 'registra', 'e', None, '(1,1)', False),
    ('experim', 'e', 'genera', 'w', None, '(0,N)', False), ('reporte', 'w', 'genera', 'e', None, '(1,1)', False),
    ('experim', 's', 'compone', 'n', None, '(0,N)', False), ('grupo', 'n', 'compone', 's', None, '(1,1)', False),
    ('grupo', 'e', 'graba', 'n', 'hv', '(1,N)', False), ('tanda', 'n', 'graba', 's', None, '(1,1)', False),
    ('especimen', 'e', 'aloja', 'w', None, '(1,1)', False), ('tanda', 'w', 'aloja', 'e', None, '(2,4)', False),
    ('tanda', 's', 'produce', 'n', None, '(1,2)', False), ('video', 'n', 'produce', 's', None, '(1,1)', False),
    ('video', 'e', 'procesa', 'w', None, '(0,1)', False), ('analisis', 'w', 'procesa', 'e', None, '(1,1)', False),
    ('especimen', 's', 'aparece', 'n', None, '(0,1)', False), ('observ', 'w', 'aparece', 's', 'hv', '(1,1)', False),
    ('video', 's', 'contiene', 'n', None, '(0,4)', False), ('observ', 'e', 'contiene', 's', 'hv', '(1,1)', False),
    ('observ', 's', 'etiqueta', 'n', None, '(1,300)', False), ('segundo', 'w', 'etiqueta', 'e', None, '(1,1)', False),
]


def borde(clave, lado):
    if clave in ENT:
        x, y, w, h = ENT[clave][0], Y(ENT[clave][1]), ENT_W, ENT_H
    else:
        x, y, w, h = REL[clave][0], Y(REL[clave][1]), REL[clave][4], REL_H
    return {'e': (x + w / 2, y), 'w': (x - w / 2, y), 'n': (x, y - h / 2), 's': (x, y + h / 2),
            'ne': (x + 68, y - h / 2)}[lado]


def ovalo(texto, x, y, lado):
    """Centro y semiejes del ovalo (letra monoespaciada de 16 px: 9.6 px por caracter)."""
    partes = texto.split('\n')
    rx = max(len(l) for l in partes) * 4.8 + 14
    ry = 18 if len(partes) == 1 else 27
    cx = x - rx if lado == 'w' else x + rx if lado in ('e', 'ner') else x
    return cx, Y(y), rx, ry


def geometria():
    """Devuelve lineas [(puntos, doble)], ovalos, cardinalidades [(texto, x, y, anclaje)] y el subconjunto."""
    lineas, ovalos, cards = [], [], []
    for ent, atributos in ATR.items():
        for texto, x, y, tipo, lado in atributos:
            cx, cy, rx, ry = ovalo(texto, x, y, lado)
            fin = {'w': (cx + rx, cy), 'e': (cx - rx, cy), 'ner': (cx - rx, cy), 'n': (cx, cy + ry),
                   's': (cx, cy - ry)}[lado]
            lineas.append(([borde(ent, 'ne' if lado == 'ner' else lado), fin], False))
            ovalos.append((texto, cx, cy, rx, ry, tipo))
    for ent, le, rel, lr, quiebre, card, doble in EDGES:
        p, q = borde(ent, le), borde(rel, lr)
        puntos = [p, (q[0], p[1]), q] if quiebre == 'hv' else [p, q]
        lineas.append((puntos, doble))
        dx, dy = puntos[1][0] - p[0], puntos[1][1] - p[1]
        if abs(dx) > abs(dy):
            s = 1 if dx > 0 else -1
            cards.append((card, p[0] + 7 * s, p[1] - 9, 'start' if s > 0 else 'end'))
        else:
            s = 1 if dy > 0 else -1
            cards.append((card, p[0] + 9, p[1] + 15 * s + 5, 'start'))
    # especializacion Usuario-Administrador: una sola subclase
    lineas.append(([borde('usuario', 's'), borde('admin', 'n')], False))
    sub = (ENT['usuario'][0], (borde('usuario', 's')[1] + borde('admin', 'n')[1]) / 2)
    return lineas, ovalos, cards, sub


LEYENDA = [('ent', 'Entidad'), ('debil', 'Entidad débil'), ('rel', 'Relación'),
           ('ident', 'Relación identificativa'), ('a', 'Atributo'), ('k', 'Atributo clave'),
           ('p', 'Clave parcial'), ('d', 'Atributo derivado'), ('sub', 'Subclase'),
           ('card', 'Participación mínima y máxima')]
LEY_X, LEY_Y, LEY_PASO = 50, 945, 49


# ================================================================ SVG
def svg():
    lineas, ovalos, cards, sub = geometria()
    alto = Y(1440) + 40
    out = []

    def poli(pts, extra=''):
        d = 'M' + ' L'.join(f'{x:.0f},{y:.0f}' for x, y in pts)
        out.append(f'<path d="{d}" fill="none" stroke="#1a1a1a" stroke-width="1.4"{extra}/>')

    def texto(x, y, s, cls, anc='middle'):
        out.append(f'<text x="{x:.0f}" y="{y:.0f}" text-anchor="{anc}" class="{cls}">{esc(s)}</text>')

    def rect(x, y, w, h, debil):
        out.append(f'<rect x="{x-w/2:.0f}" y="{y-h/2:.0f}" width="{w}" height="{h}" rx="2" fill="#ece7d8" stroke="#1a1a1a" stroke-width="1.5"/>')
        if debil:
            out.append(f'<rect x="{x-w/2+5:.0f}" y="{y-h/2+5:.0f}" width="{w-10}" height="{h-10}" fill="none" stroke="#1a1a1a" stroke-width="1.2"/>')

    def rombo(x, y, w, h, doble):
        def pol(m, fill):
            out.append(f'<polygon points="{x:.0f},{y-h/2+m:.0f} {x+w/2-m*w/h:.0f},{y:.0f} {x:.0f},{y+h/2-m:.0f} {x-w/2+m*w/h:.0f},{y:.0f}" fill="{fill}" stroke="#1a1a1a" stroke-width="1.4"/>')
        pol(0, '#ece7d8')
        if doble:
            pol(4.5, 'none')

    def elipse(cx, cy, rx, ry, s, tipo):
        dash = ' stroke-dasharray="6,4"' if tipo == 'd' else ''
        out.append(f'<ellipse cx="{cx:.0f}" cy="{cy:.0f}" rx="{rx:.0f}" ry="{ry}" fill="#fff" stroke="#1a1a1a" stroke-width="1.3"{dash}/>')
        partes = s.split('\n')
        for i, l in enumerate(partes):
            texto(cx, cy + 5 - (len(partes) - 1) * 9 + i * 18, l, 'at')
        if tipo in ('k', 'p'):
            medio = len(s) * 4.8
            poli([(cx - medio, cy + 10), (cx + medio, cy + 10)], ' stroke-dasharray="5,3"' if tipo == 'p' else '')

    def subconjunto(x, y):
        out.append(f'<path d="M{x-13:.0f},{y-15:.0f} L{x-13:.0f},{y:.0f} A13,13 0 0 0 {x+13:.0f},{y:.0f} L{x+13:.0f},{y-15:.0f}" fill="none" stroke="#1a1a1a" stroke-width="1.6"/>')

    for pts, doble in lineas:
        if doble:                                   # participacion total
            for d in (-3.5, 3.5):
                poli([(x, y + d) for x, y in pts])
        else:
            poli(pts)
    subconjunto(*sub)
    for s, cx, cy, rx, ry, tipo in ovalos:
        elipse(cx, cy, rx, ry, s, tipo)
    for x, y, nombre, debil in ENT.values():
        rect(x, Y(y), ENT_W, ENT_H, debil)
        texto(x, Y(y) + 7, nombre, 'nm')
    for x, y, nombre, ident, w in REL.values():
        rombo(x, Y(y), w, REL_H, ident)
        texto(x, Y(y) + 5, nombre, 'rl')
    for s, x, y, anc in cards:
        texto(x, y, s, 'm', anc)
    for i, (tipo, rotulo) in enumerate(LEYENDA):
        x, y = LEY_X + 34, Y(LEY_Y + i * LEY_PASO)
        if tipo in ('ent', 'debil'):
            rect(x, y, 66, 28, tipo == 'debil')
        elif tipo in ('rel', 'ident'):
            rombo(x, y, 70, 34, tipo == 'ident')
        elif tipo == 'sub':
            poli([(x, y - 18), (x, y + 18)])
            subconjunto(x, y + 2)
        elif tipo == 'card':
            texto(x, y + 6, '(mín,máx)', 'm')
        else:
            elipse(x, y, 38, 15, 'abc', tipo)
        texto(x + 54, y + 5, rotulo, 'le', 'start')
    cuerpo = f'''<svg viewBox="0 0 {W} {alto}" role="img" aria-labelledby="co-title co-desc" xmlns="http://www.w3.org/2000/svg">
<title id="co-title">Diagrama entidad-relación</title>
<desc id="co-desc">Diagrama entidad-relación con la notación de Elmasri y Navathe: 12 entidades con sus 45 atributos, 12 relaciones con restricciones de participación mínima y máxima, la entidad débil Segundo y la subclase Administrador de Usuario.</desc>
<style>
.nm{{font:600 19px Geist,sans-serif;fill:#111}}
.rl{{font:500 15px 'Geist Mono',monospace;fill:#111}}
.at{{font:400 16px 'Geist Mono',monospace;fill:#111}}
.m{{font:600 16px 'Geist Mono',monospace;fill:#000}}
.le{{font:400 16px 'Geist Mono',monospace;fill:#333}}
</style>
{chr(10).join(out)}
</svg>'''
    return alto, cuerpo


# ================================================================ TikZ
def tikz():
    lineas, ovalos, cards, sub = geometria()
    k = 0.012                                        # cm por px

    def c(x, y):
        return f'({x*k:.3f},{-y*k:.3f})'

    def t(s):
        return s.replace('_', r'\_')

    o = [r'% Generado por diagramas/diagram_design/generadores/gen_conceptual.py (no editar a mano).',
         r'% Notacion de Elmasri y Navathe (D-108). Compilar desde la raiz:',
         r'%     pdflatex -output-directory=build diagramas/esquema_conceptual.tex',
         r'\documentclass[border=8pt]{standalone}',
         r'\usepackage[utf8]{inputenc}', r'\usepackage[T1]{fontenc}', r'\usepackage{lmodern}',
         r'\usepackage[spanish,es-noshorthands]{babel}', r'\usepackage[normalem]{ulem}',
         r'\usepackage{tikz}', r'\usetikzlibrary{shapes.geometric}', r'\begin{document}',
         r'\begin{tikzpicture}[',
         r'  lin/.style  = {draw, semithick},',
         r'  ent/.style  = {draw, semithick, rectangle, fill=white, inner sep=0pt,',
         f'                 minimum width={ENT_W*k:.3f}cm, minimum height={ENT_H*k:.3f}cm,',
         r'                 font=\sffamily\bfseries\fontsize{7.4}{8}\selectfont},',
         r'  rel/.style  = {draw, semithick, diamond, fill=white, inner sep=0pt,',
         r'                 font=\sffamily\fontsize{5.6}{6.2}\selectfont},',
         r'  att/.style  = {draw, semithick, ellipse, fill=white, inner sep=0pt, align=center,',
         r'                 font=\sffamily\fontsize{6.4}{7.4}\selectfont},',
         r'  doble/.style = {double, double distance=1.3pt},',
         r'  card/.style = {inner sep=0pt, font=\ttfamily\fontsize{6.4}{7}\selectfont}',
         r']']

    def ovalo_tex(cx, cy, rx, ry, s, tipo):
        cuerpo = s.replace('\n', r'\\')
        if tipo == 'k':
            cuerpo = r'\uline{%s}' % cuerpo
        if tipo == 'p':
            cuerpo = r'\dashuline{%s}' % cuerpo
        estilo = 'att, dashed' if tipo == 'd' else 'att'
        o.append(r'\node[%s, minimum width=%.3fcm, minimum height=%.3fcm] at %s {%s};'
                 % (estilo, 2 * rx * k, 2 * ry * k, c(cx, cy), cuerpo))

    def rombo_tex(x, y, w, h, nombre, ident):
        o.append(r'\node[rel%s, aspect=%.2f, minimum width=%.3fcm, minimum height=%.3fcm] at %s {%s};'
                 % (', doble' if ident else '', w / h, w * k, h * k, c(x, y), t(nombre)))

    def rect_tex(x, y, nombre, debil, extra=''):
        o.append(r'\node[ent%s%s] at %s {%s};' % (', doble' if debil else '', extra, c(x, y), t(nombre)))

    def sub_tex(x, y):
        o.append(r'\draw[lin] %s -- %s arc[start angle=180, end angle=360, radius=%.3fcm] -- %s;'
                 % (c(x - 13, y - 15), c(x - 13, y), 13 * k, c(x + 13, y - 15)))

    for pts, doble in lineas:
        for d in ((-3.5, 3.5) if doble else (0,)):
            o.append(r'\draw[lin] %s;' % ' -- '.join(c(x, y + d) for x, y in pts))
    sub_tex(*sub)
    for s, cx, cy, rx, ry, tipo in ovalos:
        ovalo_tex(cx, cy, rx, ry, s, tipo)
    for x, y, nombre, debil in ENT.values():
        rect_tex(x, Y(y), nombre, debil)
    for x, y, nombre, ident, w in REL.values():
        rombo_tex(x, Y(y), w, REL_H, nombre, ident)
    for s, x, y, anc in cards:
        o.append(r'\node[card, anchor=%s] at %s {%s};' % ('base west' if anc == 'start' else 'base east', c(x, y), s))
    for i, (tipo, rotulo) in enumerate(LEYENDA):
        x, y = LEY_X + 34, Y(LEY_Y + i * LEY_PASO)
        if tipo in ('ent', 'debil'):
            rect_tex(x, y, '', tipo == 'debil', ', minimum width=%.3fcm, minimum height=%.3fcm' % (66 * k, 28 * k))
        elif tipo in ('rel', 'ident'):
            rombo_tex(x, y, 70, 34, '', tipo == 'ident')
        elif tipo == 'sub':
            o.append(r'\draw[lin] %s -- %s;' % (c(x, y - 18), c(x, y + 18)))
            sub_tex(x, y + 2)
        elif tipo == 'card':
            o.append(r'\node[card] at %s {(mín,máx)};' % c(x, y))
        else:
            ovalo_tex(x, y, 38, 15, 'abc', tipo)
        o.append(r'\node[anchor=west, inner sep=0pt, font=\sffamily\fontsize{6.4}{7}\selectfont] at %s {%s};'
                 % (c(x + 54, y), rotulo))
    o += [r'\end{tikzpicture}', r'\end{document}', '']
    return '\n'.join(o)


if __name__ == '__main__':
    alto, cuerpo = svg()
    pagina = f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Diagrama entidad-relación</title>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;600&family=Geist+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
html,body{{margin:0;background:#fff}}
svg{{display:block;width:{W}px;height:{alto}px;background:#fff}}
</style></head><body>{cuerpo}</body></html>'''
    open(sys.argv[1], 'w', encoding='utf-8').write(pagina)
    if len(sys.argv) > 2:
        open(sys.argv[2], 'w', encoding='utf-8', newline='\r\n').write(tikz())
    print('ok', W, 'x', alto)
