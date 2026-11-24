"""Escenas 6 a 11 del video del clasificador."""
import math
import random
from vid_lib import *
from scenes_a import B_, ORANGE


# =============================================================== ESCENA 6: LA FUSION
P_TOP = [(800, 330), (1000, 330), (1000, 452)]
P_BOT = [(1080, 650), (1337, 650), (1337, 518)]
CT_X, CT_Y, CT_W, CT_H = 960, 455, 400, 60


def concat_bar(dd, t, dropout=False):
    n_v, n_m = 64, 8
    rnd = random.Random(int(t * 3) if dropout else 1)
    for i in range(n_v + n_m):
        x = CT_X + i * (CT_W / (n_v + n_m))
        col = VIDEO if i < n_v else MED
        if dropout and rnd.random() < 0.30:
            col = (205, 205, 212)
        dd.rectangle([x, CT_Y, x + CT_W / (n_v + n_m) - 1.2, CT_Y + CT_H], fill=col)


def s6(c):
    d, t, B = c.d, c.t, c.B

    def banner(dd):
        chip(dd, 500, 380, 'lo que VE el video', VIDEO, 40, anchor='mm')
        chip(dd, 1420, 380, 'lo que dicen las MEDIDAS', MED, 40, fg=INK, anchor='mm')
        arrow(dd, (500, 430), (880, 560), GRIS, 7, 28)
        arrow(dd, (1420, 430), (1040, 560), GRIS, 7, 28)
        rr(dd, (700, 560, 1220, 690), r=40, fill=FUS)
        T(dd, (960, 625), 'FUSIÓN = JUNTAR', 56, WHITE, True, 'mm')
    c.page(B[0] + 0.5, B[1] + 0.2, banner)

    def top(dd):
        for k in range(3):
            miniframe(dd, 90 + k * 14, 270 + k * 14, 140, 110, k)
        arrow(dd, (250, 330), (330, 330), GRIS, 5, 18)
        rr(dd, (330, 270, 690, 390), r=22, fill=VIDEO)
        T(dd, (510, 316), 'R(2+1)D-18', 46, WHITE, True, 'mm')
        T(dd, (510, 360), 'mira el video', 26, mix(VIDEO, WHITE, 0.75), False, 'mm')
        arrow(dd, (690, 330), (760, 330), GRIS, 5, 18)
        for i in range(16):
            dd.rectangle([760, 250 + i * 10, 800, 258 + i * 10], fill=mix(VIDEO, WHITE, 0.0 if i % 2 == 0 else 0.25))
        T(dd, (780, 436), '512 pistas', 32, VIDEO, True, 'mm')
        T(dd, (780, 470), 'del video', 24, GRIS, False, 'mm')
    c.show(B[1] + 0.5, top)

    def bot(dd):
        rnd = random.Random(5)
        holes = {4, 11, 17}
        for i in range(22):
            y = 562 + i * 8
            if i in holes:
                dd.rectangle([90, y, 90 + 160, y + 6], outline=GRIS, width=1)
            else:
                dd.rectangle([90, y, 90 + int(160 * (0.15 + 0.85 * rnd.random() ** 2)), y + 6], fill=MED)
        T(dd, (170, 768), '22 medidas', 30, hx('a97c10'), True, 'mm')
        arrow(dd, (262, 650), (292, 650), GRIS, 4, 14)
        caja(dd, (296, 592, 520, 708), r=16, fill=WHITE, outline=MED, w=4)
        T(dd, (408, 622), 'limpiar', 34, INK, True, 'mm')
        T(dd, (408, 660), 'huecos: valor típico', 22, GRIS, False, 'mm')
        T(dd, (408, 686), 'misma escala', 22, GRIS, False, 'mm')
        arrow(dd, (522, 650), (552, 650), GRIS, 4, 14)
        for i in range(22):
            y = 562 + i * 8
            dd.rectangle([556, y, 556 + 90, y + 6], fill=mix(MED, WHITE, 0.0 if i % 2 == 0 else 0.2))
        T(dd, (601, 768), 'listas', 30, hx('a97c10'), True, 'mm')
    c.show(B[2] + 0.5, bot)

    def red(dd):
        arrow(dd, (660, 650), (720, 650), GRIS, 4, 14)
        cols = [(760, 6), (860, 5), (960, 5)]
        pos = [[(x, 650 + (j - (n - 1) / 2) * 30) for j in range(n)] for x, n in cols]
        for a, b in zip(pos[:-1], pos[1:]):
            for p in a:
                for q in b:
                    ln(dd, p, q, (225, 215, 190), 1)
        for col in pos:
            for p in col:
                circ(dd, p, 10, fill=MED, outline=INK, w=2)
        T(dd, (860, 768), '22 → 64 → 64', 28, INK, True, 'mm')
        T(dd, (860, 528), 'red pequeña', 28, GRIS, True, 'mm')
        arrow(dd, (980, 650), (1030, 650), GRIS, 4, 14)
        for i in range(14):
            dd.rectangle([1040, 580 + i * 10, 1080, 588 + i * 10], fill=mix(MED, WHITE, 0.0 if i % 2 == 0 else 0.25))
        T(dd, (1060, 768), '64 pistas', 28, hx('a97c10'), True, 'mm')
    c.show(B[3] + 0.5, red)

    def cat(dd):
        poly_arrow(dd, P_TOP, VIDEO, 5, 20)
        poly_arrow(dd, P_BOT, MED, 5, 20)
        concat_bar(dd, t, dropout=(t >= B[5]))
        rr(dd, (CT_X - 4, CT_Y - 4, CT_X + CT_W + 4, CT_Y + CT_H + 4), r=8, outline=FUS, w=4)
        T(dd, (CT_X + 190, CT_Y + CT_H + 40), '512 + 64 = 576 pistas', 34, FUS, True, 'mm')
        pulses(dd, P_TOP, t, VIDEO)
        pulses(dd, P_BOT, t, MED)
    c.show(B[4], cat)

    if t >= B[5]:
        def dr(dd):
            T(dd, (1010, 424), 'apagado al azar (dropout)', 24, QUIETO, True, 'lm')
        c.show(B[5], dr)

    def fin(dd):
        arrow(dd, (1364, 485), (1408, 485), GRIS, 5, 18)
        rr(dd, (1408, 420, 1550, 550), r=18, fill=FUS)
        T(dd, (1479, 462), 'capa final', 24, WHITE, True, 'mm')
        T(dd, (1479, 500), '576 → 3', 26, WHITE, True, 'mm')
        arrow(dd, (1552, 485), (1600, 485), GRIS, 5, 18)
        probs = [0.72, 0.20, 0.08]
        names = ['nado', 'quieto', 'trepa']
        cols = [NADO, QUIETO, TREPA]
        g = ez(pr(t, B[6] + 0.8, B[6] + 2.2))
        for i in range(3):
            x = 1620 + i * 90
            hh = 150 * probs[i] / 0.72 * g
            dd.rectangle([x, 570 - hh, x + 62, 570], fill=cols[i])
            T(dd, (x + 31, 580), names[i], 24, INK, True, 'mt')
            if g > 0.9:
                T(dd, (x + 31, 566 - hh - 24), '%d %%' % round(probs[i] * 100), 26, cols[i], True, 'mm')
        T(dd, (1730, 640), '3 probabilidades', 28, GRIS, True, 'mm')
        T(dd, (1730, 672), 'suman 1 (100 %)', 24, GRIS, False, 'mm')
    c.show(B[6], fin)

    if t >= B[7]:
        c.show(B[7], lambda dd: chip(dd, 960, 815, 'decide con lo que VE y con lo que MIDIÓ', FUS, 40, anchor='mm'))


