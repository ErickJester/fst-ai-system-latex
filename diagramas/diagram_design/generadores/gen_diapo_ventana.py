"""Ventana de 4 s centrada en cada segundo y recorrido de ese segundo por la red (diapositiva del clasificador).
Mismo estilo de carriles que los demás diagramas de la presentación. Uso: gen_diapo_ventana.py salida.html"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_diapo_carriles import Lienzo, AZUL, ROSA, INK, esc


def ventana():
    d = Lienzo(1800, 620)
    d.carril(10, 320, 'Ventana', AZUL)
    d.carril(334, 610, 'Clasificación', ROSA)
    CW, X0, Y0, H = 112, 150, 130, 84
    n, c = 11, 5
    # ventana de 4 s: 1.5 celdas antes y 1.5 después de la celda central
    wx0 = X0 + c * CW - 1.5 * CW
    wx1 = X0 + (c + 1) * CW + 1.5 * CW
    d.o.append(f'<rect x="{wx0:.0f}" y="62" width="{wx1-wx0:.0f}" height="{H+110}" rx="14" fill="#cfe0f7" fill-opacity=".55" stroke="{AZUL[4]}" stroke-width="3" stroke-dasharray="10,6"/>')
    d.o.append(f'<text x="{(wx0+wx1)/2:.0f}" y="96" text-anchor="middle" class="n">ventana de 4 s</text>')
    for i in range(n):
        x = X0 + i * CW
        centro = i == c
        fill = ROSA[3] if centro else '#fff'
        stroke = ROSA[4] if centro else '#9aa4b2'
        d.o.append(f'<rect x="{x}" y="{Y0}" width="{CW}" height="{H}" fill="{fill}" stroke="{stroke}" stroke-width="{3 if centro else 1.6}"/>')
        etiqueta = 't' if centro else ('t' + ('−' if i < c else '+') + str(abs(i - c)))
        d.o.append(f'<text x="{x+CW/2}" y="{Y0+H/2+9}" text-anchor="middle" class="{"n" if centro else "s"}">{etiqueta}</text>')
    d.o.append(f'<text x="{X0+c*CW+CW/2}" y="{Y0+H+34}" text-anchor="middle" class="l">segundo que se clasifica</text>')
    # siguiente ventana (segundo t+1)
    sx0, sx1 = wx0 + CW, wx1 + CW
    y = Y0 + H + 58
    d.o.append(f'<path d="M{sx0:.0f},{y-12} L{sx0:.0f},{y} L{sx1:.0f},{y} L{sx1:.0f},{y-12}" fill="none" stroke="{AZUL[4]}" stroke-width="3"/>')
    d.o.append(f'<text x="{(sx0+sx1)/2:.0f}" y="{y+28}" text-anchor="middle" class="l">la ventana se desliza un segundo y se repite para t+1</text>')
    # nota a la derecha
    d.txt(['Cada segundo del video', 'tiene su propia ventana,', 'centrada en él'], 1470, 150, 'start')
    d.txt(['De cada ventana salen', 'el clip y las medidas'], 1470, 262, 'start')
    # recorrido por la red
    yb = 372
    xs = [110, 470, 840, 1250]
    a = d.caja(110, 360, 290, 'Clip', ['16 fotogramas del cilindro'], ROSA, h=104)
    b = d.caja(110, 478, 290, '22 medidas', ['15 rasgos y 7 reglas'], ROSA, h=104)
    r = d.caja(470, 400, 330, 'Red de fusión', ['R(2+1)D-18 con', 'rama de medidas'], ROSA, h=142)
    s = d.caja(870, 400, 350, 'Tres salidas', ['nado · inmovilidad', 'escalamiento'], ROSA, h=142)
    g = d.caja(1290, 400, 220, 'Regla 0.80', ['conducta activa'], ROSA, h=142)
    o = d.caja(1560, 400, 200, 'Conducta', ['del segundo t'], ROSA, h=142)
    d.flecha([(a['r'], a['cy']), (435, a['cy']), (435, r['cy'] - 20), (r['x'], r['cy'] - 20)])
    d.flecha([(b['r'], b['cy']), (435, b['cy']), (435, r['cy'] + 20), (r['x'], r['cy'] + 20)])
    d.flecha([(r['r'], r['cy']), (s['x'], s['cy'])])
    d.flecha([(s['r'], s['cy']), (g['x'], g['cy'])])
    d.flecha([(g['r'], g['cy']), (o['x'], o['cy'])])
    return d.pagina('Ventana de 4 s centrada en cada segundo')


if __name__ == '__main__':
    open(sys.argv[1], 'w', encoding='utf-8').write(ventana())
    print('ok')
