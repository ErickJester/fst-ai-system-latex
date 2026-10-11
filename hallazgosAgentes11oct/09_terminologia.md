# Auditoría transversal de terminología y prohibiciones (agente TT)

Fecha: 2026-10-11 · Repo en `da96c00` · Solo lectura (único archivo escrito: este).

## Alcance auditado

- `chapters/01_introduccion.tex`, `02_estado_arte.tex`, `03_marco_teorico.tex`, `04_analisis.tex`, `05_diseno.tex` (grep exhaustivo + lectura de contexto de cada hallazgo).
- `front/portada.tex`, `documento_tecnico.tex`, `advertencia.tex`, `resumen.tex`, `glosario.tex`, `abreviaturas.tex` (`abstract.tex` y `agradecimientos.tex` están vacíos).
- `back/apendice_C.tex` y `back/apendice_D.tex`.
- Diagramas: `diagramas/*.puml`, `diagramas/puml/*.puml`, `diagramas/diagram_design/*.md|html` y `generadores/*.py` (grep sobre texto visible y comentarios). Además se abrieron las imágenes `figures/mermaid/esquema_fisico.png` y `figures/mermaid/flujo_general.png` para confirmar qué texto se ve en la figura.
- Contexto: `CLAUDE.md`, `PENDIENTES.md`, `PENDIENTES-ERICK.md` (L-2, L-6b), `PENDIENTES-VANESA.md` (L-6), `errores/preguntas-doctor.md` (D-26, D-32, D-47, D-51, D-53, D-54, D-55, D-56).
- Método: grep con y sin tildes (los `.tex` usan UTF-8 directo, no hay tildes TeX `\'o`), y dos scripts propios (en el scratchpad) para contar apariciones en cursiva/no cursiva y primera aparición de siglas en el orden real de `main.tex` (portada → documento técnico → advertencia → resumen → glosario → abreviaturas → caps. 1–5 → apéndices C y D).

## Resumen de conteos

| Severidad | Hallazgos | De ellas «pregunta abierta» |
|-----------|-----------|-----------------------------|
| Alta | 2 | 0 |
| Media | 5 | 2 (TT-03, TT-06) |
| Baja | 9 | 1 (TT-15) |
| **Total** | **16** | **3** |

### Categorías revisadas sin ninguna violación en los `.tex` incluidos (verificado con grep)

| Categoría | Resultado |
|-----------|-----------|
| κ / kappa / Cohen, MAE / error absoluto medio, «gold standard» / «estándar de oro» | 0 en `.tex` (también 0 en `bib/referencias.bib`) |
| «inteligencia artificial» | 0 (solo la sigla «IA» en el título, ver TT-03) |
| «Laboratorio de Neurociencia Conductual» como nombre del laboratorio | 0 en el cuerpo; solo se cita como nombre incorrecto en `apendice_C.tex:285-286` (ver TT-15). El nombre correcto aparece completo en 01:5, 01:53, 04:12, 04:915, resumen:13 |
| «cámara de celular» / teléfono / iPhone como cámara | 0. Cap. 2–4 dicen «cámara web» (02:21, 03:76, 04:940); «celular» solo está como opción en una pregunta del apéndice C (`apendice_C.tex:45`) |
| «ISRS» / SSRI en el cuerpo | 0. Solo `glosario.tex:180-182` (permitido) y `apendice_C.tex:290,295` (ver TT-15) |
| BORIS | 0 en `.tex`. Solo aparece en comentarios de `diagramas/flujo_general.puml` (ver TT-16) |
| «último segundo» / conducta del último segundo | 0 en `.tex`, `.puml`, `diagram_design/*.md|html|py`. Los «últimos 300 s» son la regla vigente (D-31/D-54) |
| Umbral de confianza 0.70 | 0 en `.tex`. Solo en un comentario de `seq_analisis_automatico.puml:24-26` (ver TT-16). El 0.80 de `05_diseno.tex:431` es el umbral de la regla de tres pasos (D-51), vigente |
| YOLO / ByteTrack / tracker | Solo como trabajo revisado en cap. 2 (02:77-187, 02:304) y en glosario/abreviaturas; `02_estado_arte.tex:187` dice «Este proyecto no usa YOLO». 05:191 descarta el seguimiento. Sin violación |
| ResNet-50 / Random Forest como elegidos | 0. Random Forest solo en `02_estado_arte.tex:212` como ejemplo de método clásico; ResNet-18 solo como base de R(2+1)D-18 (candidato) |
| «DER» para modelo con tipos/FK | Sin violación: `05_diseno.tex:350,366,370` usa «DER» para el conceptual y el esquema físico se llama «Esquema físico» (05:382, apéndice D:11) |

