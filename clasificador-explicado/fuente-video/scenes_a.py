"""Escenas 1 a 5 del video del clasificador."""
import math
import random
from PIL import Image, ImageDraw
from vid_lib import *


class Ctx:
    def __init__(s, img, d, t, B):
        s.img, s.d, s.t, s.B = img, d, t, B

    def p(s, i, dur=0.8):
        return ez(pr(s.t, s.B[i], s.B[i] + dur))

    def page(s, a, b, fn, fin=0.5, fout=0.5):
        t = s.t
        if t < a or t > b + fout:
            return
        al = min(pr(t, a, a + fin), 1 - pr(t, b, b + fout))
        if al <= 0:
            return
        if al >= 0.999:
            fn(s.d)
            return
        lay = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        fn(ImageDraw.Draw(lay))
        lay.putalpha(lay.getchannel('A').point(lambda v: int(v * al)))
        s.img.paste(lay, (0, 0), lay)

    def show(s, a, fn, fin=0.6):
        s.page(a, 1e9, fn, fin, 0.0)


def B_(display, spoken=None):
    return (display, spoken or display)


# =============================================================== ESCENA 1
def s1(c):
    d, t, B = c.d, c.t, c.B
    top, w, h = 215, 320, 430
    k = c.p(1, 1.2)
    x1 = lerp(960, 430, k)
    cil(d, x1, top, 'nado', t, w, h)
    if k > 0.02:
        def cm(dd):
            cam(dd, 60, 330, t)
            ln(dd, (215, 369), (x1 - w / 2 - 12, 369), GRIS, 3)
            T(dd, (60, 420), 'cámara', 30, GRIS, True)
        c.show(B[1] + 0.6, cm)
    if t >= B[2]:
        c.show(B[2], lambda dd: chip(dd, x1, top + h + 28, 'Nadar', NADO, 40, anchor='mm'))
    if t >= B[3]:
        def c2(dd):
            cil(dd, 960, top, 'quieto', t, w, h)
            chip(dd, 960, top + h + 28, 'Quieto: inmovilidad', QUIETO, 34, anchor='mm')
        c.show(B[3], c2)
    if t >= B[4]:
        def c3(dd):
            cil(dd, 1500, top, 'trepa', t, w, h)
            chip(dd, 1500, top + h + 28, 'Trepar: escalamiento', TREPA, 34, anchor='mm')
        c.show(B[4], c3)
    if t >= B[5]:
        def tira(dd):
            T(dd, (110, 738), 'Cada segundo del video necesita una respuesta: ¿nada, flota o trepa?', 32, GRIS, True)
            idx = int(t * 4) % 14
            for i in range(14):
                x = 110 + i * 120
                rr(dd, (x, 790, x + 104, 862), r=14, fill=mix(WHITE, MED, 0.55) if i == idx else WHITE, outline=LINEA, w=3)
                T(dd, (x + 52, 826), '?', 44, GRIS, True, 'mm')
        c.show(B[5], tira)


S1 = dict(title='¿Qué queremos que haga la computadora?', draw=s1, beats=[
    B_('Hola. Hoy vamos a enseñarle a una computadora a mirar un video y decir qué está haciendo un espécimen, un animalito de laboratorio.'),
    B_('Lo ponemos en un cilindro con agua y lo grabamos. En cada segundo del video, hace una de tres cosas.'),
    B_('Puede nadar.'),
    B_('Puede quedarse quieto, flotando. A eso le decimos inmovilidad.'),
    B_('O puede trepar por la pared. A eso le decimos escalamiento.'),
    B_('Revisar horas de video, segundo por segundo, cansa mucho a una persona. Por eso queremos que la computadora lo haga y nos avise.'),
])


# =============================================================== ESCENA 2
def tarjeta(d, x, y, fr, etiqueta, col=GRIS, w=200, h=240):
    caja(d, (x, y, x + w, y + h), r=20)
    fruta(d, x + w / 2, y + 100, fr, 0.9)
    if etiqueta:
        chip(d, x + w / 2, y + h - 62, etiqueta, col, 28, anchor='mm')