S6 = dict(title='La fusión: dos fuentes de pistas se juntan', draw=s6, beats=[
    B_('Ahora viene la parte más importante: la fusión. Fusionar es juntar. Vamos a juntar lo que ve la red de video con lo que dicen las medidas.'),
    B_('Imagina dos detectives. El primero mira el video y entrega 512 pistas.', 'Imagina dos detectives. El primero mira el video y entrega quinientas doce pistas.'),
    B_('El segundo lee la libreta de 22 medidas. Antes se limpia: si falta una medida, se rellena con un valor típico, y todas se ponen en la misma escala.',
       'El segundo lee la libreta de veintidós medidas. Antes se limpia: si falta una medida, se rellena con un valor típico, y todas se ponen en la misma escala.'),
    B_('Luego una red pequeña, de dos capas, resume esos 22 números en 64 pistas.', 'Luego una red pequeña, de dos capas, resume esos veintidós números en sesenta y cuatro pistas.'),
    B_('Ahora se pegan las dos listas: 512 más 64 son 576 pistas juntas.', 'Ahora se pegan las dos listas: quinientas doce más sesenta y cuatro son quinientas setenta y seis pistas juntas.'),
    B_('Mientras entrena, se apagan al azar algunas pistas, a propósito. Se llama dropout, y evita que la red dependa de una sola pista.',
       'Mientras entrena, se apagan al azar algunas pistas, a propósito. Se llama drop aut, y evita que la red dependa de una sola pista.'),
    B_('La capa final lee las 576 pistas y reparte un puntaje entre tres opciones: escalamiento, inmovilidad y nado. Los puntajes suman uno.',
       'La capa final lee las quinientas setenta y seis pistas y reparte un puntaje entre tres opciones: escalamiento, inmovilidad y nado. Los puntajes suman uno.'),
    B_('Lo importante: la red decide con las dos fuentes, lo que vio y lo que midió. Si el video confunde, las medidas ayudan, y al revés.'),
])


# =============================================================== ESCENA 7: EL CICLO
CODE = ['for xb, yb in dl:',
        '    opt.zero_grad()',
        '    perd = crit(adelante(m, xb, dev), yb)',
        '    scaler.scale(perd).backward()',
        '    scaler.step(opt)']
BOX = {1: (110, 200), 2: (580, 200), 3: (580, 410), 4: (110, 410)}
BTXT = {1: 'Un lote de\n16 clips', 2: 'La red\nadivina', 3: 'Compara con la\netiqueta: el error', 4: 'Mueve un poquito\nlas perillas'}
BCOL = {1: VIDEO, 2: NADO, 3: QUIETO, 4: TREPA}