---

## Hallazgos — Alta

### TT-01 — «rata» y «animal» en texto del cuerpo y en una figura del cap. 5
- Severidad: Alta
- Ubicación: `front/documento_tecnico.tex:79`; `chapters/05_diseno.tex:416`; `diagramas/esquema_fisico.puml:194-196` (nota visible de la figura `fig:er`, cap. 5; confirmado en `figures/mermaid/esquema_fisico.png`).
- Cita: «análisis del comportamiento animal en pruebas de nado forzado» (documento_tecnico:79) · «El sistema no guarda el número de rata del laboratorio.» (05_diseno:416) · «No se guarda el numero de rata del laboratorio: ya no hay comparacion Dia 1 contra Dia 2 por rata (D-44)» (esquema_fisico.puml:194-196, visible en el PNG).
- Fuente que decide: `CLAUDE.md` (terminología obligatoria: «animales» o «rata» en el cuerpo → «espécimen»; única mención permitida de «rata» = entrada de glosario de espécimen).
- Corrección sugerida: documento_tecnico:79 → «análisis de la conducta de los especímenes en pruebas de nado forzado»; 05_diseno:416 → «El sistema no guarda el número de identificación del espécimen en el laboratorio.»; nota de `esquema_fisico.puml` → «No se guarda el número de identificación del espécimen en el laboratorio: no hay comparación Día 1 contra Día 2 por espécimen, y el reporte solo necesita tanda y posición.» y regenerar el PNG.
- Nota: `chapters/01_introduccion.tex:39` dice «bienestar animal» (nombre de la norma NOM-062); lo dejo fuera por ser expresión normativa, no el sujeto del experimento. Confirmar en TT-15 si se acepta.

### TT-02 — El cap. 5 sigue diciendo que la «anotación experta» alimenta el entrenamiento
- Severidad: Alta
- Ubicación: `chapters/05_diseno.tex:100-102` (frente a `05_diseno.tex:250-252`, a la propia Figura `fig:flujo_sistema` = `diagramas/flujo_general.puml:69-74` y a `diagramas/diagram_design/flujo_sistema.md:55-56`).
- Cita: «el ciclo de entrenamiento del modelo ---anotación experta, dataset y entrenamiento--- alimenta al clasificador de conducta» (05_diseno:100-102) vs «El clasificador se entrena con bloques de 5~s etiquetados por el equipo, sin usar las anotaciones del laboratorio» (05_diseno:250-251) y «SIN anotación del Dr. Sandino, ni para entrenar ni para probar» (figura, flujo_general.puml:69).
- Fuente que decide: `CLAUDE.md` (prohibición vigente de κ/MAE/gold standard: el clasificador se entrena sin las anotaciones del Dr. Sandino); D-26 y D-56 (`PENDIENTES.md`, «Lo que ya está decidido»). El propio `flujo_sistema.md:55-56` ya reconoce que esa frase «contradice la estrategia vigente», pero no está en `PENDIENTES.md`.
- Corrección sugerida: «...y cómo el ciclo de entrenamiento del modelo ---clips etiquetados por el equipo, entrenamiento y conjunto de prueba propio--- alimenta al clasificador de conducta.» (ajustar «clips» vs «bloques de 5 s» según lo que el equipo confirme; hoy figura y texto de 05:251 no coinciden en eso, lo anoto como aviso para el agente de entrenamiento/pipeline).

---

## Hallazgos — Media

