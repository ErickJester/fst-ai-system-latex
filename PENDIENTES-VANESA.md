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
- **Glosario y abreviaturas son de Erick.** Si necesitas una entrada nueva, anótala al
  final de este archivo y él la agrega.

---

## 1. Capítulo 1

| # | Prioridad | Dónde | Qué hacer | Fuente |
|---|-----------|-------|-----------|--------|
| A-2 | 🔴 | Líneas 11, 114, 212, 216 | «dos evaluadores» → **tres analistas**; donde dice que el tiempo «se duplica», es que **se triplica**. (No cambies la 455 del cap. 4: habla de la literatura) | Entrevista P12 · `errores/01_introduccion/errores.md` E01-06 |
| A-3 | 🔴 | Líneas 158, 271 | Quitar «como funcionalidad opcional» del desglose por minuto: el laboratorio lo pidió como necesidad (RF-20 lo exige) | Entrevista P9 · E01-07 |
| A-4 | 🔴 | Líneas 59-66 y la tabla `tab:grupos_experimentales` | «tres grupos de entre 6 y 8» → hay **tres tipos** de grupo (control, referencia, tratamiento) y un experimento tiene **tres o más grupos** (en promedio 4), porque un tipo puede repetirse (varias moléculas o dosis). Presentar la tabla como catálogo de tipos. Los 6–8 especímenes son lo **típico**, no una regla: el sistema acepta grupos desde 2 (D-28) | Entrevista PA, P19 · E01-05 |
| A-5 | 🔴 | Propuesta y objetivos (157-198) | Agregar la **cuarta conducta**, *conducta activa* (cuando el clasificador no distingue nado de escalamiento). Hoy solo aparece en la línea 281 | RN-13 del cap. 4 |
| M-1a | 🟡 | Justificación (~206-241) | Agregar el criterio de **repetibilidad**: el mismo video analizado varias veces debe dar el mismo resultado, con variabilidad máxima de 5–10 %. Es el criterio principal del laboratorio, por encima de la velocidad. (El RNF del cap. 4 lo escribe Erick) | Entrevista P13, P8 · E01-08 |
| M-2 | 🟡 | «Fuera del alcance» (~304) | Agregar que el acervo histórico (80–100 videos de 10–12 años, ya analizados a mano) no se carga al sistema | Entrevista P19, PG · E01-11 |
| M-3 | 🟡 | Todo el capítulo | Nombrar el nivel **tanda** (sesión de grabación de 2 a 4 especímenes de un grupo) para que «experimento» signifique siempre el estudio completo | Entrevista P19 · E01-04 |

## 2. Capítulo 2

| # | Prioridad | Dónde | Qué hacer | Fuente |
|---|-----------|-------|-----------|--------|
| A-16 | 🔴 | Líneas ~64 y ~189 | La sección de DeepLabCut como clasificador del FST (Sturman et al.) está **duplicada**. Dejar una sola, en «Trabajos similares» | E02-01 |
| M-1b | 🟡 | Criterios de evaluación de los trabajos | Agregar la **repetibilidad** como criterio de comparación | Entrevista P13 · E02-02 |
| V-1 | ❓ | Descripción de YOLO-Behaviour | Verificar contra el artículo si de verdad separa detección y clasificación en dos etapas, como dice el texto | Agentes §2 |
| V-2 | ❓ | Cifras de YOLOv8 y «cientos de miles de imágenes» | No tienen cita directa: citar o quitar | Agentes §2 |

> La tabla comparativa del cap. 2 (columna «DL») **no es tuya**: cambia cuando se elija el
> clasificador (CLA-03, Erick).

## 3. Capítulo 3

