# 09 — Terminología y prohibiciones (reauditoría 11-oct, HEAD 975ec4c)

## Alcance auditado
`chapters/01` a `05`, `front/` (portada, documento_tecnico, advertencia, resumen, glosario, abreviaturas), `back/apendice_C.tex`, `back/apendice_D.tex`, y el texto visible de `diagramas/` (`.puml` que alimentan `figures/mermaid/*.png`, `esquema_conceptual.tex`, `diagram_design/`). Los PNG de `figures/mermaid/` tienen la misma fecha que sus `.puml`, así que las notas `note ... end note` y los mensajes de las secuencias son texto visible de las figuras.

| Severidad | Cantidad | De ellas, preguntas abiertas |
|---|---|---|
| Alta | 1 | 0 |
| Media | 5 | 1 (TT-05) |
| Baja | 10 | 2 (TT-14, TT-15) |
| Total | 16 | 3 |

Sin hallazgo (verificado con grep, con y sin tildes, descartando comentarios `%` y `'`): κ/kappa/Cohen, MAE, «gold standard», «inteligencia artificial», «ISRS» en el cuerpo, «cámara de celular», «Neurociencia Conductual» fuera del apéndice C, BORIS, «último segundo», umbral 0.70, ByteTrack/tracker, «F1 por clase» en prosa, «DER» aplicado a un modelo con tipos/FK (el DER del cap. 5 es el conceptual; el físico se llama «esquema físico»), `D-xx`/`P-xx`/`Q-xx` en los `.tex`, TT1/TT2 en cap. 1–3 y 5. «Rata» fuera del glosario de espécimen: solo aparece en cap. 5:416 y en la figura del esquema físico (TT-03). YOLO, ResNet y *Random Forest* aparecen solo como estado del arte o candidatos, y el texto aclara que no se usan o no están elegidos.

---

## Alta

### TT-01 — La figura de arquitectura todavía dice «correccion CLAHE» en el worker
- Severidad: Alta (contradice D-16: pipeline de tres etapas, sin CLAHE ni EMA)
- Ubicación: `diagramas/arquitectura_software.puml:87` (figura `figures/mermaid/arquitectura_software.png`, insertada en `chapters/05_diseno.tex:53`) frente a `chapters/05_diseno.tex:138` (módulo de preprocesamiento) y `diagramas/diagram_design/arquitectura_capas.md:59`
- Cita: figura: «OpenCV         Preprocesamiento y correccion CLAHE». Cap. 5:138: «\textbf{Registro de cámara.} Alinea cada cuadro contra uno de referencia». `arquitectura_capas.md:59`: «El capítulo 5 dice que el sistema *no* aplica…» (el `.md` ya documenta la discrepancia). En los `.tex` no hay ningún «CLAHE».
- Fuente que decide: D-16 (brief: «sin CLAHE ni EMA»)
- Destinatario: Erick
- Previo: nuevo
- Corrección sugerida: cambiar la línea a «OpenCV   Preprocesamiento (registro de cámara y modelo de fondo)», igual que ya está en `diagramas/pipeline.puml:42-46`. De paso, la misma figura (línea 101) lista solo «Videos .mp4 originales»; el brief dice `.mp4` y `.mov` (D-30), y «Videos anotados _tracked.mp4» arrastra el nombre de un tracker que ya no existe. Regenerar el PNG.

---

## Media

### TT-02 — Códigos D-xx y Q-E, fechas y meta-comentarios visibles dentro de las figuras
- Severidad: Media (brief: «D-xx/P-xx/Q-xx visibles en texto o figuras»)
- Ubicación (texto visible, no comentario `'`):
  - `diagramas/esquema_fisico.puml:146, 148, 193, 196, 214, 219, 222-225, 228, 230, 233, 280, 284, 286, 293, 339` (figura 5.5 del cap. 5, `chapters/05_diseno.tex:380`)
  - `diagramas/estados_analisis.puml:16` (`chapters/05_diseno.tex:313`)
  - `diagramas/seq_crear_cuenta.puml:58, 89`; `seq_consulta_progreso.puml:79, 91`; `seq_consulta_resultados.puml:80 (Q-E), 93`; `seq_descarga_reportes.puml:68`