def s2(c):
    d, t, B = c.d, c.t, c.B
    frs = ['manzana', 'platano', 'manzana', 'platano']
    nom = ['manzana', 'plátano', 'manzana', 'plátano']
    for i in range(4):
        ta = B[0] + 1.2 + i * 1.5
        k = ez(pr(t, ta, ta + 0.5))
        if k > 0:
            tarjeta(d, 100 + i * 235, 215 + (1 - k) * 40, frs[i], nom[i], FUS)
    if t >= B[1]:
        def q(dd):
            ok = t > B[1] + 3.5
            tarjeta(dd, 110, 540, 'manzana', 'manzana' if ok else '?', FUS if ok else GRIS)
            if t < B[2]:
                T(dd, (330, 640), '¿Cuál será?' if not ok else '¡Una manzana!', 40, GRIS if not ok else FUS, True)
        c.show(B[1], q)
    if t >= B[2]:
        def df(dd):
            chip(dd, 200, 168, 'ejemplo', MED, 30, fg=INK, anchor='mm')
            arrow(dd, (200, 214), (200, 252), INK, 4, 14)
            chip(dd, 200, 463, 'etiqueta', VIDEO, 30, anchor='mm')
            caja(dd, (380, 540, 1000, 790), fill=mix(WHITE, FUS, 0.10), outline=FUS, r=24, w=4)
            T(dd, (410, 560), 'Aprendizaje supervisado', 40, FUS, True)
            TW(dd, 410, 618, 'es aprender con ejemplos que ya traen su respuesta.', 36, INK, 560)
            TW(dd, 410, 700, 'La respuesta se llama etiqueta.', 36, INK, 560, True)
        c.show(B[2], df)
    if t >= B[3]:
        def clips(dd):
            T(dd, (1040, 172), 'Nuestros ejemplos: clips de 1 segundo', 32, GRIS, True)
            filas = [('nado', 'nadó', NADO), ('quieto', 'quieto', QUIETO), ('trepa', 'trepó', TREPA)]
            for r, (k, nm, col) in enumerate(filas):
                y = 215 + r * 185
                caja(dd, (1040, y, 1830, y + 160), r=20)
                for i in range(4):
                    ph = i * 0.9 if k == 'nado' else (1.0 if k == 'quieto' else 2.0 + i * 0.5)
                    miniframe(dd, 1065 + i * 128, y + 28, 112, 104, ph, shift=(30 if k == 'trepa' else 0))
                chip(dd, 1700, y + 52, nm, col, 34, anchor='mm')
                T(dd, (1700, y + 105), 'etiqueta del equipo', 24, GRIS, False, 'mm')
        c.show(B[3], clips)
    if t >= B[4]:
        c.show(B[4], lambda dd: chip(dd, 1435, 800, '≈ 8 000 segundos con su etiqueta', FUS, 40, anchor='mm'))


S2 = dict(title='Aprender con ejemplos', draw=s2, beats=[
    B_('¿Cómo aprendiste lo que es una manzana y lo que es un plátano? Alguien te mostró muchos ejemplos y te dijo el nombre de cada uno.'),
    B_('Con muchos ejemplos aprendiste a reconocerlos tú solo. Ahora, cuando ves una fruta nueva, ya sabes cuál es.'),
    B_('A esto se le llama aprendizaje supervisado: aprender con ejemplos que ya traen su respuesta. A la respuesta la llamamos etiqueta.'),
    B_('Aquí, cada ejemplo es un clip de video de un segundo. Y la etiqueta la puso el equipo, a mano: nadó, estuvo quieto o trepó.'),
    B_('Así la computadora aprende con unos ocho mil segundos de ejemplos, todos con su etiqueta.'),
])


# =============================================================== ESCENA 3
X0, BW = 150, 108


