"""Arquitectura por capas, contenedores Docker y flujo del sistema en carriles de colores (mismo estilo que
el diagrama de estados de la diapositiva), para ocupar una diapositiva completa.
Uso: gen_diapo_carriles.py CARPETA   -> capas.html, contenedores.html, flujo.html"""
import html, os, sys
esc = html.escape
INK = '#1f2430'
FONT = '<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;600&display=swap" rel="stylesheet">'
CSS = """
.n{font:600 29px Geist,'Segoe UI',sans-serif;fill:#1f2430}
.s{font:400 23px Geist,'Segoe UI',sans-serif;fill:#1f2430}
.k{font:400 18px Geist,'Segoe UI',sans-serif;fill:#6b7280}
.l{font:400 21px Geist,'Segoe UI',sans-serif;fill:#1f2430}
.c{font:600 22px Geist,'Segoe UI',sans-serif;fill:#fff}
.g{font:400 20px Geist,'Segoe UI',sans-serif;fill:#1f2430}
"""
# (fondo del carril, borde, rótulo, relleno de caja, borde de caja)
GRIS = ('#f3f4f6', '#d1d5db', '#6b7280', '#e5e7eb', '#6b7280')
AZUL = ('#eef4fc', '#bfd3ee', '#4a79c4', '#dde9f9', '#3b78c4')
MORADO = ('#f4f0fb', '#d6c9ee', '#7a5cc4', '#e8e0f7', '#7a5cc4')
ROSA = ('#fdf1ec', '#f2c9bb', '#d9693f', '#fde2d9', '#d9532c')
AMBAR = ('#fff7e8', '#f1d9a8', '#c99a2e', '#fdf0d0', '#c99a2e')
VERDE = ('#eef8f1', '#bfe3cb', '#2f8f55', '#dff3e6', '#2f8f55')


