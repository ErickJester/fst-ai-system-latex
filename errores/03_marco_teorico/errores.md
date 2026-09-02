# Errores e inconsistencias — Capítulo 3: Marco teórico

**Archivo:** `chapters/03_marco_teorico.tex`
**Última actualización:** 2026-08-30
**Fuentes de contraste:** entrevista formal (`docs/entrevista_sandino.docx`), respuestas directas del equipo, transcripción informal (`../fuentes/transcripcion_01_no-formal.md`)

> Ver [../README.md](../README.md) para la jerarquía de fuentes y la escala de severidad.

**Resumen:** 4 altas · 4 medias · 0 bajas

---

## E03-01 — El criterio visual para distinguir escalamiento está escrito para una vista que el sistema no usa 🔴

**Severidad:** Alta · **Ubicación:** `:61`–`:63` · **Fuente:** el propio capítulo, `:76` y `:148` · **Estado:** Pendiente

**Dice el LaTeX (subsección «Conductas que se observan y cómo se interpretan»):**
> «Desde la **vista cenital**, el escalamiento produce movimiento concentrado en el borde
> del cilindro, lo que lo distingue visualmente del nado.»

**Dice el mismo capítulo 15 líneas después (`:76`, subsección «Protocolo del laboratorio colaborador»):**
> «Los videos se graban desde una **vista lateral** con cámara de celular.»

**Y otra vez en `:148`:**
> «La superficie del agua puede generar reflejos que hacen que la rata aparezca duplicada
> desde la **vista lateral**.»

**El problema:** el único criterio visual que el marco teórico ofrece para separar
escalamiento de nado —la conducta que, según la entrevista P8, es precisamente la más
difícil de distinguir— está formulado para una vista cenital que el laboratorio no usa.

**Confirmación de la entrevista (P8):**
> «La mayor diferencia entre analistas ocurre al distinguir **escalamiento y nado**.»

**Corrección:** reescribir el criterio para vista lateral. El propio cap. 2 (`:256`) ya tiene
la versión correcta y se puede reutilizar:
> «la relación entre el área de movimiento y la posición vertical del centroide: el
> escalamiento produce movimiento en la **mitad superior** del cilindro mientras que el
> nado se distribuye en toda la superficie del agua.»

**Por qué importa más allá de la redacción:** este criterio es el fundamento teórico del
riesgo de que el clasificador no separe las dos conductas y haya que agruparlas como
«conducta activa». Si el criterio citado no aplica a la vista real, el fundamento del
fallback queda sin sustento en el documento.

---

## E03-02 — «capturando los cuatro cilindros al mismo tiempo» 🔴

**Severidad:** Alta · **Ubicación:** `:76` · **Fuente:** respuesta directa del equipo · **Estado:** Pendiente
**Transversal:** T-02

**Dice el LaTeX:**
> «Los videos se graban desde una vista lateral con cámara de celular, capturando **los
> cuatro cilindros** al mismo tiempo.»

**Respuesta directa del equipo (2026-08-29):**
> «Los videos pueden mostrar menos o más cilindros pero siempre más de dos. En ambos días
> siempre serán el mismo número de cilindros al de su respectivo día anterior.»

**Corrección:** «capturando todos los cilindros de la tanda al mismo tiempo». El número es
variable con mínimo 3.

**Dato nuevo que el capítulo debe recoger:** la garantía de que el número de cilindros y el
encuadre se conservan entre el Día 1 y el Día 2. Es lo que hace posible seguir al mismo
espécimen entre sesiones, y hoy no está declarado en el marco teórico.

---

## E03-03 — Esquema de datos adelantado, y además incompleto 🔴

**Severidad:** Alta · **Ubicación:** `:340`–`:349`, subsección «Persistencia de datos con PostgreSQL» · **Fuente:** entrevista PA, P11, P19 · **Estado:** Pendiente

**Dice el LaTeX:**
> «El **esquema de datos incluye tablas para usuarios, experimentos, sesiones de video y
> resultados por rata y conducta**. Las consultas se abstraen con SQLAlchemy como ORM.»

Dos problemas distintos.

### (a) Es un esquema lógico declarado en el marco teórico