- Cita: «D-10: activo evita el DELETE. Contraseña con bcrypt + sal (RNF-05, ya resuelto en el .tex)»; «D-25 (15-sep): cambioRequerido obliga…»; «Aplicado aqui por primera vez a peticion del usuario (15-sep)»; «idVideo : integer <<FK>> <<UK>> (D-24)»; «(no se suman, para que el tamaño del grupo\nno distorsione la comparación -- Q-E)»; «se generó el reporte de\ndiagnostico (D-23)»
- Fuente que decide: brief (terminología obligatoria) y regla de CLAUDE.md «sin SQL ni código dentro de los diagramas» (la nota también dice «DELETE» y `estado='error'`)
- Destinatario: Erick (esquema físico y secuencias de análisis); Vanesa (`seq_crear_cuenta`, `seq_gestion_usuarios` si aplica)
- Previo: TT-04
- Corrección sugerida: quitar de las notas todo `D-xx`, `Q-E`, fechas de sesión («15-sep», «4-oct», «5-oct») y frases de proceso («ya resuelto en el .tex», «a petición del usuario»). Dejar solo la regla en lenguaje natural, p. ej. «activo evita borrar usuarios», «el identificador del video es único: un video tiene un solo análisis vigente», «cada fila es un segundo analizado; son como máximo los últimos 300 s». Mover la trazabilidad a los comentarios `'` del `.puml`. Los PNG de `seq_cambio_pass_inv`, `seq_perfil` y `seq_notificaciones` (sin `.puml`) los leí y están limpios.

### TT-03 — «número de rata» en el cuerpo del cap. 5 y en la figura del esquema físico
- Severidad: Media (brief: «rata» solo en la entrada de glosario de espécimen)
- Ubicación: `chapters/05_diseno.tex:416`; `diagramas/esquema_fisico.puml:194-196` (nota visible de la figura, `05_diseno.tex:380`)
- Cita: cap. 5: «no guarda el número de rata del laboratorio»; figura: «No se guarda el numero de rata del laboratorio: ya no hay comparacion Dia 1 contra Dia 2 por rata (D-44)»
- Fuente que decide: brief (terminología) y D-44 (no hay comparación Día 1 vs Día 2)
- Destinatario: Erick
- Previo: TT-01
- Corrección sugerida: cap. 5: «no guarda el identificador que el laboratorio le da al espécimen». Figura: «El espécimen se distingue por su posición en el cuadro (numeroCilindro); el sistema no guarda el identificador del laboratorio».

### TT-04 — «anotación experta» alimenta el entrenamiento (cap. 5) frente a la figura de flujo que dice lo contrario
- Severidad: Media (inconsistencia entre texto y figura)
- Ubicación: `chapters/05_diseno.tex:101` frente a `chapters/05_diseno.tex:250` y `diagramas/flujo_general.puml:69, 73`
- Cita: texto del pie de la Fig. de flujo: «el ciclo de entrenamiento del modelo ---anotación experta, dataset y entrenamiento--- alimenta al clasificador»; cap. 5:250: «se entrena con bloques de 5 s etiquetados por el equipo, sin usar las anotaciones del laboratorio»; figura: «SIN anotación del Dr. Sandino, ni para entrenar ni para probar»
- Fuente que decide: lo ya decidido (CLAUDE.md, «Prohibición vigente»: el clasificador se entrena sin las anotaciones del Dr. Sandino)
- Destinatario: Erick
- Previo: TT-02
- Corrección sugerida: «…el ciclo de entrenamiento del modelo ---etiquetado de bloques por el equipo, conjunto de datos y entrenamiento--- alimenta al clasificador de conducta.» (`diagram_design/flujo_sistema.md:55` ya señala la misma discrepancia).

