# 07 — Diagramas de flujo, pipeline, casos de uso, secuencia, estados y arquitectura (reauditoría, HEAD 975ec4c)

Prefijo de IDs: `DF-`. Pasada independiente sobre los archivos tal como están hoy; al final se marcó `Previo:` contra `hallazgosAgentes11oct/07_diagramas-flujo-cu-secuencia.md`.

## Alcance auditado
- `.puml`: `pipeline`, `flujo_general`, `estados_analisis`, `estados_experimento`, `arquitectura_software`, `ciclo_vida_experimento` (huérfano), los 11 `seq_*.puml` y `puml/cu_*.puml` (6).
- `diagramas/diagram_design/`: los `.md` y los generadores de `flujo_sistema`, `pipeline_analisis`, `arquitectura_capas`, `despliegue`.
- LaTeX: cap. 4 (RF/RN) y cap. 5 (arquitectura, pipeline, estados, fichas CU-01 a CU-27, pies de figura, sección de secuencias).
- PNG abiertos y comparados: `flujo_general`, `arquitectura_software`, `pipeline`, `estados_analisis`, `estados_experimento`, `seq_notificaciones`, `seq_perfil`, `seq_cambio_pass_inv`, `seq_consulta_resultados`.

## Conteos

| Severidad | Cantidad |
|-----------|----------|
| Alta | 2 |
| Media | 13 |
| Baja | 5 |
| **Total** | **20** (2 son pregunta abierta: DF-09, DF-18) |

Nota única «D-5x pendiente de propagar»: los diagramas que dejan fuera revisión/corrección, copia H.264 y reinicio (D-57 a D-60) no se cuentan como hallazgos.

---

## Severidad Alta

### DF-01 — El texto del cap. 5 dice que la «anotación experta» alimenta el entrenamiento
- Severidad: Alta
- Ubicación: `chapters/05_diseno.tex:100-102`; `diagramas/flujo_general.puml:69`; `diagramas/diagram_design/flujo_sistema.md` («Diferencias con flujo_general.puml»)
- Cita: LaTeX «el ciclo de entrenamiento del modelo ---anotación experta, dataset y entrenamiento--- alimenta al clasificador de conducta» / figura «SIN anotación del Dr. Sandino, ni para entrenar ni para probar»
- Fuente que decide: D-26 y D-56 (rango 1), `CLAUDE.md` (entrenamiento sin las anotaciones del laboratorio).
- Destinatario: Erick
- Previo: DF-01
- Corrección sugerida: «el ciclo de entrenamiento del modelo ---clips etiquetados por el equipo, entrenamiento y evaluación--- alimenta al clasificador de conducta».

### DF-02 — La figura de arquitectura muestra «corrección CLAHE», `_tracked.mp4`, solo `.mp4` y SQL
- Severidad: Alta
- Ubicación: `diagramas/arquitectura_software.puml:79,87,101,116` (y `figures/mermaid/arquitectura_software.png`, que lo muestra igual); `chapters/05_diseno.tex:158-160`, `:97` (RN-10 en `04_analisis.tex:561`)
- Cita: figura «Preprocesamiento y correccion CLAHE», «Videos anotados  _tracked.mp4», «Validacion de archivos .mp4», «(INSERT, estado = en cola)» / LaTeX «El sistema no aplica ninguna corrección de contraste ni de iluminación»; RN-10 «.mp4 o .mov»
- Fuente que decide: CLA-04 y D-16 (sin CLAHE ni tracker), D-30 (`.mp4` y `.mov`), `CLAUDE.md` (sin SQL en diagramas).
- Destinatario: Erick
- Previo: DF-02, DF-15 (y SQL: nuevo como cita; antes DF-18 no lo incluía)
- Corrección sugerida: «Preprocesamiento (registro de cámara y modelo de fondo)», «Videos anotados», «Validación de los archivos de video», flecha «encola el análisis (estado «en cola»)»; regenerar el PNG. El PNG tampoco tiene acentos (ver DF-16) y rotula «HTTPS», que ningún capítulo menciona.

---

## Severidad Media

