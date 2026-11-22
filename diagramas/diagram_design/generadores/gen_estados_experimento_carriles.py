"""Estados de un experimento en carriles de colores (mismo estilo que los estados de un análisis).
Fuente: diagramas/estados_experimento.puml. Uso: gen_estados_experimento_carriles.py salida.html"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_diapo_carriles import Lienzo, GRIS, AZUL, MORADO, ROSA, AMBAR, VERDE, INK

CANCEL = ('#fff7e8', '#f1d9a8', '#c99a2e', '#fbd5de', '#c0405f')   # solo se usa el relleno de caja


def experimento():
    d = Lienzo(1800, 900)
    L = [(15, 165), (180, 330), (345, 495), (510, 660), (675, 825)]
    d.carril(*L[0], 'Subida', GRIS)
    d.carril(*L[1], 'Cola', MORADO)
    d.carril(*L[2], 'Proceso', AZUL)
    d.carril(*L[3], 'Fallas', ROSA)
    d.carril(*L[4], 'Usuario', AMBAR)
    # lámina 1: subida
    d.o.append(f'<circle cx="125" cy="90" r="12" fill="{INK}"/>')
    sv = d.caja(330, 55, 270, 'Sin videos', [], GRIS, h=64)
    ed = d.caja(880, 55, 320, 'En espera del Día 2', [], GRIS, h=64)
    d.flecha([(137, 90), (330, 90)])
    d.txt(['se creó el', 'experimento'], 233, 52)
    d.flecha([(sv['r'], 90), (ed['x'], 90)])
    d.txt(['subió solo el video', 'del Día 1'], 740, 52)
    # cola
    ec = d.caja(880, 215, 320, 'En cola', [], MORADO, h=64)
    d.flecha([(465, 119), (465, 235), (880, 235)])
    d.txt('subió un video del Día 2', 670, 220)
    d.flecha([(1040, 119), (1040, 215)])
    d.txt(['subió un video', 'del Día 2'], 1054, 168, 'start')
    # procesamiento
    pr = d.caja(880, 375, 320, 'Procesando', [], AZUL, h=64)
    d.flecha([(1040, 279), (1040, 375)])
    d.txt(['el Worker empezó', 'alguna tanda'], 1054, 328, 'start')
    co = d.caja(1450, 375, 270, 'Completado', [], VERDE, h=64)
    d.flecha([(pr['r'], 415), (co['x'], 415)])
    d.txt(['todas las tandas', 'terminaron bien'], 1325, 375)
    d.flecha([(1585, 375), (1585, 255), (1200, 255)])
    d.txt('se agregó una tanda nueva', 1390, 240)
    # fallas
    er = d.caja(460, 550, 300, 'Error', [], ROSA, h=64)
    d.flecha([(940, 439), (940, 590), (760, 590)], dash=True)
    d.txt(['alguna tanda', 'terminó en error'], 850, 540, 'middle')
    # usuario
    pa = d.caja(880, 715, 320, 'En pausa', [], AMBAR, dash=True, h=64)
    d.flecha([(1100, 439), (1100, 715)])
    d.txt(['alguna tanda', 'quedó en pausa'], 1114, 590, 'start')
    ca = d.caja(1450, 715, 270, 'Cancelado', [], CANCEL, h=64)
    d.flecha([(pa['r'], 755), (ca['x'], 755)])
    d.txt(['el usuario canceló', 'o pasaron 72 h'], 1325, 715)
    d.flecha([(880, 765), (260, 765), (260, 275), (880, 275)])
    d.txt('el usuario ajustó o confirmó el recuadro', 570, 750)
    # nota de prioridad (carril 1, a la derecha)
    d.txt(['El estado del experimento sale del estado de', 'sus tandas y gana el más grave:', 'error, cancelado, en pausa, procesando,', 'en cola y completado.'], 1280, 52, 'start')
    d.leyenda(865, [(GRIS, False, 'Subida'), (MORADO, False, 'Cola'), (AZUL, False, 'Procesando'), (VERDE, False, 'Completado'), (ROSA, False, 'Error'), (AMBAR, True, 'En pausa'), (CANCEL, False, 'Cancelado'), ('flecha', False, 'transición')])
    return d.pagina('Estados de un experimento')


if __name__ == '__main__':
    open(sys.argv[1], 'w', encoding='utf-8').write(experimento())
    print('ok')