### TT-05 — «despliegue» registrado en requisitos, costos y figura (D-62)
- Severidad: Media (pregunta abierta sobre el alcance de D-62)
- Ubicación: `chapters/04_analisis.tex:351` (RNF-03), `404-406` (RNF-10), `698`, `880`, `906`, `1058` (tabla de costos: «Formación técnica… y despliegue con Docker»); `chapters/05_diseno.tex:23, 30`; `diagramas/flujo_general.puml:69`; `front/glosario.tex:115` («se despliega como cuatro contenedores»)
- Cita: RNF-10: «Despliegue documentado y verificado en al menos dos entornos distintos»; costos: «cursos especializados de visión por computadora y despliegue con Docker»; figura: «(offline, antes de desplegar -- no es parte del flujo por video)»; cap. 5:23: «de comportamiento y de despliegue»
- Fuente que decide: D-62 dice que el despliegue está fuera de alcance y no debe quedar registrado en alcance, cronograma ni responsabilidades. Que el uso técnico de la palabra (Docker, contenedores, la vista de despliegue de ISO 42010) también deba desaparecer no está dicho → pregunta abierta → tú y el usuario
- Destinatario: Erick (cap. 4 y 5), Vanesa si se toca el glosario
- Previo: nuevo
- Corrección sugerida: depende de la respuesta. Mínimo, sin ambigüedad: la tabla de costos (`04_analisis.tex:1058`), el criterio de aceptación de RNF-10 («Despliegue documentado y verificado…») y la figura de flujo («antes de desplegar») tratan el despliegue como una actividad del proyecto. Reescribir RNF-10 como «El sistema se levanta con Docker Compose en un equipo con Docker instalado; prueba: arranque verificado en dos equipos» y la figura como «(fuera de línea, previo al análisis de cada video)». Los demás usos son descripciones técnicas del paquete Docker y pueden quedarse si se confirma. `diagram_design/despliegue.md:48` también habla de «el despliegue permanente… ESCOM» como alcance (no es `.tex`; solo para saberlo).

### TT-06 — La figura del pipeline dice que se analiza el video completo
- Severidad: Media (contradice D-31 / D-54: máximo los últimos 300 s)
- Ubicación: `diagramas/pipeline.puml:34` frente a `chapters/05_diseno.tex:116` y `diagramas/pipeline.puml:85`
- Cita: figura: «Video subido por el usuario\n(se analiza completo)»; cap. 5: «analiza solo sus últimos 300 segundos»; la misma figura, módulo 4: «Se queda con los últimos 300 s del video»
- Fuente que decide: D-31, D-54
- Destinatario: Erick
- Previo: nuevo
- Corrección sugerida: «Video subido por el usuario\n(se usan como máximo los últimos 300 s)». Esto afecta la lectura de «analiza» frente a «retiene»: si el pipeline procesa todo y solo conserva 300 s, el cap. 5 debe decirlo así.

---

## Baja

### TT-07 — «TT2» frente a «TT-II»
- Severidad: Baja
- Ubicación: `chapters/04_analisis.tex:345, 442, 459` frente a `front/abreviaturas.tex:62` y `chapters/04_analisis.tex:691, 967, 975`
- Cita: «fase de validación (TT2)»; abreviaturas: «TT-II & Trabajo Terminal II»; cap. 4:967: «validación en TT-II»
- Fuente que decide: `abreviaturas.tex` y cap. 1:359 («abreviados TT-I y TT-II»)
- Destinatario: Erick
- Previo: TT-05 (el resto ya se unificó a TT-I/TT-II)
- Corrección sugerida: sustituir los tres «TT2» por «TT-II».

