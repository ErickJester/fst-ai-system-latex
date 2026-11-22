"""Diagramas de la sección de pruebas de los anexos (una lámina completa cada uno), en el estilo de carriles.
Cifras del capítulo 7 (pruebas y resultados) y de evidencia/clasificador. Uso: gen_diapo_pruebas.py CARPETA"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_diapo_carriles import Lienzo, GRIS, AZUL, MORADO, ROSA, AMBAR, VERDE, INK, esc

W, H = 1800, 900
CSS_EXTRA = """
.v{font:600 26px Geist,'Segoe UI',sans-serif;fill:#1f2430}
.m{font:400 21px Geist,'Segoe UI',sans-serif;fill:#6b7280}
.b{font:600 24px Geist,'Segoe UI',sans-serif;fill:#fff}
.big{font:600 64px Geist,'Segoe UI',sans-serif;fill:#1f2430}
"""


def nuevo(titulo, c, h=H):
    d = Lienzo(W, h)
    d.carril(15, h - 15, titulo, c)
    return d


def pagina(d, nombre):
    html = d.pagina(nombre)
    return html.replace('</style>', CSS_EXTRA + '</style>', 1)


def barras(d, items, c, x0=110, y0=60, ancho=1000, altura=60, sep=26, etiq_w=520, maximo=None, formato=lambda v: str(v), extra=None, color_fn=None):
    """Barras horizontales. items = [(etiqueta, valor, nota?)]"""
    maximo = maximo or max(i[1] for i in items)
    for k, it in enumerate(items):
        y = y0 + k * (altura + sep)
        et, val = it[0], it[1]
        d.o.append(f'<text x="{x0+etiq_w-14}" y="{y+altura/2+9}" text-anchor="end" class="s">{esc(et)}</text>')
        w = max(ancho * val / maximo, 6)
        col = color_fn(k, it) if color_fn else c
        d.o.append(f'<rect x="{x0+etiq_w}" y="{y}" width="{w:.0f}" height="{altura}" rx="10" fill="{col[3]}" stroke="{col[4]}" stroke-width="2.4"/>')
        d.o.append(f'<text x="{x0+etiq_w+w+14:.0f}" y="{y+altura/2+9}" class="v">{esc(formato(val))}</text>')
        if len(it) > 2 and it[2]:
            d.o.append(f'<text x="{x0+etiq_w+w+14+len(formato(val))*15+16:.0f}" y="{y+altura/2+8}" class="m">{esc(it[2])}</text>')


def tarjeta_dato(d, x, y, w, h, grande, texto, c, sub=None):
    d.o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{c[3]}" stroke="{c[4]}" stroke-width="2.4"/>')
    d.o.append(f'<text x="{x+w/2}" y="{y+h*0.46:.0f}" text-anchor="middle" class="big">{esc(grande)}</text>')
    lines = texto if isinstance(texto, list) else [texto]
    for i, l in enumerate(lines):
        d.o.append(f'<text x="{x+w/2}" y="{y+h*0.46+44+i*30:.0f}" text-anchor="middle" class="s">{esc(l)}</text>')


# 1 ----------------------------------------------------------------------
def tipos():
    d = nuevo('Por tipo', AZUL)
    items = [('Validación de datos', 21), ('Funcional', 20), ('Negativa (rechazo)', 20), ('Seguridad', 12), ('Integración', 4), ('Rendimiento', 0, 'la prueba de carga es manual')]
    barras(d, items, AZUL, x0=110, y0=110, ancho=660, altura=70, sep=34, etiq_w=470, maximo=21)
    tarjeta_dato(d, 1380, 250, 340, 300, '77', ['pruebas automáticas', 'contra PostgreSQL real'], VERDE)
    d.txt(['Cada prueba se clasificó una sola vez', 'según su propósito principal'], 1550, 640, 'middle')
    return pagina(d, 'Pruebas por tipo')


# 2 ----------------------------------------------------------------------
def temas():
    d = nuevo('Por tema', AZUL)
    items = [('Restricciones de la base de datos', 29, ''), ('Experimentos y carga de video', 18, 'RF-08 a 12, 23, 24, 27, 30'), ('Cuentas, sesión y recuperación', 11, 'RF-03 a 07'),
             ('Resultados y reportes', 6, 'RF-18 a 22, 31'), ('Revisión segundo a segundo', 5, 'RF-32'), ('Plazo del enlace de recuperación', 4, 'RF-03'),
             ('Notificaciones y concurrencia', 3, 'RF-32, 33'), ('Pausa', 1, 'RF-15')]
    barras(d, items, AZUL, x0=100, y0=44, ancho=820, altura=70, sep=24, etiq_w=560, maximo=29)
    return pagina(d, 'Pruebas por tema')


# 3 ----------------------------------------------------------------------
def corridas():
    d = nuevo('Corridas', VERDE)
    ancho = 1500
    cel = ancho / 77
    def fila(y, titulo, partes):
        d.o.append(f'<text x="110" y="{y-18}" class="n">{esc(titulo)}</text>')
        x = 110
        for n, col, txt in partes:
            w = cel * n
            d.o.append(f'<rect x="{x:.0f}" y="{y}" width="{w:.0f}" height="110" rx="12" fill="{col[3]}" stroke="{col[4]}" stroke-width="2.6"/>')
            d.o.append(f'<text x="{x+w/2:.0f}" y="{y+64}" text-anchor="middle" class="n">{esc(txt)}</text>')
            x += w
    fila(170, 'Con la base PostgreSQL de pruebas', [(77, VERDE, '77 pasan, sin fallos ni errores')])
    fila(420, 'Sin base de datos', [(2, VERDE, ''), (75, GRIS, '75 se omiten')])
    d.txt(['2 corren: son las pruebas de la regla del', 'último Administrador, que no usan base de datos'], 110, 590, 'start')
    d.txt('Cada corrida verifica además que las entidades de la aplicación coincidan con las tablas; si no coinciden, la aplicación no arranca.', 110, 720, 'start')
    return pagina(d, 'Corridas de las 77 pruebas')


# 4 ----------------------------------------------------------------------
def restricciones():
    d = nuevo('Base de datos', AMBAR)
    cards = [('Lo válido sí entra', ['una cadena completa', 'de registros', 'tandas de 2 y 4 cilindros', 'segundos 1 y 300'], VERDE),
             ('Fuera de rango, se rechaza', ['tanda de 1 o 5 cilindros', 'segundo 0 o 301', 'duración 0 o negativa', 'diagnóstico sin error'], ROSA),
             ('Dominios cerrados', ['tipo de grupo', 'estado de análisis', 'conducta', 'fuera de su lista'], ROSA),
             ('Valores únicos', ['correo de usuario', 'ordinal, sesión y cilindro', 'nombre de experimento', 'segundo análisis del video'], ROSA),
             ('Llaves foráneas', ['no borra lo que otra', 'tabla todavía usa:', 'usuario, experimento,', 'grupo, tanda y video'], ROSA)]
    w = 310
    for i, (t, ls, c) in enumerate(cards):
        x = 105 + i * (w + 22)
        d.o.append(f'<rect x="{x}" y="150" width="{w}" height="470" rx="14" fill="{c[3]}" stroke="{c[4]}" stroke-width="2.4"/>')
        tl = t.split(', ') if ',' in t else [t]
        words = t.split(' ')
        d.o.append(f'<text x="{x+w/2}" y="210" text-anchor="middle" class="n">{esc(t if len(t) < 20 else " ".join(words[:2]))}</text>')
        if len(t) >= 20:
            d.o.append(f'<text x="{x+w/2}" y="246" text-anchor="middle" class="n">{esc(" ".join(words[2:]))}</text>')
        for k, l in enumerate(ls):
            d.o.append(f'<text x="{x+w/2}" y="{330+k*52}" text-anchor="middle" class="s">{esc(l)}</text>')
    d.txt('29 pruebas insertan, repiten o borran datos directamente en la base y comprueban que responda como el esquema establece.', 105, 740, 'start')
    return pagina(d, 'Restricciones de la base de datos')


# 5 ----------------------------------------------------------------------
def carga():
    d = nuevo('Carga', ROSA)
    x0, ancho, maximo = 760, 880, 3.0
    filas = [('Percentil 95 por ruta (el mayor), A', 0.086, VERDE), ('Percentil 95 de todas las peticiones, B', 0.041, VERDE), ('Máximo, corrida A', 0.888, AMBAR), ('Máximo, corrida B', 0.962, AMBAR), ('Límite del requisito (RNF-01)', 3.0, ROSA)]
    for k, (t, v, c) in enumerate(filas):
        y = 90 + k * 100
        d.o.append(f'<text x="{x0-16}" y="{y+40}" text-anchor="end" class="s">{esc(t)}</text>')
        w = max(ancho * v / maximo, 6)
        d.o.append(f'<rect x="{x0}" y="{y}" width="{w:.0f}" height="62" rx="10" fill="{c[3]}" stroke="{c[4]}" stroke-width="2.4"/>')
        d.o.append(f'<text x="{x0+w+14:.0f}" y="{y+42}" class="v">{v:.3f} s</text>')
    d.txt(['4 clientes, cada uno con su propia sesión (RNF-13)', 'Corrida A: 25 rondas sincronizadas, sin errores', 'Corrida B: 1,474 peticiones en 120 s, sin errores'], 110, 660, 'start')
    d.txt(['El máximo de A fue en la primera ronda, con la máquina virtual de Java sin calentar;', 'el de B, en la primera generación del XLSX'], 110, 770, 'start')
    return pagina(d, 'Prueba de carga con cuatro sesiones')


# 6 ----------------------------------------------------------------------
def video_real():
    d = Lienzo(W, H)
    d.carril(15, 380, 'Entrada', GRIS)
    d.carril(395, 885, 'Descargas', VERDE)
    v = d.caja(110, 70, 440, 'Video del día 2', ['5 minutos (301 s)', '1920 × 1080', '4 especímenes'], GRIS, h=250)
    w = d.caja(680, 70, 460, 'Análisis del worker', ['unos 9 minutos', '300 s analizados', 'sin intervención'], ROSA, h=250)
    r = d.caja(1270, 70, 440, 'Resultado', ['capturas de la interfaz', 'con el análisis real', 'no es el modo de ejemplo'], AZUL, h=250)
    d.flecha([(v['r'], v['cy']), (w['x'], w['cy'])])
    d.flecha([(w['r'], w['cy']), (r['x'], r['cy'])])
    x = 110
    dw = 390
    cs = [('PDF del experimento', ['3 páginas', 'con marcadores']), ('CSV de la tanda', ['24 filas de datos', 'más media, desviación,', 'varianza y revisión']), ('XLSX de la tanda', ['hoja «Resultados»', '25 filas y 9 columnas']), ('Excel del experimento', ['hojas «Resultados» y', '«Segundo a segundo»', '1,201 filas × 11 columnas'])]
    for i, (t, ls) in enumerate(cs):
        d.caja(110 + i * (dw + 18), 470, dw, t, ls, VERDE, h=250)
    d.txt('Las cuatro descargas del sistema se comprobaron con el análisis del video real.', 110, 800, 'start')
    return pagina(d, 'Verificación con un video real')


# 7 ----------------------------------------------------------------------
def tiempos():
    d = nuevo('Tiempo', ROSA)
    x0, ancho = 760, 800
    filas = [('A mano, por espécimen', 30, 'unos 30 minutos', AMBAR), ('A mano, video de 4 especímenes', 120, 'hasta unas 2 horas', AMBAR), ('Con el sistema (video de 5 min)', 9, 'unos 9 minutos', VERDE)]
    for k, (t, v, tx, c) in enumerate(filas):
        y = 130 + k * 150
        d.o.append(f'<text x="{x0-16}" y="{y+58}" text-anchor="end" class="s">{esc(t)}</text>')
        w = ancho * v / 120
        d.o.append(f'<rect x="{x0}" y="{y}" width="{w:.0f}" height="90" rx="12" fill="{c[3]}" stroke="{c[4]}" stroke-width="2.4"/>')
        d.o.append(f'<text x="{x0+w+16:.0f}" y="{y+58}" class="v">{esc(tx)}</text>')
    d.txt(['Una reducción de más del 90 % del tiempo de análisis.'], 110, 640, 'start')
    d.txt(['La cifra mide el procesamiento del video; la revisión segundo a segundo', 'es opcional y se suma si el investigador la hace.'], 110, 700, 'start')
    return pagina(d, 'Tiempo manual contra el sistema')


# 8 ----------------------------------------------------------------------
def validacion():
    d = nuevo('Validación', MORADO)
    d.caja(110, 70, 460, '11 videos', ['25 especímenes del laboratorio'], GRIS, h=130)
    d.txt('se agrupan por video en 5 particiones', 620, 150, 'start')
    cw = 128
    for p in range(5):
        y = 270 + p * 100
        d.o.append(f'<text x="110" y="{y+42}" class="s">Partición {p+1}</text>')
        for k in range(5):
            x = 330 + k * (cw + 12)
            es = k == p
            c = ROSA if es else AZUL
            d.o.append(f'<rect x="{x}" y="{y}" width="{cw}" height="62" rx="10" fill="{c[3]}" stroke="{c[4]}" stroke-width="2.4"/>')
            d.o.append(f'<text x="{x+cw/2}" y="{y+40}" text-anchor="middle" class="s">{"prueba" if es else "entrena"}</text>')
    d.caja(1100, 270, 600, 'Cómo se mide', ['Cada video se predice con una red', 'entrenada solo con los demás.', 'La red nunca ve el video que evalúa.', 'Se agrupa por video porque los', 'segundos vecinos comparten casi', 'el mismo clip.'], MORADO, h=360)
    d.txt('Los videos de prueba de cada partición no participan en el entrenamiento.', 110, 820, 'start')
    return pagina(d, 'Validación por video')


# 9 ----------------------------------------------------------------------
def datos_val():
    d = nuevo('Datos', MORADO)
    items = [('Nado', 3819), ('Inmovilidad', 2924), ('Escalamiento', 1244), ('Conducta activa sin distinguir', 261)]
    barras(d, items, MORADO, x0=100, y0=110, ancho=640, altura=80, sep=40, etiq_w=520, maximo=3819, formato=lambda v: f'{v:,}')
    tarjeta_dato(d, 1380, 120, 340, 280, '8,248', ['segundos etiquetados', '11 videos, 25 especímenes'], VERDE)
    tarjeta_dato(d, 1380, 450, 340, 280, '47.8 %', ['acertaría un sistema que', 'siempre dijera «nado»'], AMBAR)
    d.txt('Los 7,987 segundos de nado, inmovilidad y escalamiento son los que se califican.', 110, 800, 'start')
    return pagina(d, 'Datos de la validación')


# 10 ---------------------------------------------------------------------
def metricas():
    d = nuevo('Resultados', MORADO)
    datos = [('Escalamiento', [0.646, 0.682, 0.663]), ('Inmovilidad', [0.727, 0.710, 0.719]), ('Nado', [0.732, 0.732, 0.732])]
    series = [('Precisión', AZUL), ('Recall', VERDE), ('F1', ROSA)]
    base, alto = 700, 520
    d.o.append(f'<line x1="110" y1="{base}" x2="1380" y2="{base}" stroke="#9aa4b2" stroke-width="2"/>')
    for g, (n, vals) in enumerate(datos):
        gx = 150 + g * 410
        for s, v in enumerate(vals):
            c = series[s][1]
            hh = alto * v
            x = gx + s * 110
            d.o.append(f'<rect x="{x}" y="{base-hh:.0f}" width="96" height="{hh:.0f}" rx="8" fill="{c[3]}" stroke="{c[4]}" stroke-width="2.4"/>')
            d.o.append(f'<text x="{x+48}" y="{base-hh-12:.0f}" text-anchor="middle" class="l">{v:.3f}</text>')
        d.o.append(f'<text x="{gx+165}" y="{base+46}" text-anchor="middle" class="v">{n}</text>')
    for s, (n, c) in enumerate(series):
        y = 130 + s * 60
        d.o.append(f'<rect x="1450" y="{y}" width="34" height="34" rx="6" fill="{c[3]}" stroke="{c[4]}" stroke-width="2.4"/><text x="1498" y="{y+27}" class="s">{n}</text>')
    tarjeta_dato(d, 1450, 360, 290, 250, '0.705', ['F1 promedio', 'de las tres conductas'], VERDE)
    tarjeta_dato(d, 1450, 640, 290, 220, '71.6 %', ['exactitud', 'por segundo'], AZUL)
    return pagina(d, 'Precisión, recall y F1 por conducta')


# 11 ---------------------------------------------------------------------
def confusion():
    d = nuevo('Confusión', MORADO)
    clases = ['Escalamiento', 'Inmovilidad', 'Nado']
    m = [[848, 89, 307], [132, 2077, 715], [333, 690, 2796]]
    x0, y0, cw, ch = 520, 170, 250, 170
    d.o.append(f'<text x="{x0+1.5*cw}" y="90" text-anchor="middle" class="v">Lo que decidió el clasificador</text>')
    d.o.append(f'<text x="110" y="{y0-34}" class="m">Lo que marcó el equipo</text>')
    for j, cn in enumerate(clases):
        d.o.append(f'<text x="{x0+j*cw+cw/2}" y="{y0-34}" text-anchor="middle" class="s">{cn}</text>')
    for i, cn in enumerate(clases):
        tot = sum(m[i])
        d.o.append(f'<text x="{x0-18}" y="{y0+i*ch+ch/2+8}" text-anchor="end" class="s">{cn}</text>')
        for j in range(3):
            v = m[i][j]
            p = v / tot
            diag = i == j
            c = ROSA if not diag else VERDE
            op = 0.25 + 0.75 * p
            d.o.append(f'<rect x="{x0+j*cw}" y="{y0+i*ch}" width="{cw-8}" height="{ch-8}" rx="12" fill="{c[4]}" fill-opacity="{op:.2f}" stroke="{c[4]}" stroke-width="2.4"/>')
            d.o.append(f'<text x="{x0+j*cw+(cw-8)/2}" y="{y0+i*ch+ch/2-4}" text-anchor="middle" class="v">{v:,}</text>')
            d.o.append(f'<text x="{x0+j*cw+(cw-8)/2}" y="{y0+i*ch+ch/2+34}" text-anchor="middle" class="s">{p*100:.1f} %</text>')
    d.txt(['Los errores más frecuentes son entre', 'inmovilidad y nado (715 y 690 segundos)', 'y entre escalamiento y nado (307 y 333).'], 1330, 250, 'start')
    d.txt(['La inmovilidad casi no se confunde', 'con el escalamiento.'], 1330, 470, 'start')
    d.txt('Cada celda muestra los segundos y el porcentaje de la fila; la diagonal es el recall de cada conducta.', 110, 760, 'start')
    return pagina(d, 'Matriz de confusión')


# 12 ---------------------------------------------------------------------
def otras():
    d = nuevo('Otras', MORADO)
    cards = [('0.839', ['F1 de la conducta activa', 'en inmovilidad contra activa'], AZUL, '0.704 en inmovilidad;', 'exactitud 0.792 sobre 8,248 s'),
             ('69.9 %', ['exactitud por bloque de 5 s', 'con la conducta mayoritaria'], VERDE, 'sobre 1,400 bloques', 'completos'),
             ('0.774', ['exactitud con confianza de 0.8 o más', 'en el 75 % de los segundos'], AMBAR, 'con 0.9 o más: 0.813', 'en el 57 % de los segundos')]
    for i, (g, tx, c, s1, s2) in enumerate(cards):
        x = 105 + i * 560
        d.o.append(f'<rect x="{x}" y="120" width="530" height="560" rx="16" fill="{c[3]}" stroke="{c[4]}" stroke-width="2.4"/>')
        d.o.append(f'<text x="{x+265}" y="290" text-anchor="middle" class="big">{g}</text>')
        for k, l in enumerate(tx):
            d.o.append(f'<text x="{x+265}" y="{360+k*34}" text-anchor="middle" class="s">{esc(l)}</text>')
        d.o.append(f'<text x="{x+265}" y="520" text-anchor="middle" class="m">{esc(s1)}</text>')
        d.o.append(f'<text x="{x+265}" y="556" text-anchor="middle" class="m">{esc(s2)}</text>')
    d.txt('Una mayor exactitud implica dejar sin decidir una parte de los segundos.', 105, 770, 'start')
    return pagina(d, 'Otras mediciones del clasificador')


DIAGS = [('01_tipos', tipos), ('02_temas', temas), ('03_corridas', corridas), ('04_restricciones', restricciones), ('05_carga', carga),
         ('06_video_real', video_real), ('07_tiempos', tiempos), ('08_validacion', validacion), ('09_datos_val', datos_val),
         ('10_metricas', metricas), ('11_confusion', confusion), ('12_otras', otras)]

if __name__ == '__main__':
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    for n, f in DIAGS:
        open(os.path.join(out, n + '.html'), 'w', encoding='utf-8').write(f())
        print(n)