### DF-03 — `seq_consulta_resultados` reduce «agrupado» a dos conductas y omite la conducta activa
- Severidad: Media
- Ubicación: `diagramas/seq_consulta_resultados.puml:74,86-88,92-96` (PNG igual); `chapters/04_analisis.tex:581-586` (RN-13), `chapters/05_diseno.tex:1743`/CU-09 paso 3
- Cita: «segundos de nado activo, inmovilidad y escalamiento», «comparación entre grupos en dos conductas» / «tres conductas» / RN-13 «Un mismo análisis puede mezclar las cuatro conductas» y CU-09 «nado activo, inmovilidad, escalamiento y conducta activa»
- Fuente que decide: D-29 y D-41 (`agrupado` = algún segundo quedó como conducta activa; la interfaz solo avisa).
- Destinatario: Erick
- Previo: DF-03
- Corrección sugerida: la consulta devuelve las cuatro conductas; el aviso de nivel indica solo que hay segundos de «conducta activa». Quitar «en dos/tres conductas».

### DF-04 — «Los tres grupos del experimento» en dos secuencias
- Severidad: Media
- Ubicación: `diagramas/seq_consulta_resultados.puml:64,66,91`; `diagramas/seq_descarga_reportes.puml:81`; `diagramas/grafo_relacional_3_vigente.puml` (`EXPERIMENTO "1" --o "3..*" GRUPO`)
- Cita: «busca los tres grupos del experimento», «muestra la comparación de los tres grupos» / modelo «tres o más grupos»
- Fuente que decide: `PENDIENTES.md` («Lo que ya está decidido», tres o más grupos) y grafo vigente.
- Destinatario: Erick
- Previo: DF-07
- Corrección sugerida: «busca los grupos del experimento (control, referencia, tratamiento; un tipo puede repetirse)».

### DF-05 — Códigos internos (D-xx, Q-E) visibles dentro de las figuras
- Severidad: Media
- Ubicación: `estados_analisis.puml:16` (D-23); `seq_consulta_progreso.puml:79` (D-22), `:91` (D-23); `seq_consulta_resultados.puml:80` (Q-E), `:93` (D-41); `seq_crear_cuenta.puml:58` (D-12), `:89` (D-45); `seq_descarga_reportes.puml:68,81` (D-21, «ver encabezado»)
- Cita: «se generó el reporte de diagnostico (D-23)», «un tercio por etapa (D-22)», «-- Q-E)», «(D-12, ocultamiento en la interfaz)»
- Fuente que decide: `PENDIENTES.md` (reglas de diagramas: lenguaje natural, sin referencias internas).
- Destinatario: Erick
- Previo: DF-08
- Corrección sugerida: quitar los códigos del texto visible; las referencias a RN/RF/CU sí pueden quedar.

### DF-06 — Código, rutas HTTP y nombres de columna visibles en las secuencias
- Severidad: Media
- Ubicación: `diagramas/seq_gestion_usuarios.puml:46,60,75`; `seq_crear_cuenta.puml:69,84`; `seq_consulta_progreso.puml:91`; `seq_analisis_automatico.puml:97`
- Cita: «GET /admin/usuarios», «PATCH /admin/usuarios/{id} {activo: false}», «200 OK {usuarios…}», «contrasenaHash, activo = sí, cambioRequerido = sí», «ANALISIS.rutaDiagnostico», «(rutaDiagnostico)»
- Fuente que decide: `CLAUDE.md` («Reglas de diagramas»: sin SQL ni código).
- Destinatario: Erick
- Previo: DF-18
- Corrección sugerida: «consulta los usuarios», «marca la cuenta como inactiva», «crea la cuenta con contraseña temporal y cambio obligatorio»; nombres de tabla como `USUARIO` pueden quedar si el LaTeX los usa, no los nombres de columna.

