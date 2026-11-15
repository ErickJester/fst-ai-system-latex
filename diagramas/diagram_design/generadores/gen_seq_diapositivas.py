import os, re, sys

# Secuencias SIMPLIFICADAS para diapositiva (anexo de la presentación). Cada diagrama cuenta una sola idea, con pocos
# mensajes y texto corto. El detalle completo sigue en los diagramas del capítulo 5.
# Uso: python gen_seq_diapositivas.py CARPETA   (escribe un .puml por diagrama; el PNG lo genera PlantUML)
ACTOR = {
    'inv': 'actor Investigador as inv', 'admin': 'actor Administrador as admin', 'u': 'actor Usuario as u',
    'ui': 'participant "Interfaz web" as ui', 'api': 'participant Backend as api',
    'db': 'database "Base de datos" as db', 'fs': 'participant Archivos as fs', 'w': 'participant Worker as w',
}

# (id, título de la lámina, participantes, cuerpo)
D = []


def d(ident, titulo, parts, cuerpo):
    D.append((ident, titulo, parts, cuerpo))


T_CREAR = 'Secuencia: creación de cuenta por el administrador'
d('crear_1', T_CREAR, 'admin ui api db', """
admin -> ui: elige "Crear cuenta" y llena el formulario
ui -> api: envía identificador, nombre, apellidos y correo
api -> db: ¿es Administrador? ¿identificador o correo ya existen?
db --> api: sí / no
alt no es Administrador
  api --> ui: rechaza: no tiene permiso
else identificador o correo ya registrados
  api --> ui: informa el conflicto
  ui --> admin: muestra el error y no crea la cuenta
end
""")
d('crear_2', T_CREAR, 'admin ui api db', """
api -> api: genera una contraseña temporal
api -> db: crea el usuario como Investigador, activo y con cambio obligatorio
db --> api: confirma
api -> api: envía la contraseña temporal por correo
api --> ui: cuenta creada
ui --> admin: muestra la contraseña temporal una sola vez
""")

d('login', 'Secuencia: inicio de sesión', 'u ui api db', """
u -> ui: escribe su correo y su contraseña
ui -> api: envía correo y contraseña
api -> db: busca la cuenta con ese correo
db --> api: cuenta (contraseña cifrada, activa o no)
alt cuenta activa y contraseña correcta
  api --> ui: token de sesión, rol y si debe cambiar la contraseña
  alt debe cambiarla (primer acceso)
    ui --> u: pantalla de cambio de contraseña (CU-04)
  else
    ui --> u: lista de experimentos
  end
else correo no existe, cuenta inactiva o contraseña incorrecta
  api --> ui: error de credenciales (no dice cuál dato falló)
  ui --> u: "Correo o contraseña incorrectos"
end
""")

d('logout', 'Secuencia: cierre de sesión', 'u ui api', """
u -> ui: elige "Cerrar sesión" en el menú de usuario
ui -> api: avisa que el usuario cierra sesión
api --> ui: confirma
ui -> ui: el navegador olvida la sesión
ui --> u: muestra la pantalla de inicio de sesión
""")

T_PASS = 'Secuencia: cambio de contraseña'
d('pass_1', T_PASS, 'u ui api db', """
u -> ui: escribe la contraseña actual y la nueva
ui -> api: envía la actual y la nueva con la sesión del usuario
api -> db: lee la contraseña cifrada del usuario
db --> api: contraseña cifrada actual
alt la actual no coincide
  api --> ui: rechaza: la contraseña actual no es correcta
  ui --> u: muestra el error y no cambia nada
else la nueva no cumple (mínimo 8 caracteres, distinta de la actual)
  api --> ui: rechaza e indica el criterio incumplido
  ui --> u: pide escribir otra contraseña
end
""")
d('pass_2', T_PASS, 'u ui api db', """
api -> api: cifra la contraseña nueva
api -> db: guarda la nueva y quita el cambio obligatorio
db --> api: confirma
api --> ui: cambio realizado
alt viene del primer acceso (CU-04)
  ui --> u: confirma y muestra la lista de experimentos
else cambio voluntario desde el perfil (CU-05)
  ui --> u: confirma y se queda en Mi perfil
end
""")

