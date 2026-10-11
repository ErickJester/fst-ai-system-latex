# Auditoría DF — Diagramas de flujo, pipeline, casos de uso, secuencia, estados y arquitectura

Fecha: 2026-10-11 · Agente DF · Solo lectura (HEAD `da96c00`)

## Alcance auditado

Leídos completos:

- `diagramas/pipeline.puml`, `flujo_general.puml`, `estados_analisis.puml`, `estados_experimento.puml`, `ciclo_vida_experimento.puml`, `arquitectura_software.puml`.
- Los siete `diagramas/seq_*.puml` con fuente: `analisis_automatico`, `carga_video`, `consulta_progreso`, `consulta_resultados`, `crear_cuenta`, `descarga_reportes`, `gestion_usuarios`, `login`, `logout`, `revision_segundos`.
- `diagramas/puml/cu_vision_general.puml`, `cu_paquete1..5.puml`, `gen_pngs.sh`.
- `diagramas/diagram_design/`: `flujo_sistema.md`, `pipeline_analisis.md`, `arquitectura_capas.md`, `despliegue.md`, y los generadores `gen_flujo.py`, `gen_pipeline.py`, `gen_capas.py` (por búsqueda de textos y lectura de nodos; `gen_despliegue.py` y los `.html` solo por búsqueda de términos).
- `diagramas/grafo_relacional_3_vigente.puml` (referencia).
- Cap. 4: RF-01…RF-33, RNF-07…RNF-10, RN-01…RN-15 (líneas 40–330, 380–410, 505–615).
- Cap. 5: líneas 1–360 (arquitectura, pipeline, estados), 690–2575 (API, casos de uso y fichas, secuencias, clases) y las `\includegraphics`/pies de figura de todo el capítulo.
- PNG abiertos con Read y comparados con su `.puml`: `figures/mermaid/flujo_general.png`, `pipeline.png`, `arquitectura_software.png`, `estados_analisis.png`, `cu_vision_general.png`, `cu_paquete1.png`, `cu_paquete3.png`, `seq_notificaciones.png`, `seq_cambio_pass_inv.png`, `seq_perfil.png`.
- Fechas de commit de cada `.puml` contra su PNG (`git log -1`): todos los PNG vigentes son del mismo commit que su fuente, salvo `seq_consulta_resultados.png` (4-oct, anterior al `.puml` del 6-oct; el diff del `.puml` solo cambió comentarios, así que el PNG no está desactualizado en lo visible) y `seq_descarga_reportes.png`, `seq_gestion_usuarios.png` y `flujo_general.png`, que son posteriores a su `.puml`.

Contexto leído: `PENDIENTES.md`, `PENDIENTES-VANESA.md`, `PENDIENTES-ERICK.md`, decisiones D-16, D-17, D-22, D-29, D-31, D-41, D-47, D-49, D-51, D-53, D-54 de `errores/preguntas-doctor.md`, `PREGUNTAS.md`.

Los pendientes ya registrados (A-9a/9b, A-10…A-13, A-15, M-18…M-23, M-28, M-29, M-30, M-32, V-3, V-4 de las listas de Vanesa y Erick; D-51 sin aplicar en el comentario de `seq_analisis_automatico.puml`; D-54 aún sin aclarar en el LaTeX) **no se repiten** como hallazgo nuevo, salvo que se señale algo concreto que no figura en ellos.

## Resumen de conteos

| Severidad | Cantidad | De ellas «pregunta abierta» |
|-----------|----------|-----------------------------|
| Alta | 5 | 0 |
| Media | 10 | 4 (DF-09, DF-11, DF-13, DF-14) |
| Baja | 10 | 0 |
| **Total** | **25** | **4** |

---

## Hallazgos de severidad Alta

### DF-01 — El texto del cap. 5 dice que el entrenamiento usa «anotación experta»; la figura y la regla vigente dicen lo contrario
- Severidad: Alta
- Ubicación: `chapters/05_diseno.tex:99-102`; `diagramas/flujo_general.puml:69,73`; `figures/mermaid/flujo_general.png`; `diagramas/diagram_design/flujo_sistema.md` («Diferencias con flujo_general.puml y con el texto»)
- Cita: «el ciclo de entrenamiento del modelo ---anotación experta, dataset y entrenamiento--- alimenta al clasificador de conducta» (cap. 5) vs «SIN anotación del Dr. Sandino, ni para entrenar ni para probar» (figura que ese párrafo presenta).
- Fuente que decide: `CLAUDE.md` («Prohibición vigente»: el clasificador se entrena sin las anotaciones manuales del Dr. Sandino; no hay «gold standard»), D-26, D-56; PENDIENTES «Entrenamiento sin las anotaciones del laboratorio».
- Corrección sugerida: reescribir la oración como «…y cómo el ciclo de entrenamiento del modelo ---clips etiquetados por el equipo, entrenamiento y evaluación sobre un conjunto de prueba propio--- alimenta al clasificador de conducta». El propio `flujo_sistema.md` ya anota que este párrafo sigue sin corregirse; no figura en ninguna lista de pendientes.