### DF-07 — Las secuencias de notificaciones, perfil y cambio de contraseña no tienen `.puml` y son del 8-may; ninguna muestra el correo
- Severidad: Media
- Ubicación: `figures/mermaid/seq_notificaciones.png`, `seq_perfil.png`, `seq_cambio_pass_inv.png` (git 05-08, sin fuente en `diagramas/`); `chapters/04_analisis.tex:292-298` (RF-33); `chapters/05_diseno.tex:2373-2376`, `:2358`
- Cita: PNG «Actualiza estado del video como completado», «Registra notificacion de analisis finalizado» (sin correo, sin error ni disco), «Obtiene nombre, correo y rol del usuario» / RF-33 «por correo electrónico… si el envío falla, el aviso permanece en el panel»; D-08: `USUARIO` no tiene columna rol
- Fuente que decide: D-45 y D-08 (rango 1).
- Destinatario: Erick
- Previo: DF-10 (en parte; `seq_perfil` y rol: nuevo)
- Corrección sugerida: rehacer los tres en PlantUML. Notificaciones: crear el aviso para análisis terminado, error y alerta de disco; enviarlo también por correo; si falla, queda en el panel. Perfil: quitar «rol». Los tres carecen de acentos y del patrón «Interfaz web / Backend / Base de datos» del resto.

### DF-08 — `seq_analisis_automatico` no envía correo, usa «tubos» y fija «5 intervalos»
- Severidad: Media
- Ubicación: `diagramas/seq_analisis_automatico.puml:77,85,88,93-94,99`; `chapters/04_analisis.tex:292-296` (RF-33); `chapters/05_diseno.tex:2352` (CU-14)/D-54
- Cita: «crea la notificación de análisis terminado», «guarda sus 5 intervalos», «los recuadros de los tubos» / RF-33 «también por correo electrónico»; el propio diagrama dice «como máximo; si el video dura menos, todos»
- Fuente que decide: D-45 (correo), D-54 (sin mínimo de 300 s, luego pueden ser menos de 5 minutos).
- Destinatario: Erick
- Previo: DF-10, DF-24 (parcial)
- Corrección sugerida: añadir «envía la notificación por correo (si falla, queda en el panel)»; «sus intervalos (uno por minuto analizado)»; «cilindros» en lugar de «tubos» (también en `seq_revision_segundos.puml:43`, `estados_analisis.puml:12,16`, flujo y API del cap. 5).

### DF-09 — Salidas del módulo 4 distintas en cuatro figuras (video anotado, medidas por cuadro)
- Severidad: Media (pregunta abierta → tú y el usuario)
- Ubicación: `chapters/05_diseno.tex:242-248` y `pipeline.puml:79` (video anotado y medidas por cuadro); `seq_analisis_automatico.puml:88-89` (recuadros y copia recortada, sin medidas por cuadro); `diagram_design/pipeline_analisis.md` («Video anotado… se quitó porque el código no lo genera»); `flujo_sistema` / `gen_flujo.py:65` («video anotado»)
- Cita: «el video anotado y las medidas por cuadro» / «guarda los recuadros de los tubos… recorta el video a esos mismos últimos 300 s»
- Fuente que decide: pregunta abierta → tú y el usuario (qué guarda realmente el worker). D-57 a D-60 pendientes de propagar para la copia reproducible.
- Destinatario: Erick
- Previo: DF-14
- Corrección sugerida: decidir una lista única de salidas y alinear cap. 5 módulo 4, `pipeline.puml`, `seq_analisis_automatico`, `seq_revision_segundos` y las figuras de `diagram_design`.

### DF-10 — `seq_carga_video` valida la extensión en el servidor; D-64 la asigna a la interfaz
- Severidad: Media
- Ubicación: `diagramas/seq_carga_video.puml:66,69`; `chapters/05_diseno.tex:1360-1369` (CU-05 paso 6 y alterno), `chapters/04_analisis.tex:561-565` (RN-10)
- Cita: «valida formato (.mp4 o .mov), reproducibilidad y que el video esté en horizontal» / CU-05 «la interfaz ya comprobó que fuera .mp4 o .mov antes de enviarlo»
- Fuente que decide: D-64 (usuario, 11-oct): extensión en la interfaz; orientación y reproducibilidad en el servidor. La propia D-64 anota `seq_carga_video.puml` como pendiente.
- Destinatario: Erick
- Previo: DF-11
- Corrección sugerida: la interfaz comprueba la extensión antes de enviar; el backend valida reproducibilidad y orientación. Misma nota para `flujo_sistema.md` («valida formato y orientación») y `CU-20` (precondición «formato… en el servidor»).