def s7(c):
    d, t, B = c.d, c.t, c.B
    step = 0
    if t >= B[2]:
        step = 1
    if t >= B[3]:
        step = 2
    if t >= B[4]:
        step = 3
    if t >= B[5]:
        step = 4
    if t >= B[6] + 1.0:
        step = int(((t - B[6] - 1.0) * 0.45) % 4) + 1
    # perillas
    pa = c.p(0, 0.8)
    T(d, (445, 596), 'perillas (los pesos): millones', 30, GRIS, True, 'mm')
    rot = ez(pr(t, B[5] + 1, B[5] + 5)) * 40
    if t >= B[6]:
        rot += 14 * math.sin(t * 1.3)
    rnd = random.Random(11)
    for i in range(8):
        cx, cy = 190 + (i % 4) * 190, 680 + (i // 4) * 120
        base = rnd.uniform(-180, 180)
        knob(d, cx, cy, 34 * pa, base + (rot if i % 2 else -rot), INK)
    # ciclo
    if t >= B[1]:
        kk = ez(pr(t, B[1], B[1] + 0.8))
        for n in (1, 2, 3, 4):
            x, y = BOX[n]
            on = step == n
            rr(d, (x, y, x + 400, y + 130), r=22, fill=mix(WHITE, BCOL[n], 0.18) if on else WHITE, outline=BCOL[n] if (on or kk > 0.9) else LINEA, w=6 if on else 3)
            circ(d, (x + 48, y + 65), 28, fill=BCOL[n])
            T(d, (x + 48, y + 65), str(n), 34, WHITE, True, 'mm')
            TW(d, x + 96, y + 32, BTXT[n], 30, INK, 290, True, 1.2)
        for a, b in [((510, 265), (580, 265)), ((780, 330), (780, 410)), ((580, 475), (510, 475)), ((310, 410), (310, 330))]:
            arrow(d, a, b, GRIS, 5, 18)
        if step:
            x, y = BOX[step]
            miniframe(d, x + 330, y - 14, 64, 50, step * 0.7)
    # codigo
    if t >= B[1]:
        caja(d, (1040, 190, 1830, 478), r=18, fill=hx('fbfbfc'))
        T(d, (1064, 200), 'fst_cnn.py  →  entrenar()', 26, GRIS, True)
        hl = {1: [0], 2: [2], 3: [2], 4: [3, 4]}.get(step, [])
        for i, l in enumerate(CODE):
            y = 246 + i * 44
            if i in hl:
                rr(d, (1052, y - 4, 1818, y + 38), r=8, fill=mix(WHITE, BCOL[step], 0.22))
            d.text((1110, y), l, font=MO(28), fill=INK)
            if i in hl:
                circ(d, (1080, y + 17), 15, fill=BCOL[step])
                T(d, (1080, y + 17), str(step), 22, WHITE, True, 'mm')
    # predicciones
    if t >= B[3]:
        def pred(dd):
            caja(dd, (1040, 510, 1830, 870), r=18)
            names = ['nado', 'quieto', 'trepa']
            cols = [NADO, QUIETO, TREPA]
            ad = [0.40, 0.35, 0.25]
            if t >= B[5]:
                k = ez(pr(t, B[5] + 1.5, B[5] + 4.5))
                ad = [lerp(0.40, 0.55, k), lerp(0.35, 0.28, k), lerp(0.25, 0.17, k)]
            T(dd, (1180, 536), 'adivinó', 30, INK, True, 'mm')
            T(dd, (1620, 536), 'respuesta del equipo', 30, INK, True, 'mm')
            for i in range(3):
                xa = 1070 + i * 80
                hh = 170 * ad[i]
                dd.rectangle([xa, 760 - hh, xa + 56, 760], fill=cols[i])
                T(dd, (xa + 28, 768), names[i], 22, GRIS, True, 'mt')
                xb = 1510 + i * 80
                one = 170 if i == 0 else 4
                dd.rectangle([xb, 760 - one, xb + 56, 760], fill=cols[i])
                T(dd, (xb + 28, 768), names[i], 22, GRIS, True, 'mt')
            if t >= B[4]:
                err = 'error grande' if t < B[5] + 3 else 'error más chico'
                chip(dd, 1435, 826, err, QUIETO if t < B[5] + 3 else TREPA, 28, anchor='mm')
            T(dd, (1418, 640), '≠', 60, GRIS, True, 'mm')
        c.show(B[3], pred)
    if t >= B[6]:
        c.show(B[6], lambda dd: T(dd, (530, 840), 'y se repite con el siguiente lote', 34, FUS, True, 'mm'))
    if t >= B[3]:
        T(d, (1818, 850), 'ejemplo ilustrativo', 20, GRIS, False, 'rs')


S7 = dict(title='Cómo aprende: el ciclo de entrenamiento', draw=s7, beats=[
    B_('Al empezar, la red no sabe nada. Tiene millones de perillas, llamadas pesos, puestas en cualquier posición.'),
    B_('Entrenar es girar esas perillas poco a poco. Se hace con un ciclo de cuatro pasos.'),
    B_('Uno: la red recibe un lote de 16 clips, cada uno con sus medidas.', 'Uno: la red recibe un lote de dieciséis clips, cada uno con sus medidas.'),
    B_('Dos: adivina. Para cada clip da sus tres probabilidades.'),
    B_('Tres: compara con la etiqueta, que es la respuesta del equipo. La diferencia es el error, que en el código se llama pérdida.'),
    B_('Cuatro: hacia atrás, calcula qué perillas tuvieron la culpa y mueve cada una un poquito para equivocarse menos.'),
    B_('Y se repite con el siguiente lote, una y otra vez.'),
])


# =============================================================== ESCENA 8: LAS EPOCAS
def Lf(e):
    return 0.55 + 0.55 * math.exp(-e / 3.5)


def lrf(u):
    if u < 0.3:
        return 0.04 + 0.96 * (1 - math.cos(math.pi * u / 0.3)) / 2
    return 0.0001 + 0.9999 * (1 + math.cos(math.pi * (u - 0.3) / 0.7)) / 2


def s8(c):
    d, t, B = c.d, c.t, c.B
    ef = 15 * pr(t, B[1] + 0.5, B[4] - 0.5)
    if t < B[1]:
        ef = 0.0
    # mazo de clips
    if t < B[1]:
        f = pr(t, B[0] + 1.2, B[1] - 1.5)
        num = 1
        lleno = int(40 * f)
    else:
        f = ef - int(ef) if ef < 15 else 1.0
        num = min(15, int(ef) + 1)
        lleno = int(40 * f) if ef < 15 else 40
    T(d, (110, 172), 'Época %d de 15' % num, 44, INK, True)
    for r in range(5):
        for k in range(8):
            i = r * 8 + k
            x, y = 110 + k * 58, 240 + r * 70
            rr(d, (x, y, x + 50, y + 60), r=8, fill=mix(WHITE, FUS, 0.65) if i < lleno else WHITE, outline=LINEA if i >= lleno else FUS, w=3)
    T(d, (342, 612), 'los clips de entrenamiento', 26, GRIS, True, 'mm')
    if t >= B[1]:
        k1 = c.p(1, 0.8)
        x0, yb, w, h = 720, 550, 520, 290
        T(d, (x0, 205), 'error  ↑', 28, QUIETO, True)
        ln(d, (x0, yb), (x0 + w, yb), INK, 4)
        ln(d, (x0, yb), (x0, yb - h - 10), INK, 4)
        for e in (0, 5, 10, 15):
            T(d, (x0 + e / 15 * w, yb + 8), str(e), 22, GRIS, False, 'mt')
        T(d, (x0 + w / 2, yb + 40), 'épocas', 28, GRIS, True, 'mm')
        n = max(2, int(80 * min(ef, 15) / 15))
        pts = [(x0 + (e / 15) * w, yb - (Lf(e) - 0.5) / 0.7 * h) for e in [min(ef, 15) * i / (n - 1) for i in range(n)]]
        d.line(pts, fill=QUIETO, width=6, joint='curve')
        circ(d, pts[-1], 11, fill=QUIETO, outline=WHITE, w=3)
        T(d, (x0 + w, 220), 'ilustración', 22, GRIS, False, 'ra')
        # barras de un clip real
        pn = 0.36 + 0.50 * (1 - math.exp(-min(ef, 15) / 4))
        pq = (1 - pn) * 0.62
        ps = [pn, pq, 1 - pn - pq]
        T(d, (1570, 205), 'Un clip que es de nado:', 30, NADO, True, 'mm')
        for i, (nm, col) in enumerate([('nado', NADO), ('quieto', QUIETO), ('trepa', TREPA)]):
            x = 1350 + i * 150
            hh = 260 * ps[i]
            d.rectangle([x, 540 - hh, x + 90, 540], fill=col)
            T(d, (x + 45, 548), nm, 26, INK, True, 'mt')
            T(d, (x + 45, 536 - hh - 22), '%d %%' % round(ps[i] * 100), 28, col, True, 'mm')
    # zona de abajo
    def aug(dd):
        T(dd, (110, 640), 'Entre una época y otra, los clips cambian un poco:', 30, GRIS, True)
        var = [('original', 1.0, False, 0), ('más brillo', 1.25, False, 0), ('más oscuro', 0.7, False, 0), ('volteado', 1.0, True, 0), ('movido', 1.0, False, 40)]
        for i, (nm, br, fl, sh) in enumerate(var):
            x = 110 + i * 345
            miniframe(dd, x, 690, 300, 130, 0.6 if not fl else 0.6, bright=br, flip=fl, shift=sh)
            T(dd, (x + 150, 840), nm, 28, INK, True, 'mm')
    c.page(B[4], B[5], aug)

    def lrp(dd):
        T(dd, (110, 636), 'Tamaño del paso en cada momento del entrenamiento', 30, GRIS, True)
        x0, yb, w, h = 140, 826, 800, 105
        ln(dd, (x0, yb), (x0 + w, yb), INK, 3)
        ln(dd, (x0, yb), (x0, yb - h - 10), INK, 3)
        pts = [(x0 + u * w, yb - lrf(u) * h) for u in [i / 80 for i in range(81)]]
        dd.line(pts, fill=MED, width=6, joint='curve')
        u = pr(t, B[5] + 0.6, B[6] - 0.6)
        circ(dd, (x0 + u * w, yb - lrf(u) * h), 12, fill=QUIETO, outline=WHITE, w=3)
        T(dd, (x0 + 10, yb + 8), 'empieza chico', 26, GRIS, True, 'la')
        T(dd, (x0 + 0.30 * w, yb - h - 24), 'crece', 26, GRIS, True, 'mm')
        T(dd, (x0 + w, yb + 8), 'al final, muy chico para afinar', 26, GRIS, True, 'ra')
    c.page(B[5], B[6], lrp)

    def x10(dd):
        T(dd, (110, 636), 'Cada parte aprende a su propio ritmo', 30, GRIS, True)
        T(dd, (110, 684), 'red preentrenada (ya sabe)', 28, VIDEO, True)
        rr(dd, (110, 724, 110 + 110, 758), r=10, fill=VIDEO)
        T(dd, (240, 741), '× 1', 34, VIDEO, True, 'lm')
        T(dd, (110, 772), 'piezas nuevas (empiezan de cero)', 28, hx('a97c10'), True)
        k = ez(pr(t, B[6] + 1.0, B[6] + 2.5))
        rr(dd, (110, 812, 110 + 110 + 1000 * k, 846), r=10, fill=MED)
        T(dd, (240 + 1000 * k, 829), '× 10', 34, hx('a97c10'), True, 'lm') if k > 0.9 else None
    c.page(B[6], B[7], x10)

    def pesos(dd):
        T(dd, (110, 640), 'Los ejemplos raros pesan un poco más en el error', 30, GRIS, True)
        fr = [('nado', 3819, NADO), ('quieto', 2924, QUIETO), ('trepa', 1244, TREPA)]
        tot = sum(f for _, f, _ in fr)
        ws = [math.sqrt(tot / (3 * f)) for _, f, _ in fr]
        mw = sum(ws) / 3
        ws = [w / mw for w in ws]
        T(dd, (320, 690), 'ejemplos', 26, GRIS, True)
        T(dd, (1040, 690), 'peso en el error', 26, GRIS, True)
        for i, ((nm, f, col), w) in enumerate(zip(fr, ws)):
            y = 725 + i * 48
            T(dd, (110, y + 18), nm, 28, col, True, 'lm')
            rr(dd, (320, y, 320 + f / 3819 * 600, y + 38), r=8, fill=col)
            T(dd, (320 + f / 3819 * 600 + 12, y + 19), '{:,}'.format(f).replace(',', ' '), 26, GRIS, True, 'lm')
            rr(dd, (1040, y, 1040 + w * 420, y + 38), r=8, fill=mix(col, INK, 0.25))
            T(dd, (1040 + w * 420 + 12, y + 19), '%.2f' % w, 26, GRIS, True, 'lm')
    c.page(B[7], 1e9, pesos, 0.6, 0)


S8 = dict(title='Las épocas: repasar muchas veces', draw=s8, beats=[
    B_('Cuando la red ya vio todos los clips de entrenamiento una vez, se completó una época. Es como leer el libro entero una vez.'),
    B_('Una lectura no basta. Nuestra red hace 15 épocas: repasa los mismos ejemplos 15 veces, y cada vez se equivoca un poco menos.',
       'Una lectura no basta. Nuestra red hace quince épocas: repasa los mismos ejemplos quince veces, y cada vez se equivoca un poco menos.'),
    B_('En esta gráfica, que es una ilustración, abajo están las épocas y arriba el error. Empieza alto y baja con cada repaso.'),
    B_('Y mira la respuesta para un mismo clip que de verdad es de nado: en la primera época duda, y en la última está mucho más segura.'),
    B_('Entre una época y otra los clips cambian un poco: más brillo, más oscuros, volteados o movidos. Así la red no se aprende de memoria un video.'),
    B_('También cambia el tamaño del paso: empieza chico, crece, y al final vuelve a ser muy chico para afinar.'),
    B_('Y las piezas nuevas aprenden diez veces más rápido que la red preentrenada, porque ellas empiezan de cero.'),
    B_('Además, como hay más segundos de nado que de escalamiento, se da un poco más de peso a los ejemplos raros, para que no se olviden.'),
])


# =============================================================== ESCENA 9: EL EXAMEN
FOLDS = [[0, 1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]


def s9(c):
    d, t, B = c.d, c.t, c.B

    def A(dd):
        caja(dd, (110, 200, 920, 740), r=24, outline=QUIETO, w=4)
        T(dd, (515, 245), 'Examen injusto', 48, QUIETO, True, 'mm')
        T(dd, (150, 310), 'En clase:', 32, GRIS, True)
        caja(dd, (150, 360, 450, 460), r=16)
        T(dd, (300, 410), '7 × 8 = 56', 44, INK, True, 'mm')
        T(dd, (150, 500), 'En el examen:', 32, GRIS, True)
        caja(dd, (150, 550, 450, 650), r=16)
        T(dd, (300, 600), '7 × 8 = ?', 44, INK, True, 'mm')
        T(dd, (680, 600), '¡ya la había visto!', 32, QUIETO, True, 'mm')
        cruz(dd, 680, 410, 150, QUIETO, 16)
        caja(dd, (1000, 200, 1810, 740), r=24, outline=TREPA, w=4)
        T(dd, (1405, 245), 'Examen justo', 48, TREPA, True, 'mm')
        T(dd, (1040, 310), 'En clase:', 32, GRIS, True)
        caja(dd, (1040, 360, 1340, 460), r=16)
        T(dd, (1190, 410), '7 × 8 = 56', 44, INK, True, 'mm')
        T(dd, (1040, 500), 'En el examen:', 32, GRIS, True)
        caja(dd, (1040, 550, 1340, 650), r=16)
        T(dd, (1190, 600), '6 × 9 = ?', 44, INK, True, 'mm')
        T(dd, (1580, 600), '¡una pregunta nueva!', 32, TREPA, True, 'mm')
        tick(dd, 1580, 410, 150, TREPA, 16)
    c.page(B[0], B[1], A)

    def Bp(dd):
        for j in range(11):
            T(dd, (230 + j * 127 + 56, 222), 'video %d' % (j + 1), 22, GRIS, True, 'mm')
        for r in range(5):
            tr = B[1] + 0.8 + r * 3.4
            kk = ez(pr(t, tr, tr + 0.6))
            if kk <= 0:
                continue
            y = 250 + r * 95
            T(dd, (96, y + 39), 'parte %d' % (r + 1), 28, INK, True, 'lm')
            for j in range(11):
                x = 230 + j * 127
                te = j in FOLDS[r]
                rr(dd, (x, y, x + 112, y + 78), r=12, fill=mix(WHITE, ORANGE, 0.55) if te else mix(WHITE, VIDEO, 0.30), outline=ORANGE if te else LINEA, w=5 if te else 2)
                T(dd, (x + 56, y + 39), 'examen' if te else 'entrena', 22, INK if te else GRIS, True, 'mm')
        chip(dd, 560, 770, 'entrena con los demás videos', VIDEO, 30, anchor='mm')
        chip(dd, 1260, 770, 'examen: videos que nunca vio', ORANGE, 30, anchor='mm')
    c.page(B[1], B[2], Bp)

    def C(dd):
        xs = lambda u: 200 + u * 140
        for i in range(10):
            rr(dd, (xs(i), 260, xs(i) + 124, 330), r=12, fill=WHITE, outline=LINEA, w=3)
            T(dd, (xs(i) + 62, 295), str(i + 1), 34, INK, True, 'mm')
        T(dd, (200, 214), 'segundos de un mismo video', 28, GRIS, True)
        rr(dd, (xs(2), 396, xs(2) + 3 * 140 + 124 + 16, 436), r=10, fill=NADO)
        rr(dd, (xs(3), 446, xs(3) + 3 * 140 + 124 + 16, 486), r=10, fill=TREPA)
        T(dd, (xs(2) - 14, 416), 'clip A', 28, NADO, True, 'rm')
        T(dd, (xs(3) - 14, 466), 'clip B', 28, TREPA, True, 'rm')
        rr(dd, (xs(3), 386, xs(2) + 3 * 140 + 140, 496), r=8, outline=ORANGE, w=5)
        T(dd, (960, 560), 'el 75 % del clip A está también en el clip B', 38, ORANGE, True, 'mm')
        T(dd, (960, 650), 'Sería como poner la misma pregunta con otra letra.', 42, INK, True, 'mm')
        T(dd, (960, 720), 'Por eso la prueba se hace por video, no por segundo.', 36, GRIS, True, 'mm')
    c.page(B[2], B[3], C)

    def D(dd):
        x0 = 380
        T(dd, (x0, 200), 'Segundos que acierta (de cada 100)', 34, GRIS, True)
        for pct, y, nm, col in [(47.8, 312, 'Contestar siempre «nado»', GRIS), (71.6, 430, 'Nuestra red', FUS)]:
            k = ez(pr(t, B[3] + 1.0, B[3] + 3.0))
            T(dd, (x0, y - 8), nm, 34, INK, True, 'lb')
            rr(dd, (x0, y, x0 + 1000 * pct / 100 * k, y + 70), r=12, fill=col)
            if k > 0.95:
                T(dd, (x0 + 1000 * pct / 100 + 18, y + 35), '%.1f %%' % pct, 40, col if col != GRIS else GRIS, True, 'lm')
        T(dd, (960, 570), 'De cada 10 segundos…', 36, GRIS, True, 'mm')
        k = pr(t, B[3] + 3.5, B[3] + 6.0)
        for i in range(10):
            if i / 10 > k:
                break
            ok = i < 7
            cx = 340 + i * 138
            circ(dd, (cx, 690), 52, fill=TREPA if ok else QUIETO)
            (tick if ok else cruz)(dd, cx, 690, 70, WHITE, 9)
        if k >= 1:
            T(dd, (960, 790), 'acierta 7 y se equivoca en 3', 40, INK, True, 'mm')
    c.page(B[3], B[4], D)

    def E(dd):
        T(dd, (170, 205), 'Filas: lo que marcó el equipo  ·  Columnas: lo que dijo la red', 28, GRIS, True)
        M = [[848, 89, 307], [132, 2077, 715], [333, 690, 2796]]
        nm = ['trepa', 'quieto', 'nado']
        cc = [TREPA, QUIETO, NADO]
        x0, y0, cw, chh = 300, 300, 200, 130
        for j in range(3):
            T(dd, (x0 + j * cw + cw / 2, y0 - 26), nm[j], 30, cc[j], True, 'mm')
            T(dd, (x0 - 20, y0 + j * chh + chh / 2), nm[j], 30, cc[j], True, 'rm')
        for i in range(3):
            s = sum(M[i])
            for j in range(3):
                x, y = x0 + j * cw, y0 + i * chh
                fr = M[i][j] / s
                rr(dd, (x + 4, y + 4, x + cw - 4, y + chh - 4), r=12, fill=mix(WHITE, cc[i], 0.12 + 0.88 * fr * (1.0 if i == j else 1.0)), outline=LINEA, w=2)
                T(dd, (x + cw / 2, y + chh / 2), '{:,}'.format(M[i][j]).replace(',', ' '), 40, WHITE if fr > 0.55 else INK, True, 'mm')
        for (i, j) in [(1, 2), (2, 1)]:
            x, y = x0 + j * cw, y0 + i * chh
            rr(dd, (x + 2, y + 2, x + cw - 2, y + chh - 2), r=12, outline=ORANGE, w=7)
        T(dd, (x0 + 300, y0 + 3 * chh + 40), 'se confunde sobre todo entre nado y quieto', 30, ORANGE, True, 'mm')
        # medidor
        gx, gy, gw = 1050, 380, 700
        T(dd, (1400, 300), 'Calificación F1 (promedio)', 36, INK, True, 'mm')
        rr(dd, (gx, gy, gx + gw, gy + 50), r=14, fill=GRIS_C)
        rr(dd, (gx, gy, gx + gw * 0.705, gy + 50), r=14, fill=VIDEO)
        ln(dd, (gx + gw * 0.85, gy - 18), (gx + gw * 0.85, gy + 68), FUS, 6)
        T(dd, (gx + gw * 0.705, gy + 100), 'hoy: 0.705', 34, VIDEO, True, 'mm')
        T(dd, (gx + gw * 0.85, gy - 36), 'meta: 0.85', 34, FUS, True, 'mm')
        T(dd, (1400, 560), 'Todavía falta mejorar.', 40, INK, True, 'mm')
        T(dd, (1400, 620), 'Lo decimos con honestidad.', 32, GRIS, False, 'mm')
    c.page(B[4], 1e9, E, 0.6, 0)


S9 = dict(title='El examen justo: probar con videos nuevos', draw=s9, beats=[
    B_('¿Cómo sabemos si aprendió bien? Con un examen. Pero debe ser un examen justo: no vale preguntar lo mismo que ya se vio en clase.'),
    B_('Tenemos 11 videos. Se hacen 5 grupos: la red se entrena con los demás y se examina con videos que nunca vio. Se repite 5 veces, cambiando los videos del examen.',
       'Tenemos once videos. Se hacen cinco grupos: la red se entrena con los demás y se examina con videos que nunca vio. Se repite cinco veces, cambiando los videos del examen.'),
    B_('¿Por qué por video y no por segundo? Porque los segundos vecinos se parecen casi igual: comparten el 75 por ciento del clip. Sería como repetir la misma pregunta con otra letra.',
       '¿Por qué por video y no por segundo? Porque los segundos vecinos se parecen casi igual: comparten el setenta y cinco por ciento del clip. Sería como repetir la misma pregunta con otra letra.'),
    B_('Resultado: la red acierta en 7 de cada 10 segundos, el 71.6 por ciento. Contestar siempre nado acertaría 48 de cada 100.',
       'Resultado: la red acierta en siete de cada diez segundos, el setenta y uno coma seis por ciento. Contestar siempre nado acertaría cuarenta y ocho de cada cien.'),
    B_('No es perfecto: se confunde sobre todo entre nado e inmovilidad. Nuestra meta era sacar 85 en F1, una calificación que mezcla aciertos y errores. Vamos en 70, y todavía falta mejorar.',
       'No es perfecto: se confunde sobre todo entre nado e inmovilidad. Nuestra meta era sacar ochenta y cinco en efe uno, una calificación que mezcla aciertos y errores. Vamos en setenta, y todavía falta mejorar.'),
])


# =============================================================== ESCENA 10: LA DECISION
def panel(dd, x0, titulo, probs, t0, t, regla, chip_txt, chip_col, chip_fg, juntas=False, marca=0.8):
    k = ez(pr(t, t0, t0 + 1.2))
    if k <= 0:
        return
    caja(dd, (x0, 190, x0 + 520, 870), r=22)
    T(dd, (x0 + 260, 228), titulo, 38, INK, True, 'mm')
    base = 640
    names = ['nado', 'quieto', 'trepa']
    cols = [NADO, QUIETO, TREPA]
    for i in range(3):
        x = x0 + 70 + i * 140
        hh = 330 * probs[i] * k
        dd.rectangle([x, base - hh, x + 90, base], fill=cols[i])
        T(dd, (x + 45, base + 10), names[i], 28, INK, True, 'mt')
        if k > 0.95:
            T(dd, (x + 45, base - hh - 24), '%d %%' % round(probs[i] * 100), 30, cols[i], True, 'mm')
    return base


def s10(c):
    d, t, B = c.d, c.t, c.B
    ex = [(96, 'Segundo A', [0.91, 0.06, 0.03], B[0] + 0.5, 'nado', NADO, WHITE, 'gana: llegó a 80 %'),
          (700, 'Segundo B', [0.46, 0.14, 0.40], B[2] - 0.5, 'conducta activa', MED, INK, 'nado + trepa suman 86 %'),
          (1304, 'Segundo C', [0.45, 0.40, 0.15], B[3] - 0.5, 'nado (la más probable)', NADO, WHITE, 'nado + trepa solo suman 60 %')]
    base = 640
    for i, (x0, ti, pb, t0, res, col, fg, why) in enumerate(ex):
        if t < t0:
            continue
        panel(d, x0, ti, pb, t0, t, why, res, col, fg)
        yl = base - 330 * 0.8
        if t >= B[1] + 0.3 if i == 0 else t >= t0 + 1.5:
            for xx in range(x0 + 20, x0 + 500, 24):
                ln(d, (xx, yl), (xx + 12, yl), ORANGE, 4)
            T(d, (x0 + 500, yl - 18), '80 %', 26, ORANGE, True, 'rm')
        tr = {0: B[1] + 1.8, 1: B[2] + 2.2, 2: B[3] + 2.0}[i]
        if t >= tr:
            if i == 1:
                T(d, (x0 + 260, 300), 'nado + trepa = 86 %', 30, hx('a97c10'), True, 'mm')
                ln(d, (x0 + 115, 322), (x0 + 115, 340), MED, 4)
                ln(d, (x0 + 395, 322), (x0 + 395, 340), MED, 4)
                ln(d, (x0 + 115, 322), (x0 + 395, 322), MED, 4)
            chip(d, x0 + 260, 718, res, col, 36, fg=fg, anchor='mm')
            T(d, (x0 + 260, 800), why, 28, GRIS, True, 'mm')
    T(d, (1824, 162), 'números de ejemplo', 22, GRIS, False, 'ra')


S10 = dict(title='La decisión final de cada segundo', draw=s10, beats=[
    B_('Falta un último paso: decidir la conducta de cada segundo. La red da tres probabilidades.'),
    B_('Regla uno: si una llega a 80 por ciento, gana. Es como pedir que alguien esté bastante seguro antes de contestar.',
       'Regla uno: si una llega a ochenta por ciento, gana. Es como pedir que alguien esté bastante seguro antes de contestar.'),
    B_('Regla dos: si ninguna llega, pero nado y escalamiento juntos suman 80, el sistema dice: está activo, pero no sé si nadó o trepó. Eso es conducta activa.',
       'Regla dos: si ninguna llega, pero nado y escalamiento juntos suman ochenta, el sistema dice: está activo, pero no sé si nadó o trepó. Eso es conducta activa.'),
    B_('Regla tres: si tampoco, gana la más probable.'),
])


# =============================================================== ESCENA 11: RESUMEN
def s11(c):
    d, t, B = c.d, c.t, c.B
    boxes = [('Video', GRIS), ('Clip de\n16 fotos', GRIS), ('R(2+1)D-18\n512 pistas', VIDEO), ('Fusión\n576 pistas', FUS), ('3 probabili-\ndades', NADO), ('Regla del\n80 %', ORANGE), ('Conducta\ndel segundo', TREPA)]
    for i, (tx, col) in enumerate(boxes):
        ta = B[0] + 1.0 + i * 1.7
        k = ez(pr(t, ta, ta + 0.5))
        if k <= 0:
            continue
        x = 96 + i * 250
        rr(d, (x, 260 + (1 - k) * 30, x + 226, 430 + (1 - k) * 30), r=20, fill=col)
        TW(d, x + 113 - 103, 300 + (1 - k) * 30, tx, 26 if i == 4 else 30, WHITE, 206, True, 1.2, center=True)
        if i < 6:
            arrow(d, (x + 228, 345), (x + 248, 345), GRIS, 4, 14)
        if i == 3:
            rr(d, (x - 500, 470, x - 280, 580), r=20, fill=MED)
            TW(d, x - 500, 490, '22 medidas\n64 pistas', 30, INK, 220, True, 1.2, center=True)
            poly_arrow(d, [(x - 390, 470), (x - 390, 450), (x + 20, 450), (x + 20, 432)], MED, 4, 14)
    if t >= B[1]:
        def c1(dd):
            caja(dd, (96, 640, 920, 860), r=22, outline=FUS, w=4)
            T(dd, (508, 676), 'Aprende', 40, FUS, True, 'mm')
            TW(dd, 130, 725, 'adivinar → medir el error → mover las perillas, lote tras lote, 15 épocas', 34, INK, 760, False, 1.25, center=True)
        c.show(B[1], c1)
    if t >= B[2]:
        def c2(dd):
            caja(dd, (1000, 640, 1824, 860), r=22, outline=NADO, w=4)
            T(dd, (1412, 676), 'Se examina', 40, NADO, True, 'mm')
            TW(dd, 1034, 725, 'con videos que nunca vio: acierta 7 de cada 10 segundos', 34, INK, 760, False, 1.25, center=True)
        c.show(B[2], c2)


S11 = dict(title='Todo junto', draw=s11, beats=[
    B_('Resumamos. Un clip de 16 fotos entra a la red R(2+1)D-18, que entrega 512 pistas. Las 22 medidas entregan 64. Se fusionan en 576, y la capa final da tres probabilidades.',
       'Resumamos. Un clip de dieciséis fotos entra a la red erre, dos más uno, de, dieciocho, que entrega quinientas doce pistas. Las veintidós medidas entregan sesenta y cuatro. Se fusionan en quinientas setenta y seis, y la capa final da tres probabilidades.'),
    B_('Para aprender, la red adivina, mide su error y mueve las perillas, lote tras lote, durante 15 épocas.',
       'Para aprender, la red adivina, mide su error y mueve las perillas, lote tras lote, durante quince épocas.'),
    B_('Se examina con videos que nunca vio, y acierta 7 de cada 10 segundos. Gracias por mirar.',
       'Se examina con videos que nunca vio, y acierta siete de cada diez segundos. Gracias por mirar.'),
])
