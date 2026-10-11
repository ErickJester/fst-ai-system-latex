# Pendientes de Vanesa — capítulos 1 a 3, preliminares y casos de uso

Parte de [`PENDIENTES.md`](PENDIENTES.md), que tiene el reparto y las reglas de
coordinación. **Verificado contra el LaTeX el 2026-10-05.** Los IDs (A-, M-, L-) son los
mismos de la lista original; la evidencia larga (citas de la entrevista) está en
`errores/0X/errores.md` y `CORRECCIONES.md`.

**[corr. CU-xx]** = ID de `CORRECCIONES.md`; no confundir con las fichas CU-xx del cap. 5.

Marca aquí lo que termines (`✅`, fecha). Este archivo es solo tuyo: Erick no lo edita.

---

## Antes de empezar

- **Lee la sección «Lo que ya está decidido» de [`PENDIENTES.md`](PENDIENTES.md)** antes de escribir cualquier cosa: es lo que el texto no puede contradecir (cifras, conductas, etapas, lo que ya se quitó).
- **Lee `CLAUDE.md`.** Reglas que aplican directo a esta lista: jerarquía de fuentes (el
  LaTeX no es fuente; la entrevista sí), terminología obligatoria («espécimen», «cámara
  web», «visión por computadora» y «aprendizaje supervisado», fluoxetina sin «ISRS»), y
  commits sin ninguna mención a IA.
- **Tus archivos** (nadie más los toca mientras trabajas):
  - `chapters/01_introduccion.tex`, `chapters/02_estado_arte.tex`, `chapters/03_marco_teorico.tex`
  - `front/resumen.tex`, `front/portada.tex`, `front/documento_tecnico.tex`
  - `bib/referencias.bib` y la configuración de `biblatex` en `preamble.tex`
  - `diagramas/puml/cu_*.puml`, `diagramas/puml/gen_pngs.sh` y `figures/mermaid/cu_*.png`
  - En `chapters/05_diseno.tex`, **solo** la sección «Diseño de casos de uso» (de
    `\section{Diseño de casos de uso}` a justo antes de `\section{Diagramas de secuencia}`,
    hoy líneas 693–2333)
- **No toques** dentro de tus capítulos los párrafos sobre **preprocesamiento** (CLAHE,
  modelo de fondo por mediana, línea de agua con EMA) ni sobre el **clasificador**
  (ResNet, R(2+1)D, *gradient boosting*). Los reescribe Erick (CLA-03 y CLA-04) con el
  código de `fst_auto`.
- **BORIS ya no existe en el documento** (D-56, 7-oct). Si en tus capítulos hablas de cómo
  se etiquetan los videos, la herramienta es el **etiquetador del equipo** (propone la
  conducta y los autores la revisan y corrigen). No vuelvas a nombrar BORIS.
- **Erick quitó los códigos `D-xx` del cap. 5** (7-oct, commit `6a2b98a`). Ya no se citan
  decisiones internas en el documento: donde había una regla que lo respalda quedó
  RF-09 (tanda sugerida) o RN-11 (reporte de diagnóstico), y en el resto se borró la
  referencia. Tocó tres fichas de tu zona de casos de uso: la de administración
  (`Referencias` ahora dice solo «RF-04» y se quitó «ver D-12» de la descripción), la de carga
  de video (resumen, ahora con «RF-09») y la postcondición del análisis en cola (sin «ver D-15»).
  **Haz `git pull` antes de seguir editando esa zona** y no vuelvas a escribir códigos `D-xx`
  en el texto.
- **Regla de los bloques de 5 s: vale la mayoría** (corrige el aviso del 8-oct, commit
  `e51eaa8`). El 8-oct se cambió a «conducta del último segundo» (RN-15), pero eso no es la
  técnica de Detke et al. (1995): según Craft et al. (2010), al terminar cada periodo de 5 s
  se anota la conducta **predominante del periodo**. Se revirtió: la conducta de cada bloque
  es la que ocupa **más de sus cinco segundos**, con los desempates de D-53. La regla
  completa está en **RN-15** del cap. 4, que sigue siendo el único lugar donde se define.
  Se tocaron RF-18 y la justificación de umbrales (cap. 4) y, en el cap. 5, «Módulo 4», la
  clasificación segundo a segundo y la pantalla de resultados; ninguno está en tu zona.
  Al final de `bib/referencias.bib` (tu archivo) hay ahora dos citas agregadas:
  `detke1995` y `craft2010`. En tus capítulos y casos de uso no hay nada que cambiar,
  salvo que algún texto tuyo hable de bloques por «último segundo»: debe decir «conducta
  con más segundos» y remitir a RN-15. **Haz `git pull`** antes de seguir.