### TT-03 — Título del TT con «IA» y «RATA» (portada y documento técnico)
- Severidad: Media
- Ubicación: `front/portada.tex:36-37`; `front/documento_tecnico.tex:45-46`.
- Cita: «PROTOTIPO DE UN SISTEMA WEB DE ANÁLISIS CONDUCTUAL ASISTIDO POR IA EN UN MODELO DE CONDUCTA DEPRESIVA EN RATA MEDIANTE NADO FORZADO» (ambos archivos, idéntico).
- Fuente que decide: pregunta abierta → equipo (y directores). `CLAUDE.md` prohíbe «inteligencia artificial» y «rata» en el documento, pero presumiblemente es el título con el que se registró el TT 2026-B066; no hay fuente que diga si el título oficial se puede cambiar.
- Corrección sugerida: si el título puede cambiarse: «...ANÁLISIS CONDUCTUAL CON VISIÓN POR COMPUTADORA EN UN MODELO DE CONDUCTA DEPRESIVA EN ESPÉCIMEN MEDIANTE NADO FORZADO» (o la variante que acuerden); si es el título registrado y no puede cambiar, dejar constancia en `PENDIENTES.md` como excepción vigente para que ningún agente lo «corrija».

### TT-04 — Figuras con texto interno visible: códigos D-xx, fechas, «ya resuelto en el .tex» y SQL
- Severidad: Media
- Ubicación (texto visible, no comentario): `diagramas/esquema_fisico.puml:146-148, 193-196, 214, 219, 222-233, 277, 280-286, 293-295, 339`; `diagramas/estados_analisis.puml:16`; `diagramas/seq_consulta_progreso.puml:79, 91`; `diagramas/seq_consulta_resultados.puml:93`; `diagramas/seq_crear_cuenta.puml:58, 89`; `diagramas/seq_descarga_reportes.puml:68`. Confirmado en el PNG solo para `esquema_fisico` (las demás, solo en la fuente `.puml`; el PNG puede estar desfasado).
- Cita: «D-10: activo evita el DELETE. Contraseña con bcrypt + sal (RNF-05, ya resuelto en el .tex).» (esquema_fisico.puml:146-147) · «D-25 (15-sep): cambioRequerido obliga a cambiar...» (148) · «Su PK es la misma FK, así que PostgreSQL la indexa sola al declarar el PRIMARY KEY.» (295) · «CK segundo BETWEEN 1 AND 300» (277) · «rutaDiagnostico solo se llena si estado='error'» (225) · «el reporte guardado es más viejo que el último análisis (D-21)» (seq_descarga_reportes:68).
- Fuente que decide: `CLAUDE.md` («Lenguaje natural obligatorio: sin SQL ni código dentro de los diagramas»). Los identificadores D-xx y las fechas son notas de trabajo del equipo, no contenido para un lector del documento.
- Corrección sugerida: quitar de los textos visibles todo «D-xx», «(15-sep)», «ya resuelto en el .tex», «DELETE», «PRIMARY KEY», «BETWEEN 1 AND 300» y «estado='error'»; dejar la razón en lenguaje natural (p. ej. «El usuario no se borra: se da de baja con la columna activo» y «El segundo va de 1 a 300»). Pasar los D-xx a comentarios `'` del `.puml`. El esquema físico puede conservar tipos y llaves (es un esquema físico), pero no sentencias.

### TT-05 — «TT1/TT2» y «TT-I/TT-II» mezclados, y ninguno definido
- Severidad: Media
- Ubicación: `TT1`/`TT2`: `01_introduccion.tex:350, 369, 370, 387, 401, 444, 458`; `04_analisis.tex:345, 442, 459`. `TT-I`/`TT-II`: `02_estado_arte.tex:255`; `04_analisis.tex:686, 962, 970 (dos veces)`; `05_diseno.tex:266, 487`. Sigla suelta «TT»: primera aparición en el cuerpo `04_analisis.tex:1128` (sin «Trabajo Terminal (TT)»; el nombre completo aparece sin sigla en 01:57 y 04:1133).
- Cita: «entregas en dos etapas académicas (TT1 y TT2)» (01:350) vs «la elección se hace en TT-II con F1» (04:686) vs portada «Trabajo Terminal~I».
- Fuente que decide: `CLAUDE.md` (siglas definidas en la primera aparición). No hay fuente que fije la forma; la portada usa «Trabajo Terminal I».
- Corrección sugerida: elegir una forma (propongo «TT-I» y «TT-II», como la portada) y definirla en 01:350: «dos etapas académicas, Trabajo Terminal I (TT-I) y Trabajo Terminal II (TT-II)»; reemplazar las 10 apariciones de «TT1/TT2». Agregar TT-I y TT-II a `abreviaturas.tex` (hoy solo «TT»).