### DF-11 — `estados_analisis` solo permite el error saliendo de «cilindros»
- Severidad: Media
- Ubicación: `diagramas/estados_analisis.puml:12,16` (PNG igual); `chapters/05_diseno.tex:132-134`, `:300-304`
- Cita: «cilindros --> error : [no se pudo abrir el video o no se hallaron los tubos]» / «si el archivo no se puede abrir, el pipeline se detiene» (en preprocesamiento)
- Fuente que decide: RN-11 y D-47 (dos errores, uno por etapa).
- Destinatario: Erick
- Previo: DF-12
- Corrección sugerida: dos transiciones: `preprocesamiento --> error [no se pudo abrir el video]` y `cilindros --> error [no se hallaron los cilindros]`.

### DF-12 — Fichas CU-11 y CU-12 bajo «Paquete 5»; los diagramas y la introducción del paquete 1 las ponen en el paquete 1
- Severidad: Media
- Ubicación: `chapters/05_diseno.tex:1882-1884,1941` (encabezado «Paquete 5» antes de CU-11 y CU-12); `diagramas/puml/cu_paquete1.puml:20-21`; `chapters/05_diseno.tex:781-783` (intro P1: «crear y desactivar»)
- Cita: ficha «Paquete 5: … Gestionar cuenta de usuario (CU-11)» / figura «Paquete 1 … CU-11 Gestionar cuenta de usuario, CU-12 Crear cuenta de usuario»
- Fuente que decide: los diagramas (casos de uso de Vanesa) y la intro del paquete 1.
- Destinatario: Vanesa
- Previo: DF-09
- Corrección sugerida: mover las fichas CU-11 y CU-12 al final del paquete 1 (o corregir la figura); CU-13, CU-22, CU-23, CU-24 y CU-14 quedan en el 5.

### DF-13 — `cu_paquete4`: «Desglosar por minuto» como `<<extend>>` opcional y «Comparar grupos en Dia 2» como caso aparte
- Severidad: Media
- Ubicación: `diagramas/puml/cu_paquete4.puml:14-15,23,26`; `chapters/05_diseno.tex:1738-1748` (CU-09 pasos 4 y 5), `chapters/04_analisis.tex:193-200` (RF-20)
- Cita: «UC42 ..> CU09 : <<extend>> [solicita desglose]», «INV --> UC43» / CU-09 curso normal «4 Muestra el desglose de conductas por minuto», «5 Muestra la comparación entre grupos»
- Fuente que decide: `PENDIENTES.md` («El desglose por minuto es obligatorio, no opcional»).
- Destinatario: Vanesa
- Previo: nuevo
- Corrección sugerida: el desglose y la comparación son pasos del curso normal de CU-09; quitar el `<<extend>>` de «Desglosar por minuto» y asociar la comparación a CU-09 en lugar de a un caso suelto.

### DF-14 — Referencia a CU-21, que ya no existe
- Severidad: Media
- Ubicación: `chapters/05_diseno.tex:320`; `PENDIENTES-VANESA.md:145`
- Cita: «(ver CU-21, RF-23)» / «CU-21 ya no existe (se fusionó en CU-22, 5-oct)»
- Fuente que decide: `PENDIENTES-VANESA.md` (rango 5, pero ya registrado) y fichas vigentes (CU-22).
- Destinatario: Vanesa (anotación) / Erick (el texto es de su zona)
- Previo: nuevo
- Corrección sugerida: «(ver CU-22, RF-23)».