- **Glosario y abreviaturas son de Erick.** Si necesitas una entrada nueva, anótala al
  final de este archivo y él la agrega.

---

## 1. Capítulo 1

| # | Prioridad | Dónde | Qué hacer | Fuente |
|---|-----------|-------|-----------|--------|
| ✅ A-2 (5-oct) | 🔴 | Líneas 11, 114, 212, 216 | «dos evaluadores» → **tres analistas**; donde dice que el tiempo «se duplica», es que **se triplica**. (No cambies la 455 del cap. 4: habla de la literatura) | Entrevista P12 · `errores/01_introduccion/errores.md` E01-06 |
| ✅ A-3 (5-oct) | 🔴 | Líneas 158, 271 | Quitar «como funcionalidad opcional» del desglose por minuto: el laboratorio lo pidió como necesidad (RF-20 lo exige) | Entrevista P9 · E01-07 |
| ✅ A-4 (5-oct) | 🔴 | Líneas 59-66 y la tabla `tab:grupos_experimentales` | «tres grupos de entre 6 y 8» → hay **tres tipos** de grupo (control, referencia, tratamiento) y un experimento tiene **tres o más grupos** (en promedio 4), porque un tipo puede repetirse (varias moléculas o dosis). Presentar la tabla como catálogo de tipos. Los 6–8 especímenes son lo **típico**, no una regla: el sistema acepta grupos desde 2 (D-28) | Entrevista PA, P19 · E01-05 |
| ✅ A-5 (5-oct) | 🔴 | Propuesta y objetivos (157-198) | Agregar la **cuarta conducta**, *conducta activa* (cuando el clasificador no distingue nado de escalamiento). Hoy solo aparece en la línea 281 | RN-13 del cap. 4 |
| ✅ M-1a (5-oct) | 🟡 | Justificación (~206-241) | Agregar el criterio de **repetibilidad**: el mismo video analizado varias veces debe dar el mismo resultado, con variabilidad máxima de 5–10 %. Es el criterio principal del laboratorio, por encima de la velocidad. (El RNF del cap. 4 lo escribe Erick) | Entrevista P13, P8 · E01-08 |
| ✅ M-2 (5-oct) | 🟡 | «Fuera del alcance» (~304) | Agregar que el acervo histórico (80–100 videos de 10–12 años, ya analizados a mano) no se carga al sistema | Entrevista P19, PG · E01-11 |
| ✅ M-3 (5-oct) | 🟡 | Todo el capítulo | Nombrar el nivel **tanda** (sesión de grabación de 2 a 4 especímenes de un grupo) para que «experimento» signifique siempre el estudio completo | Entrevista P19 · E01-04 |

## 2. Capítulo 2

| # | Prioridad | Dónde | Qué hacer | Fuente |
|---|-----------|-------|-----------|--------|
| ✅ A-16 (5-oct) | 🔴 | Líneas ~64 y ~189 | La sección de DeepLabCut como clasificador del FST (Sturman et al.) está **duplicada**. Dejar una sola, en «Trabajos similares» | E02-01 |
| ✅ M-1b (5-oct) | 🟡 | Criterios de evaluación de los trabajos | Agregar la **repetibilidad** como criterio de comparación | Entrevista P13 · E02-02 |
| ✅ V-1 (6-oct) | ❓ | Descripción de YOLO-Behaviour | Verificar contra el artículo si de verdad separa detección y clasificación en dos etapas, como dice el texto | Agentes §2 |
| ✅ V-2 (6-oct) | ❓ | Cifras de YOLOv8 y «cientos de miles de imágenes» | No tienen cita directa: citar o quitar | Agentes §2 |