def s3(c):
    d, t, B = c.d, c.t, c.B
    k0 = 7  # indice del segundo a decidir (el 8)
    # deslizamiento de la ventana (beat 3)
    u = max(0.0, (t - B[3] - 0.3) / 1.6)
    u = min(u, 4.0)
    shift = int(u) + ez(u - int(u)) if u < 4 else 4.0
    if t < B[3]:
        shift = 0.0
    sec = k0 + shift          # posicion del segundo resaltado (en cajas)
    wa = sec + 0.5 - 2        # inicio de la ventana en unidades de caja
    pa = ez(pr(t, B[0] + 0.5, B[0] + 1.4))
    if pa > 0:
        T(d, (X0, 178), 'segundos del video', 28, GRIS, True)
    # ventana
    if t >= B[1]:
        kw = ez(pr(t, B[1], B[1] + 0.9))
        wx0, wx1 = X0 + wa * BW, X0 + (wa + 4) * BW
        rr(d, (wx0 - 4, 226, wx1 + 4, 330 + 22), r=14, fill=mix(BG, MED, 0.40 * kw), outline=MED if kw > 0.5 else None, w=5)
    for i in range(15):
        x = X0 + i * BW
        hl = abs(i - sec) < 0.5
        rr(d, (x, 240, x + 100, 310), r=12, fill=mix(WHITE, NADO, 0.35) if hl and pa > 0.5 else WHITE, outline=NADO if hl else LINEA, w=5 if hl else 3)
        T(d, (x + 50, 275), str(i + 1), 34, INK, True, 'mm')
    if pa > 0.5:
        cx = X0 + (sec + 0.5) * BW - 4
        T(d, (cx, 205), '▼ segundo a decidir', 28, NADO, True, 'mm')
    if t >= B[1]:
        kw = ez(pr(t, B[1], B[1] + 0.9))
        wx0, wx1 = X0 + wa * BW, X0 + (wa + 4) * BW
        T(d, ((wx0 + wx1) / 2, 338), 'ventana de 4 segundos', 28, hx('a97c10'), True, 'mm')
        # fotos
        x_start = 96
        for i in range(16):
            ta = B[1] + 0.8 + i * 0.28
            kk = ez(pr(t, ta, ta + 0.4))
            if kk <= 0 and t < B[3]:
                continue
            x = x_start + i * 108
            ph = (wa + i * 0.25) * 1.3
            miniframe(d, x, 430 + (1 - kk) * -30 if t < B[3] else 430, 100, 96, ph)
        if kk > 0 or t >= B[3]:
            pass
        ln(d, (wx0, 358), (96, 430), mix(BG, MED, 0.8), 3)
        ln(d, (wx1, 358), (96 + 15 * 108 + 100, 430), mix(BG, MED, 0.8), 3)
        T(d, (960, 562), '16 fotos', 40, INK, True, 'mm')
    if t >= B[2] and t < B[3] + 0.3:
        def comp(dd):
            caja(dd, (96, 600, 900, 870), r=22)
            T(dd, (130, 616), 'Con 1 sola foto', 34, GRIS, True)
            miniframe(dd, 130, 676, 240, 170, 0.5)
            T(dd, (500, 740), '¿flota o\nnada despacio?', 38, QUIETO, True, 'lm')
            caja(dd, (960, 600, 1824, 870), r=22)
            T(dd, (994, 616), 'Con 16 fotos se ve el cambio', 34, FUS, True)
            for i in range(4):
                miniframe(dd, 994 + i * 150, 690, 130, 100, i * 1.2 + t * 0.0)
            arrow(dd, (1000, 830), (1560, 830), FUS, 5, 20)
            T(dd, (1580, 830), 'cambia', 34, FUS, True, 'lm')
        c.page(B[2], B[3], comp)
    if t >= B[3]:
        def av(dd):
            chip(dd, 960, 720, 'la ventana avanza de 1 en 1 segundo', MED, 40, fg=INK, anchor='mm')
            T(dd, (960, 800), 'cada segundo tiene su propia decisión', 36, GRIS, True, 'mm')
        c.show(B[3] + 0.3, av)


S3 = dict(title='Lo que ve la computadora: un clip', draw=s3, beats=[
    B_('Para decidir qué pasa en un segundo, la computadora no mira una sola foto. Mira un pedacito de video.'),
    B_('Toma 16 fotos de una ventana de 4 segundos, alrededor del segundo que quiere decidir.'),
    B_('¿Por qué tantas? Porque en una sola foto no se sabe si el espécimen flota o nada despacio. Para saberlo, hay que ver cómo cambia.'),
    B_('Y la ventana avanza de un segundo en un segundo. Así, cada segundo tiene su propia decisión.'),
])