T_GEST = 'Secuencia: gestión de usuarios (administrador)'
d('gest_1', T_GEST, 'admin ui api db', """
admin -> ui: abre el panel de usuarios
ui -> api: pide la lista de usuarios con la sesión del Administrador
api -> db: ¿es Administrador? Consulta todos los usuarios
db --> api: lista de usuarios
alt no es Administrador
  api --> ui: rechaza: no tiene permiso
  ui --> admin: muestra el error y no abre el panel
else es Administrador
  api --> ui: la lista de usuarios
  ui --> admin: muestra la tabla de usuarios
end
""")
d('gest_2', T_GEST, 'admin ui api db', """
admin -> ui: modifica nombre, apellidos o correo y confirma
ui -> api: pide guardar los cambios de la cuenta
api -> db: actualiza la cuenta
db --> api: confirma
api --> ui: confirma los cambios
ui --> admin: la tabla muestra los datos nuevos
""")
d('gest_2b', T_GEST, 'admin ui api db', """
admin -> ui: cambia el rol de otro usuario y confirma
ui -> api: pide el cambio de rol
api -> db: ¿quedaría al menos un Administrador activo?
alt no quedaría ninguno
  api --> ui: rechaza: debe existir al menos un Administrador
else sí quedaría
  api -> db: agrega o quita el rol
  ui --> admin: la tabla muestra el rol nuevo
end
""")
d('gest_3', T_GEST, 'admin ui api db', """
admin -> ui: elige un usuario y confirma la desactivación
ui -> api: pide desactivar la cuenta
alt es la propia cuenta del Administrador
  api --> ui: rechaza: "Para cambiar tu propia cuenta usa Mi perfil."
else es otra cuenta
  api -> db: ¿quedaría al menos un Administrador activo?
  alt no quedaría ninguno
    api --> ui: rechaza la desactivación
  else sí quedaría
    api -> db: marca la cuenta como inactiva
    api -> api: corta las sesiones activas de esa cuenta
    ui --> admin: usuario marcado como inactivo
  end
end
""")
d('gest_4', T_GEST, 'admin ui api db', """
alt reactivar una cuenta inactiva
  admin -> ui: elige el usuario inactivo y confirma
  ui -> api: pide reactivar la cuenta
  api -> db: marca la cuenta como activa
  ui --> admin: la tabla muestra la cuenta activa
else generar una contraseña temporal nueva
  admin -> ui: elige otro usuario (activo) y confirma
  ui -> api: pide la contraseña temporal
  api -> api: genera la contraseña y la envía por correo
  api -> db: la guarda y obliga a cambiarla en el siguiente acceso
  ui --> admin: confirma la acción
end
""")

d('perfil', 'Secuencia: configuración de perfil', 'u ui api db', """
u -> ui: abre su perfil desde el menú de usuario
ui --> u: muestra nombre, apellidos y correo de la sesión
u -> ui: modifica sus datos y confirma
ui -> api: envía los datos modificados
alt el correo no tiene un formato válido
  api --> ui: rechaza: el correo no es válido
else otra cuenta ya usa ese correo
  api --> ui: informa el conflicto y no aplica el cambio
else los datos son válidos
  api -> db: actualiza los datos del usuario
  ui --> u: la barra superior muestra los datos nuevos
end
""")

