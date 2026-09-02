# Errores e inconsistencias — Capítulo 2: Estado del arte

**Archivo:** `chapters/02_estado_arte.tex`
**Última actualización:** 2026-08-30
**Fuentes de contraste:** entrevista formal (`docs/entrevista_sandino.docx`), respuestas directas del equipo, transcripción informal (`../fuentes/transcripcion_01_no-formal.md`)

> Ver [../README.md](../README.md) para la jerarquía de fuentes y la escala de severidad.

**Resumen:** 0 altas · 2 medias · 3 bajas

Este capítulo es el que menos contradicciones tiene con las fuentes primarias, porque
describe trabajo de terceros y no hace afirmaciones sobre el laboratorio. Los hallazgos
son de estructura y de criterio, no de hechos.

---

## E02-01 — Sección DeepLabCut duplicada 🟡

**Severidad:** Media · **Ubicación:** `:64`–`:75` y `:187`–`:196` · **Estado:** Pendiente

El mismo trabajo (Sturman et al., `sturman2020_dlc`) se describe dos veces con texto casi
idéntico, en dos secciones distintas:

| Ubicación | Sección | Primera frase |
|-----------|---------|---------------|
| `:64` | Trabajos similares → «DLC como clasificador de conducta en el FST» | «Sturman et al. mostraron que un clasificador entrenado sobre la representación esquelética producida por DeepLabCut puede eliminar la variabilidad entre evaluadores humanos en el FST.» |
| `:187` | Técnicas de visión por computadora → «DeepLabCut» | «Sturman et al. mostraron que un clasificador entrenado sobre la representación esquelética producida por DeepLabCut puede eliminar la variabilidad entre evaluadores humanos en el FST.» |

Ambas repiten además el mismo argumento del costo de anotación de puntos clave.

**Corrección:** conservar una sola. La ubicación natural es «Trabajos similares», porque
DeepLabCut aquí se discute como enfoque completo (pose + clasificador), no como técnica
de visión aislada. En la sección de técnicas basta una remisión.

**Nota:** ByteTrack también se describe en este capítulo (`:207`–`:228`) y otra vez en el
cap. 3 (`:177`–`:225`). Ahí la duplicación es defendible —estado del arte contra marco
teórico— pero conviene revisar que no repitan las mismas frases.

---

## E02-02 — El capítulo no contrasta contra el criterio prioritario del usuario 🟡

**Severidad:** Media · **Ubicación:** sección «Criterios de calidad para la evaluación del sistema», tabla `tab:comparativa_herramientas` · **Fuente:** entrevista P8, P13 · **Estado:** Pendiente
**Transversal:** T-04

**Dice el LaTeX:** los tres atributos de calidad son `functional correctness`, `time behaviour`
y `usability`. La tabla comparativa evalúa a cada herramienta por «Métricas reportadas».

**Dice la entrevista (P13):**
> «No tienen mayor problema con el tiempo que tarde el análisis. Lo que más importa es que
> haya menos variabilidad […] variabilidad máxima de entre el 5 y el 10 %.»

**Y P8:**
> «El objetivo principal no es tanto la velocidad sino reducir la variabilidad del factor humano.»

**El problema:** el capítulo dedica un criterio completo al tiempo de análisis —que el usuario
declaró explícitamente como no prioritario— y ninguno a la repetibilidad, que es lo que el
usuario sí pidió. La columna «Métricas reportadas» de la tabla no tiene forma de mostrar
si una herramienta es determinista.

**Corrección:** añadir la repetibilidad como cuarto criterio de evaluación y considerar una
columna en la tabla comparativa. Es además un argumento fuerte a favor de la propuesta:
ninguna de las herramientas revisadas reporta repetibilidad, y un sistema automatizado la
tiene por construcción.

**Argumento que el cap. 1 ya usa y este capítulo podría recoger:** «Un sistema automatizado
produce siempre el mismo resultado para el mismo video. Si hay error, es el mismo error en
todos los casos: documentable y corregible, no aleatorio.»

---

## E02-03 — Error de redacción en la descripción de YOLO-Behaviour 🟢

**Severidad:** Baja · **Ubicación:** `:79`–`:80` · **Estado:** Pendiente

> «Chan et al. presentaron un sistema que separa la detección **del la rata** de la
> clasificación de su conducta.»

Residuo de la sustitución «del animal» → «de la rata». Debe decir «de la rata».

---

## E02-04 — Referencia adelantada al capítulo 4 🟢

**Severidad:** Baja · **Ubicación:** `:184` · **Estado:** Pendiente

> «El **cap. 4** detalla por qué ese trade-off es conveniente dado el tamaño del dataset
> disponible.»

Dos cosas a verificar:

1. Que el cap. 4 efectivamente desarrolle ese razonamiento sobre el trade-off entre
   detección de una etapa y de dos etapas. Si no lo hace, la promesa queda sin cumplir.
2. Que la referencia siga apuntando al capítulo correcto tras cualquier reordenamiento
   de capítulos.

**Nota de estilo:** el cap. 2 remite al 4 pero el 4 no remite de vuelta al 2. Conviene
cerrar el par de referencias en ambos sentidos, o eliminar la remisión y desarrollar el
argumento aquí mismo, que es donde el lector lo está esperando.

---

## E02-05 — El «otro equipo» es un paradigma distinto, no pertenece a este capítulo 🟢

**Severidad:** Baja · **Ubicación:** ninguna — se descarta como corrección al cap. 2 · **Fuente:** transcripción informal + respuesta directa del equipo · **Estado:** Resuelto

**Dice la transcripción informal** (minuto 12:46–13:36, no presente en el `.docx` formal):
> «Lo que estamos haciendo con **el otro equipo** es que el mismo video lo analizan varias
> veces para ver justamente si el entrenamiento les está generando datos diferentes para el
> mismo video, o si está reproduciendo exactamente el mismo resultado […] con videos que no
> se usaron para entrenar.»

**Respuesta directa del equipo (2026-08-30):** «Es un equipo que trabaja con ansiolíticos y
un experimento diferente (laberinto T elevado).»

**Resuelto — no requiere corrección aquí.** El laberinto T elevado mide ansiedad con fármacos
ansiolíticos; el FST mide desesperanza conductual con antidepresivos. Son paradigmas distintos,
así que no pertenece a la tabla `tab:comparativa_herramientas` ni cambia el argumento de que
«ningún sistema existente cubre los cinco criterios al mismo tiempo» — ese argumento sigue
siendo válido porque no hay un trabajo comparable sobre FST.

**Dónde sí vale la pena mencionarlo:** el cap. 1 ya declara **RNF-11** («el módulo de
clasificación debe poder reconfigurarse para soportar paradigmas conductuales distintos al
FST»). La existencia de este equipo paralelo es evidencia real de que esa necesidad de
extensibilidad no es hipotética — ya hay, dentro de la misma institución, un caso concreto que
la ejercería. Se puede añadir como una frase de contexto en la metodología (cap. 1) si se
quiere reforzar RNF-11, pero no es obligatorio.
