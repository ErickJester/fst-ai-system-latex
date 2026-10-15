# Cierre de la auditoría del 11-oct contra la rama `accesos-login`

**Contra:** `origin/accesos-login` en `fd3d543` (fecha de la revisión: 2026-10-11). **Auditoría de origen:** `hallazgosAgentes11oct/` en `main` (`00f045a`).

**Cómo se verificó.** Cada uno de los 177 hallazgos se contrastó contra el contenido de esa rama (extraído con `git archive`, sin tocar el árbol de trabajo): se buscó la cita textual del hallazgo y, cuando hacía falta, se leyó la línea. No se compiló LaTeX ni PlantUML.

**Estados.** *Resuelto*: el texto o la fuente ya no tiene el problema. *Parcial*: se corrigió una parte (casi siempre la fuente `.puml`, pero el PNG que entra al documento sigue viejo) o quedan ocurrencias en otro archivo. *Sin resolver*: sigue igual o es pregunta abierta sin decisión.

## Resumen

| Severidad | Total | Resuelto | Parcial | Sin resolver |
|---|--:|--:|--:|--:|
| Alta | 19 | 14 | 4 | 1 |
| Media | 81 | 29 | 10 | 42 |
| Baja | 77 | 33 | 5 | 39 |
| **Total** | **177** | **76** | **19** | **82** |

| Agente | Total | Resuelto | Parcial | Sin resolver |
|---|--:|--:|--:|--:|
| 01 · Cap. 1 | 22 | 21 | 1 | 0 |
| 02 · Cap. 2 | 14 | 14 | 0 | 0 |
| 03 · Cap. 3 | 12 | 11 | 1 | 0 |
| 04 · Cap. 4 | 19 | 4 | 0 | 15 |
| 05 · Cap. 5 | 21 | 7 | 3 | 11 |
| 06 · Diagramas relacional y de clases | 13 | 0 | 1 | 12 |
| 07 · Diagramas de flujo, CU y secuencia | 25 | 6 | 6 | 13 |
| 08 · Reglas en .md | 35 | 7 | 0 | 28 |
| 09 · Terminología | 16 | 6 | 7 | 3 |

**Qué explica la mayor parte de lo «Parcial»:** los commits cambiaron las fuentes `.puml` pero no regeneraron los PNG de `figures/mermaid/` y `diagramas/`, que son los que entran al documento (el mensaje del commit `fd3d543` dice «Los PNG se regeneran aparte»).

## 01 · Cap. 1

| ID | Sev. | Hallazgo | Estado | Evidencia en `accesos-login` |
|---|---|---|---|---|
| C1-01 | A | «La propuesta original del sistema se conserva» contradice D-53 | Resuelto | Ya no dice que se conserva la propuesta original; el cap. 1 habla del origen de cada segundo |
| C1-02 | A | (Fuera del cap. 1) El cap. 5 aún promete la comparación Día 1 vs Día 2 | Resuelto | Comparación Día 1 vs. Día 2 quitada del Paquete 4 y de CU-09 (ahora entre grupos con el Día 2) |
| C1-03 | M | El cap. 1 dice que DSAAN clasifica tres conductas; el cap. 2 dice que no | Resuelto | Cap. 1 y cap. 2 coinciden: solo della_valle2025/3D-RCNN distingue las tres conductas |
| C1-04 | M | Alcance «Corrección automática de calidad»: «no preprocesa» y las condiciones que dispa… | Resuelto | «No preprocesa» desapareció; el alcance dice que se detiene y genera diagnóstico si no halla cilindros |
| C1-05 | M | «Despliegue ESCOM» en el cronograma contra «despliegue institucional fuera del alcance» | Resuelto | Despliegue fuera del alcance y fuera del cronograma y del stack (D-62) |
| C1-06 | M | «Clasifica cuadro a cuadro» frente a «cada segundo recibe una conducta» | Parcial | Cap. 1 corregido; siguen «cuadro a cuadro» en RF-17 (cap. 4:167) y cap. 5:169 |
| C1-07 | M | Descripción del análisis manual (cap. 1) frente a la entrevista P12 | Resuelto | El análisis manual se describe como una pasada por conducta (entrevista P12) |
| C1-08 | M | «Gráficas de barras de distribución por conducta» no existe en RF-21 ni en el cap. 5 | Resuelto | Quitadas las gráficas de barras |
| C1-09 | M | «OE-5» se cita desde el cap. 5, pero el cap. 1 no rotula los objetivos | Resuelto | Objetivos rotulados OG y OE-1 a OE-6 en el cap. 1 |
| C1-10 | B | «Cada video graba… en dos sesiones» confunde video con tanda | Resuelto | Reescrito: la tanda tiene uno o dos videos |
| C1-11 | B | «Cola… para hasta cuatro análisis» confunde análisis con usuarios | Resuelto | Ahora dice cuatro usuarios en el mismo periodo (L303) |
| C1-12 | B | «En minutos genera un reporte» sin respaldo en los requisitos | Resuelto | El reporte se genera «cuando termina» |
| C1-13 | B | Cronograma de Ángel: «casos de uso» en el cap. 4 y cap. 3 ausente | Resuelto | El cronograma ya no promete casos de uso en el cap. 4 |
| C1-14 | B | «Flujo óptico» en el cronograma del baseline sin respaldo en el pipeline | Resuelto | Quitado el flujo óptico del cronograma |
| C1-15 | B | Nombre del integrante: «Ángel Ali» / «Ángel Alí» / «Ángel» | Resuelto | Unificado «Ángel Alí» (queda un «Ángel» informal en L504) |
| C1-16 | B | Los requisitos mínimos de calidad de video se atribuyen a *performance efficiency* | Resuelto | Quitada la cláusula de la ISO 25010 sobre robustez |
| C1-17 | B | Siglas sin definir en su primera aparición en el cap. 1 | Resuelto | ESCOM ya no aparece; IPN, OMS, JWT y TT-I/TT-II definidos |
| C1-18 | B | Términos en inglés con peso conceptual sin \textit ni traducción | Resuelto | Forced Swim Test, pipeline, backend, frontend, dataset y sprint con cursiva y traducción |
| C1-19 | B | ANY-maze se afirma sin cita | Resuelto | ANY-maze con cita (stoelting_anymaze, entrada nueva en el .bib) |
| C1-20 | B | Concordancia de género: «con la siguiente» | Resuelto | Redacción corregida («Luego repite el proceso con el siguiente») |
| C1-21 | B | «Comparación entre grupos» descrita dos veces en el alcance | Resuelto | Ya no repite la misma comparación (quedan dos viñetas con contenido distinto) |
| C1-22 | B | Cap. 3 habla de «Sprint 6»; la metodología del cap. 1 no numera sprints | Resuelto | El cap. 3 ya no habla de «Sprint 6» |