T_NOT = 'Secuencia: notificaciones'
d('notif_1', T_NOT, 'w db api ui u', """
w -> db: crea la notificación para el usuario
w -> w: envía también el aviso por correo
loop al entrar a cada pantalla y cada 30 s
  ui -> api: pide las notificaciones del usuario
  api -> db: busca las del usuario, las más recientes primero
  api --> ui: lista de notificaciones
  ui -> u: muestra el contador de no leídas
end
u -> ui: abre una notificación
ui -> api: la marca como leída
ui --> u: lleva a la pantalla de destino
""")
d('notif_2', T_NOT, 'u ui api db', """
opt marcar todas como leídas
  u -> ui: elige "Marcar todas como leídas"
  ui -> api: marca cada notificación no leída como leída
  api -> db: actualiza las notificaciones
  ui --> u: actualiza el contador
end
opt marcar una como no leída
  u -> ui: elige "Marcar como no leída"
  ui -> api: la marca como no leída
  api -> db: actualiza la notificación
end
""")

T_CARGA = 'Secuencia: carga de video'
d('carga_1', T_CARGA, 'inv ui api db', """
inv -> ui: elige el experimento y escribe el grupo
ui -> api: busca grupos que coincidan con lo escrito
api -> db: consulta los grupos del experimento
api --> ui: sugerencias, cada una con su tanda sugerida
alt hay un grupo con ese nombre
  inv -> ui: elige la sugerencia
  ui --> inv: precarga la tanda (editable) y pide confirmarla
else no hay grupo con ese nombre
  ui --> inv: pide los datos del grupo nuevo
end
inv -> ui: elige la sesión (Día 1 o Día 2) y el archivo
""")
d('carga_2', T_CARGA, 'inv ui api fs', """
ui -> ui: comprueba el formato del video
ui -> api: envía el video con su grupo, tanda y sesión
api -> api: comprueba que quien sube sea el creador del experimento
alt no es el creador
  api --> ui: "Solo quien creó el experimento sube sus videos."
else es el creador
  api -> fs: guarda el archivo en un espacio temporal
  api -> api: valida: se reproduce, es horizontal y tiene de 2 a 4 cilindros
  alt el archivo no pasa la validación
    api -> fs: descarta el archivo temporal
    api --> ui: rechaza, con el motivo
  end
end
""")
d('carga_3', T_CARGA, 'inv ui api db fs', """
api -> db: guarda grupo, tanda, especímenes y video en una sola operación
alt la tanda ya tiene un video de esa sesión
  api -> fs: descarta el archivo temporal
  api --> ui: rechaza: la tanda ya tiene un video de esa sesión
else se guarda
  api -> fs: mueve el archivo a su lugar definitivo
  alt el video es del Día 2
    api -> db: crea el análisis en cola
    ui --> inv: confirma y lleva a la pantalla de progreso
  else es del Día 1 (habituación)
    ui --> inv: confirma que el video quedó guardado; no se analiza
  end
end
""")

T_AN = 'Secuencia: análisis automático (worker)'
d('an_1', T_AN, 'w fs db', """
w -> db: al arrancar, pasa a "en cola" los análisis que quedaron "procesando"
w -> fs: revisa el espacio libre del disco (aviso al 80 %, limpieza al 90 %)
w -> db: toma el análisis más antiguo en cola
w -> db: lo marca como "procesando"
w -> fs: verifica los archivos del video, los especímenes y el modelo
w -> w: lee ancho, alto y duración del video
alt no se puede abrir el video
  w -> fs: guarda el reporte de diagnóstico (PDF)
  w -> db: marca "error" y crea la notificación
end
""")
d('an_2', T_AN, 'w fs db', """
w -> db: actualiza la etapa a "cilindros"
w -> w: alinea la cámara y construye el fondo del video
w -> w: ubica la línea de agua y separa los cilindros
w -> w: mide al espécimen en cada cilindro
alt los cilindros no coinciden con los especímenes
  w -> fs: guarda el reporte de diagnóstico (PDF)
  w -> db: marca "error" y crea la notificación
else pierde al espécimen 3 s seguidos
  w -> db: marca "en pausa" (ver pausa y ajuste del recuadro)
end
""")
d('an_3', T_AN, 'w fs db', """
w -> db: actualiza la etapa a "clasificación"
w -> w: la red clasifica cada segundo (conducta activa con la regla de 0.80)
w -> w: conserva los últimos 300 s de cada espécimen
w -> fs: guarda la copia del video y los recuadros de los cilindros
w -> db: guarda observaciones y segundos en una sola operación
w -> db: marca "completado" y deja el video para borrarse a los 30 días
w -> db: crea la notificación de análisis terminado
w -> w: envía el aviso por correo
""")
d('an_4', T_AN, 'w fs db', """
w -> fs: una vez al día, de madrugada, revisa el espacio libre del disco
alt hay poco espacio libre
  w -> db: crea el aviso de alerta de disco para los administradores
end
opt la limpieza borra videos antes de tiempo
  w -> fs: borra videos para liberar espacio
  w -> db: avisa al creador del experimento
end
w -> fs: borra los videos que cumplen 30 días
w -> db: hace el respaldo diario de la base de datos (se conservan 7 días)
""")