### TT-08 — «cuatro módulos» frente a «tres etapas» del pipeline
- Severidad: Baja
- Ubicación: `chapters/05_diseno.tex:119` frente a `05_diseno.tex:303, 1510, 2460` y `diagramas/pipeline.puml` (cuatro `partition`)
- Cita: «Está organizado en cuatro módulos secuenciales: preprocesamiento, localización de los cilindros, clasificación de conducta y generación de resultados»; «avanza por las tres etapas del pipeline»
- Fuente que decide: D-16 (tres etapas: preprocesamiento, localización, clasificación)
- Destinatario: Erick
- Previo: nuevo
- Corrección sugerida: aclarar una vez que son tres etapas de procesamiento más la generación de resultados, y usar «etapa» para las tres primeras y «paso final» o «resultados» para la cuarta, o rotular la cuarta partición de la figura «Resultados (no es etapa)».

### TT-09 — «Requerimientos» frente a «Requisitos» (RF, RNF)
- Severidad: Baja
- Ubicación: `front/abreviaturas.tex:53, 55`, `chapters/01_introduccion.tex:402`, `03_marco_teorico.tex:81` frente a `chapters/04_analisis.tex:27, 305, 316`
- Cita: abreviaturas: «RF & Requisito Funcional», «RNF & Requisito No Funcional»; cap. 4:27: «\subsection{Requerimientos Funcionales (RF)}»; cap. 4:305: «Requerimientos No Funcionales (RNF)»
- Fuente que decide: pregunta de estilo (el brief no fija cuál); se propone «requerimiento», que es la forma del cap. 4 (14 usos frente a 1)
- Destinatario: ambos (abreviaturas y cap. 1 son de Vanesa)
- Previo: nuevo
- Corrección sugerida: abreviaturas: «Requerimiento Funcional» y «Requerimiento No Funcional»; cap. 1:402 «requerimientos funcionales y no funcionales»; igual en 01:176, 03:81, 04:790.

### TT-10 — Siglas sin definir en su primera aparición (orden de `main.tex`)
- Severidad: Baja
- Ubicación (sigla: primera aparición → definición):
  - `YOLO`: `02_estado_arte.tex:79` (título de subsección «YOLO-Behaviour») → se expande en `02:175`
  - `ResNet`: `02:52` («ResNet-3D») → `03_marco_teorico.tex:236`
  - `GPU`: `02:246`; `HTTP`: `03:300`; `URL`: `03:302`; `RN`: `03:272`; `ML` ya definida en `02:199` (sin hallazgo)
  - `MP4`/`MOV`/`PDF`/`CSV`/`XLSX`: `01:257, 289, 290`; `API`/`REST`/`UML`/`BD`: `01:405, 413`
  - `RNF`: `04:239` («ver RNF-09») antes de su encabezado en `04:305`; `ETA`: `04:265`; `ESCOM`: `04:403` (en el cuerpo nunca se expande; solo en portada y abreviaturas); `PEP`/`ESLint`: `04:416`; `MXN`: `04:989`; `PSF`/`BSD`/`MIT`: `04:1130`
  - `CU`: `05_diseno.tex:320`; `DDL`: `back/apendice_D.tex:28`
  - Además, el glosario usa `HTTP`, `JSON`, `FIFO`, `SERT`, `ORM`, `ACID`, `VP`/`FP`/`FN` antes de que `abreviaturas.tex` (que viene después) los defina.
- Cita: p. ej. `03:300`: «La API REST usa semántica HTTP estándar»; `04:403`: «servidor institucional provisto por la ESCOM»
- Fuente que decide: brief («siglas definidas en la primera aparición»); CLAUDE.md exime las de uso común en español técnico (GPU, API, REST, JSON, CSV, PDF), así que lo prioritario es: ESCOM, RN/RNF/CU (en su primera mención), ETA, PEP/ESLint, PSF/BSD/MIT, YOLO y ResNet.
- Destinatario: ambos
- Previo: TT-10
- Corrección sugerida: expandir en la primera mención: «Escuela Superior de Cómputo (ESCOM)», «tiempo estimado de término (ETA)», «reglas de negocio (RN)» en 03:272, «\textit{You Only Look Once} (YOLO)» en 02:79 y «redes residuales (ResNet)» en 02:52. Faltan en `abreviaturas.tex`: `MXN`, `FNBC`, `GMM`, `BD`, `ETA`, `PEP`, `DDL`, `SERT`, `FIFO`, `ACID`.