### TT-06 — «F1 por clase» vs «F1 por conducta»
- Severidad: Media
- Ubicación: «por clase»: `front/resumen.tex:30`; `01_introduccion.tex:174, 200, 366, 478`; `02_estado_arte.tex:268`. «por conducta»: `02_estado_arte.tex:255, 302, 306`; `04_analisis.tex:339-340, 344, 445, 458, 686-687, 700`; `05_diseno.tex:266`.
- Cita: «F1 por clase» (OE-5, resumen:30, 01:174) vs «F1 $\geq 85$\,\% por conducta (nado, inmovilidad, escalamiento)» (RNF-02, 04_analisis:344).
- Fuente que decide: pregunta abierta → tú y el usuario. `CLAUDE.md` fija el texto como «F1 por clase» (OE-5) y «F1 ≥ 85 % por clase» (RNF-02); D-53 pide «conducta» para lo que se asigna por segundo; «F1 por clase» es terminología de métricas (permitida). Hoy RNF-02 literal no dice «por clase».
- Corrección sugerida: decidir una sola forma para las dos (OE-5 y RNF-02). Si se sigue `CLAUDE.md`: RNF-02 → «F1 ≥ 85 % por clase (nado activo, inmovilidad, escalamiento)» y añadir en el cap. 1 una frase «cada clase es una conducta»; si se prefiere «por conducta», cambiar las seis ocurrencias de «por clase» y actualizar `CLAUDE.md`.

### TT-07 — «OE-5» citado sin que existan «OE» ni objetivos rotulados
- Severidad: Media
- Ubicación: `chapters/05_diseno.tex:266`; `diagramas/flujo_general.puml:74` (texto visible de la figura); lista de objetivos en `01_introduccion.tex:185-205` (enumerate numerado 1–6, sin «OE-n»); `front/abreviaturas.tex` (sin OE ni OG).
- Cita: «(ver OE-5 y RNF-02)» (05:266) · «F1 por conducta (OE-5, RNF-02)» (figura).
- Fuente que decide: `CLAUDE.md` (OE-5 existe como nombre del objetivo de evaluación); el LaTeX nunca lo rotula.
- Corrección sugerida: en 01:184 escribir «\subsection{Objetivos específicos (OE)}» y numerar con etiqueta «OE-1…OE-6» (`\begin{enumerate}[label=OE-\arabic*]`, `enumitem` ya está cargado en `preamble.tex:59`); definir también «OG» si se usa; añadir OE/OG a `abreviaturas.tex`.

---

## Hallazgos — Baja

