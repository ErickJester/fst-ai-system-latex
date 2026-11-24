s = open('scenes_c.py', encoding='utf-8').read()


def rep(a, b):
    global s
    assert a in s, a[:80]
    s = s.replace(a, b)


# pistas: leyenda solo entre B1 y B3
rep("        if t >= B[1]:\n            kk = ez(pr(t, B[1] + 0.5, B[1] + 1.2))\n            if kk > 0:\n                x0 = 1290",
    "        if B[1] <= t < B[3]:\n            kk = ez(pr(t, B[1] + 0.5, B[1] + 1.2))\n            if kk > 0:\n                x0 = 1290")
rep("T(dd, (190, 540), 'el clip', 30, GRIS, True, 'mm')", "T(dd, (190, 562), 'el clip', 30, GRIS, True, 'mm')")
rep("x = 470 + i * 31\n                dd.rectangle([x, y + 100 - 120 * v, x + 24, y + 100], fill=col)",
    "x = 470 + i * 27\n                dd.rectangle([x, y + 100 - 120 * v, x + 21, y + 100], fill=col)")
rep("T(dd, (1560, 440), '≈ parecidas', 40, NADO, True, 'mm')\n            T(dd, (1560, 690), 'distinta', 40, QUIETO, True, 'mm')",
    "T(dd, (1600, 380), '≈ parecidas', 40, NADO, True, 'lm')\n            T(dd, (1600, 720), 'distinta', 40, QUIETO, True, 'lm')")

# jurado: posiciones
rep("T(dd, (246, 238), 'pistas de la ficha (6 de 576)', 24, GRIS, True, 'mm')", "T(dd, (246, 226), 'pistas de la ficha (6 de 576)', 24, GRIS, True, 'mm')")
rep("T(dd, (960, 790), 'línea gruesa = esa pista empuja a favor   ·   línea gris fina = empuja en contra o casi nada', 26, GRIS, True, 'mm')",
    "T(dd, (960, 748), 'línea gruesa = esa pista empuja a favor   ·   línea gris fina = empuja en contra o casi nada', 26, GRIS, True, 'mm')")
rep("chip(dd, 1000, 845, 'los pesos son perillas: el entrenamiento los ajusta', FUS, 30, anchor='mm')",
    "chip(dd, 960, 815, 'los pesos son perillas: el entrenamiento los ajusta', FUS, 30, anchor='mm')")
open('scenes_c.py', 'w', encoding='utf-8').write(s)
print('ok')