### TT-11 — Anglicismos sin `\textit{}`/traducción en la primera aparición, y cursiva inconsistente después
- Severidad: Baja
- Ubicación (primera aparición): `worker` `03_marco_teorico.tex:311` («Un proceso worker independiente»; el término ya aparece en cursiva en cap. 5:1592 pero no en 5:26); `clips` `03:228` («los clips etiquetados»); `framework` `04_analisis.tex:695, 739`; `hash` `04:365`, `05:389`; `transfer learning` y `dataset` en `04:872-874` (italizados antes solo en cap. 1–2); `mockups` `05:2484`; `bounding boxes` `front/glosario.tex:308`; `one-hot` `glosario.tex:128`. Figuras: `held-out` y `offline` en `diagramas/flujo_general.puml:69, 73, 77`.
- Cita: «Un proceso worker independiente toma la tarea de la cola»; «Framework de aprendizaje profundo»; «Hash con sal usando bcrypt»; «(held-out de los mismos clips, no anotación experta)»
- Conteo de cursiva en cap. 1–5 (italizado/total): `backend` 4/22, `frontend` 3/17, `pipeline` 4/53, `dashboard` 20/38, `worker` 28/45, `dataset` 3/12.
- Fuente que decide: brief («primera aparición `\textit{término}` + traducción, luego solo `\textit{}`»)
- Destinatario: ambos
- Previo: TT-08, TT-09
- Corrección sugerida: `\textit{worker} (proceso de segundo plano)` en 03:311; `\textit{clips} (fragmentos de video)` en 03:228; `\textit{framework} (marco de trabajo)`; `\textit{hash} (resumen criptográfico)`; en la figura, «conjunto de prueba reservado de los mismos clips» y «fuera de línea». Decidir si «pipeline/backend/frontend/dashboard» van siempre en cursiva (la regla literal) o se aceptan como préstamos ya asentados; hoy se mezclan dentro del mismo capítulo.

### TT-12 — «clases» donde el clasificador asigna conductas
- Severidad: Baja
- Ubicación: `chapters/04_analisis.tex:828`, `874`
- Cita: «Diseño modular del clasificador para incorporar clases adicionales»; «unos pocos cientos de ejemplos por clase»
- Fuente que decide: brief («conducta», no «clase», para lo que se asigna por segundo). Los usos en `03_marco_teorico.tex:282, 361-363` son definición formal de métricas y son legítimos, y `02:179, 228` hablan de YOLO e ImageNet.
- Destinatario: Erick
- Previo: TT-12
- Corrección sugerida: «incorporar conductas adicionales»; «unos pocos cientos de ejemplos por conducta».

### TT-13 — «intentos de escape» como nombre de la conducta de escalamiento
- Severidad: Baja
- Ubicación: `chapters/01_introduccion.tex:271`
- Cita: «nado activo, inmovilidad e intentos de escape (escalamiento)»
- Fuente que decide: terminología del propio documento («escalamiento», cap. 3 y 4); la glosa en cap. 1 sí lo aclara, y el glosario conserva «Climbing / escape attempts» como traducción
- Destinatario: Vanesa
- Previo: TT-13 (ya se quitó en `resumen.tex`; queda una)
- Corrección sugerida: «nado activo, inmovilidad y escalamiento».