### DF-02 — La figura de arquitectura muestra «corrección CLAHE» en el worker; el cap. 5 dice que no hay corrección de contraste
- Severidad: Alta
- Ubicación: `diagramas/arquitectura_software.puml:87`; `figures/mermaid/arquitectura_software.png`; `chapters/05_diseno.tex:158-160`; `diagramas/pipeline.puml:17-18`
- Cita: «OpenCV Preprocesamiento y correccion CLAHE» (figura 5.1, cap. 5:53) vs «El sistema no aplica ninguna corrección de contraste ni de iluminación» (cap. 5:158).
- Fuente que decide: CLA-04 (5-oct, código de `fst_auto`) ya aplicado en cap. 5 Módulo 1 y en `pipeline.puml`; PENDIENTES-ERICK A-1 solo lo registra para caps. 2, 3, 4, glosario y «figura del pipeline», no para esta figura. `arquitectura_capas.md` ya lo corrige en su versión nueva y lo anota como diferencia con el `.puml`.
- Corrección sugerida: línea del worker → «OpenCV   Preprocesamiento (registro de cámara y modelo de fondo)» y regenerar el PNG de `figures/mermaid/arquitectura_software.png`. Al quitar CLAHE de la figura, la sigla ya no se define en el cap. 5 por esta vía (revisar glosario/abreviaturas: es de Erick).

### DF-03 — `seq_consulta_resultados` define «agrupado» como «dos conductas» y omite la conducta activa; contradice D-29, D-41, RN-13 y el cap. 5
- Severidad: Alta
- Ubicación: `diagramas/seq_consulta_resultados.puml:74`, `:85-89`, `:92-96` (y comentario `:24-26`); `chapters/05_diseno.tex:2776`, `:2824-2825`; `chapters/04_analisis.tex:581-586` (RN-13); `back/apendice_D.tex:63`
- Cita: «comparación entre grupos en dos conductas, con aviso de nivel "agrupado"» / «"agrupado" significa que nado activo y escalamiento se juntan en "conducta activa"» / «segundos de nado activo, inmovilidad y escalamiento» (diagrama) vs «`agrupado` si al menos uno [de los segundos] quedó [como conducta activa]» (apéndice D) y «Un mismo análisis puede mezclar las cuatro conductas» (RN-13).
- Fuente que decide: D-29 (equipo, 3-oct: cuarta conducta, un análisis puede mezclar las cuatro) y D-41 (usuario, 3-oct: `agrupado` = algún segundo quedó como conducta activa; la interfaz solo lo usa para avisar).
- Corrección sugerida: leer «segundos de nado activo, inmovilidad, escalamiento y conducta activa» en el mensaje de la línea 74; reemplazar las tres ramas finales por «comparación entre grupos en cuatro conductas; si algún análisis es "agrupado", avisar que parte de sus segundos son conducta activa». Nota de la línea 93-95 → «"agrupado" significa que al menos un segundo quedó como conducta activa (D-41)».

### DF-04 — Cap. 5 sigue hablando de comparación «Día 1 vs. Día 2»; la comparación vigente es solo entre grupos con el Día 2
- Severidad: Alta
- Ubicación: `chapters/05_diseno.tex:808-809` (intro Paquete 4), `:1758` (CU-09, curso alterno 5); contraste con `diagramas/puml/cu_paquete4.puml:15` («Comparar grupos en Dia 2»), `diagramas/seq_consulta_resultados.puml:14-18`, `chapters/04_analisis.tex:575-579` (RN-12)
- Cita: «comparación Día 1 vs. Día 2 (cuando ambos videos están disponibles)» y «Solo hay un video analizado: la comparación Día 1 vs. Día 2 no está disponible» vs «La comparación entre grupos usa solo los videos del Día 2» (RN-12).
- Fuente que decide: D-44 (no existe comparación Día 1 contra Día 2), RF-21/RN-12, D-54(d) (el Día 1 solo confirma que existe el video de habituación y no se analiza). Nota: RF-09 (`04_analisis.tex:107-110`) todavía dice que del Día 1 se analizan «los primeros 5 minutos» del grupo control; eso entra en el pendiente conocido de D-54, no se repite aparte.
- Corrección sugerida: intro P4 → «…desglose por minuto, comparación entre grupos con el Día 2, descarga…». CU-09, curso alterno 5 → «El Día 2 de algún espécimen aún no está analizado: el sistema lo señala como faltante en la comparación y muestra el resto».

### DF-05 — CU-07 (curso alterno 4) todavía muestra un «código» de error de análisis
- Severidad: Alta
- Ubicación: `chapters/05_diseno.tex:1646`; contraste con `diagramas/seq_consulta_progreso.puml:87`, `chapters/04_analisis.tex:159-163` (RF-16)
- Cita: «El sistema muestra alerta con código y descripción del error» (CU-07) vs «muestra el mensaje del error armado con la etapa» (diagrama) y «mostrar la descripción del problema, según la etapa en que se detuvo» (RF-16).
- Fuente que decide: D-47 (usuario, 4-oct): RF-16 deja de mostrar un código de error; solo se conserva en los errores de carga (CU-05/06, RF-08/10). PENDIENTES: «Sin ... códigos de error».
- Corrección sugerida: «El sistema muestra una alerta con la descripción del error, armada a partir de la etapa en que se detuvo».