### TT-08 — Anglicismos que nunca van en cursiva ni con traducción
- Severidad: Baja (L-6/L-6b siguen abiertas en `PENDIENTES-VANESA.md` / `PENDIENTES-ERICK.md`; aquí va el inventario verificado)
- Ubicación y conteo (apariciones fuera de `\texttt`, `\cite` y comentarios; solo cuerpo salvo que se diga):
  - **pipeline** (59 apariciones, 0 en cursiva): `01:155,196,203,364,418,452,488,495`; `03:284`; `04:107,140,149,416,568,733,784,810,881,894`; `05:12,27,40,72,112,115,126,133,187,273,303,373,426,433,794,1598,1606,1608,1610(×2),1633,1646,1667,1671,1673,2484,2508,2554,2559,2741`; `apendice_D:168,176,249`; glosario: 198,223,225,263,268,287,301.
  - **frontend** (19, 0 cursiva): `01:364,412,489`; `03:267,270,285,292`; `04:416,737,747`; `05:39,61,68,1610,2385,2466,2487`; glosario 115,191.
  - **backend** (27, 1 cursiva — solo `04:815`): `01:363,412,418,488`; `03:268,270,282,292`; `04:416,747`; `05:26,39,62,66,78,96,2385,2398,2465,2483,2546`; glosario 43,115,191,213,302.
  - **dataset(s)** (16, 0 cursiva): `01:490`; `02:181,183,208,230,239`; `03:192`; `04:708,791,793,865,867,888,890,1046`; `05:101`.
  - **token** (14 de 16 sin cursiva): `04:57,58,59,355`; `05:680,682,920,922,924,937,2399,2401(×2)`.
  - **hash**: `04:365`, `05:389`. **framework**: `04:690,734,737`. **endpoint(s)**: `01:495`; `05:658,663,666,2752`. **stack**: `01:487`, `04:860`. **clip(s)**: `03:203,230,236`; `04:682,830`; `05:261`. **wireframes**: `01:395`. **mockups**: `05:2580` y siguientes. **benchmarks**: `02:181`. **baseline**: `01:460`. **machine learning y deep learning**: `02:206`. **Scrum**: `01:349,354`, `04:825`. **login/logout** (en 05:680, 682 son ruta en `\path`, correcto).
- Cita: «(backend, base de datos, frontend, despliegue); Vanesa es responsable del pipeline de análisis de video» (01:363-364, primera aparición en el cuerpo, sin cursiva ni traducción; en orden de documento la primera aparición es `glosario.tex:43`).
- Fuente que decide: `CLAUDE.md` (términos en inglés con peso conceptual: primera aparición `\textit{término}` + traducción; después solo `\textit{término}`; no aplica a GPU, API, REST, JSON, CSV, PDF).
- Corrección sugerida: primera aparición de cada término en el cuerpo (01 salvo `dataset` en 02, `transfer learning` en 02): `\textit{backend} (servidor de aplicación)`, `\textit{frontend} (interfaz del navegador)`, `\textit{pipeline} (cadena de procesamiento)`, `\textit{dataset} (conjunto de datos)`, `\textit{token} (testigo de sesión)`, `\textit{hash} (resumen criptográfico)`, `\textit{framework} (marco de trabajo)`; y solo `\textit{...}` en las demás. Decidir con el equipo si «Scrum» (nombre propio de la metodología) y nombres de herramientas (Flask, React, Docker) quedan fuera, como parece razonable.

### TT-09 — Anglicismos con cursiva inconsistente o sin traducción en la primera aparición
- Severidad: Baja
- Ubicación y conteo:
  - **worker**: 29 en cursiva (`05:1443…2375`, `apendice_D:174`) y 14 sin cursiva en el cuerpo: `03:283,292`; `04:747`; `05:26,29,40,48,71,79,95,97,302,2385,2485,2489,2508,2751` (más glosario 75,115,227,299). `05:2554` es el nombre de la clase UML en negrita; correcto.
  - **dashboard**: 22 en cursiva, 17 sin cursiva: `01:409`; `04:205,215,216,224,235,242,247,249,331,388`; `05:319,820,829,1982,2155,2160`. En ningún caso con traducción.
  - **recall**: cursiva en resumen:30, 01:174, 01:200, 01:478, 02:268, 04:700, 05:266, pero sin traducción en la primera aparición (`resumen.tex:30`, y el glosario lo llama «Recall» sin versión en español) y sin cursiva en `02_estado_arte.tex:304`, `03_marco_teorico.tex:316, 322, 327 (×2)`.
  - **transfer learning**: primera aparición en el cuerpo `02:226` (título de subsección, sin cursiva ni traducción); con cursiva pero sin traducción en `02:230, 03:192, 03:196`; sin cursiva en el título `03:191` y en `04:684, 868, 888`. No hay traducción en ningún sitio.
  - **sprint**: cursiva solo en `04:825`; sin cursiva en `01:494, 496` y `03:340`.
  - **stack**: cursiva en `04:624, 972, 1123`; sin cursiva en `01:487` y `04:860`. **cron**: cursiva en 04:388; sin cursiva en `05:2356`.
  - **gradient boosting** y **bounding boxes**: bien (cursiva + traducción en 02:223 y 02:174); `HistGradientBoostingClassifier` y `time behaviour/usability/functional correctness` (01:233-236) también están bien.
  - **Forced Swim Test** sin cursiva en `resumen.tex:22` y `01_introduccion.tex:20`.