class Lienzo:
    def __init__(self, W, H):
        self.W, self.H, self.o = W, H, []

    def carril(self, y0, y1, titulo, c):
        W = self.W
        self.o.append(f'<rect x="20" y="{y0}" width="{W-40}" height="{y1-y0}" rx="10" fill="{c[0]}" stroke="{c[1]}"/>')
        self.o.append(f'<rect x="20" y="{y0}" width="52" height="{y1-y0}" rx="10" fill="{c[2]}"/>')
        self.o.append(f'<text transform="translate(53,{(y0+y1)/2}) rotate(-90)" text-anchor="middle" class="c">{esc(titulo)}</text>')

    def caja(self, x, y, w, titulo, lineas, c, ster=None, dash=False, h=None):
        top = 74 if ster else 52
        hh = h or top + len(lineas) * 31 + 14
        self.o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{hh}" rx="12" fill="{c[3]}" stroke="{c[4]}" stroke-width="2.4"' + (' stroke-dasharray="9,6"' if dash else '') + '/>')
        ty = y + 32
        if ster:
            self.o.append(f'<text x="{x+w/2}" y="{y+26}" text-anchor="middle" class="k">«{esc(ster)}»</text>')
            ty = y + 58
        self.o.append(f'<text x="{x+w/2}" y="{ty}" text-anchor="middle" class="n">{esc(titulo)}</text>')
        for i, t in enumerate(lineas):
            self.o.append(f'<text x="{x+w/2}" y="{ty + 36 + i*31}" text-anchor="middle" class="s">{esc(t)}</text>')
        return dict(x=x, y=y, w=w, h=hh, b=y + hh, r=x + w, cx=x + w / 2, cy=y + hh / 2)

    def flecha(self, pts, dash=False):
        d = 'M' + ' L'.join(f'{x:.0f},{y:.0f}' for x, y in pts)
        self.o.append(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="2"' + (' stroke-dasharray="8,6"' if dash else '') + ' marker-end="url(#ar)"/>')

    def txt(self, lineas, x, y, ancla='middle', fondo=None):
        if isinstance(lineas, str):
            lineas = [lineas]
        if fondo:
            w = max(len(l) for l in lineas) * 10.4 + 12
            x0 = x - w / 2 if ancla == 'middle' else (x - 6 if ancla == 'start' else x - w + 6)
            self.o.append(f'<rect x="{x0:.0f}" y="{y-19}" width="{w:.0f}" height="{len(lineas)*25+5}" fill="{fondo}"/>')
        for i, l in enumerate(lineas):
            self.o.append(f'<text x="{x}" y="{y + i*25}" text-anchor="{ancla}" class="l">{esc(l)}</text>')

    def leyenda(self, y, items):
        x = 60
        for c, dash, t in items:
            if c == 'flecha':
                self.o.append(f'<line x1="{x}" y1="{y-8}" x2="{x+42}" y2="{y-8}" stroke="{INK}" stroke-width="2"/><path d="M{x+33},{y-14} L{x+42},{y-8} L{x+33},{y-2}" fill="none" stroke="{INK}" stroke-width="2"/>')
                w = 56
            elif c == 'falla':
                self.o.append(f'<line x1="{x}" y1="{y-8}" x2="{x+42}" y2="{y-8}" stroke="{INK}" stroke-width="2" stroke-dasharray="7,5"/><path d="M{x+33},{y-14} L{x+42},{y-8} L{x+33},{y-2}" fill="none" stroke="{INK}" stroke-width="2"/>')
                w = 56
            else:
                self.o.append(f'<rect x="{x}" y="{y-22}" width="32" height="26" rx="5" fill="{c[3]}" stroke="{c[4]}" stroke-width="2"' + (' stroke-dasharray="5,3"' if dash else '') + '/>')
                w = 46
            self.o.append(f'<text x="{x+w}" y="{y}" class="g">{esc(t)}</text>')
            x += w + len(t) * 10.4 + 46

    def pagina(self, nombre):
        svg = (f'<svg viewBox="0 0 {self.W} {self.H}" width="{self.W}" height="{self.H}" xmlns="http://www.w3.org/2000/svg"><title>{esc(nombre)}</title>'
               f'<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M1,1 L9,5 L1,9" fill="none" stroke="{INK}" stroke-width="1.6"/></marker></defs>'
               f'<style>{CSS}</style><rect width="{self.W}" height="{self.H}" fill="#fff"/>' + '\n'.join(self.o) + '</svg>')
        return (f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{esc(nombre)}</title>{FONT}'
                f'<style>html,body{{margin:0;background:#fff}}svg{{display:block}}</style></head><body>{svg}</body></html>')


# ------------------------------------------------------------------ arquitectura por capas
def capas():
    d = Lienzo(1800, 960)
    L = [(15, 120), (134, 289), (303, 488), (502, 712), (726, 906)]
    d.carril(*L[0], 'Usuario', GRIS)
    d.carril(*L[1], 'Presentación', AZUL)
    d.carril(*L[2], 'Lógica', MORADO)
    d.carril(*L[3], 'Procesamiento', ROSA)
    d.carril(*L[4], 'Datos', AMBAR)
    P = 22
    inv = d.caja(640, L[0][0] + 18, 520, 'Investigador (navegador)', [], GRIS, dash=True, h=70)
    fe = d.caja(520, L[1][0] + P, 760, 'frontend', ['React + Vite · formularios, resultados y reportes'], AZUL, ster='contenedor', h=118)
    be = d.caja(520, L[2][0] + P, 760, 'backend', ['Spring Boot (Java 21) · API REST (JSON) con JWT', 'Valida videos y encola análisis'], MORADO, ster='contenedor', h=146)
    wk = d.caja(290, L[3][0] + P, 1220, 'worker', ['OpenCV: preprocesamiento y cilindros · PyTorch: red de fusión R(2+1)D-18',
                                                   'Python: un análisis a la vez; reencola al arrancar', 'Python: tareas diarias (borrado, aviso, disco)'], ROSA, ster='contenedor', h=186)
    yd = L[4][0] + P
    vm = d.caja(100, yd, 470, 'Volumen de modelos', ['solo lectura para el worker', 'archivo del clasificador'], AMBAR, h=136)
    vc = d.caja(630, yd, 560, 'Volumen compartido', ['videos, copias de revisión,', 'recuadros, pausas, reportes'], AMBAR, h=136)
    db = d.caja(1250, yd, 510, 'Base de datos', ['PostgreSQL 16 · 12 tablas', 'la tabla ANALISIS es la cola'], AMBAR, ster='contenedor', h=136)
    d.flecha([(inv['cx'], inv['b']), (inv['cx'], fe['y'])])
    d.flecha([(fe['cx'], fe['b']), (fe['cx'], be['y'])])
    d.txt('API REST (JSON + JWT)', fe['cx'] + 14, (fe['b'] + be['y']) / 2 + 7, 'start')
    d.flecha([(be['cx'], be['b']), (be['cx'], wk['y'])])
    d.txt('encola análisis', be['cx'] + 14, (be['b'] + wk['y']) / 2 + 7, 'start')
    d.flecha([(be['r'], be['y'] + 74), (1600, be['y'] + 74), (1600, db['y'])])
    d.txt('lee y escribe análisis', (be['r'] + 1600) / 2, be['y'] + 60, 'middle')
    d.flecha([(1380, wk['b']), (1380, db['y'])])
    d.txt('toma tareas y guarda', 1366, (wk['b'] + db['y']) / 2 + 7, 'end')
    d.flecha([(vc['cx'], wk['b']), (vc['cx'], vc['y'])])
    d.txt('guarda archivos', vc['cx'] + 14, (wk['b'] + vc['y']) / 2 + 7, 'start')
    d.flecha([(350, vm['y']), (350, wk['b'])])
    d.txt('carga al iniciar', 364, (wk['b'] + vm['y']) / 2 + 7, 'start')
    d.leyenda(938, [(GRIS, True, 'Actor'), (AZUL, False, 'Presentación'), (MORADO, False, 'Lógica'), (ROSA, False, 'Pieza clave: worker'), (AMBAR, False, 'Datos y volúmenes'), ('flecha', False, 'comunicación')])
    return d.pagina('Arquitectura por capas')


# ------------------------------------------------------------------ contenedores Docker
def contenedores():
    d = Lienzo(1800, 830)
    A, B, C = (15, 215), (229, 489), (519, 729)
    d.carril(*A, 'Exterior', GRIS)
    d.carril(*B, 'Contenedores', AZUL)
    d.carril(*C, 'Volúmenes', AMBAR)
    nav = d.caja(100, 38, 400, 'Equipo del investigador', ['Navegador web'], GRIS, ster='dispositivo', dash=True, h=150)
    mail = d.caja(980, 38, 340, 'Cuenta de correo', ['Cuenta configurable', '(avisos, RF-33)'], GRIS, ster='servicio externo', dash=True, h=150)
    web = d.caja(100, 252, 320, 'web', ['React.js + Vite · nginx', 'Interfaz del investigador'], AZUL, ster='contenedor', h=222)
    api = d.caja(540, 252, 320, 'api', ['Spring Boot · Java 21', 'API REST con JWT', 'Encola los análisis'], AZUL, ster='contenedor', h=222)
    db = d.caja(980, 252, 320, 'db', ['PostgreSQL 16', 'Cola de tareas y', 'resultados · 12 tablas'], AZUL, ster='contenedor', h=222)
    wk = d.caja(1420, 252, 320, 'worker', ['Python · OpenCV · PyTorch', 'Pipeline de análisis', 'Un video a la vez', 'Tareas diarias'], ROSA, ster='contenedor', h=222)
    vc = d.caja(540, 545, 760, 'Volumen compartido', ['Videos y copia H.264 · datos de pausa', 'Reportes PDF, CSV, XLSX'], AMBAR, h=160)
    vm = d.caja(1420, 545, 320, 'Volumen de modelos', ['Solo lectura', 'Clasificador de conducta'], AMBAR, h=160)
    d.flecha([(260, nav['b']), (260, web['y'])])
    d.txt('carga la app', 274, (nav['b'] + web['y']) / 2 + 7, 'start')
    d.flecha([(nav['r'], 113), (700, 113), (700, api['y'])])
    d.txt('API REST + JWT', 600, 98, 'middle')
    d.flecha([(820, api['y']), (820, 113), (mail['x'], 113)])
    d.txt('envía correo', 900, 98, 'middle')
    d.flecha([(api['r'], 363), (db['x'], 363)])
    d.txt('encola', (api['r'] + db['x']) / 2, 348, 'middle')
    d.flecha([(wk['x'], 363), (db['r'], 363)])
    d.txt(['consulta', 'la cola'], (db['r'] + wk['x']) / 2, 335, 'middle')
    d.flecha([(700, api['b']), (700, vc['y'])])
    d.txt('lee y sirve archivos', 714, (api['b'] + vc['y']) / 2 + 7, 'start')
    d.flecha([(1480, wk['b']), (1480, 504), (1200, 504), (1200, vc['y'])])
    d.txt('guarda resultados', 1320, 532, 'middle')
    d.flecha([(1590, vm['y']), (1590, wk['b'])])
    d.txt('carga el modelo', 1576, 532, 'end')
    d.leyenda(790, [(GRIS, True, 'Fuera de Docker'), (AZUL, False, 'Contenedor'), (ROSA, False, 'Pieza clave: worker'), (AMBAR, False, 'Volumen'), ('flecha', False, 'comunicación')])
    return d.pagina('Contenedores Docker')


# ------------------------------------------------------------------ flujo del sistema
def flujo():
    d = Lienzo(1800, 900)
    L = [(15, 185), (199, 369), (383, 603), (617, 837)]
    d.carril(*L[0], 'Entrena', AMBAR)
    d.carril(*L[1], 'Subida', GRIS)
    d.carril(*L[2], 'Worker', AZUL)
    d.carril(*L[3], 'Salida', VERDE)
    BW, GP = 330, 60
    X = [100 + i * (BW + GP) for i in range(5)]
    h1 = 128
    y1, y2 = L[0][0] + 28, L[1][0] + 28
    BW = 292
    X = [100 + i * (BW + 50) for i in range(5)]
    t = [d.caja(X[0], y1, BW, 'Videos', ['sin las anotaciones', 'manuales'], AMBAR, h=h1),
         d.caja(X[1], y1, BW, 'Etiquetado', ['el equipo revisa', 'las conductas'], AMBAR, h=h1),
         d.caja(X[2], y1, BW, 'Entrenamiento', ['con los segundos', 'etiquetados'], AMBAR, h=h1),
         d.caja(X[3], y1, BW, 'Modelo', ['en el volumen', 'de modelos'], AMBAR, h=h1),
         d.caja(X[4], y1, BW, 'Evaluación', ['precisión, recall', 'y F1 por conducta'], AMBAR, h=h1)]
    for a, b in zip(t, t[1:]):
        d.flecha([(a['r'], a['cy']), (b['x'], b['cy'])])
    W4 = 380
    X4 = [100 + i * (W4 + 46) for i in range(4)]
    s = [d.caja(X4[0], y2, W4, 'Investigador', ['sube el video', 'del experimento'], GRIS, h=h1),
         d.caja(X4[1], y2, W4, 'Backend', ['valida formato', 'y guarda el video'], GRIS, h=h1),
         d.caja(X4[2], y2, W4, 'Cola de análisis', ['estado «en cola»;', 'Día 1: solo se guarda'], GRIS, h=h1),
         d.caja(X4[3], y2, W4, 'Worker', ['toma el más antiguo;', 'un video a la vez'], GRIS, h=h1)]
    for a, b in zip(s, s[1:]):
        d.flecha([(a['r'], a['cy']), (b['x'], b['cy'])])
    y3 = L[2][0] + 26
    w = [d.caja(X4[0], y3, W4, 'Preprocesamiento', ['registro de cámara', 'y modelo de fondo'], AZUL, h=h1),
         d.caja(X4[1], y3, W4, 'Cilindros', ['localiza de 2 a 4', 'tubos por video'], AZUL, h=h1),
         d.caja(X4[2], y3, W4, 'Clasificación', ['conducta de cada', 'segundo (modelo)'], ROSA, h=h1),
         d.caja(X4[3], y3, W4, 'En pausa', ['3 s seguidos sin ver:', 'guarda imagen y avisa;', 'el usuario ajusta o cancela;', 'sin respuesta en 72 h, cancela'], AMBAR, dash=True, h=178)]
    d.flecha([(w[0]['r'], w[0]['cy']), (w[1]['x'], w[0]['cy'])])
    d.flecha([(w[1]['r'], w[0]['cy']), (w[2]['x'], w[0]['cy'])])
    d.flecha([(w[2]['r'], w[0]['cy']), (w[3]['x'], w[0]['cy'])], dash=True)
    # worker -> preprocesamiento
    ym = (s[3]['b'] + w[3]['y']) / 2 + 2
    ym = (L[1][1] + L[2][0]) / 2
    d.flecha([(s[3]['cx'], s[3]['b']), (s[3]['cx'], ym), (w[0]['cx'], ym), (w[0]['cx'], w[0]['y'])])
    y4 = L[3][0] + 26
    sal = [d.caja(X4[0], y4, W4, 'Si falla', ['no abre el video o no hay', 'cilindros: estado «error»', 'y diagnóstico; el worker', 'sigue con el siguiente'], ROSA, h=178),
           d.caja(X4[1], y4, W4, 'Investigador', ['revisa cada segundo;', 'los totales se recalculan;', 'puede reiniciar el análisis'], VERDE, h=150),
           d.caja(X4[2], y4, W4, 'Resultados', ['conducta de cada segundo;', 'tiempos por minuto;', 'copia H.264 para revisión'], VERDE, h=150),
           d.caja(X4[3], y4, W4, 'Reportes', ['descarga en PDF,', 'CSV o XLSX'], VERDE, h=150)]
    d.flecha([(w[0]['cx'], w[0]['b']), (w[0]['cx'], sal[0]['y'])], dash=True)
    d.txt('falla', w[0]['cx'] + 14, (w[0]['b'] + sal[0]['y']) / 2 + 7, 'start')
    d.flecha([(w[2]['cx'], w[2]['b']), (w[2]['cx'], sal[2]['y'])])
    d.txt('éxito', w[2]['cx'] + 14, (w[2]['b'] + sal[2]['y']) / 2 + 7, 'start')
    d.flecha([(sal[2]['x'], sal[2]['cy']), (sal[1]['r'], sal[2]['cy'])])
    d.flecha([(sal[2]['r'], sal[2]['cy']), (sal[3]['x'], sal[2]['cy'])])
    d.leyenda(878, [(AMBAR, False, 'Fuera de línea'), (GRIS, False, 'Subida y cola'), (AZUL, False, 'Pipeline'), (ROSA, False, 'Clasificación y falla'), (VERDE, False, 'Salida'), ('flecha', False, 'flujo'), ('falla', False, 'falla')])
    return d.pagina('Flujo del sistema')


if __name__ == '__main__':
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    for n, f in (('capas', capas), ('contenedores', contenedores), ('flujo', flujo)):
        open(os.path.join(out, n + '.html'), 'w', encoding='utf-8').write(f())
        print(n)