> La tabla comparativa del cap. 2 (columna «DL») **no es tuya**: cambia cuando se elija el
> clasificador (CLA-03, Erick).

## 3. Capítulo 3

| # | Prioridad | Dónde | Qué hacer | Fuente |
|---|-----------|-------|-----------|--------|
| ✅ A-6 (5-oct) | 🔴 | Línea 62 | El criterio de escalamiento dice «desde la **vista cenital**»; el sistema usa **vista lateral**. Reescribir: en vista lateral, el escalamiento produce movimiento en la mitad superior del cilindro y el nado se distribuye en toda la superficie del agua (así lo dice ya el cap. 2) | E03-01 |
| ✅ A-7 (5-oct) | 🔴 | Líneas 285-287 | Quitar la lista de tablas («usuarios, experimentos, sesiones de video y resultados por rata y conducta»): es el modelo viejo y el marco teórico no debe adelantar el esquema. Dejar solo la idea de base de datos relacional con ORM | E03-03 |
| ✅ M-5 (5-oct) | 🟡 | Líneas 55-56 | «los antidepresivos tipo antidepresivos como la fluoxetina (antidepresivo de referencia)» → «la fluoxetina (antidepresivo de referencia)» | E03-04 |
| ✅ M-6 (5-oct) | 🟡 | Protocolo del FST | Agregar la estructura: típicamente 6–8 especímenes por grupo (no es regla, D-28), tres o más grupos por experimento (en promedio 4), grabados en tandas de 2 a 4 especímenes, y 3–4 experimentos por semestre | Entrevista PA · E03-05 |
| ✅ M-7 (5-oct) | 🟡 | Protocolo del FST | Agregar el valor de referencia de iluminación | E03-08 (tiene la cifra y su fuente) |
| ✅ M-8 (6-oct) | 🟡 | Línea 276 | La portabilidad se atribuye a la ISO/IEC/IEEE 12207; es un atributo de calidad de la **ISO/IEC 25010** | Norma |

## 4. Preliminares y bibliografía

| # | Prioridad | Dónde | Qué hacer |
|---|-----------|-------|-----------|
| ⏳ A-14 (reabierto 11-oct: los nombres sí se unificaron; la fecha sigue en «Mayo 2026» y falta la fecha de entrega) | 🔴 | `portada.tex:73`, `documento_tecnico.tex:32` | Fecha «Mayo 2026» → la de entrega. Unificar los nombres entre los dos archivos (acentos y orden de apellidos: «Ángel Alí» contra «Angel Ali») |
| ✅ A-2b (5-oct) | 🔴 | `resumen.tex:7` | Mismo cambio que A-2: tres analistas, se triplica |
| ✅ M-4 (5-oct) | 🟡 | `resumen.tex:4` | «entre una y dos horas» → «entre una hora y media y dos horas» (como el cap. 1); expandir ISO e IEEE en su primera aparición |
| ✅ L-4 (5-oct) | 🟢 | `referencias.bib:293` | Quitar el comentario sobrante «INSTRUCCIONES: Pegar estas entradas…» |
| ✅ L-5 (5-oct; 11-oct: `zhang2022_bytetrack` se queda porque lo cita `chapters/06_desarrollo.tex`, que está fuera de `main.tex`) | 🟢 | `referencias.bib` | Quitar las entradas que nadie cita: `abadi2016`, `henriques2015`, `lauer2022_madlc`, `lukezic2017`, `zhang2022_bytetrack`, `bewley2016_sort`, `wojke2017_deepsort`. Antes busca cada clave en `chapters/`, `front/` y `back/` por si alguien la volvió a citar |
| ✅ L-7 (6-oct) | 🟢 | `preamble.tex` (`biblatex`) | Que la bibliografía diga siempre lo mismo («et al.» o «y col.») en cualquier compilación |

## 5. Siglas, términos en inglés y normas (caps. 1–3 y preliminares)

