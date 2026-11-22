"""Tres diagramas de estados más, en carriles de colores: ciclo de vida del video, estados de una cuenta y origen
de un segundo en la revisión. Fuentes: RN-05, RN-06, RN-09, RF-03, RF-05, RN-16 (cap. 4) y secciones de cuentas y revisión
(cap. 6). Uso: gen_estados_extra_carriles.py CARPETA"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_diapo_carriles import Lienzo, GRIS, AZUL, MORADO, ROSA, AMBAR, VERDE, INK

CANCEL = ('#fff7e8', '#f1d9a8', '#c99a2e', '#fbd5de', '#c0405f')


def fin(d, cx, cy):
    d.o.append(f'<circle cx="{cx}" cy="{cy}" r="15" fill="#fff" stroke="{INK}" stroke-width="2"/><circle cx="{cx}" cy="{cy}" r="8.5" fill="{INK}"/>')


def inicio(d, cx, cy):
    d.o.append(f'<circle cx="{cx}" cy="{cy}" r="12" fill="{INK}"/>')


# ---------------------------------------------------------------- ciclo de vida del video
def video():
    d = Lienzo(1800, 900)
    L = [(15, 195), (210, 390), (405, 585), (600, 810)]
    d.carril(*L[0], 'Archivo', GRIS)
    d.carril(*L[1], 'Análisis', AZUL)
    d.carril(*L[2], 'Retención', AMBAR)
    d.carril(*L[3], 'Borrado', ROSA)
    inicio(d, 125, 105)
    su = d.caja(330, 70, 330, 'Subido', ['el video se guardó'], GRIS, h=102)
    d.flecha([(137, 105), (330, 105)])
    d.txt(['se subió', 'el video'], 233, 62)
    an = d.caja(330, 252, 330, 'Analizado', ['con copia de revisión'], AZUL, h=102)
    d.flecha([(495, 172), (495, 252)])
    d.txt(['el análisis terminó', 'con éxito'], 510, 205, 'start')
    pv = d.caja(330, 447, 330, 'Por vencer', ['aviso en la interfaz'], AMBAR, dash=True, h=102)
    d.flecha([(495, 354), (495, 447)])
    d.txt(['quedan 7 días para', 'el borrado'], 510, 392, 'start')
    bo = d.caja(330, 660, 330, 'Borrado', ['no se puede deshacer'], CANCEL, h=102)
    d.flecha([(495, 549), (495, 660)])
    d.txt(['se cumplieron 30 días', 'del análisis'], 510, 598, 'start')
    fin(d, 240, 711)
    d.flecha([(330, 711), (256, 711)])
    # excepciones
    d.flecha([(660, 303), (1010, 303), (1010, 700), (660, 700)], dash=True)
    d.txt(['el disco pasó del 90 %: se adelanta', 'el borrado de los más antiguos y se', 'avisa al investigador'], 1310, 410, 'start')
    d.flecha([(660, 120), (1280, 120), (1280, 740), (660, 740)], dash=True)
    d.txt(['se eliminó el experimento'], 1310, 650, 'start')
    # nota
    d.txt(['Los resultados y los reportes se conservan', 'aunque el video ya se haya borrado.'], 1010, 55, 'start')
    d.leyenda(865, [(GRIS, False, 'Subido'), (AZUL, False, 'Analizado'), (AMBAR, True, 'Por vencer'), (CANCEL, False, 'Borrado'), ('flecha', False, 'transición'), ('falla', False, 'excepción')])
    return d.pagina('Ciclo de vida del video')


# ---------------------------------------------------------------- estados de una cuenta
def cuenta():
    d = Lienzo(1800, 900)
    L = [(15, 165), (180, 330), (345, 495), (510, 825)]
    d.carril(*L[0], 'Alta', GRIS)
    d.carril(*L[1], 'Uso', AZUL)
    d.carril(*L[2], 'Baja', AMBAR)
    d.carril(*L[3], 'Recuperación', MORADO)
    inicio(d, 125, 90)
    ct = d.caja(330, 58, 430, 'Con contraseña temporal', [], GRIS, h=64)
    d.flecha([(137, 90), (330, 90)])
    d.txt(['el administrador', 'creó la cuenta'], 233, 48)
    ac = d.caja(330, 218, 430, 'Activa', [], AZUL, h=64)
    d.flecha([(500, 122), (500, 218)])
    d.txt(['el usuario la cambió en', 'su primer ingreso'], 486, 160, 'end')
    d.flecha([(620, 218), (620, 122)])
    d.txt(['el administrador generó', 'otra contraseña temporal'], 634, 160, 'start')
    ia = d.caja(330, 385, 430, 'Inactiva', [], CANCEL, h=64)
    d.flecha([(500, 282), (500, 385)])
    d.txt(['el administrador', 'la desactivó'], 486, 328, 'end')
    d.flecha([(620, 385), (620, 282)])
    d.txt(['el administrador', 'la reactivó'], 634, 328, 'start')
    d.txt(['El sistema nunca borra cuentas.', 'No se desactiva la última cuenta de', 'administrador activa ni la propia.'], 840, 380, 'start')
    # recuperación
    d.flecha([(ac['r'], 250), (1210, 250), (1210, 570)])
    d.txt('pidió recuperar la contraseña', 985, 235, 'middle')
    ev = d.caja(1010, 570, 400, 'Enlace vigente', ['dura 60 minutos'], MORADO, h=102)
    us = d.caja(1580, 590, 190, 'Usado', [], VERDE, h=64)
    d.flecha([(ev['r'], 622), (us['x'], 622)])
    d.txt(['cambió la', 'contraseña'], 1495, 580, 'middle')
    vc = d.caja(1010, 730, 400, 'Vencido', [], GRIS, h=64)
    d.flecha([(1210, 672), (1210, 730)])
    d.txt('pasaron 60 minutos', 1226, 708, 'start')
    d.txt(['El enlace sirve una sola vez.'], 1480, 760, 'start')
    d.leyenda(865, [(GRIS, False, 'Con contraseña temporal'), (AZUL, False, 'Activa'), (CANCEL, False, 'Inactiva'), (MORADO, False, 'Enlace vigente'), (VERDE, False, 'Usado'), ('flecha', False, 'transición')])
    return d.pagina('Estados de una cuenta')


# ---------------------------------------------------------------- origen de un segundo
def segundo():
    d = Lienzo(1800, 900)
    L = [(15, 235), (250, 500), (515, 800)]
    d.carril(*L[0], 'Sistema', AZUL)
    d.carril(*L[1], 'Revisión', AMBAR)
    d.carril(*L[2], 'Reinicio', GRIS)
    inicio(d, 125, 125)
    ma = d.caja(720, 85, 360, 'De la máquina', ['la conducta la puso el sistema'], AZUL, h=102)
    d.flecha([(137, 125), (720, 125)])
    d.txt('el clasificador analizó el segundo', 430, 108, 'middle')
    xs = [380, 900, 1420]
    nombres = [('Confirmado', ['la conducta se conserva'], VERDE, 'el usuario confirma la conducta'), ('Corregido', ['reemplaza la conducta'], AMBAR, 'el usuario cambia la conducta'), ('Dudoso', ['sin conducta'], CANCEL, 'el usuario marca «No se ve»')]
    cajas = []
    for x, (t, ls, c, et) in zip(xs, nombres):
        cajas.append(d.caja(x - 170, 335, 340, t, ls, c, h=102))
    ym = 262
    d.flecha([(900, 187), (900, ym), (380, ym), (380, 335)])
    d.flecha([(900, 187), (900, 335)])
    d.flecha([(900, 187), (900, ym), (1420, ym), (1420, 335)])
    d.txt('el usuario confirma la conducta', 640, 250, 'middle')
    d.txt('el usuario cambia la conducta', 914, 305, 'start')
    d.txt('el usuario marca «No se ve»', 1160, 250, 'middle')
    # reinicio
    yb = 610
    for x in xs:
        d.flecha([(x, 437), (x, yb)]) if False else None
    d.o.append(f'<path d="M380,437 L380,{yb} M900,437 L900,{yb} M1420,437 L1420,{yb}" fill="none" stroke="{INK}" stroke-width="2" stroke-dasharray="8,6"/>')
    d.flecha([(1420, yb), (180, yb), (180, 160), (720, 160)], dash=True)
    d.txt('se reinició el análisis y los segundos vuelven a salir de la máquina', 800, 592, 'middle', fondo='#f3f4f6')
    d.txt(['Solo se puede revisar un análisis completado.', 'Al guardar, el nivel del análisis se recalcula.', 'El origen conserva que el segundo fue revisado.'], 130, 700, 'start')
    d.leyenda(865, [(AZUL, False, 'De la máquina'), (VERDE, False, 'Confirmado'), (AMBAR, False, 'Corregido'), (CANCEL, False, 'Dudoso'), ('flecha', False, 'transición'), ('falla', False, 'reinicio')])
    return d.pagina('Origen de un segundo en la revisión')


if __name__ == '__main__':
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    for n, f in (('video', video), ('cuenta', cuenta), ('segundo', segundo)):
        open(os.path.join(out, n + '.html'), 'w', encoding='utf-8').write(f())
        print(n)
