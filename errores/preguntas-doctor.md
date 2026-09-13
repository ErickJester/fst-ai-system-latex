# Material para la reunión presencial en ESCOM

**Última actualización:** 2026-09-03, tras la reunión virtual del mismo día
**Cuándo:** lunes o viernes, 14:00–16:00 · pendiente confirmar disponibilidad de la Dra. Martha Cordero
**Asistentes previstos:** Dr. Sandino · Dr. Israel Salas · Dra. Martha Cordero · Ángel · Vanesa

> La reunión del 3-sep cerró siete preguntas. Lo que queda son tres para el laboratorio, un
> bloque para la Dra. Cordero —que no estuvo en la virtual— y los compromisos pendientes.
> Fuente de las respuestas nuevas: [`fuentes/transcripcion_02_reunion_2026-09-03.md`](fuentes/transcripcion_02_reunion_2026-09-03.md).

---

# 1 · Preguntas prioritarias

## Q-A · Las dos técnicas de cuantificación 🔴

**Por qué se pregunta.** En la reunión apareció que el laboratorio ha usado dos formas de
contar la conducta, y producen números de distinta naturaleza:

| | Cómo se hace | Qué sale |
|---|---|---|
| **Por segundo** (continua) | Cronómetro corriendo; se acumula cuánto duró cada conducta | «Nadó 43 segundos» |
| **Por eventos** | Se mira a la rata exactamente en 0:05, 0:10, 0:15… y se anota qué hace en ese instante | «12 eventos de nado» |

El sistema produce **segundos**. Si un archivo de referencia está hecho por eventos y se usa para
medir el desempeño del clasificador, se estarían comparando segundos contra conteos y el
resultado no significaría nada.

**Qué preguntar:**

1. De los archivos de Excel que nos va a compartir, ¿cómo distinguimos cuáles se hicieron
   contando segundos y cuáles por eventos? ¿Viene indicado en el archivo o hay que preguntarlo
   caso por caso?
2. ¿La técnica por eventos se sigue usando hoy, o ya solo cuentan por segundo?
3. ¿Le serviría que el sistema, además de los segundos, reporte el conteo por eventos? Es
   barato de calcular a partir del mismo análisis.

**Qué cambia según la respuesta:** si la mayoría de los análisis manuales son por eventos, el
conjunto de prueba se reduce a los que sean continuos, o hay que agregar el reporte por eventos
para poder comparar. Afecta al objetivo específico 5 y al requisito RNF-02.

**De paso, aclarar una duda relacionada:** el criterio de que una conducta debe durar de 3 a 5
segundos para contar, ¿pertenece al conteo continuo, o viene de la técnica que muestrea cada 5
segundos? El requisito RF-18 del documento lo tiene fijado en 3 segundos continuos.

## Q-B · Cuántos videos deja un experimento completo 🔴

**Por qué se pregunta.** Es una cuenta que no cierra y que está metida en el diagrama. La
entrevista dice que un experimento genera «alrededor de 8 videos». Pero si 32 ratas se graban de
4 en 4, son 8 tandas — y si cada tanda se graba los dos días, serían 16 videos, no 8.

**Qué preguntar, en concreto:**

> En un experimento completo de tres grupos de 8 ratas: ¿cuántos archivos de video quedan
> grabados en total? ¿Solo los del Día 2, o también se graban los del Día 1 de cada grupo?

**Qué cambia:** el número que aparece en el diagrama y en el capítulo 1. Hoy asumimos que los
8 son los del Día 2 y que el Día 1 se graba solo a veces — pero esa lectura es nuestra, él nunca
lo dijo así.

## Q-C · Volumen real de trabajo 🟡

**Por qué se pregunta.** El capítulo 1 justifica el proyecto con «en un semestre con entre 32 y
40 videos… más de 200 horas-persona». Esa cifra venía de la entrevista formal. En la reunión dijo
que no hay cadencia por calendario: los experimentos dependen del avance del proyecto, y un
proyecto dura de 1 a 4 años. Con eso, «por semestre» deja de ser una unidad defendible.

**Qué preguntar, evitando el marco del calendario:**

1. ¿Cuántos experimentos completos alcanzaron a correr **en el último año**?
2. ¿Cuántos videos de nado forzado tienen guardados **en total** a día de hoy?
3. Cuando corren un experimento, ¿cuánto tiempo pasa entre que se graba y que terminan de
   analizarlo a mano?

**Por qué así.** Las tres son retrospectivas y contables, no tasas. Con la primera y la respuesta
a Q-B sale el volumen anual sin discutir semestres.

**Qué haríamos con la respuesta:** reformular la justificación del capítulo 1 **por experimento**
en vez de por semestre. Un experimento de 8 videos de Día 2, a ~2 h por video y por analista, con
tres analistas, son ~48 horas-persona por experimento. Ese número aguanta cualquier cadencia.

---

# 2 · Preguntas sin prioridad

## Q-D · El nivel «proyecto» ⚪

En la reunión mencionó que un proyecto contiene 5 o 6 experimentos y dura de 1 a 4 años. Nuestro
modelo no tiene ese nivel: el `Experimento` es lo más alto.

**Decisión tomada:** no se modela, y **no se escribe nada sobre «proyecto» en el documento**
hasta confirmar a qué se refiere. No hay prisa por preguntarlo.

Si alguna vez preguntan: ¿le sería útil ver sus experimentos agrupados por proyecto dentro del
sistema, o con la lista plana es suficiente?

---

# 3 · Para la Dra. Martha Cordero — revisión de notación

No estuvo en la reunión virtual, así que la revisión de construcción de diagramas que quedó
solicitada en la simulación de defensa sigue pendiente. Llevar el diagrama entidad-relación y el
grafo relacional final.