# =============================================================== ESCENA 4
def s4(c):
    d, t, B = c.d, c.t, c.B
    xs = [470, 730, 990, 1250, 1510]
    cnt = [4, 6, 7, 6, 4]
    ys = [[480 + (j - (n - 1) / 2) * 76 for j in range(n)] for n in cnt]

    def pageA(dd):
        for i in range(4):
            for a in ys[i]:
                for b in ys[i + 1]:
                    ln(dd, (xs[i], a), (xs[i + 1], b), (222, 222, 230), 2)
        wave = (t * 1.1) % 6.5
        for i in range(5):
            lit = max(0.0, 1 - abs(i - wave) / 1.1)
            for y in ys[i]:
                circ(dd, (xs[i], y), 24, fill=mix(WHITE, VIDEO, 0.15 + 0.85 * lit), outline=VIDEO, w=3)
        for k in range(3):
            miniframe(dd, 110 + k * 22, 410 + k * 22, 170, 130, k)
        arrow(dd, (320, 490), (xs[0] - 40, 490), GRIS, 4, 16)
        arrow(dd, (xs[4] + 40, 490), (1700, 490), GRIS, 4, 16)
        T(dd, (1760, 490), 'números', 34, VIDEO, True, 'mm')
        T(dd, (200, 600), 'el clip', 32, GRIS, True, 'mm')
        if t >= B[1]:
            for j, (i, txt) in enumerate([(0, 'bordes y manchas'), (2, 'partes del cuerpo'), (4, 'movimientos')]):
                kk = ez(pr(t, B[1] + 1.0 + j * 3.0, B[1] + 1.5 + j * 3.0))
                if kk > 0:
                    chip(dd, xs[i], 760, txt, VIDEO, 32, anchor='mm')
    c.page(B[0], B[2] + 0.3, pageA)

    # ------- pagina B: las tres ideas
    def pageB(dd):
        T(dd, (960, 232), 'R(2+1)D-18', 100, VIDEO, True, 'mm')
        cards = [(96, '1', '(2+1): forma y cambio'), (700, '2', '18 capas'), (1304, '3', 'Preentrenada')]
        for i, (x0, n, tt) in enumerate(cards):
            kk = ez(pr(t, B[2] + 1.5 + i * 0.7, B[2] + 2.0 + i * 0.7))
            if kk <= 0:
                continue
            caja(dd, (x0, 330, x0 + 520, 860), r=24, outline=VIDEO, w=4)
            circ(dd, (x0 + 46, 380), 26, fill=VIDEO)
            T(dd, (x0 + 46, 380), n, 34, WHITE, True, 'mm')
            T(dd, (x0 + 90, 380), tt, 34, VIDEO, True, 'lm')
        # tarjeta 1
        if t >= B[3]:
            x0 = 96
            sx = 150 + (200 - 60) * (0.5 + 0.5 * math.sin(t * 1.6))
            sy = 440 + (150 - 60) * (0.5 + 0.5 * math.cos(t * 1.1))
            miniframe(dd, 150, 440, 200, 150, 0.6)
            rr(dd, (sx, sy, sx + 60, sy + 60), r=6, outline=MED, w=5)
            TW(dd, 380, 450, '2D: mira la forma de cada foto', 30, INK, 230, True)
            half = (B[3] + B[4]) / 2
            if t >= half:
                for i in range(4):
                    miniframe(dd, x0 + 30 + i * 118, 650, 100, 78, i * 0.9)
                arrow(dd, (x0 + 40, 765), (x0 + 480, 765), FUS, 5, 18)
                T(dd, (x0 + 260, 810), '1D: mira cómo cambia', 30, FUS, True, 'mm')
        # tarjeta 2
        if t >= B[4]:
            x0 = 700
            n = int(18 * pr(t, B[4] + 0.6, B[5] - 1.0)) + (1 if t >= B[4] + 0.6 else 0)
            n = min(n, 18)
            for i in range(n):
                y = 790 - i * 20
                rr(dd, (x0 + 40, y, x0 + 340, y + 15), r=6, fill=mix(VIDEO, WHITE, 0.0 if i % 2 == 0 else 0.35))
            T(dd, (x0 + 430, 560), str(n), 110, VIDEO, True, 'mm')
            T(dd, (x0 + 430, 650), 'capas', 34, GRIS, True, 'mm')
        # tarjeta 3
        if t >= B[5]:
            x0 = 1304
            kinds = [('correr', 'correr'), ('saltar', 'saltar'), ('nadar', 'nadar'), ('bailar', 'bailar')]
            for i, (kd, lb) in enumerate(kinds):
                kk = ez(pr(t, B[5] + 1.0 + i * 1.6, B[5] + 1.5 + i * 1.6))
                if kk <= 0:
                    continue
                x = x0 + 30 + (i % 2) * 240
                y = 420 + (i // 2) * 190
                caja(dd, (x, y, x + 215, y + 170), r=16)
                palito(dd, x + 107, y + 104, 0.85, kd, t)
                T(dd, (x + 107, y + 152), lb, 26, GRIS, True, 'mm')
            T(dd, (x0 + 260, 808), '400 actividades · Kinetics', 28, VIDEO, True, 'mm')
        if t >= B[6]:
            kk = ez(pr(t, B[6], B[6] + 0.8))
            T(dd, (x0 + 260, 836), 'ya sabe de movimiento', 28, FUS, True, 'mm') if False else None
    c.page(B[2], B[7] + 0.3, pageB)

    # ------- pagina C: salida de 512 pistas
    def pageC(dd):
        for k in range(3):
            miniframe(dd, 110 + k * 22, 400 + k * 22, 180, 140, k)
        arrow(dd, (330, 490), (500, 490), GRIS, 5, 18)
        rr(dd, (500, 370, 960, 610), r=26, fill=VIDEO)
        T(dd, (730, 460), 'R(2+1)D-18', 50, WHITE, True, 'mm')
        T(dd, (730, 530), 'la red que mira el clip', 28, mix(VIDEO, WHITE, 0.7), False, 'mm')
        arrow(dd, (960, 490), (1040, 490), GRIS, 5, 18)
        rnd = random.Random(7)
        for i in range(48):
            hgt = 40 + rnd.random() * 230
            hgt *= 0.85 + 0.15 * math.sin(t * 2 + i)
            x = 1070 + i * 15
            dd.rectangle([x, 625 - hgt, x + 10, 625], fill=VIDEO)
        T(dd, (1430, 690), '512 números', 46, VIDEO, True, 'mm')
        T(dd, (1430, 750), '¿qué son? Es lo más importante: lo vemos enseguida', 30, GRIS, True, 'mm')
    c.page(B[7], 1e9, pageC, 0.6, 0)


S4 = dict(title='R(2+1)D-18: la red que mira el video', draw=s4, beats=[
    B_('Ahora, ¿quién mira ese clip? Una red neuronal. Imagínala como una fila de detectores pequeños, puestos capa tras capa.'),
    B_('Los primeros detectan cosas simples, como bordes y manchas. Los siguientes juntan eso para reconocer partes del cuerpo, y después movimientos.'),
    B_('La nuestra se llama R(2+1)D-18. Suena complicado, pero son tres ideas.',
       'La nuestra se llama: erre, dos más uno, de, dieciocho. Suena complicado, pero son tres ideas.'),
    B_('Primera idea: el 2 + 1. Primero mira cada foto sola, para ver la forma: son 2 dimensiones. Después mira cómo cambia de una foto a otra, el tiempo: es 1 dimensión.',
       'Primera idea: el dos más uno. Primero mira cada foto sola, para ver la forma: son dos dimensiones. Después mira cómo cambia de una foto a otra, el tiempo: es una dimensión.'),
    B_('Segunda idea: el 18 es el número de capas que aprenden.', 'Segunda idea: el dieciocho es el número de capas que aprenden.'),
    B_('Tercera idea: viene preentrenada. Antes de conocer a nuestro espécimen, ya vio muchísimos videos de personas haciendo 400 actividades distintas. Esa colección se llama Kinetics.',
       'Tercera idea: viene preentrenada. Antes de conocer a nuestro espécimen, ya vio muchísimos videos de personas haciendo cuatrocientas actividades distintas. Esa colección se llama Kinétics.'),
    B_('Así ya sabe algo de movimiento, como quien ya sabe leer y solo aprende un idioma nuevo.'),
    B_('Al final, la red entrega 512 números. ¿Qué son? Eso es lo más importante, y lo vemos en la siguiente parte.',
       'Al final, la red entrega quinientos doce números. ¿Qué son? Eso es lo más importante, y lo vemos en la siguiente parte.'),
])


# =============================================================== ESCENA 5
ORANGE = hx('e67e22')


def s5(c):
    d, t, B = c.d, c.t, c.B
    rnd = random.Random(3)
    vals = [0.25 + 0.75 * rnd.random() for _ in range(22)]
    act = 'all'
    if t >= B[2]:
        act = 'a'
    if t >= B[3]:
        act = 'b'
    if t >= B[4]:
        act = 'all'
    pa = c.p(0, 0.8)
    caja(d, (96, 185, 560, 800), r=24, fill=WHITE)
    for i in range(0, 22):
        y = 208 + i * 26
        col = MED if i < 15 else ORANGE
        on = act == 'all' or (act == 'a' and i < 15) or (act == 'b' and i >= 15)
        col = col if on else GRIS_C
        v = vals[i] * (0.9 + 0.1 * math.sin(t * 2 + i))
        rr(d, (120, y, 120 + 400, y + 22), r=8, fill=(238, 238, 242))
        rr(d, (120, y, 120 + int(400 * v * pa), y + 22), r=8, fill=col)
    T(d, (328, 815), 'libreta de 22 medidas', 32, INK, True, 'mm')
    if t >= B[1] and t < B[2] + 0.4:
        def reg(dd):
            rr(dd, (680, 300, 1700, 380), r=14, fill=hx('f7e3a1'), outline=INK, w=4)
            for i in range(21):
                x = 700 + i * 48
                ln(dd, (x, 300), (x, 330 if i % 5 else 350), INK, 3)
            T(dd, (1190, 270), 'regla', 32, GRIS, True, 'mm')
            circ(dd, (1190, 560), 110, fill=WHITE, outline=INK, w=6)
            circ(dd, (1190, 560), 8, fill=INK)
            a = t * 3
            ln(dd, (1190, 560), (1190 + 90 * math.sin(a), 560 - 90 * math.cos(a)), QUIETO, 6)
            rr(dd, (1170, 425, 1210, 445), r=6, fill=INK)
            T(dd, (1190, 700), 'cronómetro', 32, GRIS, True, 'mm')
        c.page(B[1], B[2], reg)
    if t >= B[2]:
        def A(dd):
            tiles = [(640, 'Movimiento', 'cuánto se mueve el cuerpo'), (1050, 'Postura', 'qué tan vertical está'), (1460, 'Trayectoria', 'qué camino recorre')]
            for i, (x0, tt, sub) in enumerate(tiles):
                kk = ez(pr(t, B[2] + 1.0 + i * 3.2, B[2] + 1.6 + i * 3.2))
                if kk <= 0:
                    continue
                caja(dd, (x0, 215, x0 + 380, 600), r=22, outline=MED, w=4)
                T(dd, (x0 + 190, 252), tt, 38, hx('a97c10'), True, 'mm')
                T(dd, (x0 + 190, 296), sub, 26, GRIS, False, 'mm')
                cx, cy = x0 + 190, 450
                if i == 0:
                    for j in range(3):
                        pts = [(cx - 130 + k * 13, cy - 30 + j * 30 + 14 * math.sin(t * 5 + k * 0.7 + j)) for k in range(21)]
                        dd.line(pts, fill=MED, width=6, joint='curve')
                elif i == 1:
                    a = 0.65 * math.sin(t * 1.5)
                    ln(dd, (cx, cy - 90), (cx, cy + 90), GRIS, 3)
                    ln(dd, (cx - 3, cy + 90), (cx + 150 * math.sin(a) * 0.6 - 3, cy + 90 - 180 * math.cos(a)), INK, 10)
                    circ(dd, (cx + 150 * math.sin(a) * 0.6, cy - 90 + 180 * (1 - math.cos(a)) * 0.0), 18, fill=MED, outline=INK, w=3)
                else:
                    circ(dd, (cx, cy), 100, outline=INK, w=5)
                    pts = []
                    n = int(60 * min(1.0, ((t * 0.25) % 1.4)))
                    for k in range(max(2, n)):
                        a = k * 0.2
                        pts.append((cx + (60 * math.sin(a * 0.8 + 1) + 20 * math.sin(a * 2.3)) * 1.0, cy + 60 * math.cos(a * 0.9) * 0.9))
                    dd.line(pts, fill=MED, width=6, joint='curve')
            T(dd, (1050, 650), '15 rasgos', 56, hx('a97c10'), True, 'mm')
        c.page(B[2], B[3], A)
    if t >= B[3]:
        def Bz(dd):
            cx, top, w, h = 900, 185, 300, 640
            x0, x1, y0, y1, yw = cilindro(dd, cx, top, w, h)
            yb = yw + 150
            rata(dd, cx, yb, 1.5, (0, -1), t, 'quieto')
            rr(dd, (cx - 140, yw - 78, cx + 140, yw + 6), r=10, outline=TREPA, w=5)
            rr(dd, (cx - 70, yb - 105, cx + 70, yb), r=10, outline=NADO, w=5)
            rr(dd, (cx - 70, yb, cx + 70, yb + 105), r=10, outline=ORANGE, w=5)
            items = [(yw - 36, TREPA, 'nariz', 'se mueve justo arriba de la línea del agua', (cx + 140, yw - 36)),
                     (yb - 52, NADO, 'patas de adelante', 'mitad alta del cuerpo bajo el agua', (cx + 70, yb - 52)),
                     (yb + 52, ORANGE, 'patas de atrás', 'mitad baja del cuerpo bajo el agua', (cx + 70, yb + 52))]
            for y, col, a, b, pt in items:
                ln(dd, pt, (1130, y), col, 4)
                chip(dd, 1140, y - 24, a, col, 30, anchor='la')
                T(dd, (1146, y + 24), b, 26, GRIS, False, 'la')
            T(dd, (1500, 230), '7 reglas', 56, ORANGE, True, 'mm')
        c.page(B[3], B[4], Bz)
    if t >= B[4]:
        def Cz(dd):
            for cx, top, w, h, s, off, nm in [(900, 200, 300, 520, 1.15, 10, 'cerca'), (1450, 330, 170, 300, 0.65, 8, 'lejos')]:
                x0, x1, y0, y1, yw = cilindro(dd, cx, top, w, h)
                yb = yw + 0.3 * h
                xs = cx + off
                rata(dd, xs, yb, s, (1, -0.05), 0.0, 'nado')
                xa, xb = xs - 60 * s, xs + 100 * s
                ya = yb + 52 * s
                ln(dd, (xa, ya), (xb, ya), NADO, 5)
                ln(dd, (xa, ya - 10), (xa, ya + 10), NADO, 5)
                ln(dd, (xb, ya - 10), (xb, ya + 10), NADO, 5)
                T(dd, ((xa + xb) / 2, ya + 30), '1 largo de cuerpo' if s > 1 else '1 largo', 24 if s > 1 else 22, NADO, True, 'mm')
                T(dd, (cx, y1 + 28), nm, 30, GRIS, True, 'mm')
            chip(dd, 1175, 805, 'Mismo espécimen, mismas medidas: cerca o lejos', FUS, 32, anchor='mm')
        c.page(B[4], B[5], Cz)

    def contraste(dd):
        mid = (B[5] + B[6]) / 2
        tarjetas = [(190, 'Pistas de la red de video: 512', VIDEO, ['las descubrió la red sola', 'no tienen nombre', 'miran todo el clip'], B[5] + 0.6),
                    (520, 'Medidas: 22', hx('a97c10'), ['las diseñamos nosotros', 'cada una tiene nombre', 'miden solo el cuerpo del espécimen'], mid)]
        for y, tt, col, items, ta in tarjetas:
            k = ez(pr(t, ta, ta + 0.6))
            if k <= 0:
                continue
            caja(dd, (640, y, 1830, y + 290), r=24, outline=col, w=5)
            T(dd, (680, y + 22), tt, 42, col, True)
            for i, s_ in enumerate(items):
                circ(dd, (700, y + 112 + i * 56), 9, fill=col)
                T(dd, (730, y + 112 + i * 56), s_, 34, INK, False, 'lm')
    c.page(B[5], 1e9, contraste, 0.6, 0)


S5 = dict(title='Las medidas: la libreta del detective', draw=s5, beats=[
    B_('Pero la red de video no está sola. Hay una segunda fuente de pistas, que funciona muy distinto: las medidas.'),
    B_('Son 22 números que se calculan con reglas, como si midiéramos con una regla y un cronómetro.',
       'Son veintidós números que se calculan con reglas, como si midiéramos con una regla y un cronómetro.'),
    B_('Quince son rasgos del espécimen: cuánto se mueve su cuerpo, qué tan vertical está, y qué camino recorre.'),
    B_('Siete son reglas de observación: cuánto patalea con las patas de atrás y con las de adelante, y si se mueve la nariz justo arriba de la línea del agua. Un movimiento brusco de nariz apunta a trepar.'),
    B_('Las distancias se miden en largos de cuerpo, no en píxeles. Así, un video grabado más cerca o más lejos da números comparables.'),
    B_('Fíjate en la diferencia. Las pistas de la red las descubrió la red sola y no tienen nombre. Las medidas las diseñamos nosotros: cada una tiene nombre y mide solo el cuerpo del espécimen.'),
])