| # | Prioridad | Qué hacer |
|---|-----------|-----------|
| ✅ L-6 (5-oct) | 🟢 | Definir cada sigla en su primera aparición: nombre completo + sigla entre paréntesis (OMS, ENMyH-IPN, TT1/TT2, ROI, ML…). Términos en inglés con peso conceptual: primera vez `\textit{término}` (traducción), después solo `\textit{término}` (*time behaviour*, *recall*, *trade-off*). No aplica a GPU, API, REST, JSON, CSV o PDF |
| ✅ M-17a (5-oct) | 🟡 | Definir cada norma la primera vez que aparece, si esa primera vez cae en tus capítulos (por ejemplo ISO/IEC 25010 y NOM-062 en el cap. 1). Las que aparecen por primera vez en los caps. 4–5 las hace Erick |

## 6. Casos de uso: diagramas y fichas del cap. 5

Diagramas en `diagramas/puml/cu_*.puml`; el LaTeX incluye los PNG de
`figures/mermaid/cu_*.png`. Genera con PlantUML 1.2026.8 (la versión con la que se
verificó todo) y revisa la imagen antes de comitear.

**Regla de oro:** cada `<<include>>` o `<<extend>>` del diagrama aparece también en la fila
«Referencias» de la ficha (en el cap. 5). Si cambias uno, cambia el otro en el mismo
commit.

| # | Prioridad | Dónde | Qué hacer |
|---|-----------|-------|-----------|
| ✅ A-10 (5-oct) | 🔴 | `cu_paquete2.puml`, `cu_paquete5.puml` | Quitar «:Sistema:» como actor: un actor es externo al sistema. Usar un solo catálogo de actores: Investigador, Administrador y Worker [corr. CU-01, CU-03] |
| ✅ A-11 (5-oct) | 🔴 | `cu_vision_general.puml:26-27` | El Administrador solo llega a P1 y P5, así que no puede subir videos ni ver resultados. Pero es un Investigador con permisos extra (D-08): dibujar la herencia `Investigador <|-- Administrador` también aquí [corr. CU-17] |
| ✅ A-12 (5-oct) | 🔴 | Fichas CU-05 (~1266) y CU-08 (~1618) | CU-05 «Incluye: CU-07» → debe ser *extend*: monitorear es opcional, porque el análisis sigue aunque se cierre la pestaña (RF-15). CU-08 «Extendido por: CU-07» está al revés: CU-08 **extiende** a CU-07, porque solo ocurre si hubo error [corr. CU-18, CU-19] |
| ✅ A-9a (5-oct) | 🔴 | Fichas (~983, 989, 1274, 1396) | Quitar las citas internas «D-XX»: el lector de la tesis no tiene `preguntas-doctor.md`. Si la decisión importa, explicarla en una frase |
| ✅ M-18 (5-oct) | 🟡 | P1 | `UC17 ..> UC15a <<include>>` es una postcondición, no un include [corr. CU-05]. `UC15 ..> UC15b <<include>>` → desactivar es opcional: *extend* o caso independiente [corr. CU-06] |
| ✅ M-19 (5-oct) | 🟡 | P1, P2, P3, P5 | Sacar la descomposición funcional del diagrama de casos de uso: UC31–UC34 (etapas del pipeline, van en el diagrama de actividad), UC23/UC24 (validaciones internas), UC14 «Verificar rol y permisos» y UC55 «Conservar resultados» (es la regla RN-06). **UC14 tiene ficha (CU-15)**: decide si la ficha se va o se fusiona [corr. CU-02] |
| ✅ M-20 (5-oct) | 🟡 | P2 | La cadena `UC22 → UC23 → UC24 → UC25` dice que «Validar formato» incluye «Encolar análisis»: los tres deben colgar de UC22 [corr. CU-10]. `UC26 ..> UC24` está duplicado y «formato inválido» corresponde a UC23 [corr. CU-11] |
| ✅ M-21 (5-oct) | 🟡 | P4 | Solo existe «Descargar reporte PDF»; RF-22 pide también CSV y XLSX [corr. CU-12] |
| ✅ M-22 (5-oct) | 🟡 | P5 | La alerta de disco extiende a «Monitorear estado», así que solo existiría si el administrador está mirando el panel [corr. CU-15] |
| ✅ M-23 (5-oct) | 🟡 | P2, P3, P5 | UC27, UC35 y UC51 son el mismo objetivo («ver en qué va mi experimento»). Fusionar los diagramas **y** sus fichas (hoy CU-21, CU-07 y CU-22) [corr. CU-21] |
| ✅ M-30 (5-oct) | 🟡 | `gen_pngs.sh` | Rutas absolutas a `/home/vane/` y `/tmp/plantuml.jar` (INF-03): usar rutas relativas al repositorio |
| ✅ V-3 (6-oct) | ❓ | Fichas | Verificar que las fichas no se contradigan entre sí: CU-04/CU-05, CU-05/CU-07, CU-09/CU-10 |
| ✅ V-4 (6-oct) | ❓ | Diagramas y fichas | Nombres distintos entre diagrama y ficha (p. ej. UC14 «Verificar rol y permisos» contra CU-15 «Verificar pertenencia a Administrador»); CU-06 y CU-08 tienen ficha pero no caso de uso dibujado |
| ✅ B-3 (7-oct) | 🔒 | — | Cuando los casos de uso estén corregidos, agendar la revisión con la Dra. Martha Rosa Cordero López [corr. CU-22] |