---

## Hallazgos de severidad Media

### DF-06 — La figura del flujo del sistema (`flujo_general`) no coincide con el texto vigente en conductas, preprocesamiento y camino de error
- Severidad: Media
- Ubicación: `diagramas/flujo_general.puml:93-94`; `figures/mermaid/flujo_general.png`; `chapters/05_diseno.tex:99-102,130-160,303-307`; `chapters/04_analisis.tex:140-145,167-172`
- Cita: «Clasificación de conducta (nado activo, inmovilidad, escalamiento)» y «Preprocesamiento (cuadros y limpieza)» (figura) vs cuatro conductas incluida «conducta activa» (RN-13, RF-17) y «registro de cámara y modelo de fondo» (RF-13, Módulo 1). La figura tampoco dibuja el camino de error (RN-11), que el texto que la introduce sí describe; el pie dice solo «Diagrama de flujo del sistema».
- Fuente que decide: RN-13/RF-17 (cuatro conductas, D-29), RF-13, D-16 revisado. `flujo_sistema.md` documenta las dos primeras diferencias y no se propagaron al `.puml` ni al PNG que entra al documento.
- Corrección sugerida: «Clasificación de conducta\n(nado activo, inmovilidad, escalamiento\ny conducta activa)» y «Preprocesamiento\n(registro de cámara y modelo de fondo)»; agregar una salida «error: reporte de diagnóstico» desde Preprocesamiento/Localización o aclarar en el pie que es un flujo del camino exitoso.

### DF-07 — «Los tres grupos del experimento» en dos secuencias; el modelo vigente es de tres o más grupos
- Severidad: Media
- Ubicación: `diagramas/seq_consulta_resultados.puml:64,66,91`; `diagramas/seq_descarga_reportes.puml:80-81`; `diagramas/grafo_relacional_3_vigente.puml:240` (`EXPERIMENTO "1" --o "3..*" GRUPO`)
- Cita: «busca los tres grupos del experimento» / «muestra la comparación de los tres grupos» / «entre los especímenes de cada uno de los tres grupos del experimento» vs PENDIENTES «tres o más grupos (en promedio 4)» y cardinalidad `3..*`.
- Fuente que decide: PENDIENTES «El estudio», grafo vigente (3..*), RF-31 («control, referencia, tratamiento» son tres tipos).
- Corrección sugerida: «busca los grupos del experimento (tres o más; tipos control, referencia y tratamiento)»; «muestra la comparación de los grupos»; «entre los especímenes de cada grupo del experimento».

### DF-08 — Códigos internos de decisión (D-xx, Q-E) visibles dentro de las figuras que entran al documento
- Severidad: Media
- Ubicación: `diagramas/seq_consulta_progreso.puml:79` (D-22), `:91` (D-23); `seq_consulta_resultados.puml:80` (Q-E), `:93` (D-41); `seq_crear_cuenta.puml:58` (D-12), `:89` (D-45); `seq_descarga_reportes.puml:68` (D-21); `estados_analisis.puml:16` (D-23); las cinco figuras están incluidas en `chapters/05_diseno.tex:2514,2521,2408,2528,313`
- Cita: p. ej. «un tercio por etapa (D-22)», «se generó el reporte de diagnostico (D-23)», «para que el tamaño del grupo no distorsione la comparación -- Q-E».
- Fuente que decide: PENDIENTES-ERICK A-9b y PENDIENTES-VANESA A-9a (citas internas «D-XX» que el lector de la tesis no puede resolver); Erick las quitó del texto el 7-oct (commit `6a2b98a`), pero no de las figuras.
- Corrección sugerida: quitar los paréntesis con códigos en esas ocho líneas visibles (dejar la regla en lenguaje natural: «un tercio por etapa», «reporte de diagnóstico») y regenerar los PNG. `Q-E` pertenece a una pregunta abierta al laboratorio; sacar la mención de la figura.