T_PROG = 'Secuencia: consulta de progreso y manejo de error'
d('prog_1', T_PROG, 'inv ui api db fs', """
inv -> ui: abre la pantalla de progreso del experimento
loop mientras la pantalla está abierta
  ui -> api: pide el estado de los análisis
  api -> db: busca los análisis del experimento
  api -> fs: lee el avance de cada análisis activo
  api --> ui: estado, etapa y porcentaje de cada análisis
  ui -> inv: actualiza la barra de progreso de cada video
end
""")
d('prog_2', T_PROG, 'inv ui', """
alt algún análisis llegó a "completado"
  ui -> inv: habilita el acceso a los resultados
else algún análisis quedó "en pausa"
  ui -> inv: muestra el enlace "Ajustar o cancelar"
else algún análisis quedó "cancelado"
  ui -> inv: muestra "El análisis se canceló."
else algún análisis llegó a "error"
  ui -> inv: muestra el error, con la etapa donde se detuvo
  ui -> inv: habilita la descarga del reporte de diagnóstico
end
""")
d('prog_3', 'Secuencia: consulta de progreso y manejo de error', 'inv ui api fs', """
inv -> ui: elige descargar el reporte de diagnóstico
ui -> api: pide el reporte de este análisis
api -> fs: busca el reporte
alt el reporte está listo
  api --> ui: reporte de diagnóstico
  ui --> inv: descarga inmediata en el navegador
else el Worker todavía no lo generó
  api --> ui: aún no está disponible
  ui -> api: reintenta, con un tope de intentos
end
""")

T_PAU = 'Secuencia: pausa, ajuste del recuadro y cancelación'
d('pau_1', T_PAU + ' (el Worker pausa)', 'w fs db', """
w -> w: ve 3 s seguidos sin ver al espécimen
w -> fs: guarda la imagen fija y los recuadros
w -> fs: guarda los datos de la pausa
w -> db: marca "en pausa"
w -> db: crea la notificación
w -> w: suelta el video y atiende el siguiente
""")
d('pau_2', T_PAU + ' (el usuario abre la pausa)', 'inv ui api db fs', """
inv -> ui: abre la notificación
ui -> api: pide los datos de la pausa
api -> db: lee el análisis
api -> fs: lee los datos y la imagen
api --> ui: imagen, recuadro y tiempo que queda
ui --> inv: muestra la imagen y tres botones: Ajustar, Continuar y Cancelar
""")
d('pau_3', T_PAU + ' (ajustar el recuadro)', 'inv ui api db fs', """
inv -> ui: arrastra el recuadro y pulsa Ajustar
ui -> api: envía el recuadro nuevo
api -> api: revisa el recuadro
alt el recuadro queda fuera de la imagen
  api --> ui: rechaza: queda fuera de la imagen
else casi no cambió (3 px o menos)
  api --> ui: rechaza: casi no cambió
else el recuadro es válido
  api -> fs: agrega el recuadro nuevo a la pausa
  api -> db: pasa a "en cola"
  ui --> inv: avisa que continuará cuando el sistema esté libre
end
""")
d('pau_4', T_PAU + ' (continuar o cancelar)', 'inv ui api db', """
alt el recuadro está bien
  inv -> ui: pulsa "El recuadro está bien, continuar"
  ui -> api: pide continuar
  api -> db: pasa a "en cola"
  ui --> inv: avisa que continuará
else cancelar el análisis
  inv -> ui: pulsa "Cancelar análisis" y confirma
  ui -> api: pide cancelar
  api -> db: pasa a "cancelado"
  ui --> inv: muestra el análisis como cancelado
end
""")
d('pau_5', T_PAU + ' (retomar o vencer)', 'w fs db', """
w -> db: toma el análisis en cola y lo marca "procesando"
w -> fs: lee los datos de la pausa
w -> w: procesa el video desde el principio con el recuadro corregido
loop en cada vuelta de la cola
  w -> db: busca los análisis "en pausa"
  opt pasaron más de 72 horas
    w -> db: pasa a "cancelado"
    w -> db: crea la notificación de análisis cancelado
  end
end
""")