---

## Para Erick (entradas de glosario, abreviaturas o dudas)

- **CU-21 ya no existe** (se fusionó en CU-22, 5-oct). En `chapters/05_diseno.tex:262` queda «(ver CU-21, RF-23)»: cámbialo a «(ver CU-22, RF-23)». Es tu zona, no la mía.
- **Siglas y términos que no toqué porque están en párrafos tuyos:** ROI (`03_marco_teorico.tex`, subsección de la línea de agua), SVM (`02_estado_arte.tex`, clasificadores clásicos), TT-II (`02_estado_arte.tex`, redes 3D), «transfer learning» en el título de la subsección de redes convolucionales del cap. 2 (`02_estado_arte.tex`) y BORIS en la tabla de cronograma del cap. 1 (`01_introduccion.tex`).
- **M-8 resuelto (6-oct):** se decidió citar la ISO/IEC 25010 en su edición 2011 (la que llama «portabilidad» y «usabilidad» a esos atributos). Se cambió `25010:2023` por `25010:2011` en todo el documento, incluidos `04_analisis.tex` y `05_diseno.tex` (zona de Ángel, solo el año y la atribución de la portabilidad); conviene que él lo revise.
- **Casos de uso sin ficha propia** (su contenido está dentro de otra ficha): «Ejecutar pipeline de análisis» y «Reportar error de pipeline» (CU-07), «Desglosar por minuto» y «Comparar grupos en Día 2» (CU-09), «Generar archivo de reporte» (CU-10).
- **CU-06 se fusionó en CU-22** (6-oct), igual que CU-21. CU-24 «Gestionar experimentos globales» se solapa con CU-22 y CU-23 y queda como decisión abierta de Ángel.

---

## 7. Auditoría del 11-oct (`hallazgosAgentes11oct/`)

Aplicado el 2026-10-11 en mi zona: capítulos 1 a 3, `front/`, `bib/` y casos de uso.

**✅ Aplicado (11-oct)**

- **Cap. 1:** C1-01, 04, 06, 07, 09, 10, 11, 13, 15, 17, 18, 20 y 21 (parcial: «los grupos del experimento»); TT-13 («escalamiento»); TT-05 (TT-I/TT-II definidos en el cap. 1); OG y OE-1…OE-6 rotulados.
- **Cap. 2:** C2-07, 08, 09, 11.
- **Cap. 3:** C3-01 (subsección de *gradient boosting* y portada del capítulo), 02, 05, 07, 09, 11, 12; ORM como *Object-Relational Mapping*.
- **Bibliografía:** C2-02 y C2-03 corregidos contra Crossref; C2-01 ya estaba corregido (solo se añadió `number`).
- **Preliminares:** TT-01 (`documento_tecnico`), TT-13 (`resumen`), TT-14 y entrada CNN del glosario, abreviaturas nuevas (CU, DL, OE, OG, TT-I, TT-II).
- **Casos de uso (cap. 5):** C5-07 (número de especímenes en CU-05). C5-01, C5-02, C5-16, DF-04, DF-05, DF-22 y DF-25 ya estaban corregidos.

**❓ Pendiente de decidir (preguntas abiertas)**