### DF-09 — CU-11 y CU-12 están en el Paquete 1 del diagrama, pero sus fichas y la introducción del paquete 5 los tratan como del Paquete 5
- Severidad: Media
- Ubicación: `diagramas/puml/cu_paquete1.puml:19,23` («Gestionar cuenta de usuario», «Crear cuenta de usuario»); `chapters/05_diseno.tex:1982-2046` (fichas CU-11 «Gestionar cuenta de investigador» y CU-12 bajo «Paquete 5»); `:820-824` (intro P5: «Exclusivo del Administrador: gestión de cuentas… creación de cuentas y monitoreo»); `diagramas/puml/cu_paquete5.puml:11-14,28-31` (P5 dibuja Investigador, Worker y Sistema)
- Cita: «Exclusivo del Administrador» (intro P5) vs P5 con `INV --> UC51`, `INV --> UC53`, `WRK --> UC54`, `SYS --> UC52`; y P1 con `ADMIN --> UC15`, `ADMIN --> UC17` mientras las fichas están en P5. El texto de P1 (`:767-769`) tampoco menciona gestión de usuarios ni perfil.
- Fuente que decide: sin fuente de rango superior sobre qué paquete aloja CU-11/12 → **pregunta abierta → tú y el usuario** (Vanesa diseñó los CU; la lista V-4 solo señala «nombres distintos entre diagrama y ficha», no esta reubicación). La referencia cruzada concreta: CU-11 y CU-12 deben aparecer en el mismo paquete en diagrama, ficha e introducción.
- Corrección sugerida: mover las dos fichas a la subsección «Paquete 1», o dibujarlas en P5 y quitarlas de P1; reescribir la intro de P5 sin «Exclusivo del Administrador» (el paquete también cubre dashboard, eliminar experimento y borrado automático, que son del Investigador y del Worker).

### DF-10 — El envío de correo (RF-33, D-45) no aparece en ninguna figura del cap. 5: ni en notificaciones, ni en el análisis automático, ni en la arquitectura
- Severidad: Media
- Ubicación: `figures/mermaid/seq_notificaciones.png` (sin `.puml`; pasos 2 y 4-9); `diagramas/seq_analisis_automatico.puml:93,99`; `diagramas/arquitectura_software.puml` (sin nodo de correo); `chapters/05_diseno.tex:2463-2467`; `chapters/04_analisis.tex:292-299` (RF-33)
- Cita: «Registra notificacion de analisis finalizado para el usuario» / «crea la notificación de análisis terminado» vs «avisar al usuario… en el panel de notificaciones… y también por correo electrónico» (RF-33). Además `seq_notificaciones.png` paso 1: «Actualiza estado del video como completado»: `VIDEO` no tiene estado (el estado es `ANALISIS.estado`, grafo vigente).
- Fuente que decide: D-45 (usuario, 4-oct) y RF-33; grafo vigente para la columna. `despliegue.md` sí dibuja la cuenta de correo, pero esa figura no entra al documento.
- Corrección sugerida: rehacer `seq_notificaciones` en PlantUML (ya está en M-29) con «envía también la notificación por correo; si falla, el aviso queda en el panel» y «actualiza el estado del análisis»; en `seq_analisis_automatico` agregar tras las líneas 93 y 99 «envía el correo con la notificación (si falla, queda el aviso en el panel)»; agregar a la arquitectura un nodo externo «Cuenta de correo (configurable)» enlazado al backend o al worker (decisión abierta de `despliegue.md`).

### DF-11 — `seq_carga_video` valida el formato en el backend después de subir; RN-10 y RF-08 piden rechazarlo antes de subir (en el cliente)
- Severidad: Media
- Ubicación: `diagramas/seq_carga_video.puml:66-74`; `chapters/04_analisis.tex:99-101` (RF-08), `:561-565` (RN-10); `chapters/05_diseno.tex:1361` (CU-05 alt. 6)
- Cita: «ui -> api: envía el video… api -> api: valida formato (.mp4 o .mov), reproducibilidad y que el video esté en horizontal» vs «La validación de formato ocurre en el cliente» (RN-10) y «rechazado… antes de intentar subirlo al servidor» (RF-08); CU-05 alt. 6 dice «antes de iniciar la transmisión».
- Fuente que decide: rango 5 vs rango 5 (cap. 4 contra cap. 5/diagrama), sin fuente superior → **conviene confirmar con el equipo** si la validación del formato es en cliente y la de reproducibilidad/orientación en servidor (lo más plausible, ya que RF-10 exige que el video sea reproducible).
- Corrección sugerida: separar en la figura dos pasos: «la interfaz comprueba la extensión (.mp4/.mov) antes de enviar» y «el backend comprueba reproducibilidad y orientación horizontal»; igualar CU-05 paso 6 a esa división.

### DF-12 — `estados_analisis` solo permite el error saliendo de «cilindros»; el texto dice que el video que no se abre se detiene en el preprocesamiento
- Severidad: Media
- Ubicación: `diagramas/estados_analisis.puml:16`; `figures/mermaid/estados_analisis.png`; `chapters/05_diseno.tex:132-134` («si el archivo no se puede abrir, el pipeline se detiene»), `:303-307`; `diagramas/pipeline.puml:36-41`
- Cita: «cilindros --> error : [no se pudo abrir el video o no se hallaron los tubos]» vs «Preprocesamiento: si el archivo no se puede abrir, el pipeline se detiene y genera el reporte de diagnóstico» (cap. 5) y `pipeline.puml`, que sí dibuja la salida de error en la etapa 1.
- Fuente que decide: cap. 5 Módulo 1, RN-11, D-16 revisado. M-32 de PENDIENTES-ERICK cubre solo los `seq_*`; esta figura (que sí entra al documento) no está incluida.
- Corrección sugerida: agregar `preprocesamiento --> error : [no se pudo abrir el video]` y dejar en la transición desde `cilindros` solo «[no se hallaron los tubos]»; quitar «(D-23)» (DF-08).

