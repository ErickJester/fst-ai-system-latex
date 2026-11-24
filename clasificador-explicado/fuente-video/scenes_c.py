"""Escenas nuevas: que son las pistas, y la fusion explicada de nuevo."""
import math
import random
from vid_lib import *
from scenes_a import B_, ORANGE
from scenes_b import P_TOP, P_BOT, CT_X, CT_Y, CT_W, CT_H, concat_bar

AMBAR = hx('a97c10')


# =============================================================== PISTAS
def sp(c):
    d, t, B = c.d, c.t, c.B
    rnd = random.Random(21)
    base = [[rnd.random() for _ in range(8)] for _ in range(6)]
    GX, GY, PX, PY = 500, 260, 88, 78

    def val(i, j):
        return cl(base[i][j] * 0.78 + 0.22 * (0.5 + 0.5 * math.sin(t * 1.3 + i * 0.9 + j * 0.6)))

    def A(dd):
        for k in range(3):
            miniframe(dd, 100 + k * 20, 360 + k * 20, 170, 130, k + t * 0.4)
        T(dd, (190, 562), 'el clip', 30, GRIS, True, 'mm')
        arrow(dd, (310, 460), (GX - 60, 460), GRIS, 4, 16)
        T(dd, (GX + 3.5 * PX, 205), 'la red = 512 inspectores (aquí dibujamos 48)', 30, VIDEO, True, 'mm')
        for i in range(6):
            for j in range(8):
                v = val(i, j)
                cx, cy = GX + j * PX, GY + i * PY
                circ(dd, (cx, cy), 30, fill=mix(WHITE, VIDEO, 0.08 + 0.92 * v), outline=VIDEO, w=3)
                if t >= B[1] and t < B[3]:
                    T(dd, (cx, cy), '%.1f' % (v * 4), 22, WHITE if v > 0.5 else INK, True, 'mm')
                elif t >= B[3]:
                    T(dd, (cx, cy), '?', 30, WHITE if v > 0.5 else INK, True, 'mm')
        if B[1] <= t < B[3]:
            kk = ez(pr(t, B[1] + 0.5, B[1] + 1.2))
            if kk > 0:
                x0 = 1290
                circ(dd, (x0 + 24, 290), 30, fill=VIDEO, outline=VIDEO, w=3)
                T(dd, (x0 + 80, 290), 'número alto:\n¡lo vi mucho!', 32, INK, True, 'lm')
                circ(dd, (x0 + 24, 420), 30, fill=mix(WHITE, VIDEO, 0.08), outline=VIDEO, w=3)
                T(dd, (x0 + 80, 420), 'número bajo:\ncasi no lo vi', 32, INK, True, 'lm')
                T(dd, (x0 + 24, 520), 'Cada inspector se fija en un patrón distinto de forma y de movimiento.', 28, GRIS, False, 'la') if False else None
                TW(dd, x0, 500, 'Cada inspector se fija en un patrón distinto de forma y de movimiento del clip.', 30, GRIS, 520, False)
        if t >= B[2]:
            kk = ez(pr(t, B[2] + 0.4, B[2] + 1.2))
            arrow(dd, (GX + 3.5 * PX, 690), (GX + 3.5 * PX, 735), GRIS, 4, 16)
            n = 48
            w = 704 / n
            for k in range(n):
                v = val(k // 8, k % 8) * kk
                x = GX - 30 + k * (1200 / n) * 0.62 + 0
                dd.rectangle([GX - 30 + k * w * 1.0, 830 - 70 * v, GX - 30 + k * w * 1.0 + w - 3, 830], fill=VIDEO)
            T(dd, (GX - 30 + 352, 856), 'la ficha del clip: 512 casillas = 512 pistas', 30, VIDEO, True, 'mm')
        if t >= B[3]:
            kk = ez(pr(t, B[3] + 0.4, B[3] + 1.2))
            if kk > 0:
                chip(dd, 1550, 270, 'nadie les puso nombre', QUIETO, 32, anchor='mm')
                TW(dd, 1290, 330, 'La red los descubrió sola, viendo videos:', 30, INK, 520, True)
                chip(dd, 1550, 470, '1  videos de Kinetics', VIDEO, 30, anchor='mm')
                chip(dd, 1550, 540, '2  nuestros videos', VIDEO, 30, anchor='mm')
                TW(dd, 1290, 600, 'Por eso no sabemos decir qué mira cada uno. Pero sirven.', 30, GRIS, 520, False)
    c.page(B[0], B[4], A)

    def Bp(dd):
        rr2 = random.Random(5)
        p1 = [rr2.random() for _ in range(40)]
        p2 = [rr2.random() for _ in range(40)]
        T(dd, (960, 205), 'Clips parecidos dan fichas parecidas', 44, INK, True, 'mm')
        filas = [('clip de nado A', NADO, p1, 0.07, 290), ('clip de nado B', NADO, p1, 0.07, 480), ('clip de quieto', QUIETO, p2, 0.0, 670)]
        rn = random.Random(9)
        for k, (nm, col, pat, ruido, y) in enumerate(filas):
            ta = B[4] + 0.6 + k * 2.2
            kk = ez(pr(t, ta, ta + 0.7))
            if kk <= 0:
                continue
            chip(dd, 96, y - 20, nm, col, 28, anchor='la')
            for i in range(40):
                v = cl(pat[i] + (rn.random() - 0.5) * 2 * ruido) * kk
                x = 470 + i * 27
                dd.rectangle([x, y + 100 - 120 * v, x + 21, y + 100], fill=col)
        if t >= B[4] + 5.5:
            T(dd, (1600, 380), '≈ parecidas', 40, NADO, True, 'lm')
            T(dd, (1600, 720), 'distinta', 40, QUIETO, True, 'lm')
        T(dd, (1824, 165), 'ilustración', 22, GRIS, False, 'ra')
    c.page(B[4], 1e9, Bp, 0.6, 0)


SP = dict(title='Las pistas: ¿qué son esos 512 números?', draw=sp, beats=[
    B_('Piensa en la red como 512 inspectores. Cada inspector mira el clip, y cada uno está pendiente de un patrón distinto de forma y de movimiento.'),
    B_('Cada inspector contesta con un número: cuánto vio de lo suyo. Un número alto significa: lo vi mucho. Uno bajo: casi no lo vi.'),
    B_('Esos 512 números juntos son las pistas. Es como una ficha con 512 casillas, y cada casilla dice cuánto hay de un patrón en el clip.',
       'Esos quinientos doce números juntos son las pistas. Es como una ficha con quinientas doce casillas, y cada casilla dice cuánto hay de un patrón en el clip.'),
    B_('Nadie les puso nombre a los inspectores. La red los descubrió sola, viendo primero los videos de Kinetics y después los nuestros. Por eso no sabemos decir qué mira cada uno.',
       'Nadie les puso nombre a los inspectores. La red los descubrió sola, viendo primero los videos de Kinétics y después los nuestros. Por eso no sabemos decir qué mira cada uno.'),
    B_('Pero sirven: dos clips de nado dan fichas parecidas, y un clip de inmovilidad da una ficha distinta. Con eso la red puede decidir.'),
])


# =============================================================== FUSION
def dibuja_top(dd, t):
    for k in range(3):
        miniframe(dd, 90 + k * 14, 270 + k * 14, 140, 110, k + t * 0.3)
    arrow(dd, (250, 330), (330, 330), GRIS, 5, 18)
    rr(dd, (330, 270, 690, 390), r=22, fill=VIDEO)
    T(dd, (510, 316), 'R(2+1)D-18', 46, WHITE, True, 'mm')
    T(dd, (510, 360), 'mira el video', 26, mix(VIDEO, WHITE, 0.75), False, 'mm')
    arrow(dd, (690, 330), (760, 330), GRIS, 5, 18)
    for i in range(16):
        dd.rectangle([760, 250 + i * 10, 800, 258 + i * 10], fill=mix(VIDEO, WHITE, 0.0 if i % 2 == 0 else 0.25))
    T(dd, (780, 436), '512 pistas', 32, VIDEO, True, 'mm')
    T(dd, (780, 470), 'sin nombre', 24, GRIS, False, 'mm')


def dibuja_bot(dd, t):
    rnd = random.Random(5)
    holes = {4, 11, 17}
    for i in range(22):
        y = 562 + i * 8
        if i in holes:
            dd.rectangle([90, y, 90 + 160, y + 6], outline=GRIS, width=1)
        else:
            dd.rectangle([90, y, 90 + int(160 * (0.15 + 0.85 * rnd.random() ** 2)), y + 6], fill=MED)
    T(dd, (170, 768), '22 medidas', 30, AMBAR, True, 'mm')
    arrow(dd, (262, 650), (292, 650), GRIS, 4, 14)
    caja(dd, (296, 592, 520, 708), r=16, fill=WHITE, outline=MED, w=4)
    T(dd, (408, 622), 'limpiar', 34, INK, True, 'mm')
    T(dd, (408, 660), 'huecos: valor típico', 22, GRIS, False, 'mm')
    T(dd, (408, 686), 'misma escala', 22, GRIS, False, 'mm')
    arrow(dd, (522, 650), (552, 650), GRIS, 4, 14)
    for i in range(22):
        y = 562 + i * 8
        dd.rectangle([556, y, 556 + 90, y + 6], fill=mix(MED, WHITE, 0.0 if i % 2 == 0 else 0.2))
    T(dd, (601, 768), 'listas', 30, AMBAR, True, 'mm')


def dibuja_red(dd, t):
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
    T(dd, (860, 528), 'red pequeña: mezcla', 24, GRIS, True, 'mm')
    arrow(dd, (980, 650), (1030, 650), GRIS, 4, 14)
    for i in range(14):
        dd.rectangle([1040, 580 + i * 10, 1080, 588 + i * 10], fill=mix(MED, WHITE, 0.0 if i % 2 == 0 else 0.25))
    T(dd, (1060, 768), '64 pistas', 28, AMBAR, True, 'mm')


def dibuja_cat(dd, t, dropout):
    poly_arrow(dd, P_TOP, VIDEO, 5, 20)
    poly_arrow(dd, P_BOT, MED, 5, 20)
    concat_bar(dd, t, dropout=dropout)
    rr(dd, (CT_X - 4, CT_Y - 4, CT_X + CT_W + 4, CT_Y + CT_H + 4), r=8, outline=FUS, w=4)
    T(dd, (CT_X + 190, CT_Y + CT_H + 40), '512 + 64 = 576 pistas', 34, FUS, True, 'mm')
    pulses(dd, P_TOP, t, VIDEO)
    pulses(dd, P_BOT, t, MED)
    if dropout:
        T(dd, (1010, 424), 'apagado al azar (dropout)', 24, QUIETO, True, 'lm')


def dibuja_fin(dd, t, t0):
    arrow(dd, (1364, 485), (1408, 485), GRIS, 5, 18)
    rr(dd, (1408, 420, 1550, 550), r=18, fill=FUS)
    T(dd, (1479, 462), 'capa final', 24, WHITE, True, 'mm')
    T(dd, (1479, 500), '576 → 3', 26, WHITE, True, 'mm')
    arrow(dd, (1552, 485), (1600, 485), GRIS, 5, 18)
    probs = [0.72, 0.20, 0.08]
    names = ['nado', 'quieto', 'trepa']
    cols = [NADO, QUIETO, TREPA]
    g = ez(pr(t, t0, t0 + 1.4))
    for i in range(3):
        x = 1620 + i * 90
        hh = 150 * probs[i] / 0.72 * g
        dd.rectangle([x, 570 - hh, x + 62, 570], fill=cols[i])
        T(dd, (x + 31, 580), names[i], 24, INK, True, 'mt')
        if g > 0.9:
            T(dd, (x + 31, 566 - hh - 24), '%d %%' % round(probs[i] * 100), 26, cols[i], True, 'mm')
    T(dd, (1730, 640), '3 puntajes', 28, GRIS, True, 'mm')


W0 = [[.2, .1, .3], [.0, .2, .1], [.3, .0, .2], [.1, .3, .0], [.2, .1, .2], [.0, .2, .1]]
W1 = [[1.2, -.4, .1], [.2, .3, -.2], [.9, .1, .2], [.8, -.3, .5], [-.3, 1.0, -.4], [.4, .2, .8]]
CL = [0.9, 0.4, 0.7, 0.8, 0.2, 0.6]


def softmax(xs):
    m = max(xs)
    e = [math.exp(x - m) for x in xs]
    s = sum(e)
    return [v / s for v in e]


def sf(c):
    d, t, B = c.d, c.t, c.B

    # ---------- pagina A: dos fuentes, fortalezas y limites
    def A(dd):
        for x0, col, tt, sub, mk in [(96, VIDEO, 'Red de video', '512 pistas, sin nombre', B[1]), (990, MED, 'Medidas', '22 números, con nombre', B[2])]:
            caja(dd, (x0, 190, x0 + 834, 790), r=26, outline=col, w=5)
            T(dd, (x0 + 417, 232), tt, 48, col if col == VIDEO else AMBAR, True, 'mm')
            T(dd, (x0 + 417, 282), sub, 30, GRIS, True, 'mm')
            rr0 = random.Random(3 if col == VIDEO else 4)
            n = 40 if col == VIDEO else 22
            for i in range(n):
                v = 0.2 + 0.8 * rr0.random()
                w = 600 / n
                dd.rectangle([x0 + 117 + i * w, 400 - 70 * v, x0 + 117 + i * w + w - 3, 400], fill=col)
            k = ez(pr(t, mk, mk + 0.8))
            if k <= 0:
                continue
            if col == VIDEO:
                lines = [(True, 'mira todo el clip y descubre patrones que a nosotros no se nos ocurrirían'),
                         (False, 'puede fijarse en cosas que no son el espécimen: el fondo, la luz')]
            else:
                lines = [(True, 'miden justo lo que observa un experto: el pataleo, la nariz, la postura'),
                         (False, 'son pocas y no lo ven todo')]
            for i, (ok, s_) in enumerate(lines):
                y = 480 + i * 150
                circ(dd, (x0 + 60, y + 38), 30, fill=TREPA if ok else QUIETO)
                (tick if ok else cruz)(dd, x0 + 60, y + 38, 44, WHITE, 6)
                TW(dd, x0 + 110, y, s_, 32, INK, 690, False, 1.25)
    c.page(B[0], B[3], A)

    def banner(dd):
        chip(dd, 500, 380, 'lo que VE el video', VIDEO, 40, anchor='mm')
        chip(dd, 1420, 380, 'lo que dicen las MEDIDAS', MED, 40, fg=INK, anchor='mm')
        arrow(dd, (500, 430), (880, 560), GRIS, 7, 28)
        arrow(dd, (1420, 430), (1040, 560), GRIS, 7, 28)
        rr(dd, (660, 560, 1260, 690), r=40, fill=FUS)
        T(dd, (960, 625), 'FUSIÓN = JUNTAR', 56, WHITE, True, 'mm')
        T(dd, (960, 770), 'para decidir con las dos a la vez', 40, INK, True, 'mm')
    c.page(B[3], B[4] + 0.2, banner)

    # ---------- diagrama que se arma
    end = B[8]
    c.page(B[4], end, lambda dd: dibuja_top(dd, t))
    c.page(B[4] + 0.8, end, lambda dd: dibuja_bot(dd, t))
    c.page(B[5], end, lambda dd: dibuja_red(dd, t))
    c.page(B[6], end, lambda dd: dibuja_cat(dd, t, False))
    if t >= B[7]:
        c.page(B[7], end, lambda dd: T(dd, (1010, 424), 'apagado al azar (dropout)', 24, QUIETO, True, 'lm'))

    # ---------- el jurado
    def jurado(dd):
        k1 = ez(pr(t, B[9] + 0.8, B[9] + 0.8 + (B[10] - B[9]) * 0.65)) if t >= B[9] else 0.0
        W = [[lerp(W0[i][j], W1[i][j], k1) for j in range(3)] for i in range(6)]
        sc = [sum(CL[i] * W[i][j] for i in range(6)) for j in range(3)]
        pb = softmax(sc)
        T(dd, (960, 205), 'La capa final es como un jurado', 44, FUS, True, 'mm')
        ys = [270 + i * 82 for i in range(6)]
        yo = [360, 480, 600]
        cols = [NADO, QUIETO, TREPA]
        names = ['nado', 'quieto', 'trepa']
        ka = ez(pr(t, B[8] + 0.5, B[8] + 2.0))
        for i in range(6):
            col = VIDEO if i < 3 else MED
            lab = 'pista video %d' % (i + 1) if i < 3 else 'pista medida %d' % (i - 2)
            rr(dd, (96, ys[i] - 26, 396, ys[i] + 26), r=14, fill=WHITE, outline=col, w=4)
            dd.rectangle([104, ys[i] - 8, 104 + 120 * CL[i], ys[i] + 8], fill=col)
            T(dd, (240, ys[i]), lab, 22, col if col == VIDEO else AMBAR, True, 'lm')
            for j in range(3):
                w = W[i][j]
                if ka <= 0:
                    continue
                if w >= 0:
                    ln(dd, (400, ys[i]), (1330, yo[j]), mix(BG, cols[j], 0.35 + 0.65 * ka), max(1, int(w * 7 * ka)))
                else:
                    ln(dd, (400, ys[i]), (1330, yo[j]), (190, 190, 196), 1)
        T(dd, (246, 226), 'pistas de la ficha (6 de 576)', 24, GRIS, True, 'mm')
        for j in range(3):
            T(dd, (1350, yo[j]), names[j], 34, cols[j], True, 'lm')
            rr(dd, (1480, yo[j] - 26, 1480 + 340, yo[j] + 26), r=12, fill=GRIS_C)
            if ka > 0.5:
                rr(dd, (1480, yo[j] - 26, 1480 + max(10, 340 * pb[j]), yo[j] + 26), r=12, fill=cols[j])
                T(dd, (1480 + max(10, 340 * pb[j]) + 12, yo[j]), '%d %%' % round(pb[j] * 100), 28, cols[j], True, 'lm')
        T(dd, (960, 748), 'línea gruesa = esa pista empuja a favor   ·   línea gris fina = empuja en contra o casi nada', 26, GRIS, True, 'mm')
        if t >= B[9]:
            chip(dd, 960, 815, 'los pesos son perillas: el entrenamiento los ajusta', FUS, 30, anchor='mm')
        T(dd, (1824, 165), 'ilustración', 22, GRIS, False, 'ra')
    c.page(B[8], B[10], jurado)

    # ---------- ejemplo
    def ejemplo(dd):
        cards = [(96, 'Solo la red de video', VIDEO, [40, 38, 22], ['duda entre nado', 'y quieto']),
                 (700, 'Lo que dicen las medidas', MED, [18, 66, 16], ['el pataleo trasero es suave', 'la nariz no se movió']),
                 (1304, 'Juntas', FUS, [22, 70, 8], ['el jurado se inclina', 'por quieto'])]
        cols = [NADO, QUIETO, TREPA]
        names = ['nado', 'quieto', 'trepa']
        for i, (x0, tt, col, vals, txt) in enumerate(cards):
            ta = B[10] + 0.4 + i * 3.4
            k = ez(pr(t, ta, ta + 0.7))
            if k <= 0:
                continue
            caja(dd, (x0, 190, x0 + 520, 790), r=24, outline=col, w=5)
            T(dd, (x0 + 260, 232), tt, 36, col if col != MED else AMBAR, True, 'mm')
            T(dd, (x0 + 260, 290), txt[0], 28, INK, False, 'mm')
            T(dd, (x0 + 260, 326), txt[1], 28, INK, False, 'mm')
            for j in range(3):
                x = x0 + 70 + j * 150
                hh = 300 * vals[j] / 100 * k
                dd.rectangle([x, 700 - hh, x + 90, 700], fill=cols[j])
                T(dd, (x + 45, 712), names[j], 26, INK, True, 'mt')
                T(dd, (x + 45, 694 - hh - 20), '%d %%' % vals[j], 28, cols[j], True, 'mm')
        T(dd, (650, 490), '+', 70, GRIS, True, 'mm')
        T(dd, (1254, 490), '=', 70, GRIS, True, 'mm')
        T(dd, (1824, 165), 'ejemplo inventado para ilustrar', 22, GRIS, False, 'ra')
    c.page(B[10], B[11], ejemplo)

    # ---------- diagrama final completo
    def completo(dd):
        dibuja_top(dd, t)
        dibuja_bot(dd, t)
        dibuja_red(dd, t)
        dibuja_cat(dd, t, True)
        dibuja_fin(dd, t, B[11] + 0.6)
        chip(dd, 960, 815, 'dos fuentes de pistas, una sola decisión', FUS, 40, anchor='mm')
    c.page(B[11], 1e9, completo, 0.7, 0)


SF = dict(title='La fusión: juntar dos fuentes de pistas', draw=sf, beats=[
    B_('Ya tenemos dos listas de pistas: las 512 de la red de video y las 22 medidas.',
       'Ya tenemos dos listas de pistas: las quinientas doce de la red de video y las veintidós medidas.'),
    B_('¿Por qué usar las dos? Porque ven cosas distintas. La red de video mira todo el clip y descubre patrones que a nosotros no se nos ocurrirían, pero puede fijarse en cosas que no son el espécimen, como el fondo o la luz.'),
    B_('Las medidas se calculan solo sobre el cuerpo del espécimen y miden justo lo que un experto observa, como el pataleo y la nariz. Pero son pocas, y no lo ven todo.'),
    B_('Por eso se fusionan: se juntan las dos listas para decidir con las dos a la vez.'),
    B_('Primero se limpian las medidas: si falta una, se rellena con un valor típico, y todas se ponen en la misma escala, para que ninguna pese más solo por tener números más grandes.'),
    B_('Luego una red pequeña mezcla las 22 medidas y las convierte en 64 pistas nuevas. Cada una puede combinar varias medidas, por ejemplo: patalea fuerte y de golpe.',
       'Luego una red pequeña mezcla las veintidós medidas y las convierte en sesenta y cuatro pistas nuevas. Cada una puede combinar varias medidas, por ejemplo: patalea fuerte y de golpe.'),
    B_('Ahora se pegan las dos listas: 512 más 64 son 576 pistas, una sola ficha.',
       'Ahora se pegan las dos listas: quinientas doce más sesenta y cuatro son quinientas setenta y seis pistas, una sola ficha.'),
    B_('Mientras entrena, se apagan algunas pistas al azar, a propósito. Se llama dropout, y evita que la red dependa de una sola pista.',
       'Mientras entrena, se apagan algunas pistas al azar, a propósito. Se llama drop aut, y evita que la red dependa de una sola pista.'),
    B_('La capa final es como un jurado. Cada pista tiene un peso: cuánto empuja hacia nado, hacia quieto o hacia trepa. El jurado suma los empujes y da un puntaje a cada opción.'),
    B_('Esos pesos son las perillas que se ajustan al entrenar. Así la red aprende cuánto confiar en cada pista, tanto en las del video como en las de las medidas.'),
    B_('Un ejemplo inventado: el video duda entre nado y quieto. Pero las medidas dicen que el pataleo es suave y que la nariz no se movió. Al juntar todo, el jurado se inclina por quieto.'),
    B_('Eso es la fusión: dos fuentes distintas de pistas, y una sola decisión.'),
])