### TT-14 — «animal(es)» en la descripción de trabajos relacionados (cap. 2)
- Severidad: Baja (pregunta abierta → equipo)
- Ubicación: `chapters/02_estado_arte.tex:81, 82, 86` (también `01_introduccion.tex:38`, «bienestar animal», nombre de la norma)
- Cita: «cuantificar conductas animales en video»; «detectar primero al animal y clasificarlo después»; «se ha aplicado a animales y escenarios muy distintos»
- Fuente que decide: el brief prohíbe «animales» en el cuerpo, pero aquí se describe un trabajo ajeno que cubre aves y otras especies, donde «espécimen» sería impreciso → pregunta abierta → equipo
- Destinatario: Vanesa
- Previo: nuevo
- Corrección sugerida: si se aplica la regla literal: «cuantificar conductas de especímenes»; «detectar primero al espécimen»; «a especies y escenarios muy distintos». «Bienestar animal» (cap. 1:38) se queda por ser la denominación de la NOM.

### TT-15 — Meta de F1 lista solo tres conductas
- Severidad: Baja (pregunta abierta → equipo)
- Ubicación: `chapters/04_analisis.tex:344`
- Cita: «F1 $\geq 85$\,\% por conducta (nado, inmovilidad, escalamiento)»; `04:958` y `05:442` listan cuatro conductas
- Fuente que decide: pregunta abierta → equipo (¿la meta de 85 % aplica también a la conducta activa, que el diseño trata como categoría de respaldo?)
- Destinatario: Erick
- Previo: nuevo
- Corrección sugerida: si aplica a las cuatro: «por conducta (nado activo, inmovilidad, escalamiento y conducta activa)»; si no, decirlo: «por conducta (excepto conducta activa, que es de respaldo)».

### TT-16 — Discrepancia CLAUDE.md ↔ LaTeX: «F1 por clase» frente a «F1 por conducta» (D-65)
- Severidad: Baja (no es error del LaTeX)
- Ubicación: `CLAUDE.md`, sección «Prohibición vigente — métricas de validación» («F1 por clase», «F1 ≥ 85 % por clase») frente a `chapters/01_introduccion.tex:179, 204`, `04_analisis.tex:340-345, 445`, `front/resumen.tex:29`
- Cita: CLAUDE.md: «precisión, \textit{recall} y F1 por clase»; LaTeX: «F1 por conducta»
- Fuente que decide: D-65
- Destinatario: tú y el usuario (CLAUDE.md)
- Previo: TT-06 (el LaTeX ya se corrigió; queda el `.md`)
- Corrección sugerida: cambiar en `CLAUDE.md` «por clase» por «por conducta».

---

## Cobertura y límites
- Leí completos los `.tex` incluidos en `main.tex` (cap. 1–5, front, apéndices C y D) mediante grep sobre líneas no comentadas más lectura de contexto de cada hallazgo; en las figuras, los `.puml` activos, `esquema_conceptual.tex` (texto de nodos limpio), `diagram_design/*.md|py|html` por grep, y los tres PNG sin `.puml` (`seq_notificaciones`, `seq_perfil`, `seq_cambio_pass_inv`). No abrí el resto de PNG: asumo que corresponden a sus `.puml` por tener la misma fecha de modificación.
- Apéndice C: tiene «celular», «animal», «rata», «ISRS» y el nombre viejo del laboratorio, todos dentro de la transcripción literal (excepción del brief); no son hallazgo. La introducción del apéndice usa el nombre correcto del laboratorio.
- D-57 a D-60 pendientes de propagar: `diagramas/seq_analisis_automatico.puml:98` y `chapters/05_diseno.tex:1510` siguen diciendo «el investigador no puede reiniciarlo (RN-04)». Se menciona solo aquí.
- `diagramas/relacional.puml` (tabla `ANIMALES`) es un diagrama antiguo que no entra en ningún `\includegraphics`; no lo cuento.
- Las siglas las revisé con un script sobre el orden real de `main.tex` (resumen, glosario, abreviaturas, cap. 1–5, apéndice D) y revisé a mano la lista; puede haberme dejado alguna sigla de menos de dos mayúsculas.
- No pude determinar si los usos técnicos de «despliegue» (TT-05) deben eliminarse; queda como pregunta abierta.