### DF-13 — `diagram_design/pipeline_analisis` presenta la CNN de fusión como flujo principal y deja fuera la conducta activa; contradice cap. 5, `pipeline.puml` y «el clasificador no se elige todavía»
- Severidad: Media
- Ubicación: `diagramas/diagram_design/pipeline_analisis.md:13-14,25-36,46-49,60-76`; `generadores/gen_pipeline.py:87`; contraste con `chapters/05_diseno.tex:194-269`, `diagramas/pipeline.puml:57-75`, `chapters/04_analisis.tex:166-173` (RF-17), RN-13
- Cita: «Esta versión describe la CNN de fusión… No es lo que describe hoy el cap. 5» y «Decide la conducta del segundo: inmovilidad, nado o escalamiento… tampoco "conducta activa"» vs PENDIENTES «Clasificador: todavía no se elige. Candidatos: gradient boosting sobre rasgos y R(2+1)D-18 (CLA-03)» y cuatro conductas.
- Fuente que decide: **pregunta abierta → equipo** (Erick). La descripción del 8-oct del pipeline (CNN de fusión) no está registrada como decisión en `errores/preguntas-doctor.md` ni en PENDIENTES; mientras no lo esté, vale CLA-03. El `.md` ya reconoce la discrepancia y que `pipeline.puml` «sigue la versión anterior».
- Corrección sugerida: decidir si el clasificador sigue «sin elegir». Si la CNN de fusión pasa a ser el flujo principal, registrarlo (D-xx), actualizar PENDIENTES y propagarlo a `pipeline.puml`, cap. 5 Módulo 3 y RN-13/RF-17; si no, marcar el diagrama como «alternativa en evaluación» y agregar «conducta activa» al cuadro de salida.

### DF-14 — «Video anotado»: unas figuras lo guardan y otra dice que se quitó porque el código no lo genera
- Severidad: Media
- Ubicación: `diagramas/diagram_design/pipeline_analisis.md:55-56` («Se quitó… porque el código no lo genera»); `flujo_sistema.md` paso 6 y `generadores/gen_flujo.py:65` («video anotado»); `arquitectura_capas.md:33-34` y `gen_capas.py:68` («Videos originales y anotados»); `diagramas/pipeline.puml:79`, `arquitectura_software.puml:101` («Videos anotados _tracked.mp4»); `chapters/05_diseno.tex:284-286` (cuarta salida del Módulo 4); `diagramas/seq_analisis_automatico.puml:89` (copia recortada reproducible, sin anotaciones)
- Cita: «"Video anotado". Se quitó de lo que guarda el módulo 4 porque el código no lo genera» vs «Video anotado: video original con el recuadro de cada cilindro y la etiqueta de conducta superpuestos» (cap. 5).
- Fuente que decide: el cap. 5 es de rango 5; no hay decisión superior → **pregunta abierta → equipo** (Erick): ¿el sistema entrega un video anotado, o solo la copia recortada y reproducible del video más el archivo de recuadros? Hoy los diagramas se contradicen entre sí y con el texto. Además el nombre `_tracked.mp4` remite a un seguimiento que ya no existe.
- Corrección sugerida: tras decidir, igualar los cinco documentos; si se mantiene, renombrar «_tracked» (p. ej. «video anotado») en la figura de arquitectura.

### DF-15 — La figura de arquitectura valida solo `.mp4`; el sistema acepta `.mp4` y `.mov`
- Severidad: Media
- Ubicación: `diagramas/arquitectura_software.puml:79,101` (y su PNG); `chapters/04_analisis.tex:99-101` (RF-08), `:561-566` (RN-10)
- Cita: «Validacion de archivos .mp4» / «Videos .mp4 originales» vs «únicamente archivos en formato .mp4 o .mov» (RF-08) y «Los videos reales del laboratorio son .mov» (RN-10).
- Fuente que decide: D-30 (formatos `.mp4` y `.mov`), PENDIENTES «El video».
- Corrección sugerida: «Validación de archivos de video (.mp4 / .mov)» y «Videos originales (.mp4 / .mov)».

---

## Hallazgos de severidad Baja

### DF-16 — `ciclo_vida_experimento.puml` (huérfano): ninguna fuente vigente lo usa; conserva un botón «Iniciar Análisis» y tablas del modelo viejo
- Severidad: Baja
- Ubicación: `diagramas/ciclo_vida_experimento.puml:37-47,63-65,86-92,94-99`; búsqueda en todo el repo: solo lo mencionan `errores/*`, `PENDIENTES.md:147` y `para-notebooklm/` (no `main.tex`, ningún `.tex`, ningún `.md` de diseño)
- Cita: «Investigador presiona "Iniciar Análisis"» (contradice RN-04); «consulta `jobs.status = QUEUED`… actualiza `progress_pct`» (tablas inexistentes; incluye código dentro del diagrama); «`behavior_results` se conservan» (tabla del modelo viejo); estados «Incompleto/SinSujetos/Archivado».
- Fuente que decide: RN-04, grafo vigente (no hay `jobs`, `progress_pct` ni `behavior_results`), estados vigentes en `estados_analisis`/`estados_experimento`.
- Corrección sugerida: no hace falta editarlo si no entra al documento (PENDIENTES ya lo clasifica como huérfano); si se conserva en el repo, agregar una línea de cabecera «OBSOLETO: modelo viejo, no usar» para que no se recicle.

