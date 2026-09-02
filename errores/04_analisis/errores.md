# Errores e inconsistencias — Capítulo 4: Análisis

**Archivo:** `chapters/04_analisis.tex`
**Última actualización:** 2026-08-30
**Fuentes de contraste:** entrevista formal (`docs/entrevista_sandino.docx`), respuestas directas del equipo, transcripción informal (`../fuentes/transcripcion_01_no-formal.md`)

> Ver [../README.md](../README.md) para la jerarquía de fuentes y la escala de severidad.

**Resumen:** 4 altas · 3 medias · 0 bajas

> **Nota de alcance.** Estos hallazgos se recogieron en una pasada previa a que el análisis se
> acotara a los capítulos 1 a 3. Están verificados uno por uno contra el archivo, pero el capítulo
> no ha recibido una revisión completa como la que sí tienen los capítulos 1 a 3. Tratar esta lista
> como parcial.

---

## E04-01 — «los cuatro cilindros» en requerimiento y regla de negocio 🔴

**Severidad:** Alta · **Ubicación:** `:139` (RF-14), `:531` (RN-11), `:846` (factibilidad tecnológica) · **Fuente:** respuesta directa del equipo · **Estado:** Pendiente
**Transversal:** T-02

| Línea | Elemento | Dice |
|-------|----------|------|
| `:139` | RF-14 | «detectar automáticamente la posición de **los cuatro cilindros** en el encuadre con una confianza mínima de 0.70» |
| `:531` | RN-11 | «Si la confianza de detección de **los cuatro cilindros** no alcanza 0.70…» |
| `:846` | Factibilidad | «vista lateral, **cuatro cilindros simultáneos**, cámara de celular» |

**Respuesta directa del equipo (2026-08-29):**
> «Los videos pueden mostrar menos o más cilindros pero siempre más de dos.»
> «Lo máximo que se verá a cuadro son 4 cilindros.»

**Corrección:** el requerimiento y la regla deben expresarse sobre un número variable —«todos los
cilindros presentes en el encuadre», con `n ∈ {3, 4}`—, no sobre la constante cuatro.

**Consecuencia:** RN-11 define la condición de fallo del pipeline. Tal como está redactada, **un video
de tres cilindros no la satisface nunca**, porque no existen «los cuatro cilindros» que evaluar. El
pipeline quedaría bloqueado sin motivo real.

---

## E04-02 — RF-11 declara mal el mínimo del número de ratas 🔴

**Severidad:** Alta · **Ubicación:** `:118` · **Fuente:** respuesta directa del equipo, entrevista P19 · **Estado:** Pendiente
**Transversal:** T-02

**Dice el LaTeX (RF-11):**
> «número de ratas a analizar (típicamente 4, pero puede ser **entre 1 y 4** según el diseño
> experimental)»

**Respuesta directa del equipo:** siempre **más de dos** y como máximo **cuatro a cuadro**.

El máximo está bien; el mínimo no:

| | LaTeX | Fuente primaria |
|---|-------|-----------------|
| Mínimo | 1 | **3** |
| Máximo | 4 | 4 ✓ |

**Corrección:** el rango correcto es `n ∈ {3, 4}`. El máximo está bien; el mínimo no. Un experimento
con una sola rata a cuadro no ocurre.

**Nota de alcance sobre el requerimiento.** RF-11 registra el número de ratas como atributo del
«experimento». Con la jerarquía correcta ese atributo pertenece a la **tanda**, no al experimento,
que tiene entre 32 y 48 especímenes repartidos en grupos. Ver T-01 en el README.

---

## E04-03 — La factibilidad operativa contradice a RN-03 🔴

**Severidad:** Alta · **Ubicación:** `:885`–`:886` contra `:493` · **Fuente:** entrevista P19 · **Estado:** Pendiente
**Transversal:** T-01

| Línea | Elemento | Dice |
|-------|----------|------|
| `:493` | RN-03 | «Un experimento tiene como **máximo dos videos**: uno del Día 1 (20 min) y uno del Día 2 (5 min).» |
| `:885` | Factibilidad operativa | «cada uno con entre 6 y 8 especímenes divididos en grupos […] Cada experimento genera **entre 6 y 8 videos** de 5 min en el segundo día.» |

Dos afirmaciones incompatibles sobre el mismo objeto, en el mismo capítulo.