| # | Prioridad | Dónde | Qué hacer | Fuente |
|---|-----------|-------|-----------|--------|
| A-6 | 🔴 | Línea 62 | El criterio de escalamiento dice «desde la **vista cenital**»; el sistema usa **vista lateral**. Reescribir: en vista lateral, el escalamiento produce movimiento en la mitad superior del cilindro y el nado se distribuye en toda la superficie del agua (así lo dice ya el cap. 2) | E03-01 |
| A-7 | 🔴 | Líneas 285-287 | Quitar la lista de tablas («usuarios, experimentos, sesiones de video y resultados por rata y conducta»): es el modelo viejo y el marco teórico no debe adelantar el esquema. Dejar solo la idea de base de datos relacional con ORM | E03-03 |
| M-5 | 🟡 | Líneas 55-56 | «los antidepresivos tipo antidepresivos como la fluoxetina (antidepresivo de referencia)» → «la fluoxetina (antidepresivo de referencia)» | E03-04 |
| M-6 | 🟡 | Protocolo del FST | Agregar la estructura: típicamente 6–8 especímenes por grupo (no es regla, D-28), tres o más grupos por experimento (en promedio 4), grabados en tandas de 2 a 4 especímenes, y 3–4 experimentos por semestre | Entrevista PA · E03-05 |
| M-7 | 🟡 | Protocolo del FST | Agregar el valor de referencia de iluminación | E03-08 (tiene la cifra y su fuente) |
| M-8 | 🟡 | Línea 276 | La portabilidad se atribuye a la ISO/IEC/IEEE 12207; es un atributo de calidad de la **ISO/IEC 25010** | Norma |

## 4. Preliminares y bibliografía

| # | Prioridad | Dónde | Qué hacer |
|---|-----------|-------|-----------|
| A-14 | 🔴 | `portada.tex:73`, `documento_tecnico.tex:32` | Fecha «Mayo 2026» → la de entrega. Unificar los nombres entre los dos archivos (acentos y orden de apellidos: «Ángel Alí» contra «Angel Ali») |
| A-2b | 🔴 | `resumen.tex:7` | Mismo cambio que A-2: tres analistas, se triplica |
| M-4 | 🟡 | `resumen.tex:4` | «entre una y dos horas» → «entre una hora y media y dos horas» (como el cap. 1); expandir ISO e IEEE en su primera aparición |
| L-4 | 🟢 | `referencias.bib:293` | Quitar el comentario sobrante «INSTRUCCIONES: Pegar estas entradas…» |
| L-5 | 🟢 | `referencias.bib` | Quitar las entradas que nadie cita: `abadi2016`, `henriques2015`, `lauer2022_madlc`, `lukezic2017`, `zhang2022_bytetrack`, `bewley2016_sort`, `wojke2017_deepsort`. Antes busca cada clave en `chapters/`, `front/` y `back/` por si alguien la volvió a citar |
| L-7 | 🟢 | `preamble.tex` (`biblatex`) | Que la bibliografía diga siempre lo mismo («et al.» o «y col.») en cualquier compilación |

## 5. Siglas, términos en inglés y normas (caps. 1–3 y preliminares)

| # | Prioridad | Qué hacer |
|---|-----------|-----------|
| L-6 | 🟢 | Definir cada sigla en su primera aparición: nombre completo + sigla entre paréntesis (OMS, ENMyH-IPN, TT1/TT2, ROI, ML…). Términos en inglés con peso conceptual: primera vez `\textit{término}` (traducción), después solo `\textit{término}` (*time behaviour*, *recall*, *trade-off*). No aplica a GPU, API, REST, JSON, CSV o PDF |
| M-17a | 🟡 | Definir cada norma la primera vez que aparece, si esa primera vez cae en tus capítulos (por ejemplo ISO/IEC 25010 y NOM-062 en el cap. 1). Las que aparecen por primera vez en los caps. 4–5 las hace Erick |

## 6. Casos de uso: diagramas y fichas del cap. 5

Diagramas en `diagramas/puml/cu_*.puml`; el LaTeX incluye los PNG de
`figures/mermaid/cu_*.png`. Genera con PlantUML 1.2026.8 (la versión con la que se
verificó todo) y revisa la imagen antes de comitear.