### DF-15 — Diagrama de despliegue con el servidor institucional ESCOM; D-62 lo excluye del documento
- Severidad: Media
- Ubicación: `diagramas/diagram_design/despliegue.md`, `generadores/gen_despliegue.py:45-46` («Servidor institucional ESCOM · Docker Compose»); `chapters/05_diseno.tex:23,30` (menciones de «vista de despliegue» y «complejidad en el despliegue»)
- Cita: «Es la vista de despliegue que pide la ISO/IEC/IEEE 42010», «el despliegue permanente… está fuera del alcance» (y aun así se dibuja)
- Fuente que decide: D-62 (usuario, 11-oct): el despliegue queda fuera y no se registra en el documento. Hoy la figura no entra a `main.tex`; D-62 ya anota «pendiente: RNF-10 y las menciones del cap. 5».
- Destinatario: Erick
- Previo: nuevo
- Corrección sugerida: no incluir la figura; retirar del cap. 5 «y de despliegue» (línea 23) y «en el despliegue» (línea 30); si se conserva `despliegue` como material interno, quitar «Servidor institucional ESCOM».

---

## Severidad Baja

### DF-16 — Textos de figuras sin acentos ni eñes
- Severidad: Baja
- Ubicación: `diagramas/puml/cu_*.puml` (títulos y casos: «Autenticacion», «contrasena», «analisis», «Dia 2», «diagnostico»); `arquitectura_software.puml:71-105` («Visualizacion», «correccion», «evaluacion»); `estados_analisis.puml:16` («diagnostico»); `seq_notificaciones.png`, `seq_perfil.png`, `seq_cambio_pass_inv.png`
- Cita: «CU-03 Recuperar contrasena», «Reportes de diagnostico PDF»
- Fuente que decide: ortografía (el LaTeX escribe «contraseña», «análisis»).
- Destinatario: Vanesa (cu_*) / Erick (resto)
- Previo: DF-19
- Corrección sugerida: poner acentos y eñes y regenerar los PNG (`gen_pngs.sh`).

### DF-17 — `flujo_general` dibuja tres conductas, sin camino de error, y «Preprocesamiento (cuadros y limpieza)»
- Severidad: Baja
- Ubicación: `diagramas/flujo_general.puml:93-94` (y PNG); `chapters/05_diseno.tex:130-160`, `04_analisis.tex:166-172`
- Cita: «Clasificación de conducta (nado activo, inmovilidad, escalamiento)» / RF-17 «una cuarta conducta», RN-07 cuatro conductas
- Fuente que decide: D-29, RN-13.
- Destinatario: Erick
- Previo: DF-06
- Corrección sugerida: «(nado activo, inmovilidad, escalamiento y conducta activa)»; «Preprocesamiento (registro de cámara y modelo de fondo)». `diagram_design/flujo_sistema` ya lo hace.

### DF-18 — `diagram_design/pipeline_analisis` presenta la CNN de fusión como flujo principal y omite la conducta activa
- Severidad: Baja (pregunta abierta → tú y el usuario; puede subir a Media si la figura entra al documento)
- Ubicación: `diagram_design/pipeline_analisis.md` («Esta versión describe la CNN de fusión… decide cada segundo»); `generadores/gen_pipeline.py` nodos `cnn` y `cond` («inmovilidad, nado o escalamiento»); `chapters/05_diseno.tex:226-243`, `pipeline.puml:57-75`
- Cita: «CNN 3D con medidas de apoyo… Conducta del segundo: inmovilidad, nado o escalamiento» / «Clasificador sin elegir» (CLA-03), «Candidata en evaluación: red R(2+1)D-18»
- Fuente que decide: pregunta abierta → tú y el usuario (descripción del 8-oct no registrada como D-xx). Contra CLA-03 el LaTeX y `pipeline.puml` están correctos hoy.
- Destinatario: Erick
- Previo: DF-13
- Corrección sugerida: registrar una D-xx si la fusión pasa a ser el diseño; si no, no usar esta figura en el documento.

### DF-19 — Texto de cap. 5 y figuras con cuatro módulos / dos actores frente a lo dibujado
- Severidad: Baja
- Ubicación: `chapters/05_diseno.tex:119` («cuatro módulos secuenciales»), `:748` («dos actores principales»); `cu_vision_general.puml:13` (tercer actor «Worker»), `pipeline.puml` (cuatro particiones) frente a «tres etapas» en `:300-304` y RF-13
- Cita: «cuatro módulos» / «tres etapas del pipeline»; «dos actores» / figura con Investigador, Administrador y Worker
- Fuente que decide: D-16 (tres etapas; «Resultados» no es una etapa de análisis).
- Destinatario: Erick (pipeline) / Vanesa (actores)
- Previo: DF-23 (cuatro módulos); actores: nuevo
- Corrección sugerida: «tres etapas más la generación de resultados»; «dos actores humanos y el *Worker* como actor del sistema».