T_RES = 'Secuencia: consulta de resultados'
d('res_1', T_RES, 'inv ui api db', """
inv -> ui: abre los resultados del experimento
ui -> api: pide los resultados
api -> db: busca los especímenes analizados y los segundos de cada conducta
db --> api: segundos por conducta de cada espécimen
api --> ui: resultados por espécimen
ui -> inv: muestra la tabla por espécimen, con su tanda y "Sin ver"
inv -> ui: elige ver el grupo completo o una tanda
ui -> ui: calcula media, desviación estándar y varianza
""")
d('res_2', T_RES, 'inv ui api db', """
ui -> api: pide la comparación entre grupos
api -> db: busca los grupos del experimento y sus tandas
loop por cada grupo
  api -> db: busca los especímenes y su video del Día 2
  alt el espécimen tiene el Día 2 analizado
    api -> db: cuenta los segundos de cada conducta
  else sin resultado del Día 2
    api -> api: lo marca como dato faltante
  end
end
""")
d('res_3', T_RES, 'inv ui api', """
api -> api: calcula media, desviación estándar y varianza por conducta
alt el grupo mezcla niveles de clasificación
  api -> api: no promedia el grupo: lo separa por tanda
end
api --> ui: comparación entre grupos en las cuatro conductas
ui -> inv: muestra la comparación (solo Día 2) y avisa de los faltantes
inv -> ui: descarga en CSV o XLSX lo que ve
""")

T_REV = 'Secuencia: revisión segundo a segundo'
d('rev_1', T_REV, 'u ui api db fs', """
u -> ui: elige "Revisar segundo a segundo"
ui -> api: pide los datos de la revisión
api -> db: ¿análisis completado? ¿el usuario subió el video o es Administrador?
alt el análisis no está completado
  api --> ui: rechaza la petición
  ui --> u: muestra el motivo
else está completado
  api -> db: consulta las etiquetas de cada segundo
  api -> fs: lee los recuadros de los cilindros
  api --> ui: duración, especímenes, etiquetas y recuadros
  ui -> api: pide el video con un permiso temporal
  api --> ui: video por partes (se puede adelantar y retroceder)
end
""")
d('rev_2', T_REV, 'u ui api db fs', """
u -> ui: elige una conducta o "No se ve" para un segundo
ui -> ui: guarda un borrador en el navegador
u -> ui: elige "Guardar"
ui -> api: envía las correcciones (espécimen, segundo, conducta)
api -> db: actualiza la conducta y el origen de cada segundo
api -> db: recalcula el nivel de clasificación
api -> db: borra los reportes guardados del experimento
api --> ui: guardado, con los totales recalculados
ui --> u: confirma que se guardó
""")
d('rev_3', T_REV, 'u ui api db fs', """
u -> ui: elige "Reiniciar el análisis"
ui --> u: avisa que se borran el resultado y toda la revisión
u -> ui: confirma el reinicio
ui -> api: pide reiniciar el análisis del video
api -> fs: borra los resultados de la corrida anterior
api -> db: borra el resultado y la revisión; deja el análisis "en cola"
ui --> u: lleva a la pantalla de progreso
""")

