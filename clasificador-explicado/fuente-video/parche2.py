s = open('scenes_c.py', encoding='utf-8').read()
a = "lab = 'pista del video %d' % (i + 1) if i < 3 else 'pista de medidas %d' % (i - 2)"
assert a in s
s = s.replace(a, "lab = 'pista video %d' % (i + 1) if i < 3 else 'pista medida %d' % (i - 2)")
b = "            T(dd, (240, ys[i] + 0), '', 20, GRIS)\n            T(dd, (404, ys[i]), '', 20, GRIS)\n            T(dd, (112, ys[i] - 40), lab, 20, GRIS, True, 'la') if False else None\n"
assert b in s
s = s.replace(b, "            T(dd, (240, ys[i]), lab, 22, col if col == VIDEO else AMBAR, True, 'lm')\n")
c = "        for i in range(6):\n            col = VIDEO if i < 3 else MED\n            T(dd, (760, ys[i]), '', 20, GRIS)\n"
assert c in s
s = s.replace(c, "")
open('scenes_c.py', 'w', encoding='utf-8').write(s)
m = open('vid_main.py', encoding='utf-8').read()
m = m.replace("from scenes_b import S6, S7, S8, S9, S10, S11", "from scenes_b import S7, S8, S9, S10, S11\nfrom scenes_c import SP, SF")
m = m.replace("ESCENAS = [S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11]", "ESCENAS = [S1, S2, S3, S4, SP, S5, SF, S7, S8, S9, S10, S11]")
open('vid_main.py', 'w', encoding='utf-8').write(m)
print('ok')
