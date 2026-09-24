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

## Q-E · Comparación de grupos: ¿suma o promedio? ⚪

**Por qué se pregunta.** Al comparar el grupo control contra el grupo tratamiento en el Día 2
(ver §5 "Qué se compara"), hay que combinar los segundos por conducta de todos los especímenes
de cada grupo en un solo número. El tamaño de grupo no tiene tope en el sistema (§5 "Tamaño de
grupo") — si un grupo tiene más ratas que otro, sumar todos sus segundos hace que el grupo más
grande se vea con más "actividad" aunque el comportamiento promedio por rata sea igual.

**Qué preguntar:** ¿el laboratorio compara los grupos por el total acumulado de todas sus ratas,
o por el promedio por rata?

**Decisión provisional, mientras se confirma:** promedio por espécimen, para que el tamaño del
grupo no distorsione la comparación. Usado así en `diagramas/seq_consulta_resultados.puml`.

## Q-F · Grupo con especímenes en distinto nivel de clasificación ⚪

**Por qué se pregunta.** El clasificador reporta tres conductas por separado ("preciso") o, si no
alcanza 85% de F1 distinguiendo nado activo de escalamiento, las junta en "conducta activa"
("agrupado", ver RN-13, cap. 4). Si dentro de un mismo grupo unos especímenes salen "preciso" y
otros "agrupado" —por ejemplo, si el clasificador se reentrena a la mitad de una tanda de
análisis—, sumarlos sin avisar mezclaría categorías que no significan lo mismo.

**Qué preguntar:** ¿le sirve al laboratorio ver esos especímenes separados por su nivel de
clasificación cuando esto pase, o prefiere que el sistema fuerce todo al nivel "agrupado" para
poder comparar sin advertencias?

**Decisión provisional, mientras se confirma:** mostrarlos separados por nivel, con aviso, en vez
de forzar una conversión. Usado así en `diagramas/seq_consulta_resultados.puml`.

## Q-G · ¿Todo o nada si no detecta los 4 cilindros? ⚪

**Por qué se pregunta.** El cap. 5 (`chapters/05_diseno.tex:225-232`, "Separación por
espécimen") describe que si el sistema detecta menos cilindros de los esperados, reporta cuáles
especímenes pudo procesar y cuáles no, **en vez de** abortar el análisis completo. Pero esto es
del capítulo 5 (fuente de menor autoridad) y nunca se validó con el laboratorio ni en la reunión
del 3-sep — y choca con RN-11 (cap. 4, rango más alto), que sí describe un pipeline todo-o-nada:
si la confianza de detección de los cuatro cilindros no alcanza 0.70, se detiene el análisis
completo.

**Qué preguntar:** si el sistema no logra detectar los cuatro cilindros esperados en un video,
¿le sirve al laboratorio ver los resultados de los especímenes que sí se procesaron, o prefiere
que el análisis completo se marque como error y no se genere ningún resultado parcial?

**Decisión provisional, mientras se confirma (equipo, 2026-09-13):** todo o nada, siguiendo
RN-11 — no hay procesamiento parcial. Si no se detectan los cuatro cilindros con confianza
suficiente, el análisis completo se marca como `error`, igual que si la confianza general no
alcanzara 0.70. El comportamiento de "reporta cuáles pudo procesar" del cap. 5 **no se
implementa** mientras no se confirme con el doctor. Usado así en
`diagramas/seq_analisis_automatico.puml`.

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
| D-01 | ~~Cómo se crea una cuenta: el cap. 1 dice «registro con aprobación del administrador» y el cap. 4 (RF-07) dice que no existe autoregistro~~ **Resuelto (equipo, 2026-09-13):** solo el Administrador crea cuentas, sin autoregistro. El cap. 1 queda mal (hay que corregirlo al RF-07) | Equipo |
| D-02 | ~~Identificador de usuario: la boleta no sirve, el Dr. Sandino tiene número de empleado~~ **Resuelto (equipo, 2026-09-12):** identificador institucional único, un solo campo que acepta boleta (estudiantes) o número de empleado (personal). Falta afinar la regla que distingue cuál es cuál al validar — detalle menor, no bloquea. **Longitud (equipo, 2026-09-13):** `varchar(10)` | Equipo |
| D-03 | ~~Si reprocesar videos viejos tras reentrenar el clasificador en TT-II. Es motivo del sistema, no del laboratorio, y decide si `Video — Análisis` es (1,1) o (1,N)~~ **Resuelto (equipo, 2026-09-13):** se reemplaza. Un video tiene como mucho un análisis vigente — al reanalizar, el resultado nuevo sustituye al anterior, no se conserva historial. `VIDEO — ANALISIS` queda en (1,1), no en (1,N). Pendiente de aplicar en `diagramas/grafo_relacional_reconciliado.puml` (hoy dice `"1" --o "1..*"`) | Equipo |
| D-05 | ~~¿El sistema permite correr dos veces la misma `CONFIGURACION` sobre el mismo video? Decide si `(idVideo, idConfig)` es clave alterna de `ANALISIS`~~ **Se disolvió sola (2026-09-13) al resolver D-03:** con reanálisis que reemplaza, un video nunca tiene más de un `ANALISIS` a la vez, así que no puede haber una segunda fila que compita con la primera — la pregunta deja de aplicar | Equipo |
| D-06 | ~~El pipeline usa más de un modelo (YOLOv8 + ResNet-18/50), pero `CONFIGURACION` solo guarda un `hashModelo` — ¿`MODELO`↔`CONFIGURACION` debe ser N:M en vez de 1:N?~~ **Resuelto (equipo, 2026-09-13):** no cambia, se queda en 1:N. Lo que importa registrar no es la combinación exacta de modelos que se usó, sino las métricas de resultado (F1, precisión, recall) que esa combinación produjo — eso ya se captura en el reporte, no hace falta la relación N:M para lograrlo | Equipo |
| D-04 | ~~Cómo se garantiza que el número de rata no se repita dentro de su grupo, ahora que `idGrupo` no está en `ESPECIMEN`: disparador o redundancia controlada~~ **Resuelto (equipo, 2026-09-13):** redundancia controlada. Se repone `ESPECIMEN.idGrupo` (derivable vía `TANDA`, pero se guarda de todas formas) y se declara `UNIQUE (idGrupo, numeroRata)`. Motivo doble: (1) permite declarar la regla directamente en vez de con disparador, y (2) los reportes necesitan consultar "todas las ratas del grupo X" todo el tiempo para comparar grupos entre sí, y sin `idGrupo` en la tabla cada consulta tendría que pasar por `TANDA`. **Esto es una decisión de la etapa física, no toca el grafo relacional lógico** (`grafo_relacional_reconciliado.puml` se queda en BCNF estricta, sin `idGrupo` en `ESPECIMEN`) — la redundancia se declara solo en el esquema físico/DDL, que es donde el método (Cardona, actividad 5 de diseño físico) la permite. **Sincronización resuelta (equipo, 2026-09-13):** disparador `BEFORE INSERT OR UPDATE OF idTanda` que recalcula `idGrupo` a partir de `TANDA` antes de guardar la fila — la aplicación no necesita mandar `idGrupo`, la base de datos lo calcula sola, así que nunca queda una versión vieja pegada | Equipo |
| D-07 | **Idea sin decidir, dos partes.** (a) Que el usuario dibuje el recuadro sobre las 4 ratas antes del análisis, en vez de que el pipeline lo detecte solo (Módulo 2, "Detección de ROIs"). (b) Que el usuario también pueda ajustar a mano la **línea de agua** (waterline) de cada cilindro, en vez de que el filtro EMA la estime sola (mismo Módulo 2). Las dos son correcciones manuales al mismo módulo. De confirmarse cualquiera de las dos: `ROI` deja de ser 100% derivado (revierte `CAMBIOS-CAP5.md` §E); el Módulo 2 de `chapters/05_diseno.tex:127`–`134` deja de describir detección automática; el diagrama del pipeline (`docs/diagramas.pdf` pág. 3) y los métodos de `PipelineAnalisis` en `diagramas/clases.puml` necesitarían rehacerse. **No aplicar todavía**, son solo ideas | Equipo |
| D-08 | ~~`USUARIO` no distingue Investigador de Administrador~~ **Resuelto (equipo, 2026-09-13):** Administrador **no es un tipo de usuario separado** — es un Investigador con permisos extra (el Dr. Sandino es los dos a la vez). Se modela como **subtipo/generalización**: tabla `ADMINISTRADOR(idInstitucional*)` en relación (1,1)–(0,1) con `USUARIO` — si el usuario no aparece ahí, es investigador simple. Respaldado por Kendall & Kendall p. 405 ("subtipo de entidad") y Cardona ("generalización/especialización"). En `diagramas/clases.puml`, `Investigador` se fusionó con `Usuario` (ya no es abstracta) y `Administrador` hereda de `Usuario`. Ya ejecutado: `ADMINISTRADOR(idInstitucional* [FK])` agregado a `grafo_relacional_reconciliado.puml` en relación `USUARIO "1" --o "0..1" ADMINISTRADOR` — pasa de 15 a 16 relaciones, 73 atributos, 17 llaves foráneas | Equipo |
| D-09 | ~~`ANALISIS` sin columnas de seguimiento de progreso~~ **Resuelto (equipo, 2026-09-13):** el progreso vive **solo en memoria** de `Worker`/`PipelineAnalisis` mientras corre — no se persiste. `ANALISIS` se queda tal cual en el grafo reconciliado, **sin cambio de esquema**. Si el sistema se reinicia a medio análisis, el progreso se pierde (a diferencia de D-08, esto no agrega ninguna relación). En `diagramas/clases.puml`, `actualizarProgreso()` y `marcarError()` se agregaron a `PipelineAnalisis`, no a `Analisis` | Equipo |
| D-10 | ~~`USUARIO` sin columna `activo`~~ **Resuelto (equipo, 2026-09-13):** se agrega `activo : Boolean` a `USUARIO`. Justificación con los dos libros: Kendall & Kendall (p. 425-426) nombra esto **anomalía de eliminación** — "se elimina un registro y como resultado se pierden otros datos relacionados", exactamente el caso de borrar un usuario con experimentos. Cardona et al., Apéndice A (p. 117-118, esquema físico ya normalizado), declara **todas** sus llaves foráneas con `ON DELETE NO ACTION` — aplicado a `EXPERIMENTO.idBoleta → USUARIO`, la BD directamente **rechazaría** borrar a un usuario con algún experimento. `activo` evita que el `DELETE` sea siquiera necesario. Ya aplicado en `diagramas/clases.puml`, `grafo_relacional_final.puml` y `grafo_relacional_reconciliado.puml` — `Administrador.desactivarCuentaUsuario()` de vuelta en el diagrama de clases | Equipo |
| D-11 | ~~Qué SGBD usar (actividad 1 de la etapa de diseño físico, Cardona §1.4.4)~~ **Resuelto (equipo, 2026-09-13):** **PostgreSQL**. El cap. 3 del TT ya lo mencionaba, pero esto lo confirma como decisión de equipo, no solo texto del documento. Motivo, específico al proyecto y no copiado del libro: los reportes comparan grupos (control/fluoxetina/tratamiento) sobre datos de `OBSERVACION`/`INTERVALO`/`PRESENTA` — series por minuto por espécimen —, y ahí PostgreSQL tiene mejor soporte de funciones de ventana y agregación que MySQL. Además `CONFIGURACION` guarda umbrales que definen cómo se generó cada análisis (importante para poder comparar corridas en TT-II); PostgreSQL rechaza valores inválidos por defecto de forma más estricta que MySQL, que por default trunca en vez de rechazar salvo modo estricto activado. **Pendiente de ejecutar:** falta actividad física 2 (representar el esquema lógico en DDL real de PostgreSQL) | Equipo |
| D-12 | ~~Contradicción de la actividad 4 de diseño físico: la etapa lógica cerró con «una sola vista, sin permisos diferenciados», pero D-08 le da al Administrador cuatro métodos que un Investigador no tiene~~ **Resuelto (equipo, 2026-09-13):** sí hay una vista diferenciada. Misma aplicación, mismo login — a un `Administrador` le aparece una pestaña/sección adicional que a un `Investigador` no le aparece, y ahí es donde ejecuta `crearCuentaUsuario`, `desactivarCuentaUsuario`, `listarUsuarios` y `monitorearSistema`. El control vive **en la aplicación** (no en roles separados de PostgreSQL) y es doble: (1) esa sección **se oculta** de la interfaz si el usuario no está en `ADMINISTRADOR`, y (2) el sistema **verifica el rol antes de ejecutar** cualquiera de esas cuatro acciones, sin importar por dónde llegue la petición — no basta con esconder el botón, porque alguien podría invocar la acción directamente sin pasar por la pantalla | Equipo |
| D-13 | ~~Si la restricción «sin acceso» de la actividad 5 lógica (cualquier investigador consulta los experimentos de cualquier otro) sigue vigente ahora que se está hablando de permisos~~ **Resuelto (equipo, 2026-09-13):** sigue vigente, y ahora con motivo explícito: los investigadores necesitan ver los experimentos de los demás **para poder comparar sus resultados** entre sí. Es una restricción distinta e independiente de D-12 — esta es entre investigadores, D-12 es investigador contra administrador | Equipo |
| D-14 | ~~Con qué función se calcula `MODELO.hashModelo` — no está en ningún `.tex`, ni siquiera el cap. 5 (fuente de menor autoridad) lo menciona~~ **Resuelto (equipo, 2026-09-13):** **SHA-256**. Se usa `hashlib.sha256(archivo).hexdigest()` de Python sobre el archivo del modelo entrenado, sin necesidad de implementar nada propio. Columna `char(64)` — es la longitud fija del código que produce SHA-256 al escribirlo en el formato usual (letras y números). No confundir con el hash de contraseñas, que ya usa `bcrypt` (documentado en cap. 4 RNF-05 y cap. 5) | Equipo |
| D-15 | ~~`ANALISIS.estado` documentado con solo 3 valores (`en proceso`, `completado`, `error`, cap. 4) — ¿falta un cuarto para representar la espera en la cola?~~ **Resuelto (equipo, 2026-09-13):** sí, son **4 valores**: `en cola`, `procesando`, `completado`, `error`. Respaldado por requisitos ya escritos que nadie había cruzado con este dominio: el cap. 1 pide «cola de procesamiento secuencial para hasta cuatro análisis en un mismo período», el cap. 3 describe el patrón asíncrono («el backend encola la tarea... un Worker independiente toma la tarea de la cola»), y el cap. 5 —en la tabla `TRABAJOS` del modelo viejo— ya había escrito el estado completo como `en_cola, procesando, completado, error`. Sin el cuarto valor, un análisis recién pedido pero que el Worker todavía no toca no tiene forma correcta de representarse. Nombres elegidos: `en cola` (sin guion bajo, para que combine en estilo con los otros tres) en vez de `pendiente` (más genérico, se presta a confundirse con otras cosas pendientes del sistema); y `procesando` en vez de `en proceso` — cambiado por el equipo el 13-sep, coincide exactamente con como ya lo escribió el cap. 5 | Equipo |
| D-16 | ~~`ANALISIS.etapa` — son cuatro etapas del pipeline, pero sus nombres no estaban confirmados como dominio~~ **Resuelto (equipo, 2026-09-13):** `preprocesamiento`, `deteccion`, `seguimiento`, `clasificacion`. El cap. 4 (RF, rango más alto que el cap. 5) ya las nombraba como requisito: «el pipeline de análisis debe ejecutar cuatro etapas secuenciales: preprocesamiento del video..., detección de cilindros, seguimiento de ratas (*tracking*) y clasificación de conductas». El cap. 5 las repite como Módulo 1–4. Se acortaron los calificativos («de cilindros», «de conducta») para que el dominio quede tan corto como los demás ya escritos. Inconsistencia menor detectada y no arrastrada: el paso a paso del CU-07 le dice «rastreo» a la etapa 3 en vez de «seguimiento» — se tomó el nombre que domina en el resto del documento | Equipo |
| D-17 | ~~`ANALISIS.nivelClasif` — sin ningún valor documentado en ningún `.tex`~~ **Resuelto (equipo, 2026-09-13):** dos valores, `preciso` y `agrupado`. El motivo sí está documentado, aunque el nombre no: RN-13 (cap. 4) dice que si el clasificador no alcanza F1 ≥ 85 % distinguiendo las tres conductas por separado (nado activo, inmovilidad, escalamiento), el sistema junta nado activo y escalamiento en una sola categoría («conducta activa») y reporta solo dos. El reporte debe indicar «explícitamente qué nivel de clasificación se aplicó» (cap. 4), pero el documento nunca le puso nombre a los dos lados de esa regla — los nombres son de esta decisión, no del `.tex` | Equipo |
| D-18 | ~~Política de respaldo de la base de datos — no está en ningún `.tex`, a diferencia de la política de retención de videos (RNF-08/RNF-09), que sí lo está~~ **Resuelto (equipo, 2026-09-13):** respaldo automático diario con `pg_dump`, conservando los últimos 7 días. Es distinto del borrado de videos a 30 días (RNF-08): eso es sobre archivos de video, esto es sobre la base de datos completa (experimentos, resultados, cuentas) | Equipo |
| D-20 | ~~¿Qué pasa si el pipeline no detecta los cuatro cilindros esperados: procesar parcial (cap. 5, `05_diseno.tex:225-232`) o marcar error completo (RN-11)?~~ **Resuelto, provisional (equipo, 2026-09-13):** todo o nada, siguiendo RN-11. Si no se detectan los cuatro cilindros con confianza suficiente, el análisis completo se marca `error` — no hay estado intermedio ni resultado parcial. El comportamiento de "reporta cuáles especímenes pudo procesar" que describe el cap. 5 no se implementa; ese capítulo es de menor autoridad y esa parte nunca se validó con el laboratorio. Ver Q-G, pendiente de confirmar. Aplicado en `diagramas/seq_analisis_automatico.puml` | Equipo |
| D-23 | ~~CU-08 dice que el Worker genera un PDF de diagnóstico cuando un análisis falla, y que el sistema lo sirve al investigador — pero `ANALISIS` no tiene ninguna columna para guardar la ruta de ese archivo (ni `REPORTE`, que solo se relaciona con `EXPERIMENTO`, no con un análisis en particular)~~ **Resuelto (equipo, 2026-09-13):** columna nueva, `ANALISIS.rutaDiagnostico`, nula salvo cuando `estado = 'error'`. Mismo patrón que `VIDEO.archivo`. **Pendiente de aplicar** en `diagramas/grafo_relacional_reconciliado.puml` — no se toca hasta que se pida explícitamente. Usado ya en `diagramas/seq_consulta_progreso.puml` (fusionado ahí, no tiene archivo propio — ver nota en ese `.puml` sobre por qué CU-08 no amerita diagrama aparte, según Kendall & Kendall) | Equipo |
| D-22 | ~~RF-15 pide barra de **porcentaje** en tiempo real, pero D-09 dice que el progreso vive solo en memoria del Worker y no se persiste — `ANALISIS` no tiene columna de porcentaje. ¿De dónde saca el porcentaje el backend que atiende el polling del frontend?~~ **Resuelto (equipo, 2026-09-13):** se aproxima por etapa, no se persigue precisión fina. Cada una de las 4 etapas de D-16 vale 25% fijo (preprocesamiento=25%, detección=50%, seguimiento=75%, clasificación=100%), calculado al vuelo a partir de `ANALISIS.etapa` en cada consulta — no hace falta que el Worker comparta memoria con el backend ni ningún canal adicional. Aplicado en `diagramas/seq_consulta_progreso.puml` | Equipo |
| D-21 | ~~`REPORTE` cachea el archivo generado (`ruta` es AK, CU-10 dice "genera o recupera") — pero si el experimento se reanaliza después de generar un reporte (D-03, reemplaza resultados), ¿el reporte cacheado se sigue sirviendo tal cual, o se regenera?~~ **Resuelto (equipo, 2026-09-13):** se invalida solo si hubo reanálisis. Al pedir la descarga, el sistema compara `REPORTE.fechaGeneracion` contra la fecha del análisis más reciente del experimento (`ANALISIS.fechaAnalisis`, vía sus videos); si hay un análisis más nuevo que el reporte guardado, lo regenera y reemplaza `ruta`; si no, reusa el archivo existente. Evita servir un reporte con datos que ya no reflejan un reanálisis, sin regenerar en cada descarga cuando nada cambió | Equipo |
| D-19 | ~~Cómo infiere el sistema la Tanda al subir un video — para el diagrama de secuencia de carga de video (`MIGRACION-DIAGRAMAS.md` §3.4), sin fuente previa~~ **Resuelto (equipo, 2026-09-13):** al subir un video, el investigador escribe el nombre del grupo/tratamiento con autocompletado. Si el nombre coincide con un grupo **del mismo experimento** ya usado antes, el sistema infiere que es la siguiente tanda de ese grupo y pre-llena el campo de tanda (letra `A`, `B`, `C`... en la interfaz — sigue siendo `TANDA.ordinal` entero en la base de datos). El campo es editable, pero además el sistema pide una **confirmación explícita** ("¿esta es la tanda B de [grupo]?") antes de guardar — no basta con dejar el valor pre-llenado sin que el investigador lo confirme, porque una tanda mal asignada contamina la comparación entre grupos sin que se note. La coincidencia de nombre se busca **solo dentro del experimento actual**, nunca en todo el sistema, para no cruzar grupos de experimentos distintos que compartan el mismo nombre de tratamiento (p. ej. "fluoxetina" como referencia se repite entre experimentos) | Equipo |

| D-24 | ~~`ANALISIS.idVideo` tiene cardinalidad (1,1) declarada en `grafo_relacional_reconciliado.puml` (D-03), pero la columna no lleva `[AK]` — la regla "un video, un análisis vigente" no está forzada por ninguna restricción, solo por convención de la aplicación~~ **Resuelto (equipo, 2026-09-15):** se declara `UNIQUE (idVideo)` en `ANALISIS`. Respaldado por Kendall & Kendall, cap. 13 "Diseño de bases de datos", p. 425 (sección "Restricciones de integridad"): el libro reconoce la "clave única" como herramienta de integridad de entidad para forzar unicidad en una columna que no es la llave primaria. Aplica el principio general de la etapa física: una regla de negocio ya decidida en la lógica (D-03) se traduce a una restricción real del gestor, no se deja dependiendo de que la aplicación siempre borre antes de insertar. **Consecuencia sobre la actividad 3 del artifact "Diseño Físico FST":** `ANALISIS.idVideo` pasa de la columna "8 · hay que declarar el índice" a la de "9 · ya queda indexada" (UNIQUE crea su índice solo) — ese artifact queda en 8/9 y no en 9/8. **Pendiente de aplicar** ahí — no se toca hasta que se pida explícitamente | Equipo |

| D-25 | ~~RF-05/RF-07 y CU-12 dicen que el sistema obliga a cambiar la contraseña temporal en el primer ingreso, pero ni `clases.puml` ni `grafo_relacional_reconciliado.puml` tienen columna para guardar ese estado — `USUARIO` solo tiene `activo`. El esquema físico viejo sí traía `debe_cambiar_contrasena`, se perdió en el rediseño sin registrarse~~ **Resuelto (equipo, 2026-09-15):** se agrega `USUARIO.cambioRequerido : boolean`. Mismo patrón que `activo` (D-10): la regla se declara en la base de datos en vez de vivir solo en el código. Se descartó inferirlo por fechas (comparar creación contra último cambio de contraseña) porque exigiría una columna nueva de todas formas, con lógica más frágil. **Aplicado** en `grafo_relacional_reconciliado.puml`, `clases.puml` y `esquema_fisico.puml` — los tres vigentes. No se tocó `grafo_relacional_inicial.puml`, `grafo_relacional_final.puml` ni `relacional.puml`: son fotos históricas del método (el "antes" y el "después" de la validación de la etapa lógica), no se actualizan con decisiones posteriores | Equipo |

> **Fundamento de D-08, verificado en los dos libros (15-sep):**
> - Kendall & Kendall, *Análisis y Diseño de Sistemas*, cap. 13 "Diseño de bases de
>   datos", p. 405, define **subtipo de entidad**: "una relación especial de uno a uno
>   empleada para representar los atributos adicionales de otra entidad que tal vez no
>   estén presentes en todos los registros... elimina la situación en la que una entidad
>   puede tener campos nulos". En su notación conceptual se dibuja como un rectángulo más
>   pequeño *anidado dentro* del rectángulo de la entidad — no como tabla aparte; esa
>   notación es de la etapa conceptual, y `ADMINISTRADOR` no está dibujado en
>   `diagramas/esquema_conceptual.tex` todavía, solo en lógico/físico.
> - Cardona, *Diseño e implementación de bases de datos desde una perspectiva práctica*,
>   sección 2.5.2 "Generalización", pp. 35-37: **"las cardinalidades mínimas y máximas
>   siempre son (1,1) en el supertipo y (0,1) en los subtipos"** — cita textual, coincide
>   exacto con `USUARIO (1,1) — (0,1) ADMINISTRADOR`. La Figura 2.34 del libro usa
>   "administrador" como ejemplo de subtipo (con "persona" y "director"), aunque no es tu
>   caso exacto. Nota: los 4 patrones con nombre del libro (parcial/total ×
>   exclusiva/solapada) están pensados para 2+ subtipos hermanos; con un solo subtipo
>   (tu caso) ese eje no aplica, solo la regla general de cardinalidad.
> - Lo que no se pudo verificar: el símbolo gráfico exacto de Cardona para la
>   generalización (está en figuras/imágenes del PDF, sin lector de páginas disponible
>   en este entorno).