## 02 · Cap. 2

| ID | Sev. | Hallazgo | Estado | Evidencia en `accesos-login` |
|---|---|---|---|---|
| C2-01 | M | chan2025_yolo: autores del .bib no corresponden al artículo | Resuelto | Autores de chan2025_yolo corregidos (Alex Hoi Hang Chan et al.) |
| C2-02 | M | della_valle2025: lista de autores incompleta/alterada | Resuelto | della_valle2025 con Pilati y los demás autores |
| C2-03 | M | meng2024_dsaan: nombres de pila de los autores no coinciden | Resuelto | meng2024_dsaan con nombres corregidos y número de artículo |
| C2-04 | M | Descripción de YOLO-Behaviour como «detección + clasificador independiente» (pregunta a… | Resuelto | Sección reescrita como «detección directa de la conducta»; la comprobación contra el artículo no se repitió |
| C2-05 | M | «Los de aprendizaje profundo más recientes sí clasifican las tres conductas» contradice… | Resuelto | La conclusión del cap. 2 ya no afirma que los de aprendizaje profundo clasifican las tres conductas |
| C2-06 | M | Escalamiento: «mitad superior del cilindro» (cap. 2) vs. «vista cenital … borde del cil… | Resuelto | Quitada la «vista cenital» del cap. 3 |
| C2-07 | M | «Este proyecto sigue ese camino con un clasificador de gradient boosting» suena a decis… | Resuelto | Gradient boosting presentado como uno de los dos candidatos |
| C2-08 | B | «Los de código abierto no usan aprendizaje profundo ni tienen interfaz web» contradice … | Resuelto | Frase de herramientas de código abierto corregida |
| C2-09 | B | Párrafo de YOLO: afirma relevancia y recomendaciones de entrenamiento para algo que el … | Resuelto | Quitadas las frases de relevancia y de entrenamiento del párrafo de YOLO |
| C2-10 | B | Sturman et al. y DeepLabCut descritos dos veces casi textualmente | Resuelto | Sturman/DeepLabCut ya aparece una sola vez |
| C2-11 | B | Términos en inglés sin \textit{} o sin traducción; siglas y abreviaturas sin definir | Resuelto | machine learning, deep learning, transfer learning y atributos ISO con cursiva y traducción |
| C2-12 | B | ANY-maze descrito sin cita (EthoVision sí la tiene) | Resuelto | ANY-maze citado |
| C2-13 | B | armario2021 citada para un descriptor que ese artículo (revisión conceptual del FST) pr… | Resuelto | Descriptor de armario2021 reemplazado por la descripción de los rasgos |
| C2-14 | B | Métrica de tiempo del cap. 2 no aparece en el cap. 4 | Resuelto | Tiempo de análisis en segundos; umbral fijado en pruebas (cap. 3) |

## 03 · Cap. 3

| ID | Sev. | Hallazgo | Estado | Evidencia en `accesos-login` |
|---|---|---|---|---|
| C3-01 | A | El cap. 3 presenta la CNN como el clasificador y no menciona el *gradient boosting* (cl… | Resuelto | Subsección de gradient boosting y portada del capítulo con los dos candidatos |
| C3-02 | M | «Se predice la conducta con mayor probabilidad» y tres conductas: omite la cuarta condu… | Resuelto | Regla de la cuarta conducta tras el softmax |
| C3-03 | M | cryan2005 es un artículo sobre la prueba de suspensión de la cola en ratón, citado para… | Parcial | cryan2005 quitada de los caps. 1 y 3; sigue en RN-07 (cap. 4:547) |
| C3-04 | M | Explicación de ResNet: atribuye la degradación al gradiente que se desvanece, lo que el… | Resuelto | ResNet explicada como problema de degradación |
| C3-05 | M | El Día 1 aparece como «línea base»; las decisiones lo dejan como sesión de estrés/habit… | Resuelto | El Día 1 pasa de «línea base» a habituación |
| C3-06 | M | La relación de tiempo de análisis está invertida respecto al cap. 2 | Resuelto | Tiempo de análisis en segundos, umbral en la fase de pruebas |
| C3-07 | B | «Lo que sigue cubre esos cuatro bloques» y el capítulo tiene cinco secciones | Resuelto | Frase de «cuatro bloques» reescrita |
| C3-08 | B | «Sprint~6» no existe en el documento | Resuelto | «Sprint 6» sustituido por «fase de pruebas» |
| C3-09 | B | Dominio de origen del *transfer learning*: ImageNet, aunque el candidato se preentrena … | Resuelto | Quitado ImageNet como dominio de origen |
| C3-10 | B | Sigla FPS sin definir en su primera aparición | Resuelto | FPS definida: «cuadros por segundo (FPS, frames per second)» |
| C3-11 | B | *Transfer learning* y *vanishing gradient problem* sin traducción en su primera aparici… | Resuelto | transfer learning con traducción en su primera aparición |
| C3-12 | B | Notación y nombre desalineados con glosario y abreviaturas (TP/VP, *Deep Residual Netwo… | Resuelto | Notación VP/FP/FN y ORM unificadas con glosario y abreviaturas |

## 04 · Cap. 4

| ID | Sev. | Hallazgo | Estado | Evidencia en `accesos-login` |
|---|---|---|---|---|
| C4-01 | A | R-03 sigue suponiendo que el laboratorio entrega registros para entrenar y validar | Resuelto | R-03 ya no supone registros del laboratorio |
| C4-02 | M | RN-15 afirma que el laboratorio usó la técnica de predominancia de Detke; la transcripc… | Sin resolver | RN-15 sin cambios; la atribución al laboratorio sigue (pregunta abierta, Q-A sin responder) |
| C4-03 | M | RF-33 no incluye la notificación del borrado adelantado, que RN-05, RF-25, RNF-09 y el … | Sin resolver | RF-33 sigue sin la notificación del borrado adelantado |
| C4-04 | M | RF-20 (desglose por minuto) tiene prioridad Media aunque el desglose es obligatorio | Sin resolver | RF-20 sigue en prioridad Media |
| C4-05 | M | «tres grupos» fijos en la factibilidad operativa; la lista vigente dice «tres o más (en… | Resuelto | Factibilidad: 3 a 4 experimentos con tres o más grupos y ~8 videos |
| C4-06 | M | RN-15 no cubre todos los casos de empate ni indica cómo cuenta la conducta «activa» por… | Sin resolver | RN-15 sin cambios (empates y conducta activa por segundo) |
| C4-07 | M | «PDF final», «resumen ejecutivo» y «reporte en PDF» nombran (¿o no?) lo mismo | Sin resolver | «PDF final» y «resumen ejecutivo» sin unificar |
| C4-08 | B | RF-05 y RF-07 duplican el alta de cuentas; «autoregistro» mal escrito | Sin resolver | RF-05/RF-07 siguen duplicados; «autoregistro» en L91 |
| C4-09 | B | RN-07 pide «exactamente una conducta» por cuadro, pero hay segundos sin conducta («no s… | Sin resolver | RN-07 sigue diciendo «en cada cuadro» |
| C4-10 | B | Dónde se valida la orientación del video: RN-10 (antes de subir, cliente) vs RF-10 (ant… | Resuelto | RN-10 separa extensión (interfaz) de orientación y reproducibilidad (servidor), D-64 |
| C4-11 | B | Siglas y términos en inglés sin definir o sin el formato del proyecto | Sin resolver | ETA, frontend/backend y transfer learning siguen sin formato |
| C4-12 | B | Notación TT2 / TT-II mezclada dentro del capítulo | Sin resolver | TT2 en L345, 441, 458 frente a TT-II en otras |
| C4-13 | B | La referencia «véase la sección umbrales» en RN-11 ya no lleva a nada que le corresponda | Sin resolver | RN-11 sigue remitiendo a la sección de umbrales |
| C4-14 | B | Criterio de tiempo: R-04 remite a RNF-02, que dice que el tiempo no es criterio; la fac… | Sin resolver | Criterio de tiempo sin decidir (pregunta abierta) |
| C4-15 | B | Atribuciones a normas dudosas: «atributo de portabilidad» de ISO/IEC/IEEE 12207 y nombr… | Resuelto | ISO 25010 citada en su edición 2011 (decisión del 6-oct) y 12207 sin «portabilidad» |
| C4-16 | B | Pressman citado como respaldo de los umbrales de 80/90 % de disco | Sin resolver | Pressman sigue respaldando los umbrales de disco |
| C4-17 | B | Privacidad: «no registra datos personales» frente a cuentas con nombre, apellidos y cor… | Sin resolver | Privacidad y «almacenamiento cifrado» sin cambios |
| C4-18 | B | «cuadros etiquetados» / «clase» / «clases adicionales» para lo que ahora son segundos y… | Sin resolver | «cuadros etiquetados» y «clases adicionales» siguen (L795-874) |
| C4-19 | B | RNF-02 lista solo tres conductas en la métrica; el resto del capítulo tiene cuatro | Sin resolver | RNF-02 sigue listando tres conductas |

## 05 · Cap. 5

| ID | Sev. | Hallazgo | Estado | Evidencia en `accesos-login` |
|---|---|---|---|---|
| C5-01 | A | Comparación «Día 1 vs. Día 2» sigue en el paquete 4 y en el curso alterno de CU-09 | Resuelto | Paquete 4 y CU-09 hablan de comparación entre grupos con el Día 2 |
| C5-02 | A | CU-07 aún promete «código y descripción del error» para fallos del análisis | Resuelto | CU-07 ya no muestra código del error del análisis |
| C5-03 | A | La figura de arquitectura (arquitectura_software.png) contradice el texto del cap. 5 y … | Parcial | Arreglado en arquitectura_software.puml; el PNG del cap. 5 sigue del 5-oct |
| C5-04 | M | diagramas/clases.png está desactualizado respecto de clases.puml y el texto no describe… | Sin resolver | clases.png (6-oct) sigue anterior a clases.puml (8-oct) |
| C5-05 | M | El cap. 5 afirma que físico y lógico tienen «las mismas columnas», pero rutaDiagnostico… | Sin resolver | L594 sigue diciendo «las mismas columnas» |
| C5-06 | M | Dominio de SEGUNDO.origen: el cap. 5 y RF-32 dicen cuatro valores, apéndice D y esquema… | Sin resolver | Dominio de origen sin decidir (pregunta abierta) |
| C5-07 | M | Dónde se captura el número de especímenes: CU-04, CU-05 y el Paquete 2 no coinciden | Resuelto | CU-04 y CU-05 piden el número de especímenes de la tanda, como el Paquete 2 |
| C5-08 | M | La eliminación de un experimento: CU-23 dice «desde el dashboard», la pantalla dice «en… | Resuelto | Eliminar desde el dashboard o el detalle, sin nombre ni contraseña (D-63) |
| C5-09 | M | Tabla de formas normales: dos filas incoherentes con el esquema | Sin resolver | Tabla de normalización sin cambios (L620, L639) |
| C5-10 | M | Figuras del cap. 5 con códigos D-xx, fechas internas y «rata» visibles | Parcial | Fuentes .puml limpias de D-xx, SQL y «rata»; los PNG no se regeneraron |
| C5-11 | M | El texto dice que «anotación experta» alimenta al clasificador; la figura y las fuentes… | Resuelto | El ciclo de entrenamiento usa clips etiquetados por el equipo |
| C5-12 | M | Detección parcial de cilindros: el cap. 5 dice «no aborta», RF-14/RN-11/CU-07 dicen «se… | Resuelto | Si no hay cilindros el pipeline se detiene sin resultados parciales |
| C5-13 | M | Remisión al «Capítulo 6» que no existe en el documento compilado | Sin resolver | Sigue la remisión al Capítulo 6 (L432) |
| C5-14 | B | «número de rata» en el cuerpo | Sin resolver | Sigue «número de rata» (L415) |
| C5-15 | B | «Cuatro módulos» frente a «tres etapas» del pipeline | Sin resolver | Sigue «cuatro módulos» (L118) |
| C5-16 | B | Listas de conductas con tres valores donde son cuatro | Parcial | CU-07 y CU-09 corregidos; flujo_general.puml sigue con tres conductas (L94) |
| C5-17 | B | Regla «siempre al menos un Administrador activo» sin RF ni RN (pregunta abierta) | Resuelto | Nueva RN-16 (al menos un Administrador activo), referenciada en CU-11 y CU-17 |
| C5-18 | B | El panel de administración muestra «el modelo del clasificador en uso»; ningún RF lo pi… | Sin resolver | El panel sigue mostrando «el modelo del clasificador en uso» (L2743) |
| C5-19 | B | Tabla de la API sin endpoints que las fichas necesitan; un endpoint de carga citado com… | Sin resolver | Tabla de la API sin cambios (L2656) |
| C5-20 | B | Términos en inglés sin criterio uniforme (cursiva y traducción) | Sin resolver | «worker» sin cursiva en L26-79 |
| C5-21 | B | «Esquema lógico» y «quince relaciones del esquema lógico» sin que el capítulo presente … | Sin resolver | Sigue «esquema lógico» sin presentarlo (L592) |

## 06 · Diagramas relacional y de clases

| ID | Sev. | Hallazgo | Estado | Evidencia en `accesos-login` |
|---|---|---|---|---|
| DR-01 | A | diagramas/clases.png (el que entra al cap. 5) quedó desactualizado frente a clases.puml | Sin resolver | clases.png no regenerado |
| DR-02 | M | Multiplicidad Intervalo 2..4 — Conducta escrita al revés (UML) en clases, generador, HT… | Sin resolver | clases.puml:196 igual |
| DR-03 | M | Experimento–Notificación: NOTIFICACION.idExperimento es nulo, pero grafo y físico dibuj… | Sin resolver | Cardinalidad de NOTIFICACION sin unificar |
| DR-04 | M | Video de Día 1 sin análisis ni observaciones (D-54 d) contra cardinalidades «1» y «2..4… | Sin resolver | Pregunta abierta; cardinalidades Video–Análisis (1,1) y Video–Observación (2,4) iguales |
| DR-05 | M | clases_completo.md dice que el documento «no tiene» los valores de origen humano_ciego … | Sin resolver | clases_completo.md sin cambios |
| DR-06 | M | El cap. 5 afirma que físico y lógico tienen «las mismas columnas»; el físico tiene una … | Sin resolver | L594 sigue diciendo «las mismas columnas» |
| DR-07 | M | El cap. 5 nombra «el esquema lógico» pero nunca lo muestra ni lo introduce (pregunta ab… | Sin resolver | Pregunta abierta; el cap. 5 sigue sin presentar el esquema lógico |
| DR-08 | M | Tabla de normalización: la lista de excepciones a la clave subrogada omite a PRESENTA | Sin resolver | PRESENTA sigue fuera de la lista de claves (L620) |
| DR-09 | M | Fila 3FN de USUARIO mal rotulada y razonamiento inexacto sobre el correo | Sin resolver | Fila 3FN de USUARIO igual (L639) |
| DR-10 | M | La figura del esquema físico (PNG del cap. 5) lleva SQL, siglas de decisiones internas … | Parcial | esquema_fisico.puml limpio de SQL y D-xx; el PNG (6-oct) no se regeneró |
| DR-11 | B | Encabezado del grafo vigente cuenta mal sus relaciones de «dominio experimental» | Sin resolver | Encabezado del grafo sin cambios |
| DR-12 | B | Comentario de arquitectura_software.puml dice 16 relaciones | Sin resolver | arquitectura_software.puml:36 sigue con «16 relaciones» |
| DR-13 | B | relacional.puml y er.png conservan el modelo descartado sin marca de obsoleto | Sin resolver | relacional.puml y er.png sin marca de obsoleto |

## 07 · Diagramas de flujo, CU y secuencia

| ID | Sev. | Hallazgo | Estado | Evidencia en `accesos-login` |
|---|---|---|---|---|
| DF-01 | A | El texto del cap. 5 dice que el entrenamiento usa «anotación experta»; la figura y la r… | Resuelto | Texto del cap. 5 ya no habla de anotación experta |
| DF-02 | A | La figura de arquitectura muestra «corrección CLAHE» en el worker; el cap. 5 dice que n… | Parcial | Quitados CLAHE y _tracked del .puml; el PNG sigue viejo |
| DF-03 | A | seq_consulta_resultados define «agrupado» como «dos conductas» y omite la conducta acti… | Parcial | seq_consulta_resultados.puml usa las cuatro conductas; el PNG sigue viejo |
| DF-04 | A | Cap. 5 sigue hablando de comparación «Día 1 vs. Día 2»; la comparación vigente es solo … | Resuelto | Día 1 vs. Día 2 quitado de la intro del Paquete 4 y de CU-09 |
| DF-05 | A | CU-07 (curso alterno 4) todavía muestra un «código» de error de análisis | Resuelto | CU-07 sin código de error |
| DF-06 | M | La figura del flujo del sistema (flujo_general) no coincide con el texto vigente en con… | Sin resolver | flujo_general.puml sigue con tres conductas y preprocesamiento viejo (L93-94) |
| DF-07 | M | «Los tres grupos del experimento» en dos secuencias; el modelo vigente es de tres o más… | Parcial | Texto de «tres grupos» corregido en los .puml; PNG viejos |
| DF-08 | M | Códigos internos de decisión (D-xx, Q-E) visibles dentro de las figuras que entran al d… | Parcial | D-xx y Q-E quitados de las fuentes .puml; PNG viejos |
| DF-09 | M | CU-11 y CU-12 están en el Paquete 1 del diagrama, pero sus fichas y la introducción del… | Resuelto | Fichas de CU-11 y CU-12 movidas al Paquete 1 |
| DF-10 | M | El envío de correo (RF-33, D-45) no aparece en ninguna figura del cap. 5: ni en notific… | Sin resolver | Sigue sin aparecer el correo en las figuras |
| DF-11 | M | seq_carga_video valida el formato en el backend después de subir; RN-10 y RF-08 piden r… | Sin resolver | seq_carga_video sigue validando en el backend tras subir (L69) |
| DF-12 | M | estados_analisis solo permite el error saliendo de «cilindros»; el texto dice que el vi… | Parcial | estados_analisis.puml permite error desde preprocesamiento; PNG viejo |
| DF-13 | M | diagram_design/pipeline_analisis presenta la CNN de fusión como flujo principal y deja … | Sin resolver | pipeline_analisis.md sin cambios (pregunta abierta) |
| DF-14 | M | «Video anotado»: unas figuras lo guardan y otra dice que se quitó porque el código no l… | Sin resolver | Video anotado sin unificar (pregunta abierta) |
| DF-15 | M | La figura de arquitectura valida solo .mp4; el sistema acepta .mp4 y .mov | Parcial | Arquitectura valida .mp4 y .mov en el .puml; PNG viejo |
| DF-16 | B | ciclo_vida_experimento.puml (huérfano): ninguna fuente vigente lo usa; conserva un botó… | Sin resolver | ciclo_vida_experimento.puml sin cambios |
| DF-17 | B | Comentarios de cabecera de varios .puml describen un modelo que ya cambió | Sin resolver | Comentarios de cabecera con BORIS y modelo viejo siguen |
| DF-18 | B | Código y detalles de transporte dentro de diagramas que deben estar en lenguaje natural | Sin resolver | seq_gestion_usuarios.puml sin cambios |
| DF-19 | B | Textos de figuras sin acentos ni eñes («Autenticacion», «Vision», «analisis», «especimen») | Sin resolver | Los cu_*.puml siguen sin acentos |
| DF-20 | B | seq_login no muestra el cambio obligatorio de contraseña al primer ingreso que seq_crea… | Sin resolver | seq_login sin cambios |
| DF-21 | B | seq_gestion_usuarios cubre crear y desactivar, pero RF-05 y CU-11 incluyen modificar datos | Sin resolver | seq_gestion_usuarios sin cambios |
| DF-22 | B | CU-07 (paso 5) y CU-09 (paso 3) listan solo tres conductas | Resuelto | CU-07 y CU-09 listan las cuatro conductas |
| DF-23 | B | «Cuatro módulos» en el texto y la figura del pipeline contra «tres etapas» en estados, … | Sin resolver | Sigue «cuatro módulos» (cap. 5:118) |
| DF-24 | B | seq_analisis_automatico: «programa la eliminación» sin columna que la respalde, «5 inte… | Sin resolver | seq_analisis_automatico: siguen «5 intervalos» y «programa la eliminación» |
| DF-25 | B | Introducciones de paquete y descripciones de figura del cap. 5 que no coinciden con lo … | Resuelto | Intro del Paquete 2 y Paquete 3 reescritas; la frase de «estado de la cola» ya no está |

## 08 · Reglas en .md

| ID | Sev. | Hallazgo | Estado | Evidencia en `accesos-login` |
|---|---|---|---|---|
| MD-01 | A | INSTRUCCIONES-WEB R-03 sigue diciendo que el Día 1 del grupo control se analiza | Resuelto | INSTRUCCIONES-WEB R-03: solo el Día 2 se analiza |
| MD-02 | A | DISENO-BD.md deja P-08/D-03 «sin resolver» cuando D-03 está resuelto, aplicado y reforz… | Resuelto | DISENO-BD: P-08/D-03 cerrada, Video–Análisis (1,1) |
| MD-03 | A | Cap. 5 describe procesamiento parcial si faltan cilindros; D-20 lo descarta (todo o nada) | Resuelto | Cap. 5 L338: no se entregan resultados parciales |
| MD-04 | A | Cap. 5 dice que el entrenamiento se alimenta de «anotación experta»; contradice la proh… | Resuelto | Se fue la «anotación experta» |
| MD-05 | M | INSTRUCCIONES-WEB A.11 (tareas programadas) contradice §8 y D-51 sobre VIDEO.archivo y … | Sin resolver | Archivo sin cambios o sin tocar ese punto |
| MD-06 | M | INSTRUCCIONES-WEB A.9 trae una seq_analisis_automatico anterior a D-35/D-54, aunque se … | Sin resolver | Archivo sin cambios o sin tocar ese punto |
| MD-07 | M | INSTRUCCIONES-WEB sigue pidiendo el «disparador de ESPECIMEN.idGrupo» que D-55 eliminó | Sin resolver | Archivo sin cambios o sin tocar ese punto |
| MD-08 | M | INSTRUCCIONES-WEB omite «Conducta activa» en las columnas de los reportes y en el resum… | Sin resolver | Archivo sin cambios o sin tocar ese punto |
| MD-09 | M | INSTRUCCIONES-WEB: la secuencia de progreso todavía muestra un «código» de error | Sin resolver | Archivo sin cambios o sin tocar ese punto |
| MD-10 | M | INSTRUCCIONES-WEB define dos rutas distintas para la misma comparación entre grupos | Sin resolver | Archivo sin cambios o sin tocar ese punto |
| MD-11 | M | Apéndice D declara NOT NULL columnas de ANALISIS que el backend deja vacías al encolar … | Sin resolver | Archivo sin cambios o sin tocar ese punto |
| MD-12 | M | Filas D-04, D-06 y D-14 sin marca de «sin objeto»; D-06 aparece con dos estados y las l… | Sin resolver | Archivo sin cambios o sin tocar ese punto |
| MD-13 | M | DISENO-BD.md sigue diciendo que el cap. 5 y diagramas/ «están mal y no se usan», y que … | Sin resolver | Archivo sin cambios o sin tocar ese punto |
| MD-14 | M | DISENO-BD.md §4 «El modelo, en corto» se contradice dentro de la misma sección | Sin resolver | Archivo sin cambios o sin tocar ese punto |
| MD-15 | M | DISENO-BD.md da dos juegos distintos de URLs para los mismos tres artifacts | Sin resolver | Archivo sin cambios o sin tocar ese punto |
| MD-16 | M | PENDIENTES-ERICK.md / PENDIENTES-VANESA.md / PENDIENTES.md listan como pendientes ítems… | Sin resolver | PENDIENTES.md y PENDIENTES-ERICK.md sin cambios; los ítems resueltos siguen listados |
| MD-17 | M | PREGUNTAS.md conserva una pregunta ya respondida y con «primeros 300 s» | Resuelto | PREGUNTAS.md quedó sin preguntas abiertas |
| MD-18 | M | README.md describe un proyecto anterior (IA, TensorFlow, anotaciones expertas, cap. 5 «… | Sin resolver | Archivo sin cambios o sin tocar ese punto |
| MD-19 | M | MIGRACION-DIAGRAMAS.md presenta como vigentes cifras y decisiones ya revertidas (sin av… | Sin resolver | Archivo sin cambios o sin tocar ese punto |
| MD-20 | M | COMPARATIVA-FIGURAS-CAP5.md afirma que ninguna figura está insertada en el cap. 5 | Sin resolver | Archivo sin cambios o sin tocar ese punto |
| MD-21 | M | errores/pendientes.md sin banner: T-02 «mínimo 3» y cap. 5 «sin revisar» presentados co… | Sin resolver | Archivo sin cambios o sin tocar ese punto |
| MD-22 | M | Cap. 4 «Factibilidad operativa» describe tres grupos y 6–9 videos por experimento; ning… | Resuelto | Factibilidad operativa corregida (3 a 4 experimentos, tres o más grupos) |
| MD-23 | M | D-44 figura «aplicado en CU-09», pero el cap. 5 conserva dos menciones de «comparación … | Resuelto | Día 1 vs. Día 2 quitado de L808 y L1758 |
| MD-24 | M | Pregunta abierta: cómo queda el video del Día 1 en el modelo si D-54 dice que no se ana… | Sin resolver | Pregunta abierta: el Día 1 en el modelo sigue sin decidir |
| MD-25 | M | Pregunta abierta: quién borra los videos a los 30 días (worker o tarea del backend) | Sin resolver | Pregunta abierta: quién borra a los 30 días |
| MD-26 | M | Pregunta abierta: pipeline_analisis.md (11-oct) presenta la CNN de fusión como clasific… | Sin resolver | Pregunta abierta: la CNN de fusión como línea principal |
| MD-27 | B | D-52: cifras que no cuadran ni con su propia aritmética ni con las vigentes | Sin resolver | Archivo sin cambios o sin tocar ese punto |
| MD-28 | B | Filas de §6 con notas de aplicación caducadas (D-03, D-26, D-31, D-54) | Sin resolver | Archivo sin cambios o sin tocar ese punto |
| MD-29 | B | preguntas-doctor.md §1–5: premisas superadas sin nota y fecha de cabecera vieja | Sin resolver | Archivo sin cambios o sin tocar ese punto |
| MD-30 | B | CLAUDE.md: punteros a documentos que se declaran desactualizados y menciones de CLAHE/B… | Sin resolver | CLAUDE.md sin cambios (incluye «F1 por clase») |
| MD-31 | B | Números de línea y citas desfasadas en PENDIENTES*.md | Sin resolver | Archivo sin cambios o sin tocar ese punto |
| MD-32 | B | INSTRUCCIONES-WEB: detalles menores desfasados | Sin resolver | Archivo sin cambios o sin tocar ese punto |
| MD-33 | B | Ortografía inconsistente: «autoregistro» / «autorregistro» | Sin resolver | «autoregistro» sigue en cap. 4:91 |
| MD-34 | B | Copias y documentos de apoyo fuera de la lista, con contenido ya superado | Sin resolver | Archivo sin cambios o sin tocar ese punto |
| MD-35 | B | Pregunta abierta: el .docx de la simulación nombra a otra directora distinta de la que … | Sin resolver | Pregunta abierta: nombre de la directora en el .docx |

## 09 · Terminología

| ID | Sev. | Hallazgo | Estado | Evidencia en `accesos-login` |
|---|---|---|---|---|
| TT-01 | A | «rata» y «animal» en texto del cuerpo y en una figura del cap. 5 | Parcial | documento_tecnico y glosario limpios; siguen cap. 5:415 («número de rata») y el título con «RATA» |
| TT-02 | A | El cap. 5 sigue diciendo que la «anotación experta» alimenta el entrenamiento | Resuelto | Se fue la «anotación experta» |
| TT-03 | M | Título del TT con «IA» y «RATA» (portada y documento técnico) | Resuelto | Decidido en PENDIENTES-VANESA (11-oct): el título registrado no se cambia; «IA» y «RATA» se quedan |
| TT-04 | M | Figuras con texto interno visible: códigos D-xx, fechas, «ya resuelto en el .tex» y SQL | Parcial | Fuentes .puml limpias; los PNG viejos aún muestran D-xx, SQL y fechas |
| TT-05 | M | «TT1/TT2» y «TT-I/TT-II» mezclados, y ninguno definido | Parcial | Cap. 1 define TT-I/TT-II; el cap. 4 sigue con «TT2» |
| TT-06 | M | «F1 por clase» vs «F1 por conducta» | Resuelto | Cap. 1, 2 y resumen dicen «F1 por conducta» (D-65); CLAUDE.md sigue con «por clase» |
| TT-07 | M | «OE-5» citado sin que existan «OE» ni objetivos rotulados | Resuelto | El cap. 1 rotula OE-1 a OE-6 |
| TT-08 | B | Anglicismos que nunca van en cursiva ni con traducción | Parcial | Corregido en el cap. 1; ~43 «pipeline» sin cursiva en otros capítulos |
| TT-09 | B | Anglicismos con cursiva inconsistente o sin traducción en la primera aparición | Parcial | Mejorado en los caps. 1 a 3; no se revisó el resto |
| TT-10 | B | Siglas sin definir en su primera aparición (en el orden real del documento) | Parcial | Siglas corregidas en el cap. 1; no se revisó el resto |
| TT-11 | B | abreviaturas.tex desfasado respecto del documento | Parcial | abreviaturas.tex ganó CU, DL, OE, OG, TT-I, TT-II, ACID, GMM y VP |
| TT-12 | B | «clases» donde el clasificador asigna conductas | Sin resolver | «clases» siguen en cap. 4 (L795-874) |
| TT-13 | B | «intentos de escape» como nombre de la conducta de escalamiento | Resuelto | Ya no aparece «intentos de escape» |
| TT-14 | B | «rata» extra en el glosario (más de la mención permitida) | Resuelto | Glosario: queda solo la «rata» de la definición de espécimen |
| TT-15 | B | Apéndice C: transcripción con «animal», «rata», «ISRS», «celular» y el nombre viejo del… | Sin resolver | Apéndice C (transcripción) conserva «celular» (pregunta abierta) |
| TT-16 | B | Comentarios y archivo huérfano de diagramas con términos prohibidos (sin efecto en la f… | Sin resolver | BORIS sigue en comentarios de .puml |