La metodología de diseño de bases de datos exige el orden conceptual → lógico → físico, y
que el modelo conceptual sea independiente de cualquier gestor. Aquí el documento nombra
cuatro tablas, un SGBD concreto y un ORM antes de que exista un esquema conceptual del que
derivarlos. El marco teórico puede describir qué es PostgreSQL; no debería afirmar cuál es
el esquema.

### (b) Al esquema le faltan dos conjuntos, y sin ellos no se cumple lo que el usuario pidió

Faltan **Grupo** y **Tanda**.

**Dice la entrevista (P11):**
> «Analizan estadísticamente **por grupo**: calculan media y desviación estándar de todas
> las ratas del grupo para cada conducta y luego comparan ese grupo contra los demás grupos
> de diferentes tratamientos.»

Sin la entidad Grupo y la relación Espécimen–Grupo no hay forma de calcular ese estadístico.
Y el cap. 1 lo promete explícitamente en el Alcance («estadísticos de grupo… para caracterizar
el perfil conductual del conjunto de especímenes de cada grupo experimental»).

Falta también **Tanda**, sin la cual «experimentos» y «sesiones de video» no se relacionan
correctamente: un experimento tiene 4 a 6 grupos y unos 8 videos, no una sesión por experimento.

**Corrección:** eliminar la enumeración de tablas del marco teórico y dejar solo la descripción
conceptual de PostgreSQL y el ORM. El esquema pertenece al capítulo de diseño, y debe derivarse
del modelo conceptual, no anticiparse.

---

## E03-04 — Edición mal cerrada al sustituir «ISRS» 🟡

**Severidad:** Media · **Ubicación:** `:55`–`:56` · **Estado:** Pendiente

**Dice el LaTeX:**
> «Se asocia al sistema serotoninérgico; **los antidepresivos tipo antidepresivos como la
> fluoxetina** (antidepresivo de referencia) aumentan esta conducta específicamente.»

Residuo de la sustitución «los antidepresivos tipo ISRS (como la fluoxetina)» → «antidepresivos
como la fluoxetina». Quedaron las dos versiones encadenadas.

**Corrección:**
> «Se asocia al sistema serotoninérgico; la fluoxetina (antidepresivo de referencia) aumenta
> esta conducta específicamente.»

**Respaldo de la entrevista (PF):**
> «Con decir "fluoxetina, que es un antidepresivo de referencia" es suficiente. Usar la sigla
> ISRS abre líneas de pregunta sobre farmacología que no son necesarias para la defensa del TT.»

---

## E03-05 — El protocolo descrito omite la estructura de grupos y tandas 🟡

**Severidad:** Media · **Ubicación:** `:71`–`:82`, subsección «Protocolo del laboratorio colaborador» · **Fuente:** entrevista PA, P19 · **Estado:** Pendiente

**Dice el LaTeX:** describe las dos sesiones, la vista lateral, la cámara y las condiciones de
iluminación, pero no dice cuántos grupos hay, cuántos especímenes por grupo, ni cuántas
grabaciones componen un experimento.

**Dice la entrevista (PA):**
> «Siempre se usan entre 6 y 8 especímenes por grupo. Normalmente trabajan con mínimo tres
> grupos: (1) grupo control […] (2) grupo de referencia […] (3) grupo de tratamiento experimental.»

**Y P19:**
> «Por semestre se realizan entre 3 y 4 experimentos independientes, con promedio de 4 grupos
> y 32 a 48 especímenes, lo que genera alrededor de 8 videos por experimento.»

**Qué falta:** la estructura completa del experimento. El cap. 1 tiene la tabla de grupos, pero
el marco teórico —que es donde se describe el protocolo— no la menciona. El lector que llega
al capítulo de diseño no tiene de dónde deducir la jerarquía Experimento → Grupo → Tanda →
Espécimen.

**Corrección:** añadir la estructura al protocolo, con las cifras de la entrevista.

---

## E03-06 — El criterio de episodio válido no aparece en el marco teórico 🟡

**Severidad:** Media · **Ubicación:** `:45`–`:70`, subsección «Conductas que se observan y cómo se interpretan» · **Fuente:** entrevista P6 · **Estado:** Pendiente