### DF-17 — Comentarios de cabecera de varios `.puml` describen un modelo que ya cambió
- Severidad: Baja
- Ubicación: `diagramas/flujo_general.puml:11-47` («BORIS», «análisis de conducta en vivo» en `:38-39`); `seq_analisis_automatico.puml:24-30` («umbral de confianza 0.70 de RN-11», pendiente D-51 ya conocido), `:36-40` («la capacidad del modelo activo (RN-13, F1 >= 85%)… idConfig»); `seq_gestion_usuarios.puml:14-17` («CU-11 declara <<include>> de CU-12… 05_diseno.tex:920»); `seq_descarga_reportes.puml:15-16` («columnas Tiempo, Nado, Escalamiento, Inmovilidad»); `seq_consulta_progreso.puml:53-54` («pendiente de aplicar en grafo_relacional_3_vigente.puml»)
- Cita: p. ej. «el Worker etiqueta el analisis como "preciso" o "agrupado" segun la capacidad del modelo activo (idConfig)» vs D-41 (`agrupado` si algún segundo quedó como conducta activa) y D-51 (sin `idConfig`); «CU-11 declara <<include>> de CU-12» vs ficha CU-11 «Relacionado: CU-12».
- Fuente que decide: D-41, D-51, D-56 (BORIS ya no aparece), RF-22 (cinco columnas, incluye «Conducta activa»). Son comentarios (no se imprimen), pero un lector que reabra la fuente se confunde. El caso de `seq_analisis_automatico` por 0.70 ya es pendiente conocido; aquí se agregan los demás.
- Corrección sugerida: actualizar o recortar esos bloques de comentario al regenerar cada figura.

### DF-18 — Código y detalles de transporte dentro de diagramas que deben estar en lenguaje natural
- Severidad: Baja
- Ubicación: `diagramas/seq_gestion_usuarios.puml:46` («GET /admin/usuarios»), `:60` («200 OK {usuarios, con marca de administrador}»), `:75` («PATCH /admin/usuarios/{id} {activo: false}»), `:86`, `:51-52`; `seq_crear_cuenta.puml:73` («403, no autorizado»); `seq_gestion_usuarios.puml:67-68` (ruta de archivo «diagramas/seq_crear_cuenta.puml» dentro de la figura); `seq_gestion_usuarios.puml:50-61` y `:64` (nombres de tabla `ADMINISTRADOR`, `USUARIO` en mensajes)
- Cita: «PATCH /admin/usuarios/{id} {activo: false}» (diagrama) vs «Lenguaje natural obligatorio: sin SQL ni código dentro de los diagramas» (`CLAUDE.md`, «Reglas de diagramas»).
- Fuente que decide: `CLAUDE.md` (reglas de diagramas). M-28 de PENDIENTES-ERICK solo señala la discrepancia `/admin/usuarios` contra `/admin/users`, no la regla de lenguaje natural.
- Corrección sugerida: «el sistema solicita la lista de usuarios con la sesión del Administrador», «responde con la lista, marcando a los administradores», «solicita desactivar la cuenta», «responde: no autorizado»; sustituir la ruta de archivo por «ver CU-12 "Crear cuenta de usuario"».

### DF-19 — Textos de figuras sin acentos ni eñes («Autenticacion», «Vision», «analisis», «especimen»)
- Severidad: Baja
- Ubicación: `diagramas/puml/cu_vision_general.puml:3,15-19`; `cu_paquete1..5.puml` (títulos y casos: «Autenticacion», «Gestion», «analisis», «especimen», «contrasena», «sesion», «Dia 2», «administracion»); `arquitectura_software.puml:71,87,101` («Visualizacion», «correccion», «Localizacion», «diagnostico»); `estados_analisis.puml:16` («diagnostico»); `figures/mermaid/*.png` correspondientes
- Cita: «Plataforma Web FST / Paquete 1 - Autenticacion y gestion de usuarios» (figura) vs «Paquete 1: Autenticación y gestión de usuarios» (cap. 5:765).
- Fuente que decide: ortografía; los otros diagramas (`pipeline`, `seq_*`) sí llevan acentos.
- Corrección sugerida: acentuar al regenerar; sirve además para unificar el nombre del Paquete 3 («Pipeline de analisis conductual» en la figura contra «Análisis conductual» en el cap. 5:792,801).