- C1-03 / C2-05 (DSAAN: ¿tres conductas?), C2-04 (YOLO-Behaviour), C2-10 (Sturman duplicado).
- C3-03 (`cryan2005`), C3-04 (ResNet), C2-13 (`armario2021`), C1-16 (atributo de la ISO 25010).
- C1-19 / C2-12 (ANY-maze sin cita).
- C1-05 (despliegue ESCOM), C1-08 (gráficas de barras), C1-12 («en minutos»), C1-14 (flujo óptico), C1-22 / C3-08 («Sprint 6»), C2-14 / C3-06 (unidad del tiempo de análisis).
- TT-03 (título con «IA» y «RATA»), TT-06 (F1 por clase o por conducta).
- DF-09 (CU-11 y CU-12 en el paquete 1 o 5), DF-11 (validación del formato en cliente o servidor), C5-08 (eliminar experimento).

**🟢 Pendiente con fuente, zona compartida**

- Anglicismos con cursiva y traducción en los caps. 4 y 5 y en el glosario (TT-08, TT-09), y TT1/TT2 en el cap. 4 (TT-05): es zona de Erick.

### Decisiones del 11-oct y su aplicación

Vanesa respondió las preguntas abiertas de la auditoría. Aplicado en caps. 1 a 3, bibliografía y
casos de uso:

- ✅ Cap. 1: solo `della_valle2025` como trabajo de aprendizaje profundo que clasifica las tres
  conductas (DSAAN no); se quitó `cryan2005` del cap. 1 y del cap. 3; se quitó la cláusula de
  ISO 25010 sobre robustez; se cita ANY-maze (`stoelting_anymaze`, nueva); «cuando termina» en
  vez de «en minutos» (cap. 1, resumen y documento técnico); sin «gráficas de barras»; sin
  «flujo óptico».
- ✅ Despliegue fuera del TT y sin registro: se quitó del cap. 1 el apartado del alcance, el
  «despliegue» del reparto de responsabilidades, del cronograma y del stack.
- ✅ «F1 por conducta» en resumen y caps. 1 y 2; en el cap. 3 cada conducta se presenta como
  una clase del clasificador.
- ✅ Tiempo de análisis en segundos (cap. 2 y 3); sin «Sprint 6».
- ✅ Cap. 2: el 3D-RCNN es el único de aprendizaje profundo con tres conductas; el descriptor
  de `armario2021` se reemplazó por la descripción de los rasgos; YOLO-Behaviour y Sturman ya
  estaban bien.
- ✅ Cap. 3: ResNet explicada como problema de degradación.
- ✅ Casos de uso: CU-23 elimina desde el *dashboard* o el detalle, con aviso de «¿está
  seguro?» y sin pedir nombre ni contraseña; CU-05 valida la extensión en la interfaz y la
  orientación/reproducibilidad en el servidor. Las fichas de CU-11 y CU-12 ya concuerdan con
  los paquetes 1 y 5.
- ✅ Título de la portada: no se cambia («IA» y «RATA» se quedan, es el título registrado).
  Los agentes no deben «corregirlo».

**Para Erick (zona suya, no la toqué):**

- **Despliegue fuera del alcance y sin registro:** RNF-10 (cap. 4) y cualquier mención del
  despliegue en la ESCOM en los caps. 4 y 5.
- **Eliminar un experimento:** RN-09 y RF-27 pedían confirmación explícita; el texto de la
  pantalla (`05_diseno.tex`, «nombre del experimento y la contraseña») debe decir solo un aviso
  de «¿está seguro?», y el mockup v2 también.
- **Validación del video:** extensión en la interfaz y orientación/reproducibilidad en el
  servidor; ajustar RF-10, RN-10 y `seq_carga_video.puml`.
- **`cryan2005`** sigue citado en `04_analisis.tex` (RN, ~548).
- **F1 «por conducta»:** `CLAUDE.md` todavía dice «por clase» (OE-5, RNF-02).
- **Anglicismos y TT1/TT2** en los caps. 4 y 5 (TT-08, TT-09, TT-05).