### DF-20 — `seq_login` y `seq_gestion_usuarios` quedan cortos frente a CU-16 y CU-11
- Severidad: Baja
- Ubicación: `diagramas/seq_login.puml:38-44`; `diagramas/seq_gestion_usuarios.puml:65-89`; `chapters/05_diseno.tex:1077-1100` (CU-16), `:1913` (CU-11 paso 3b)
- Cita: login termina en «muestra el panel principal» / CU-16 «Detecta la marca de «cambio obligatorio»… redirige»; CU-11 «(b) editar datos de cuenta existente» sin rama en la secuencia
- Fuente que decide: D-25 (cambio obligatorio), fichas CU-11/CU-16.
- Destinatario: Erick
- Previo: DF-20, DF-21
- Corrección sugerida: añadir en `seq_login` la rama «cuenta con cambio obligatorio → pantalla de cambio de contraseña» y en `seq_gestion_usuarios` la acción «editar datos».

---

## Revisados y sin hallazgo
- Includes/extends de los cinco paquetes coinciden con la fila «Referencias» de las fichas: CU-16→CU-01, CU-17→CU-11, CU-05 incluye CU-19, CU-20 y CU-07 extienden CU-05, CU-08 extiende CU-07, CU-10 extiende CU-09, CU-26 extiende CU-25 e incluye CU-27. CU-15 queda sin dibujar con explicación en el texto.
- `seq_crear_cuenta`, `seq_logout`, `seq_revision_segundos`, `seq_consulta_progreso`: coherentes con CU-12, CU-02, CU-25/26/27 y CU-07/08 en lo funcional (correo con respaldo en pantalla, RN-16, reportes borrados al guardar).
- `pipeline.puml` y `arquitectura_software.puml`: sin YOLO, sin tracker, sin umbral de detección 0.70; «Día 1 vs Día 2» ausente de las figuras.
- Tablas: 15 en el grafo vigente y en `diagram_design` (el comentario de `arquitectura_software.puml:36` dice «16 relaciones»; es un comentario).
- Vigilantes: ninguna figura muestra «código de error», «rata» ni «animales»; «IA» solo en comentarios de `.puml`.
- Los `.puml` donde el PNG es más viejo que el fuente (`seq_consulta_resultados`, 04-oct frente a 06-oct) no difieren en texto visible: sin hallazgo.
- D-57 a D-60 pendientes de propagar (copia reproducible, reinicio): sin hallazgo adicional.

## Cobertura y límites
- Leídos completos: todos los `.puml` listados, `diagram_design/*.md`, `gen_flujo.py` y `gen_pipeline.py`, extractos de `gen_capas.py` y `gen_despliegue.py` (los `.html` no se abrieron; son salida de los generadores). Cap. 5 secciones 1-2, 3 (estados), casos de uso (todas las fichas), secuencias y clases; cap. 4 RF y RN.
- PNG abiertos: los nueve listados arriba. No abrí los PNG de `cu_*`, `seq_carga_video`, `seq_descarga_reportes`, `seq_gestion_usuarios`, `seq_crear_cuenta`, `seq_login`, `seq_logout`, `seq_revision_segundos`; sus fechas git coinciden con las del `.puml`, así que asumo que reflejan el fuente (los acentos faltantes en `cu_*` salen del `.puml`).
- No verifiqué si `RNF-10` (cap. 4) todavía registra el despliegue; es de otro agente (D-62 ya lo marca pendiente).
- `ciclo_vida_experimento.puml` sigue huérfano (botón «Iniciar Análisis», `jobs.status`, `progress_pct`) y no entra al documento; ya estaba en la auditoría previa (DF-16), no lo cuento de nuevo.