### DF-20 — `seq_login` no muestra el cambio obligatorio de contraseña al primer ingreso que `seq_crear_cuenta` da por hecho
- Severidad: Baja
- Ubicación: `diagramas/seq_login.puml:38-44`; `seq_crear_cuenta.puml:34-36`; `chapters/05_diseno.tex:1077` (CU-16), `:2401-2404`
- Cita: «D-25: la cuenta se crea con cambioRequerido = true, así el login (fuera de este diagrama) sabe que debe forzar el cambio» vs `seq_login` sin ninguna rama de cambio requerido.
- Fuente que decide: D-25, RF-05/RF-07 («obliga al usuario a cambiarla en el primer ingreso»), CU-16.
- Corrección sugerida: en la rama exitosa de `seq_login` agregar «si la cuenta tiene el cambio requerido, ofrece la pantalla de cambio de contraseña (CU-16) antes del panel principal», o dejar la nota «el cambio obligatorio se ve en la figura de cambio de contraseña».

### DF-21 — `seq_gestion_usuarios` cubre crear y desactivar, pero RF-05 y CU-11 incluyen modificar datos
- Severidad: Baja
- Ubicación: `diagramas/seq_gestion_usuarios.puml:63-89`; `chapters/05_diseno.tex:2438-2441,2448`; `chapters/04_analisis.tex:77-82` (RF-05); ficha CU-11 paso 3(b) («editar datos de cuenta existente»)
- Cita: «Secuencia: gestión de usuarios por administrador (crear y desactivar)» vs RF-05 «crear, modificar y desactivar cuentas».
- Fuente que decide: RF-05, RF-04 (el Administrador puede modificar cuentas), CU-11.
- Corrección sugerida: agregar una rama «editar cuenta» (o aclarar en el pie y en el párrafo del cap. 5 que modificar se omite por ser análogo a CU-18).

### DF-22 — CU-07 (paso 5) y CU-09 (paso 3) listan solo tres conductas
- Severidad: Baja
- Ubicación: `chapters/05_diseno.tex:1629`, `:1743`; contraste con `chapters/04_analisis.tex:166-173,581-586` y `diagramas/seq_analisis_automatico.puml:79`
- Cita: «clasificación de conductas (nado activo, inmovilidad, escalamiento)» y «tabla de tiempos por espécimen: nado activo, inmovilidad y escalamiento» vs CU-27 («una fila por cada una de las cuatro conductas») y `seq_analisis_automatico` («nado, inmovilidad, escalamiento o conducta activa»).
- Fuente que decide: D-29, RN-13, RF-22.
- Corrección sugerida: «(nado activo, inmovilidad, escalamiento y conducta activa)» en ambos pasos.

### DF-23 — «Cuatro módulos» en el texto y la figura del pipeline contra «tres etapas» en estados, progreso y RF-13
- Severidad: Baja
- Ubicación: `chapters/05_diseno.tex:118-120`, `:71-73`, `:302-304`; `diagramas/pipeline.puml:35,46,57,77` (cuatro particiones, la 4.ª «Resultados»); `chapters/04_analisis.tex:140-145` (RF-13)
- Cita: «Está organizado en cuatro módulos secuenciales: preprocesamiento, localización de los cilindros, clasificación de conducta y generación de resultados» vs «El pipeline… debe ejecutar tres etapas secuenciales» (RF-13) y «las tres etapas del pipeline» (cap. 5:303).
- Fuente que decide: D-16 revisado (tres etapas: `preprocesamiento`, `cilindros`, `clasificacion`).
- Corrección sugerida: aclarar una vez que «el módulo 4 (resultados) no es una etapa con indicador de progreso: son las tres etapas y el guardado final», o rotular la partición 4 de la figura como «Guardado de resultados (no es etapa)».

### DF-24 — `seq_analisis_automatico`: «programa la eliminación» sin columna que la respalde, «5 intervalos» fijos y una errata
- Severidad: Baja
- Ubicación: `diagramas/seq_analisis_automatico.puml:82,85,92`; `chapters/05_diseno.tex:2339,2356-2362` (CU-14); `grafo_relacional_3_vigente.puml:247,250-251`; D-54 (respuesta a)
- Cita: «w -> db: programa la eliminación del video 30 días después (RNF-08)» vs CU-14: tarea diaria que identifica videos «con análisis exitoso hace ≥ 23 días y < 30 días» (se deriva de `ANALISIS.fechaAnalisis`; el grafo no tiene columna de fecha de borrado). «guarda sus 5 intervalos» vs D-54: «`INTERVALO` puede quedar incompleto» en un video corto. Además «especímen» (`:82`) lleva tilde indebida.
- Fuente que decide: grafo vigente y CU-14; D-54 (a).
- Corrección sugerida: quitar la línea 92 (el borrado lo hace el cron diario del Worker, CU-14) o decir «el video queda sujeto al borrado automático a los 30 días»; «guarda sus intervalos (hasta 5)» y «espécimen».