- Fuente que decide: `CLAUDE.md` (misma regla de cursiva y traducción).
- Corrección sugerida: unificar a `\textit{worker}`, `\textit{dashboard}`, `\textit{transfer learning}` (aprendizaje por transferencia), `\textit{sprint}`, `\textit{stack}` y `\textit{cron}` en todas las apariciones; traducir solo la primera: `\textit{recall} (exhaustividad)` en `resumen.tex:30`; `\textit{dashboard} (panel de control)` en 01:409; `\textit{transfer learning} (aprendizaje por transferencia)` en 02:226; `\textit{Forced Swim Test} (prueba de nado forzado, FST)` en resumen:22.

### TT-10 — Siglas sin definir en su primera aparición (en el orden real del documento)
- Severidad: Baja
- Ubicación (sigla: primera aparición → dónde se define, si se define):
  - `OMS`: `01:17` → nunca en el cuerpo (solo `abreviaturas`). `FPS`: `03:90` → nunca. `ETA`: `04:265` → nunca. `BD`: `01:395, 403` → nunca (ni en abreviaturas). `DDL`: `apendice_D:28` → nunca.
  - `RN`: primera `04:110` → nunca definida en el cuerpo (el encabezado `04:490` dice «Reglas de negocio» sin «(RN)»). `RF` y `RNF`: primera `01:392` (cronograma) → se definen en `04:27` y `04:305`.
  - `CU`: primera `05:320` (73 apariciones) → nunca definida y no está en `abreviaturas`.
  - `ML` / `DL`: primera `01:446` → nunca; `02:206` escribe «machine learning y deep learning» sin sigla; `DL` no está en `abreviaturas`.
  - `CNN`: primera `02:228` → se define hasta `03:179`.
  - `JWT`: primera `01:406`, y en cap. 4 `04:57` → se define en `04:1110`.
  - `UML`: primera `01:395` → se define en `05:15-16` (OMG, `05:16`).
  - `DLC`: `02:64` (encabezado) → nunca se escribe «DeepLabCut (DLC)».
  - `ISO`, `IEC`, `IEEE`: primera `front/resumen.tex:32` sin expansión; se expanden hasta `01:145-146`.
  - `MXN` (`04:984` encabezado de tabla) y `LFDA`: la primera sí se define (04:1129); `MXN` no.
  - Definidas bien: ENMyH-IPN (resumen:13-15), NOM-062 (01:37-38), TST (02:136), GMM (02:160), ROI (05:181), ORB, RANSAC (03:102-104), ACID (03:299), FNBC/1FN/2FN/3FN (05:496-572), PK/FK/UK/CK (apéndice D:14-17), LFPDPPP (04:1108).
- Fuente que decide: `CLAUDE.md` (siglas: nombre completo + sigla entre paréntesis en la primera aparición).
- Corrección sugerida: p. ej. «Organización Mundial de la Salud (OMS)» en 01:17; «requerimientos funcionales (RF) y no funcionales (RNF)» en 01:392 (o evitar la sigla en el cronograma); «reglas de negocio (RN)» en 04:490 y mover antes de 04:110 la primera referencia; «casos de uso (CU)» en 05:320 o en 05:~690 (inicio de la sección); «redes neuronales convolucionales (CNN)» en 02:228; «aprendizaje automático (\textit{machine learning}, ML) y aprendizaje profundo (\textit{deep learning}, DL)» en 02:206 y añadir DL, CU, BD, ETA, MXN a `abreviaturas.tex`; «International Organization for Standardization (ISO)…» en resumen:32 o quitar las siglas del resumen.