**Dice la entrevista (P6):**
> «Sí, la conducta debe mantenerse **alrededor de 3 a 5 segundos** para contarse como episodio
> válido.»

**Qué falta:** la definición operativa de «episodio» es parte de cómo el laboratorio define las
conductas, no un parámetro de implementación. El marco teórico describe las tres conductas pero
no dice cuándo una conducta cuenta. El umbral aparece solo en el cap. 1 (Alcance) y en el cap. 4.

**Corrección:** incorporar el criterio de duración mínima a la definición de conducta en el marco
teórico, señalando que el rango declarado por el laboratorio es de 3 a 5 s y que el sistema adopta
el extremo inferior.

**Relacionado:** la entrevista P7 también aporta a la definición y el capítulo tampoco lo recoge:
> «El buceo podría ser una variante del nado y se clasificaría como tal. Es la conducta que podría
> costar un poco más de trabajo clasificar, pero se trataría como nado.»

El cap. 1 sí menciona la regla del buceo; el marco teórico, que es donde se definen las conductas,
no.

---

## E03-07 — Dispositivo de captura incorrecto: es cámara web, no celular 🔴

**Severidad:** Alta · **Ubicación:** `:76` · **Fuente:** respuesta directa del equipo (2026-08-30) · **Estado:** Pendiente

**Dice el LaTeX:** «con cámara de celular».

**Respuesta directa del equipo (2026-08-30):** «Cámara web.»

**Resuelto — el documento está equivocado.** No es un celular. Es coherente con las dos
fuentes previas que apuntaban hacia Mac sin confirmarlo del todo: la entrevista formal (P5,
«graban con Mac») y la transcripción informal (minuto 4:45, «como las grabamos con Mac») — una
cámara web conectada a o integrada en la Mac explica ambas citas exactamente. Sube a severidad
alta porque ya no es una pregunta sin resolver: es una corrección confirmada por la fuente de
mayor autoridad (rango 1) que contradice directamente el texto actual.

**Corrección:** «con cámara web» en lugar de «con cámara de celular», en `:76` y en
cualquier otro lugar del documento que repita «cámara de celular» (verificar cap. 4,
factibilidad tecnológica, línea `:846`, que también dice «cámara de celular»).

**Por qué importa:** el dispositivo determina resolución, tasa de cuadros y estabilidad —
entradas directas de los requisitos mínimos de calidad de video que el capítulo promete
definir durante las pruebas. Una cámara web fija tiene un perfil de estabilidad muy distinto
al de un celular sostenido o trípode improvisado, lo que además refuerza la garantía de
encuadre constante entre sesiones que el equipo ya confirmó (ver T-02 en el README).

---

## E03-08 — Falta el valor de referencia de iluminación en el protocolo 🟡

**Severidad:** Media · **Ubicación:** `:71`–`:82`, subsección «Protocolo del laboratorio colaborador» · **Fuente:** transcripción informal + respuesta directa del equipo · **Estado:** Pendiente

**Dice el LaTeX:** «La iluminación y el nivel del agua varían entre experimentos… los
requisitos mínimos de calidad de video se definirán durante las pruebas de validación.»

**Dato de la transcripción informal** (minuto ~1:15): el entrevistador recuerda una
conversación previa donde el laboratorio mencionó un estándar de referencia de **~2,500
lúmenes**, sin que el Dr. Sandino lo confirmara en ese audio.

**Confirmado (respuesta directa del equipo, 2026-08-30):** «Es el estándar.» Ya no es una cifra
recordada de memoria — es el valor real que maneja el laboratorio. Sube de baja a media porque
pasa de ser un dato por verificar a un dato confirmado que el documento simplemente omite.

**Corrección:** añadir la cifra al protocolo del cap. 3 como referencia de iluminación —
manteniendo la distinción ya establecida en sesión de trabajo de que es un objetivo de mejor
esfuerzo, no una garantía formal del laboratorio. Por ejemplo: «el laboratorio procura mantener
un nivel de iluminación de referencia de aproximadamente 2,500 lúmenes, aunque no lo garantiza
formalmente entre sesiones.»