**Regla de oro:** cada `<<include>>` o `<<extend>>` del diagrama aparece también en la fila
«Referencias» de la ficha (en el cap. 5). Si cambias uno, cambia el otro en el mismo
commit.

| # | Prioridad | Dónde | Qué hacer |
|---|-----------|-------|-----------|
| A-10 | 🔴 | `cu_paquete2.puml`, `cu_paquete5.puml` | Quitar «:Sistema:» como actor: un actor es externo al sistema. Usar un solo catálogo de actores: Investigador, Administrador y Worker [corr. CU-01, CU-03] |
| A-11 | 🔴 | `cu_vision_general.puml:26-27` | El Administrador solo llega a P1 y P5, así que no puede subir videos ni ver resultados. Pero es un Investigador con permisos extra (D-08): dibujar la herencia `Investigador <|-- Administrador` también aquí [corr. CU-17] |
| A-12 | 🔴 | Fichas CU-05 (~1266) y CU-08 (~1618) | CU-05 «Incluye: CU-07» → debe ser *extend*: monitorear es opcional, porque el análisis sigue aunque se cierre la pestaña (RF-15). CU-08 «Extendido por: CU-07» está al revés: CU-08 **extiende** a CU-07, porque solo ocurre si hubo error [corr. CU-18, CU-19] |
| A-9a | 🔴 | Fichas (~983, 989, 1274, 1396) | Quitar las citas internas «D-XX»: el lector de la tesis no tiene `preguntas-doctor.md`. Si la decisión importa, explicarla en una frase |
| M-18 | 🟡 | P1 | `UC17 ..> UC15a <<include>>` es una postcondición, no un include [corr. CU-05]. `UC15 ..> UC15b <<include>>` → desactivar es opcional: *extend* o caso independiente [corr. CU-06] |
| M-19 | 🟡 | P1, P2, P3, P5 | Sacar la descomposición funcional del diagrama de casos de uso: UC31–UC34 (etapas del pipeline, van en el diagrama de actividad), UC23/UC24 (validaciones internas), UC14 «Verificar rol y permisos» y UC55 «Conservar resultados» (es la regla RN-06). **UC14 tiene ficha (CU-15)**: decide si la ficha se va o se fusiona [corr. CU-02] |
| M-20 | 🟡 | P2 | La cadena `UC22 → UC23 → UC24 → UC25` dice que «Validar formato» incluye «Encolar análisis»: los tres deben colgar de UC22 [corr. CU-10]. `UC26 ..> UC24` está duplicado y «formato inválido» corresponde a UC23 [corr. CU-11] |
| M-21 | 🟡 | P4 | Solo existe «Descargar reporte PDF»; RF-22 pide también CSV y XLSX [corr. CU-12] |
| M-22 | 🟡 | P5 | La alerta de disco extiende a «Monitorear estado», así que solo existiría si el administrador está mirando el panel [corr. CU-15] |
| M-23 | 🟡 | P2, P3, P5 | UC27, UC35 y UC51 son el mismo objetivo («ver en qué va mi experimento»). Fusionar los diagramas **y** sus fichas (hoy CU-21, CU-07 y CU-22) [corr. CU-21] |
| M-30 | 🟡 | `gen_pngs.sh` | Rutas absolutas a `/home/vane/` y `/tmp/plantuml.jar` (INF-03): usar rutas relativas al repositorio |
| V-3 | ❓ | Fichas | Verificar que las fichas no se contradigan entre sí: CU-04/CU-05, CU-05/CU-07, CU-09/CU-10 |
| V-4 | ❓ | Diagramas y fichas | Nombres distintos entre diagrama y ficha (p. ej. UC14 «Verificar rol y permisos» contra CU-15 «Verificar pertenencia a Administrador»); CU-06 y CU-08 tienen ficha pero no caso de uso dibujado |
| B-3 | 🔒 | — | Cuando los casos de uso estén corregidos, agendar la revisión con la Dra. Martha Rosa Cordero López [corr. CU-22] |

---

## Para Erick (entradas de glosario, abreviaturas o dudas)

*(vacío)*