**Además, el pasaje de factibilidad es internamente inconsistente:** si un experimento tiene 6 a 8
especímenes en total y caben varios por video, no puede generar 6 a 8 videos.

**Lo que dice la fuente (P19):**
> «Por semestre se realizan entre 3 y 4 experimentos independientes, con promedio de 4 grupos y
> **32 a 48 especímenes**, lo que genera alrededor de **8 videos por experimento**.»

Es decir: 32 a 48 especímenes por experimento (no 6 a 8), y ~8 videos por experimento (no 2).

**Corrección:** ambas afirmaciones se resuelven introduciendo el nivel **Tanda**. RN-03 es correcta
si se aplica a la tanda («una tanda tiene como máximo dos videos, uno por sesión»); la factibilidad
es correcta si se aplica al experimento. Ver T-01 en el README.

**Por verificar (transcripción informal, rango 3):** el audio crudo de la entrevista dice
literalmente «por **bimestre** se pueden realizar entre tres y cuatro experimentos
independientes», pero cierra la cuenta con «por **semestre** estaríamos hablando de entre 32
y 40 videos». La aritmética de este mismo hallazgo solo cierra con «semestre» — con
«bimestre» saldrían 9 a 12 experimentos y más de 70 videos por semestre. El `.docx` formal ya
normalizó esto a «semestre» en ambos lugares, probablemente corrigiendo un lapsus al hablar,
pero conviene confirmarlo con el laboratorio antes de descartarlo del todo. Ver Q-06 en el
README.

---

## E04-04 — Cinco referencias cruzadas RN → RF obsoletas 🟡

**Severidad:** Media · **Ubicación:** `:441`, `:509`, `:525`, `:541`, `:804` · **Estado:** Pendiente

Referencias desfasadas tras la renumeración de requerimientos funcionales. Verificadas una por una
contra el contenido real de cada RF.

| Línea | Elemento | Dice | Debe decir | Por qué |
|-------|----------|------|------------|---------|
| `:441` | sec. umbrales, duración de episodio | `ver RF-30` | **RF-18** | RF-30 es gestión de experimentos por el Admin; la regla de los 3 s es RF-18 |
| `:509` | RN-06 | `Ver RF-25` | **RF-26** | RF-25 es el borrado automático de video; la conservación indefinida es RF-26 |
| `:525` | RN-09 | `Ver RF-26` | **RF-27** | RF-26 es la conservación; el borrado de experimento es RF-27 |
| `:541` | RN-12 | `Ver RF-20` | **RF-21** | RF-20 es el desglose por minuto; la comparación Día 1 contra Día 2 es RF-21 |
| `:804` | R-06 | `ver RF-28` | **RF-29** | RF-28 es la lista de usuarios; el monitoreo de disco es RF-29 |

**Nota:** conviene revisar también `:520` (RN-08 → `RF-29`), que parece deber apuntar a RF-30
(gestión de experimentos de cualquier investigador) y no a RF-29 (monitoreo de disco).

---

## E04-05 — Falta un RNF de repetibilidad, y ya hay línea base para justificarlo 🔴

**Severidad:** Alta · **Ubicación:** tabla `tab:rnf` · **Fuente:** entrevista P13, P8, transcripción informal · **Estado:** Pendiente
**Transversal:** T-04

**Dice la entrevista (P13):**
> «Lo ideal sería que el mismo video analizado múltiples veces arroje siempre el mismo resultado,
> con una **variabilidad máxima de entre el 5 y el 10 %**.»

**Qué falta:** RNF-02 recoge la concordancia con el analista humano (F1 ≥ 85 %), pero no existe
ningún RNF sobre la repetibilidad del propio sistema. Son dos criterios distintos:

| Criterio | Valor | Fuente | ¿Está en el documento? |
|----------|-------|--------|------------------------|
| Concordancia con el analista humano | ≥ 85 % | P8 | Sí, RNF-02 |
| Repetibilidad entre corridas del mismo video | variabilidad ≤ 5–10 % | P13 | **No** |

