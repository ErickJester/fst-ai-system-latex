import re
p = 'scenes_b.py'
s = open(p, encoding='utf-8').read()


def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b)


rep("P_TOP = [(270, 330), (1137, 330), (1137, 452)]", "P_TOP = [(800, 330), (1000, 330), (1000, 452)]")
rep("P_BOT = [(1080, 640), (1337, 640), (1337, 518)]", "P_BOT = [(1080, 650), (1337, 650), (1337, 518)]")
old_bot = s[s.index("    def bot(dd):"):s.index("    c.show(B[2] + 0.5, bot)")]
new_bot = '''    def bot(dd):
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
'''
s = s.replace(old_bot, new_bot)
old_red = s[s.index("    def red(dd):"):s.index("    c.show(B[3] + 0.5, red)")]
new_red = '''    def red(dd):
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
'''
s = s.replace(old_red, new_red)
rep("""            chip(dd, 1130, 590, 'dropout: se apagan algunas al azar', QUIETO, 26, anchor='mm') if False else None
            T(dd, (1130, 618), 'se apagan algunas al azar (dropout)', 26, QUIETO, True, 'mm')""",
    """            T(dd, (1010, 424), 'se apagan algunas al azar (dropout)', 24, QUIETO, True, 'lm')""")
rep("""        arrow(dd, (1364, 485), (1420, 485), GRIS, 5, 18)
        rr(dd, (1420, 420, 1540, 550), r=18, fill=FUS)
        T(dd, (1480, 462), 'capa final', 26, WHITE, True, 'mm')
        T(dd, (1480, 500), '576 → 3', 28, WHITE, True, 'mm')
        arrow(dd, (1542, 485), (1596, 485), GRIS, 5, 18)""",
    """        arrow(dd, (1364, 485), (1408, 485), GRIS, 5, 18)
        rr(dd, (1408, 420, 1550, 550), r=18, fill=FUS)
        T(dd, (1479, 462), 'capa final', 24, WHITE, True, 'mm')
        T(dd, (1479, 500), '576 → 3', 26, WHITE, True, 'mm')
        arrow(dd, (1552, 485), (1600, 485), GRIS, 5, 18)""")
rep("chip(dd, 960, 835, 'decide con lo que VE y con lo que MIDIÓ', FUS, 40, anchor='mm')",
    "chip(dd, 960, 815, 'decide con lo que VE y con lo que MIDIÓ', FUS, 40, anchor='mm')")

# S7
rep("hh = 190 * ad[i]\n                dd.rectangle([xa, 780 - hh, xa + 56, 780], fill=cols[i])\n                T(dd, (xa + 28, 790), names[i], 22, GRIS, True, 'mt')",
    "hh = 170 * ad[i]\n                dd.rectangle([xa, 760 - hh, xa + 56, 760], fill=cols[i])\n                T(dd, (xa + 28, 768), names[i], 22, GRIS, True, 'mt')")
rep("one = 190 if i == 0 else 4\n                dd.rectangle([xb, 780 - one, xb + 56, 780], fill=cols[i])\n                T(dd, (xb + 28, 790), names[i], 22, GRIS, True, 'mt')",
    "one = 170 if i == 0 else 4\n                dd.rectangle([xb, 760 - one, xb + 56, 760], fill=cols[i])\n                T(dd, (xb + 28, 768), names[i], 22, GRIS, True, 'mt')")
rep("chip(dd, 1435, 838, err, QUIETO if t < B[5] + 3 else TREPA, 28, anchor='mm')",
    "chip(dd, 1435, 826, err, QUIETO if t < B[5] + 3 else TREPA, 28, anchor='mm')")
rep("T(dd, (1418, 650), '≠', 60, GRIS, True, 'mm')", "T(dd, (1418, 640), '≠', 60, GRIS, True, 'mm')")
rep("""        c.show(B[6], lambda dd: chip(dd, 530, 840, 'y se repite con el siguiente lote', FUS, 32, anchor='mm') if False else T(dd, (530, 840), 'y se repite con el siguiente lote  ↻', 32, FUS, True, 'mm'))
    T(d, (1820, 880), 'ejemplo ilustrativo', 20, GRIS, False, 'rs') if t >= B[3] else None""",
    """        c.show(B[6], lambda dd: T(dd, (530, 840), 'y se repite con el siguiente lote', 34, FUS, True, 'mm'))
    if t >= B[3]:
        T(d, (1818, 850), 'ejemplo ilustrativo', 20, GRIS, False, 'rs')""")