| Ref | Qué poner sobre la mesa |
|-----|-------------------------|
| MC-01 | La **entidad asociativa** `Observación`: reúne una rata con un video y de ahí cuelga el desglose por minuto. La modelamos con identificador propio y dos interrelaciones ordinarias, no como agregación. ¿Está bien construida así? |
| MC-02 | `Espécimen` **cuelga de dos entidades**: del Grupo, que dice qué tratamiento recibió, y de la Tanda, que dice en qué video salió. ¿Se lee bien esa doble dependencia? |
| MC-03 | Las **cardinalidades** están anotadas como par mínimo-máximo en cada extremo, con valores del protocolo. ¿La notación es correcta y están del lado que corresponde? |
| MC-04 | Confirmar que los **tres diagramas** corresponden a lo esperado: el entidad-relación es la etapa conceptual, el grafo relacional es la lógica en sus dos versiones, y el de clases es UML por otro eje |
| MC-05 | Los **casos de uso** que quedaron observados: la autenticación no es visible en el diagrama general, el `extend` no refleja las condiciones del flujo, y los casos de uso por paquete no se ven |

---

# 4 · Compromisos pendientes del laboratorio

| Entregable | Estado |
|---|---|
| Carpeta «nado forzado» en Teams con los videos faltantes | Prometido para el día siguiente a la reunión |
| Artículo de Porsolt — describe cómo se interpreta cada conducta | Prometido |
| Video de protocolos que explica conducta por conducta | Lo iba a buscar; puede que ya no esté disponible |
| Presentación en Teams › Compartidos › «Sesión Depresión» | ✅ Entregado en la sesión |
| Acceso a Teams para Ángel y Vanesa | ✅ Concedido en la sesión |

**Del equipo:** recordarle por la mañana lo de los videos y los artículos.

---

# 5 · Ya respondido — no volver a preguntar

| Tema | Respuesta | Fuente |
|------|-----------|--------|
| Identificación de la rata | Marca de plumón indeleble en la cola, con líneas. Numeradas del 1 al 8 dentro de su grupo | Reunión 3-sep |
| Alcance del identificador | Vive solo mientras dura el experimento: las ratas se sacrifican al terminar. No hay seguimiento entre experimentos | Equipo |
| ¿Un video mezcla grupos? | No. Cada video lleva solo ratas del mismo tratamiento | Reunión 3-sep |
| Posición entre sesiones | La misma rata vuelve al mismo cilindro el Día 2 | Reunión 3-sep · equipo (90 % de certeza) |
| Tamaño de grupo | 8 es lo normal, 6 el mínimo, 12 lo habitual como máximo. **Sin límite** en el sistema | Reunión 3-sep · equipo |
| Nombre de «tanda» | El laboratorio no tiene palabra para ese nivel. Sí llama «sesión» a cada una de las dos grabaciones | Reunión 3-sep |
| Reanálisis de un video | Se conserva solo el análisis más reciente. No hay escenario real de reanálisis desde el laboratorio | Reunión 3-sep · equipo |
| Día 1 | Cada grupo puede tener o no su Día 1. Sirve para verificar que todas lleguen igual de estresadas, no para medir el efecto del tratamiento | Equipo |
| Grupo control | Sí recibe placebo el Día 2, porque el estrés de la inyección debe ser igual en los tres grupos. El Día 1 nadie recibe nada | Equipo |
| Qué se compara | Los 5 minutos del Día 2, entre los tres grupos | Reunión 3-sep |
| Roles de usuario | Un solo rol de investigador, sin permisos diferenciados | Entrevista P1 |
| Acceso a resultados | Todos los que tengan cuenta ven todos los experimentos | Entrevista P18 |
| Formato de video | Siempre MP4 | Entrevista P5 |
| Conductas | Tres: nado activo, inmovilidad y escalamiento. El buceo cuenta como nado | Entrevista P7 |
| Concordancia aceptable | 85 % o más contra el analista humano | Entrevista P8 |
| Variabilidad humana actual | 15–20 % entre analistas | Transcripción 01 |
| Tiempo de análisis manual | ~30 min por rata; ~2 h por video de 4 ratas; por triplicado | Entrevista P12 |
| Retención de videos | 30 días es suficiente | Entrevista P17 |
| Disponibilidad | 24/7 sería lo ideal | Entrevista P16 |
| Infraestructura | Preferentemente en la nube | Entrevista P15 |
| Estructura del CSV | Cabecera de tiempo + una columna por conducta, en segundos | Entrevista P10 |
| Entrenamiento del modelo | Con clips cortos de conducta inequívoca, no con los reportes completos | Entrevista PD |
| Nombre del laboratorio | Laboratorio de Bioquímica Estructural, Sección de Posgrado, ENMyH-IPN | Entrevista PE |

---

# 6 · Decisiones internas, no son para el laboratorio

| Ref | Decisión | Quién |
|-----|----------|-------|
| D-01 | Cómo se crea una cuenta: el cap. 1 dice «registro con aprobación del administrador» y el cap. 4 (RF-07) dice que no existe autoregistro. Hay que elegir uno | Directores |
| D-02 | Identificador de usuario: la boleta no sirve, el Dr. Sandino tiene número de empleado | Directores |
| D-03 | Si reprocesar videos viejos tras reentrenar el clasificador en TT-II. Es motivo del sistema, no del laboratorio, y decide si `Video — Análisis` es (1,1) o (1,N) | Equipo |
| D-04 | Cómo se garantiza que el número de rata no se repita dentro de su grupo, ahora que `idGrupo` no está en `ESPECIMEN`: disparador o redundancia controlada | Equipo |