**Dato nuevo que sube la severidad (transcripción informal, rango 3, minuto 11:54–13:29):** el
Dr. Sandino cuantifica la variabilidad humana actual —«cada uno va a tener una variabilidad,
anda por ahí del 15 % en cada una de las conductas, un poquito más, 20 % de diferencia en
tiempos»— con tres analistas trabajando de forma independiente. Ya no es solo una meta sin
sustento: hay una **línea base humana documentada (15–20 %)** contra la meta objetivo del
sistema (5–10 %). Sube de media a alta porque el RNF que falta ahora tiene el dato exacto que
lo justifica y lo hace verificable.

**Corrección:** añadir el RNF, con ambos números —la línea base humana y la meta del sistema—
como justificación en la sección de umbrales. Es además el criterio que el usuario declaró
como prioritario por encima del tiempo de procesamiento, y el documento ya reconoce en RNF-02
que «el tiempo de procesamiento no es el criterio prioritario para el laboratorio».

---

## E04-06 — Dos umbrales de concordancia distintos sin distinguir 🟡

**Severidad:** Media · **Ubicación:** `:410`–`:425`, subsección «Justificación de umbrales» · **Fuente:** entrevista P8, PD · **Estado:** Pendiente

La entrevista da **dos cifras para dos cosas distintas**, y el documento solo lleva una:

| Fuente | Cifra | Aplica a |
|--------|-------|----------|
| P8 | **85 %** | Concordancia aceptable entre el sistema y el analista humano |
| PD | **80 %** | Umbral razonable al medir contra los videos ya analizados manualmente, usados como conjunto de prueba |

**Dice PD:**
> «Una vez entrenado, sí se pueden usar los videos ya analizados manualmente como conjunto de prueba
> para medir qué tan cerca llega el modelo (**80 % o más de concordancia es un umbral razonable**).»

**Qué falta:** la subsección de umbrales justifica el 85 % pero no menciona el 80 % ni distingue los
dos contextos. Conviene explicitar cuál se aplica en qué fase, o justificar por qué se adopta uno solo.

**Relacionado —dato de PD que el capítulo debería recoger en la estrategia de entrenamiento:**
> «No es recomendable usar los reportes completos para entrenamiento porque el modelo podría
> sobre-entrenarse hacia esos patrones específicos. Lo ideal es entrenar con **clips cortos donde la
> conducta sea inequívoca**.»

El riesgo R-08 menciona los clips inequívocos, pero solo como mitigación del riesgo de confusión
entre nado y escalamiento, no como la estrategia general de entrenamiento que el investigador
recomendó.

---

## E04-07 — RN-04 no distingue reinicio manual de reanálisis administrativo 🟡

**Severidad:** Media · **Ubicación:** `:497`–`:499` (RN-04), `:153`–`:154` (RF-16) · **Fuente:** respuesta directa del equipo (2026-08-30) · **Estado:** Pendiente

**Dice el LaTeX (RN-04):**
> «El análisis lo inicia el sistema automáticamente al terminar la carga. El investigador no
> puede iniciarlo, pausarlo, cancelarlo ni reiniciarlo desde la interfaz.»

**Respuesta directa del equipo**, a la pregunta de si un video puede volver a analizarse más
de una vez (por ejemplo tras mejorar el modelo): «Sí, se puede volver a hacer.»

**No es una contradicción dura, pero sí una ambigüedad real.** Las dos afirmaciones son
compatibles si se entiende que RN-04 restringe únicamente el **reinicio manual por el
investigador desde la interfaz** (eso se mantiene), mientras que el **reanálisis
administrativo o automatizado** —por ejemplo, tras actualizar el modelo entrenado— es un caso
distinto y permitido. Pero el documento no hace esa distinción en ningún lugar. Tal como está
redactado, un lector puede entender razonablemente que ningún video se reanaliza jamás.

**Corrección:** aclarar en RN-04 o en una nota aparte que el reinicio manual está prohibido
solo desde la interfaz del investigador, y que el sistema puede reanalizar un video de forma
administrativa (por ejemplo, al mejorar el clasificador) sin que eso constituya una excepción a
la regla.

**Consecuencia estructural para el esquema conceptual:** la relación Video–Análisis deja de
ser (1,1) y pasa a **(1,N)** — un video puede acumular más de un registro de análisis a lo
largo del tiempo, cada uno con su propia confianza, estado y nivel de clasificación. Afecta el
esquema publicado en la actividad 5 (sección «Lo que queda abierto», ítem «Reanálisis de un
video»), que hasta ahora lo dejaba como cardinalidad provisional sin confirmar.