# S8
rep("x0, yb, w, h = 140, 850, 800, 150", "x0, yb, w, h = 140, 826, 800, 105")
rep("""        T(dd, (x0 + 0.02 * w, yb - 36), 'empieza chico', 26, GRIS, True, 'ma')
        T(dd, (x0 + 0.30 * w, yb - h - 30), 'crece', 26, GRIS, True, 'mm')
        T(dd, (x0 + 0.92 * w, yb - 60), 'muy chico para afinar', 26, GRIS, True, 'ra')""",
    """        T(dd, (x0 + 10, yb + 8), 'empieza chico', 26, GRIS, True, 'la')
        T(dd, (x0 + 0.30 * w, yb - h - 24), 'crece', 26, GRIS, True, 'mm')
        T(dd, (x0 + w, yb + 8), 'al final, muy chico para afinar', 26, GRIS, True, 'ra')""")
rep("T(dd, (110, 640), 'Tamaño del paso en cada momento del entrenamiento', 30, GRIS, True)",
    "T(dd, (110, 636), 'Tamaño del paso en cada momento del entrenamiento', 30, GRIS, True)")

# S9
rep("T(dd, (680, 410), '✗', 120, QUIETO, True, 'mm')", "cruz(dd, 680, 410, 150, QUIETO, 16)")
rep("T(dd, (1580, 410), '✓', 120, TREPA, True, 'mm')", "tick(dd, 1580, 410, 150, TREPA, 16)")
rep("""            circ(dd, (cx, 690), 52, fill=TREPA if ok else QUIETO)
            T(dd, (cx, 690), '✓' if ok else '✗', 56, WHITE, True, 'mm')""",
    """            circ(dd, (cx, 690), 52, fill=TREPA if ok else QUIETO)
            (tick if ok else cruz)(dd, cx, 690, 70, WHITE, 9)""")
rep("T(dd, (200, 225), 'segundos de un mismo video', 28, GRIS, True)", "T(dd, (200, 214), 'segundos de un mismo video', 28, GRIS, True)")

# S10
rep("""                ln(d, (xx, yl), (xx + 12, yl), ORANGE, 4)
            T(d, (x0 + 24, yl - 18), '80 %', 26, ORANGE, True, 'lm')""",
    """                ln(d, (xx, yl), (xx + 12, yl), ORANGE, 4)
            T(d, (x0 + 500, yl - 18), '80 %', 26, ORANGE, True, 'rm')""")
rep("T(d, (1820, 885), 'números de ejemplo', 22, GRIS, False, 'rs')", "T(d, (1824, 162), 'números de ejemplo', 22, GRIS, False, 'ra')")

# S11
rep("x = 96 + i * 250\n        rr(d, (x, 260 + (1 - k) * 30, x + 220, 430 + (1 - k) * 30), r=20, fill=col)\n        TW(d, x + 110 - 100, 300 + (1 - k) * 30, tx, 30, WHITE, 200, True, 1.2, center=True)\n        if i < 6:\n            arrow(d, (x + 222, 345), (x + 248, 345), GRIS, 4, 14)",
    "x = 96 + i * 250\n        rr(d, (x, 260 + (1 - k) * 30, x + 226, 430 + (1 - k) * 30), r=20, fill=col)\n        TW(d, x + 113 - 103, 300 + (1 - k) * 30, tx, 26 if i == 4 else 30, WHITE, 206, True, 1.2, center=True)\n        if i < 6:\n            arrow(d, (x + 228, 345), (x + 248, 345), GRIS, 4, 14)")
rep("('3 probabilidades', NADO)", "('3 probabili-\\ndades', NADO)")
rep("TW(dd, 130, 712, 'adivinar → medir el error → mover las perillas, lote tras lote, 15 épocas', 30, INK, 760, False, 1.25, center=True)",
    "TW(dd, 130, 725, 'adivinar → medir el error → mover las perillas, lote tras lote, 15 épocas', 34, INK, 760, False, 1.25, center=True)")
rep("TW(dd, 1034, 712, 'con videos que nunca vio: acierta 7 de cada 10 segundos', 30, INK, 760, False, 1.25, center=True)",
    "TW(dd, 1034, 725, 'con videos que nunca vio: acierta 7 de cada 10 segundos', 34, INK, 760, False, 1.25, center=True)")
open(p, 'w', encoding='utf-8').write(s)

m = open('vid_main.py', encoding='utf-8').read()
a = "rr(d, (110, 892, 1810, 1058), r=26, fill=WHITE, outline=LINEA, w=3)\n    f = F(40, False)\n    lines = wrap(txt, f, 1620)\n    y = 975 - len(lines) * 26\n    for l in lines:\n        d.text((960, y), l, font=f, fill=INK, anchor='ma')\n        y += 52"
assert a in m
m = m.replace(a, "rr(d, (110, 880, 1810, 1064), r=26, fill=WHITE, outline=LINEA, w=3)\n    f = F(38, False)\n    lines = wrap(txt, f, 1620)\n    y = 972 - len(lines) * 24\n    for l in lines:\n        d.text((960, y), l, font=f, fill=INK, anchor='ma')\n        y += 48")
open('vid_main.py', 'w', encoding='utf-8').write(m)
print('ok')
