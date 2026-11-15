import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_cu_actores import construir

# Un diagrama por caso de uso (25 fichas del cap. 5): el caso de uso al centro, sus actores a la izquierda y,
# a la derecha, los casos de uso con los que se relaciona por <<include>> o <<extend>>. Uso:
#   python gen_cu_individuales.py CARPETA_SALIDA
N = {
    1: 'Iniciar sesión', 2: 'Cerrar sesión', 3: 'Recuperar contraseña', 4: 'Registrar experimento',
    5: 'Subir video', 7: 'Monitorear progreso del análisis', 8: 'Descargar reporte de diagnóstico',
    9: 'Consultar resultados del análisis', 10: 'Descargar reporte (PDF, CSV o XLSX)',
    11: 'Gestionar cuenta de usuario', 12: 'Crear cuenta de usuario', 13: 'Monitorear estado del sistema',
    14: 'Borrar video automáticamente', 15: 'Verificar pertenencia a Administrador',
    16: 'Cambiar contraseña al primer acceso', 17: 'Desactivar cuenta de usuario',
    18: 'Actualizar perfil propio', 19: 'Encolar análisis automático', 20: 'Notificar rechazo de video',
    22: 'Consultar lista de experimentos', 23: 'Eliminar experimento', 24: 'Gestionar experimentos globales',
    25: 'Revisar segundo a segundo', 26: 'Corregir etiqueta de un segundo',
    27: 'Consultar estadísticas de grupo o tanda'}


# Las claves de N, SPEC y cu() son los números anteriores; M da el número definitivo (sin hueco).
# orden de las fichas (numeración definitiva = posición en esta lista, empezando en 1; los valores son la numeración anterior)
ORDEN = [3, 1, 2, 15, 17, 4, 5, 18, 19, 20, 21, 6, 7, 8, 9, 25, 23, 24, 14, 10, 11, 16, 12, 22, 13]
_ACT = {v: i + 1 for i, v in enumerate(sorted(N))}          # clave de N -> numeración anterior
M = {v: ORDEN.index(_ACT[v]) + 1 for v in N}


def partir(t, n=22):
    """Parte un texto en líneas de hasta n caracteres."""
    out, cur = [], ''
    for w in t.split():
        if cur and len(cur) + 1 + len(w) > n:
            out.append(cur)
            cur = w
        else:
            cur = (cur + ' ' + w).strip()
    out.append(cur)
    return '\n'.join(out)


def cu(n):
    return ('CU-%02d\n' % M[n]) + partir(N[n])


# actores: 'I' Investigador (el Administrador lo hereda), 'A' solo Administrador, 'V' sin sesión, 'W' Worker
# rel: (texto, tipo, sentido): sentido 'in' = el otro apunta al caso (lo extiende o lo incluye);
#      'out' = el caso apunta al otro.
E = 'ext'
I = 'inc'
SPEC = {
    1: ('I', [(cu(16), E, 'in')], ''),
    2: ('I', [], ''),
    3: ('V', [], 'Al iniciar sesión (CU-02) pasa a ser Investigador o Administrador.'),
    4: ('I', [], ''),
    5: ('I', [(cu(19), E, 'in'), (cu(20), E, 'in')], ''),
    7: ('IW', [(cu(8), E, 'in')], 'Investigador: solo observa el avance. Worker: reporta cada etapa.'),
    8: ('IW', [(cu(7), E, 'out')], 'Solo cuando el análisis terminó en error.'),
    9: ('I', [(cu(27), E, 'in')], ''),
    10: ('I', [('Generar archivo\nde reporte', I, 'out')], ''),
    11: ('A', [('Listar usuarios', I, 'out'), (cu(12), E, 'in'), ('Editar datos\nde la cuenta', E, 'in'),
               ('Dar o quitar el rol\nde Administrador', E, 'in'), (cu(17), E, 'in'),
               ('Reactivar cuenta', E, 'in'), ('Generar contraseña\ntemporal nueva', E, 'in')], ''),
    12: ('A', [(cu(11), E, 'out')], ''),
    13: ('A', [('Notificar uso\nde disco', E, 'in')], ''),
    14: ('W', [], 'Se ejecuta de forma programada, sin intervención del usuario.'),
    15: ('A', [(cu(11), I, 'in'), (cu(12), I, 'in'), (cu(13), I, 'in'), (cu(17), I, 'in'), (cu(24), I, 'in')],
         'Regla de control de acceso: se aplica antes de cada acción de administración.'),
    16: ('I', [(cu(1), E, 'out')], ''),
    17: ('A', [(cu(11), E, 'out'), ('Seleccionar cuenta\nde la lista', I, 'out')], ''),
    18: ('I', [], ''),
    19: ('I', [(cu(5), E, 'out')], 'Solo si el video es del Día 2.'),
    20: ('I', [(cu(5), E, 'out')], ''),
    22: ('I', [('Filtrar experimentos', E, 'in'), ('Avisar expiración\nde video', E, 'in')], ''),
    23: ('I', [('Confirmar eliminación', I, 'out')], ''),
    24: ('A', [], ''),
    25: ('I', [(cu(26), E, 'in'), ('Reiniciar el análisis', E, 'in')],
         'Reiniciar: solo el creador del experimento o un Administrador.'),
    26: ('I', [(cu(25), E, 'out')], ''),
    27: ('I', [(cu(9), E, 'out')], ''),
}
ACT = {'I': 'Investigador', 'A': 'Administrador', 'V': 'Usuario\nsin sesión', 'W': 'Worker'}


def diagrama(n):
    quien, rels, nota = SPEC[n]
    ns = len(rels)
    alto = max(380 if quien in ('I', 'IW') else 330, 150 + ns * 95)
    cy = alto // 2
    con_sat = ns > 0
    ancho = 820 if con_sat else 640
    caja = (190, 20, 600 if con_sat else 410, alto - 40)
    cx = 350 if con_sat else 410
    nodos = {'C': (cu(n), cx, cy)}
    aristas = []
    if quien == 'I':
        actores = [('I', 'Investigador', 70, cy - 70, ''), ('A', 'Administrador', 70, cy + 110, '')]
        aristas += [('I', 'C', 'a'), ('A', 'I', 'gen')]
        nota = (nota + ' ' if nota else '') + 'El Administrador hereda este caso de uso.'
    elif quien == 'IW':
        actores = [('I', 'Investigador', 70, cy - 70, ''), ('W', 'Worker', 70, cy + 110, 'system')]
        aristas += [('I', 'C', 'a'), ('W', 'C', 'a')]
    else:
        k = quien
        actores = [(k, ACT[k], 70, cy, 'system' if k == 'W' else '')]
        aristas += [(k, 'C', 'a')]
    y0 = cy - (ns - 1) * 95 / 2
    for i, (txt, tipo, sent) in enumerate(rels):
        k = 'S%d' % i
        nodos[k] = (txt, 650, int(y0 + i * 95))
        aristas.append((k, 'C', tipo) if sent == 'in' else ('C', k, tipo))
    d = dict(titulo='CU-%02d — %s' % (M[n], N[n]), ancho=ancho, alto=alto, caja=caja, actores=actores,
             nodos=nodos, aristas=aristas)
    if nota:
        d['nota'] = (205, alto - 22, nota)
    return d


if __name__ == '__main__':
    out_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
    os.makedirs(out_dir, exist_ok=True)
    for n in SPEC:
        page, W, H = construir('cu%02d' % n, diagrama(n))
        open(os.path.join(out_dir, 'CU-%02d.html' % M[n]), 'w', encoding='utf-8').write(page)
        print('CU-%02d' % M[n], W, H)