- ✅ **Registro en `errores/preguntas-doctor.md`:** D-57 a D-65 (revisión, copia H.264, intervención
  humana, reinicio del análisis, Administrador activo, despliegue, eliminar experimento,
  validación del video, F1/tiempo/título). **D-57 a D-60 no están aplicados** a RN-04, RN-14, RF-32
  ni al cap. 5: cambian el diseño de la revisión y hay que decidir cómo antes de propagarlos.
- ✅ RN-16 (Administrador activo) agregada al cap. 4 y referida en CU-11 y CU-17.

### Reauditoría del 11-oct (`hallazgosAgentes11oct-reauditoria/`)

Aplicado el 2026-10-11, primer bloque (hallazgos con fuente que decide):

- ✅ **Cap. 1:** C1-01 y C1-03 (el Día 1 solo es habituación; 300 s es un máximo), C1-02 (el control recibe placebo
  el Día 2), C1-05, C1-08, C1-10, C1-11, C1-13, C1-14, C1-17, C1-19, C1-22 y TT-13; el resumen ya no dice que el
  usuario «ejecuta» el análisis (C1-04).
- ✅ **Cap. 2:** C2-02 (YOLO definido al primer uso), C2-03 (Redmon 2016 y Ren 2017 en `referencias.bib`), C2-07.
- ✅ **Cap. 3 y abreviaturas:** C3-11 (*worker*, *clips*, *recall*), C3-12 (notación) y siglas ACID, GMM y VP.
- ✅ **Casos de uso:** DF-12 (fichas CU-11 y CU-12 movidas al Paquete 1) y DF-14 (CU-22 en vez de CU-21).
- ⏳ **Sin aplicar de ese bloque:** DF-13, DF-16 y DF-19 (`cu_*.puml`: acentos y el `<<extend>>` del desglose) porque
  hay que regenerar los PNG y este equipo no tiene `plantuml.jar`; C3-09 (renombrar claves del `.bib`) y C3-13
  (reestructurar la sección del clasificador del cap. 3), que cambian mucho texto sin una fuente que lo exija.
- ⏳ **Para Erick:** RF-09, RN-03 y RF-19 (el Día 1 no se analiza), R-03, RNF-10 y el volumen de la factibilidad
  (cap. 4); la pantalla de eliminar experimento y el apartado «Arquitectura» (cap. 5); la figura de arquitectura;
  `INSTRUCCIONES-WEB.md` R-03; `DISENO-BD.md` P-08; el glosario («colaborador clínico»).

**Segundo bloque (11-oct), zona de Erick incluida por pedido de Vanesa:**

- ✅ **Cap. 4:** RF-09 (el Día 1 no se analiza; 300 s es un máximo), RF-19 («por espécimen»), RF-27 y RN-09 (eliminar
  desde el *dashboard* o el detalle, solo aviso), RN-10 (extensión en la interfaz; orientación y reproducibilidad en el
  servidor), RNF-03 y RNF-10 (sin despliegue), R-03 (sin registros del laboratorio), y las menciones de despliegue y el
  volumen de la factibilidad.
- ✅ **Cap. 5:** «anotación experta» (línea 101), procesamiento parcial de cilindros (todo o nada), apartado «Arquitectura»
  y portabilidad (sin despliegue), pantalla de eliminar experimento (sin nombre ni contraseña).
- ✅ **`INSTRUCCIONES-WEB.md`** (R-03 y ruta de subida) y **`DISENO-BD.md`** (P-08/D-03 cerrada).
- ✅ **`.puml`** (fuente de las figuras): arquitectura (sin CLAHE, `_tracked`, solo `.mp4` ni SQL), esquema físico (sin
  `D-xx`, SQL ni «rata»), `estados_analisis`, `seq_consulta_progreso`, `seq_consulta_resultados` (cuatro conductas),
  `seq_crear_cuenta`, `seq_descarga_reportes` y `flujo_general`.
- ⏳ **PNG sin regenerar:** las figuras de `figures/mermaid/` y `diagramas/clases.png` siguen mostrando lo anterior hasta
  regenerarlas con PlantUML (no hay `plantuml.jar` en este equipo).
- ⏳ **Mockups** `experimento` y `experimentos` (`figures/mockups/v2/`): hay que revisar que no pidan nombre y contraseña.