### TT-11 — `abreviaturas.tex` desfasado respecto del documento
- Severidad: Baja (es el ítem L-2 de `PENDIENTES-ERICK.md`, sigue vigente)
- Ubicación: `front/abreviaturas.tex:22-23 (FN, FP), 29 (HTTPS), 36 (MB), 53 (SQL)`; faltan `CU`, `MXN`, `FNBC`, `GMM`, `DL`, `BD`, `ETA`, `OE`, `TT-I/TT-II` (ver TT-05, TT-07, TT-10); `ORM` dice «Object-Relational Mapping» (abreviaturas:44 y glosario:211) pero el cuerpo escribe «Object-Relational Mapper» (`03_marco_teorico.tex:304`).
- Cita: «ORM & Object-Relational Mapping» (abreviaturas:44) vs «ORM (\textit{Object-Relational Mapper})» (03:304).
- Fuente que decide: `CLAUDE.md` (siglas), `PENDIENTES-ERICK.md` L-2.
- Corrección sugerida: quitar las siglas que el cuerpo no usa (HTTPS, MB, SQL, FN y FP solo si el glosario los deja de usar; hoy `glosario.tex:237, 249` sí los usa, así que conviene dejar FN/FP y marcar solo HTTPS, MB y SQL como sobrantes) y añadir las faltantes; unificar «Mapper» o «Mapping» en los tres sitios.

### TT-12 — «clases» donde el clasificador asigna conductas
- Severidad: Baja
- Ubicación: `04_analisis.tex:823` (riesgo R-07), `04_analisis.tex:869`.
- Cita: «Diseño modular del clasificador para incorporar clases adicionales sin reescribir la arquitectura» (823) · «unos pocos cientos de ejemplos por clase» (869).
- Fuente que decide: D-53 (clase y conducta eran sinónimos; se dice «conducta»).
- Corrección sugerida: 823 → «incorporar conductas adicionales»; 869 → «unos pocos cientos de ejemplos por conducta». Las demás «clase(s)» son legítimas (UML: 05:20, 2541-2562; ImageNet «1 000 clases»: 02:232, 03:199; probabilidades de clase en CNN/YOLO: 02:174, 03:185, 03:254; «F1 por clase»: ver TT-06).

### TT-13 — «intentos de escape» como nombre de la conducta de escalamiento
- Severidad: Baja
- Ubicación: `front/resumen.tex:17-18`; `01_introduccion.tex:135, 180-181, 261` (en 261 sí glosa «(escalamiento)»).
- Cita: «tiempos de nado activo, inmovilidad e intentos de escape por espécimen y sesión» (resumen:17-18; 01:135).
- Fuente que decide: `PENDIENTES.md` («Cuatro conductas: nado activo, inmovilidad, escalamiento y conducta activa») y el resto del documento (03:54-56, 04:545, 05:226, glosario:79).
- Corrección sugerida: usar «escalamiento» (o «escalamiento, intentos de escape» solo en la primera mención del resumen) para que el nombre sea el mismo del cap. 3 al apéndice D.
- Nota para el agente de conductas: el resumen y el cap. 1 hablan de «tres conductas» y el cap. 4 de cuatro con «conducta activa»; no lo audité aquí.

### TT-14 — «rata» extra en el glosario (más de la mención permitida)
- Severidad: Baja
- Ubicación: `front/glosario.tex:86` (entrada «Conducta de nado activo»), `front/glosario.tex:153` (entrada «FST»). La permitida es `glosario.tex:133` (espécimen).
- Cita: «desplazan a la rata por el cilindro» (86) · «en el que una rata se coloca en un cilindro con agua» (153).
- Fuente que decide: `CLAUDE.md` (la entrada de espécimen es «única mención permitida de “rata”»).
- Corrección sugerida: 86 → «desplazan al espécimen por el cilindro»; 153 → «en el que un espécimen se coloca en un cilindro con agua de la que no puede escapar».