### DF-25 — Introducciones de paquete y descripciones de figura del cap. 5 que no coinciden con lo dibujado
- Severidad: Baja
- Ubicación: `chapters/05_diseno.tex:781-783` (intro P2: «registrar metadatos (nombre, fecha, tratamiento, número de especímenes)»), `:794-796` (intro P3: «consultar el estado de la cola»), `:2491-2493` (descripción de la figura de resultados)
- Cita: P2: «registrar metadatos (nombre, fecha, tratamiento, número de especímenes)» vs RF-11 (al crear el experimento solo se registran nombre, fecha y notas; el grupo, tratamiento y número de especímenes se capturan al subir el primer video) y `seq_carga_video`. P3: «consultar el estado de la cola» no corresponde a ningún caso de uso del paquete 3 dibujado (los casos son Monitorear progreso y Reportar error; la cola es de CU-13/Paquete 5). Resultados: «la consulta de resultados (Figura 5.x) devuelve los tiempos por espécimen y conducta» vs `seq_consulta_resultados`, que dibuja la comparación entre grupos con el Día 2.
- Fuente que decide: RF-11, RF-21, diagramas vigentes.
- Corrección sugerida: P2 → «registrar nombre, fecha y notas; el grupo, tratamiento y número de especímenes se capturan al subir el primer video»; P3 → quitar «consultar el estado de la cola»; resultados → «devuelve la comparación entre grupos con el Día 2 (promedio por espécimen de cada grupo, con el nivel de clasificación)».

---

## Verificado y sin hallazgo

- **Etapas del pipeline:** `pipeline.puml`, `estados_analisis.puml`, `seq_analisis_automatico.puml`, `seq_consulta_progreso.puml` y `cu_paquete3.puml` usan solo preprocesamiento, localización de cilindros (`cilindros`) y clasificación; ni YOLO ni tracker salvo en comentarios históricos.
- **«Último segundo»:** no aparece en ningún diagrama, `.md` ni generador de mi área; la regla de bloques por mayoría figura solo en `clases_completo.md:96-98` (fuera de mi área, correcta).
- **300 s máximo sin mínimo:** `pipeline.puml:78` y `seq_analisis_automatico.puml:80,89` lo expresan bien (máximo, renumeración de 1 a 300). El «solo últimos 300 s» sin aclaración del cap. 5:115 es el pendiente del 6-oct ya conocido.
- **RN-04** (el análisis arranca solo): respetada en `seq_carga_video`, `seq_analisis_automatico`, `cu_paquete3`, `estados_analisis`; solo la viola el huérfano (DF-16).
- **RN-05/D-39** (30 días, 90 %): `cu_paquete5`, CU-14 y `seq_analisis_automatico` coinciden; ver DF-24 por «programa».
- **Sin autorregistro, sin bloqueo por intentos, sin «último acceso», cierre de sesión por descarte del token:** `seq_crear_cuenta`, `seq_login`, `seq_logout` coinciden con D-01, D-36, D-37, D-48. `seq_logout` y CU-02 coinciden palabra por palabra en el punto del token.
- **Nombres de tabla/columna** de las secuencias (`ANALISIS`, `ADMINISTRADOR`, `USUARIO`, `SEGUNDO`, `INTERVALO`, `PRESENTA`, `REPORTE`, `OBSERVACION`, `nivelClasif`, `cambioRequerido`, `origen`, `fechaAnalisis`, `fechaGeneracion`, `ruta`) existen en el grafo vigente. La única columna que no está es `ANALISIS.rutaDiagnostico` (M-24 ya conocido: sí está en `esquema_fisico.puml` y apéndice D).
- **PNG contra `.puml`:** `flujo_general`, `pipeline`, `arquitectura_software`, `estados_analisis`, `cu_vision_general`, `cu_paquete1`, `cu_paquete3` reflejan exactamente su fuente.
- **Terminología prohibida** («inteligencia artificial», «animales», «rata», «ISRS», «gold standard», «κ», «MAE», «cámara de celular»): solo aparece en comentarios históricos (`seq_analisis_automatico.puml:15-31`, `flujo_general.puml:11-47`, `pipeline.puml:7`, `grafo_relacional_3_vigente.puml:18`) como registro de lo que se quitó; no en texto visible.

## Cobertura y límites

- No abrí los PNG de `seq_login`, `seq_logout`, `seq_carga_video`, `seq_consulta_progreso`, `seq_crear_cuenta`, `seq_descarga_reportes`, `seq_gestion_usuarios`, `seq_revision_segundos`, `estados_experimento`, `cu_paquete2/4/5`: confié en que cada PNG es el render del `.puml` por tener el mismo commit (verificado por `git log`) o posterior.
- `diagram_design/*.html` y `generadores/gen_despliegue.py` no se leyeron línea por línea; se verificó solo por búsqueda de términos que no hubiera términos prohibidos ni «último segundo». `gen_clases.py`, `clases_completo.md` y `clases.puml` quedan para el agente de clases.
- No audité los mockups (`figures/mockups/`), que fuera de `\includegraphics` de mockups no son diagramas de flujo, ni el apéndice D salvo para cruzar `nivelClasif` y `rutaDiagnostico`.
- `gen_pngs.sh` (rutas absolutas `/home/vane/…`, `/tmp/plantuml.jar`) es el pendiente conocido M-30; no se repite.
- Para DF-09 y DF-11 no hay fuente de rango superior que decida; quedan como inconsistencias para resolver con el equipo.