T_REP = 'Secuencia: descarga de reportes'
d('rep_1', T_REP, 'inv ui api db', """
inv -> ui: elige el formato (CSV, XLSX o PDF) en resultados
ui -> api: pide el reporte en ese formato
api -> db: ¿hay análisis completados en el experimento?
alt no hay análisis completados
  alt CSV o XLSX
    api --> ui: rechaza la descarga, con el motivo
    ui --> inv: muestra que no hay resultados todavía
  else PDF
    api --> ui: documento "Sin resultados"
    ui --> inv: descarga ese documento
  end
end
""")
d('rep_2', T_REP, 'inv ui api db fs', """
api -> db: ¿ya hay un reporte guardado en ese formato y vista?
alt no hay, o ya no sirve
  api -> api: genera el archivo con los datos actuales
  api -> fs: guarda el archivo
  api -> db: registra el reporte nuevo
else ya hay uno vigente
  api -> fs: recupera el archivo guardado
end
api --> ui: archivo listo
ui --> inv: descarga inmediata en el navegador
""")


# subtítulo de cada parte, para que ninguna lámina se vea suelta
DESC = {
    'crear_1': 'validaciones', 'crear_2': 'alta de la cuenta',
    'pass_1': 'validar las contraseñas', 'pass_2': 'guardar y volver',
    'gest_1': 'abrir el panel', 'gest_2': 'editar datos', 'gest_2b': 'dar o quitar el rol',
    'gest_3': 'desactivar una cuenta', 'gest_4': 'reactivar o contraseña temporal',
    'notif_1': 'crear y consultar', 'notif_2': 'marcar como leída o no leída',
    'carga_1': 'elegir grupo y tanda', 'carga_2': 'validar el archivo', 'carga_3': 'guardar y encolar',
    'an_1': 'toma del análisis y preprocesamiento', 'an_2': 'localización de cilindros',
    'an_3': 'clasificación y cierre', 'an_4': 'tareas diarias',
    'prog_1': 'seguir el avance', 'prog_2': 'según el estado', 'prog_3': 'descargar el diagnóstico',
    'res_1': 'por espécimen', 'res_2': 'comparación entre grupos', 'res_3': 'estadísticas y descarga',
    'rev_1': 'abrir la revisión', 'rev_2': 'corregir y guardar', 'rev_3': 'reiniciar el análisis',
    'rep_1': 'pedir el reporte', 'rep_2': 'generar o reutilizar',
}


def envolver(t, n=40):
    out, cur = [], ''
    for w in t.split():
        if cur and len(cur) + 1 + len(w) > n:
            out.append(cur)
            cur = w
        else:
            cur = (cur + ' ' + w).strip()
    out.append(cur)
    return '\\n'.join(out)


PAT = re.compile(r'^(\s*)(\w+) (-->|->) (\w+): (.*)$')


def cuerpo_envuelto(c):
    res = []
    for l in c.strip('\n').split('\n'):
        m = PAT.match(l)
        res.append('%s%s %s %s: %s' % (m.group(1), m.group(2), m.group(3), m.group(4), envolver(m.group(5))) if m else l)
    return '\n'.join(res)


if __name__ == '__main__':
    carpeta = sys.argv[1]
    os.makedirs(carpeta, exist_ok=True)
    meta = []
    for ident, titulo, parts, cuerpo in D:
        src = '@startuml %s\n!include ../estilo_doc.iuml\nskinparam dpi 200\n' % ident
        src += '\n'.join(ACTOR[p] for p in parts.split()) + '\n\n' + cuerpo_envuelto(cuerpo) + '\n@enduml\n'
        open(os.path.join(carpeta, ident + '.puml'), 'w', encoding='utf-8').write(src)
        desc = DESC.get(ident)
        meta.append((ident, '%s (%s)' % (titulo, desc) if desc and '(' not in titulo else titulo))
    import json
    json.dump(meta, open(os.path.join(carpeta, 'indice.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(len(D), 'diagramas')