### TT-15 — Apéndice C: transcripción con «animal», «rata», «ISRS», «celular» y el nombre viejo del laboratorio
- Severidad: Baja
- Ubicación: preguntas del equipo: `apendice_C.tex:45` («celular»), `147` («por animal»), `168` («animal por animal»), `285-286` («Laboratorio de Neurociencia Conductual»), `290` («ISRS~+~fluoxetina»). Respuestas literales del Dr.: `151` («por animal»), `174` («ratas del grupo»), `188-189` («4 ratas», «por rata», «Con 4 ratas»), `295` («la sigla ISRS»).
- Fuente que decide: pregunta abierta → equipo. El apéndice se presenta como «transcripción de la entrevista» (apendice_C:8), así que las respuestas citan literal; las preguntas en cambio las escribió el equipo.
- Corrección sugerida: en las preguntas reformular («por espécimen»; «¿...con “ISRS + fluoxetina”?» → «con la sigla de la clase farmacológica»), y para las respuestas añadir una nota inicial: «Las respuestas se transcriben literalmente; el documento usa “espécimen” en lugar de “rata”/“animal”». Los pares PE/PF existen justamente porque el Dr. Sandino corrigió el nombre y «ISRS»; basta con mantenerlos como evidencia o moverlos a una nota de metodología.

### TT-16 — Comentarios y archivo huérfano de diagramas con términos prohibidos (sin efecto en la figura)
- Severidad: Baja
- Ubicación (solo comentarios `'` o archivos fuera del documento): `diagramas/arquitectura_software.puml:33` («ANIMALES»); `esquema_fisico.puml:21` («ANIMALES»); `grafo_relacional_3_vigente.puml:18` («cada rata»); `seq_analisis_automatico.puml:15-31` («Pipeline IA», «animales», «umbral de confianza 0.70», «confianza < 0.70»); `flujo_general.puml:17-34` («BORIS», «gold standard»); `pipeline.puml:7-12` («YOLOv8 + ByteTrack», «ResNet-18/50»); `diagramas/relacional.puml:125-195` (tablas `ANIMALES`, `SUJETOS`, `id_animal`, `ultimo_acceso`: modelo viejo huérfano, no se incluye en ningún `.tex`).
- Cita: «'    ...agrega el umbral de confianza 0.70 de RN-11 ... confianza < 0.70 detiene el pipeline» (seq_analisis_automatico.puml:24-26).
- Fuente que decide: D-32/D-47 (sin umbral 0.70), D-56 (sin BORIS), `CLAUDE.md` (terminología). Son comentarios que documentan por qué se quitó cada cosa, y el comentario de `seq_analisis_automatico.puml` es parte del pendiente D-51 ya registrado.
- Corrección sugerida: no hace falta tocarlos para el documento; si el equipo quiere que ningún `grep` encuentre términos prohibidos, reescribir esos comentarios sin los términos o borrar `relacional.puml`.

---

## Cobertura y límites

- **No revisé** caps. 6–8 ni apéndices A, B y `trabajo_futuro.tex` (comentados en `main.tex`), `protocolo_fst.tex`, `casos_uso.tex`, los mockups HTML (`figures/mockups`, `mockups/`) ni la bibliografía más allá de buscar κ/Cohen/BORIS/gold en `bib/referencias.bib` (0 coincidencias).
- **Figuras:** solo abrí `esquema_fisico.png` y `flujo_general.png`. Para el resto de `.puml` el hallazgo se apoya en la fuente `.puml`, no en el PNG, que podría estar desfasado; no pude compilar ni regenerar. No leí `ciclo_vida_experimento.puml` (huérfano) más allá del grep.
- **Cursiva:** mi script cuenta una aparición como «en cursiva» solo si está dentro de `\textit{}` o `\emph{}` en la misma línea; un `\textit{...}` partido en dos líneas se contaría como no cursiva. Los `\textit{` partidos en dos líneas (`01:170`, `02:230`, `03:102`, `03:300`, `03:312`, `05:222`) los revisé a mano; solo cambiaban `transfer learning`, ya corregido en TT-09.
- La lista de anglicismos no es exhaustiva: cubrí los que la tarea nombra y los que encontró un barrido de unos 100 términos comunes (hardware, software y web los excluí por estar asentados en español).
- «Bienestar animal» (`01_introduccion.tex:39`) y «neurociencia conductual» en la descripción de herramientas comerciales (`02_estado_arte.tex:97`) los dejé fuera por ser expresiones del dominio, no el sujeto ni el nombre del laboratorio.
- No audité el conteo de conductas («tres» vs «cuatro»), la regla de bloques de 5 s ni los D-xx en general: son de otros agentes.
