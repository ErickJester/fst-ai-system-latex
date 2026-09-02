# Errores e inconsistencias — Capítulo 1: Introducción

**Archivo:** `chapters/01_introduccion.tex`
**Última actualización:** 2026-08-30
**Fuentes de contraste:** entrevista formal (`docs/entrevista_sandino.docx`), respuestas directas del equipo, transcripción informal (`../fuentes/transcripcion_01_no-formal.md`)

> Ver [../README.md](../README.md) para la jerarquía de fuentes y la escala de severidad.

**Resumen:** 5 altas · 5 medias · 2 bajas

---

## E01-01 — Tiempo de anotación manual inflado 4× 🔴

**Severidad:** Alta · **Ubicación:** `:101`, `:211` · **Fuente:** entrevista P12 · **Estado:** Pendiente
**Transversal:** T-03

**Dice el LaTeX (Planteamiento del problema):**
> «Anotar el video de 5 minutos de **un espécimen** —cronómetro en mano, observando la grabación cuadro a cuadro— lleva entre una hora y media y dos horas.»

**Dice la entrevista (P12):**
> «Para un video de 5 minutos con 4 ratas, el análisis manual tarda alrededor de **30 minutos por rata** (se repasa el video tres veces, una por conducta). Con 4 ratas, **un solo video toma aproximadamente 2 horas en total**.»

**Corrección:** la cifra de 2 h es **por video de la tanda completa**, no por espécimen. Por espécimen son ~30 min.

**Por qué importa:** el documento infla el costo unitario por un factor de 4. Es la cifra que sostiene toda la justificación del proyecto, y es exactamente el número que un jurado pide desglosar. Además `front/resumen.tex` tiene la versión correcta («por video»), lo que hace que el resumen contradiga al capítulo.

**Dato que falta recoger:** la anotación manual requiere **tres pases del video, uno por conducta**. Eso explica el costo y refuerza el argumento.

**Confirmación explícita (transcripción informal, rango 3, minuto 10:56–11:35):** el Dr.
Sandino describe el mecanismo sin ambigüedad — «es rata por rata… en su computadora cada uno
lleva su video y analiza una rata a la vez… por cada rata nos tardamos cerca de 30 minutos…
en un video que tiene cuatro ratas nos tardamos como 2 horas» —, y lo hacen «por triplicado».
Esto ya no es una reconstrucción a partir de cifras sueltas: confirma que el costo real por
video es **3 analistas × 2 h = 6 horas-persona**, cada uno trabajando en paralelo sobre su
propia copia del video, rata por rata.

---

## E01-02 — «Cada experimento graba cuatro ratas al mismo tiempo» 🔴

**Severidad:** Alta · **Ubicación:** `:95` · **Fuente:** entrevista P19, respuesta directa del equipo · **Estado:** Pendiente
**Transversal:** T-01, T-02

**Dice el LaTeX (Planteamiento del problema):**
> «Cada experimento graba cuatro ratas al mismo tiempo desde una vista lateral, en dos sesiones: 20 minutos el primer día y 5 minutos el segundo.»

**Dos errores en una sola frase:**

1. **«experimento» debería ser «tanda»** o «corrida». Un experimento, según la entrevista P19, tiene 32 a 48 especímenes repartidos en 4 a 6 grupos y genera unos 8 videos. Lo que graba un conjunto de ratas a la vez es la tanda, no el experimento.
2. **«cuatro ratas» es incorrecto como constante.** Respuesta directa del equipo: «los videos pueden mostrar menos o más cilindros pero siempre más de dos» y «lo máximo que se verá a cuadro son 4 cilindros». El dominio es `n ∈ {3, 4}`: cuatro es el tope, no el valor.

**Corrección propuesta:**
> «Cada tanda graba entre tres y cuatro especímenes al mismo tiempo desde una vista lateral, en dos sesiones: 20 minutos el primer día y 5 minutos el segundo.»

---

## E01-03 — «los cuatro cilindros» / «hasta cuatro ratas» 🔴

**Severidad:** Alta · **Ubicación:** `:165`, `:247`, `:254` · **Fuente:** respuesta directa del equipo · **Estado:** Pendiente
**Transversal:** T-02

Tres ocurrencias que fijan el número en cuatro:

| Línea | Sección | Dice |
|-------|---------|------|
| `:165` | Propuesta de solución | «vista lateral con los cuatro cilindros visibles» |
| `:247` | Alcance · incluido | «con los cuatro cilindros visibles simultáneamente en el encuadre» |
| `:254` | Alcance · incluido | «identificación automática de hasta cuatro ratas dentro de la grabación» |

**Corrección:** «todos los cilindros de la tanda» / «entre tres y cuatro especímenes».

**Por qué importa:** el máximo de cuatro es correcto; el error es tratarlo como **constante**. El sistema debe aceptar grabaciones de tres cilindros, y hoy el documento las excluye por redacción. Donde esto deja de ser cosmético es en la regla de negocio que hace depender de ello la condición de fallo del pipeline: «si la confianza de detección de los cuatro cilindros no alcanza 0.70…» no se satisface nunca en un video de tres.

**Nota:** la línea `:280` («hasta cuatro análisis en un mismo período») **no** es este error — se refiere a la concurrencia de usuarios y es correcta según la entrevista P14.

---

## E01-04 — «Experimento» significa dos cosas dentro del mismo capítulo 🔴

**Severidad:** Alta · **Ubicación:** `:59` contra `:95` · **Fuente:** entrevista P19, PA · **Estado:** Pendiente
**Transversal:** T-01

Las dos frases están a 36 líneas de distancia y usan la misma palabra para cosas distintas:

| Línea | Dice | Cuántas ratas |
|-------|------|---------------|
| `:59` | «En un **experimento** de FST típico, las ratas se dividen en tres grupos de entre 6 y 8 especímenes cada uno» | 18–24 |
| `:95` | «Cada **experimento** graba cuatro ratas al mismo tiempo» | 4 |

**Confirmación de la entrevista (P19):**
> «Por semestre se realizan entre 3 y 4 experimentos independientes, con promedio de 4 grupos y 32 a 48 especímenes, lo que genera alrededor de 8 videos por experimento.»

**Corrección:** introducir el nivel **Tanda** en el capítulo y usar cada término de forma consistente. Ver T-01 en el README para la jerarquía completa.

---

## E01-05 — La tabla de grupos experimentales fija tres grupos 🟡

**Severidad:** Media · **Ubicación:** `:59`–`:90`, tabla `tab:grupos_experimentales` · **Fuente:** entrevista PA, P19 · **Estado:** Pendiente

**Dice el LaTeX:** tres grupos exactos — Control, Referencia (fluoxetina), Tratamiento experimental.

**Dice la entrevista:**
- **PA:** «Normalmente trabajan con **mínimo tres grupos**»
- **P19:** «con **promedio de 4 grupos**»

**Corrección:** hay tres **tipos** de grupo, pero un experimento tiene 4 o más **grupos**. Un tipo puede repetirse (varias moléculas, varias dosis). La tabla debe presentarse como catálogo de tipos, no como enumeración cerrada.

**Consecuencia para el diseño:** `Grupo` es una **entidad** con atributo `tipo`, no un dominio de tres valores.

**Lo que la tabla sí recoge bien:** según PB, el control no recibe placebo, solo entra al cilindro. Eso hace que `tratamiento` sea un **atributo opcional** del grupo.

---

## E01-06 — «dos evaluadores» contra tres analistas 🟡

**Severidad:** Media · **Ubicación:** `:11`, `:101`, `:211`, `:215` · **Fuente:** entrevista P12 · **Estado:** Pendiente

**Dice el LaTeX:** «dos evaluadores», en cuatro lugares distintos.

**Dice la entrevista (P12):**
> «Además cada analista lo hace de forma independiente, entonces **con 3 analistas** se multiplica ese tiempo.»

**El problema no es solo el número: la aritmética no cierra.** El capítulo afirma «más de 200 horas-persona» por semestre.

| Supuesto | Cuenta | Resultado |
|----------|--------|-----------|
| 2 evaluadores (lo que dice el texto) | 40 videos × 2 h × 2 | 160 h ✗ |
| 3 analistas (lo que dice la entrevista) | 40 videos × 2 h × 3 | 240 h ✓ |

La cifra total de «más de 200 horas-persona» **solo es correcta con 3 analistas**. Con el número que el propio texto declara, no llega.

---

## E01-07 — El desglose por minuto está marcado como opcional 🟡

**Severidad:** Media · **Ubicación:** `:157`, `:267` · **Fuente:** entrevista P9 · **Estado:** Pendiente

**Dice el LaTeX:**
> `:157` — «La salida es el tiempo total por conducta y rata y, **como funcionalidad opcional**, el desglose por minuto.»
> `:267` — «desglose por minuto **como funcionalidad opcional**»

**Dice la entrevista (P9):**
> «**Necesita**: (1) el tiempo total de cada conducta por animal y por sesión; (2) el desglose por minuto de cada conducta, es decir, el porcentaje de nado, escalamiento e inmovilidad en el minuto 1, 2, 3, 4 y 5. **Esto es relevante para la dinámica farmacológica.**»

**Corrección:** el usuario lo enumeró como necesidad y explicó su propósito científico. No es opcional.

**Consecuencia para el diseño:** el desglose por minuto es un conjunto de pleno derecho en el esquema conceptual, no un extra descartable.

---

## E01-08 — Falta el criterio de repetibilidad 🟡

**Severidad:** Media · **Ubicación:** Justificación (`:206`–`:241`) y Alcance · **Fuente:** entrevista P13, P8 · **Estado:** Pendiente
**Transversal:** T-04

**Dice la entrevista (P13):**
> «No tienen mayor problema con el tiempo que tarde el análisis. Lo que más importa es que haya menos variabilidad […] Lo ideal sería que el mismo video analizado múltiples veces arroje siempre el mismo resultado, con una **variabilidad máxima de entre el 5 y el 10 %**.»

**Y P8:**
> «El objetivo principal **no es tanto la velocidad** sino reducir la variabilidad del factor humano.»

**Qué falta:** el capítulo trata el tiempo de procesamiento como criterio de valor («en minutos genera un reporte», y `time behaviour` en la Justificación) y no menciona la repetibilidad. El usuario dijo lo contrario: el tiempo no le preocupa, la variabilidad sí.

**Corrección:** añadir el criterio de repetibilidad (variabilidad ≤ 5–10 % entre corridas del mismo video) y reordenar el énfasis de la Justificación.

---

## E01-09 — Duración mínima de episodio fijada en 3 s sin matizar 🟢

**Severidad:** Baja · **Ubicación:** Alcance, `:262` · **Fuente:** entrevista P6 · **Estado:** Pendiente

**Dice el LaTeX:** «un episodio debe tener una duración mínima de tres segundos consecutivos.»

**Dice la entrevista (P6):** «la conducta debe mantenerse **alrededor de 3 a 5 segundos** para contarse como episodio válido.»

**Corrección:** el dominio real es un intervalo. Tomar 3 s como límite conservador es una decisión válida, pero conviene decir en el cap. 1 que es el extremo inferior de un rango declarado por el laboratorio.

---

## E01-10 — Palabra duplicada 🟢

**Severidad:** Baja · **Ubicación:** `:18`–`:19` · **Estado:** Pendiente

> «los investigadores necesitan **modelos**
> **modelos** preclínicos con roedores que reproduzcan aspectos observables del trastorno.»

Residuo de la sustitución «modelos animales» → «modelos preclínicos con roedores». Eliminar la primera ocurrencia.

---

## E01-12 — Cap. 1 y cap. 4 se contradicen sobre cómo se crea una cuenta 🔴

**Severidad:** Alta · **Ubicación:** `:279` contra `04_analisis.tex:86`–`:92` (RF-07) · **Fuente:** contradicción interna del documento · **Estado:** Pregunta abierta (Q-08)

| Fuente | Dice |
|--------|------|
| **Cap. 1**, Alcance (`:279`) | «interfaz accesible desde el navegador con **registro de usuario con aprobación del administrador**» — implica autoregistro seguido de aprobación |
| **Cap. 4**, RF-07 | «Solo el Administrador puede crear cuentas de usuario. **No existe formulario público de autoregistro.** El Administrador asigna nombre, correo institucional y contraseña temporal» |

Las dos afirmaciones son incompatibles: o hay formulario de autoregistro con aprobación
posterior, o no hay autoregistro en absoluto y el Admin crea las cuentas. No pueden ser ambas.

**La entrevista no lo resuelve.** P1 responde sobre **roles**, no sobre el flujo de alta:
> «Todos los que participan en los proyectos podrían subir sus propios videos. Bastaría con un
> rol de investigador en general; no se necesitan permisos diferenciados entre ellos.»

Y P18 confirma que el acceso a datos es uniforme, pero tampoco dice quién crea las cuentas.

**Rastro probable:** las notas del proyecto (`CLAUDE.md`) registran que RF-07 se resolvió en su
momento como «autoregistro + aprobación admin + notificaciones email», que es exactamente lo
que dice el cap. 1. Después RF-07 se reescribió al texto actual, pero **el cap. 1 se quedó con
la redacción vieja**. Es la hipótesis más simple, aunque conviene confirmarla.

**Consecuencia para el esquema conceptual.** Afecta directamente a la entidad `Usuario`. Si
existe una función de administrador con capacidades propias —aprobar altas, crear cuentas—,
`Usuario` necesita al menos un atributo que la distinga, y posiblemente una especialización.
El esquema actual la modela **plana**, apoyándose en P1 y P18, que hablan de permisos sobre
datos, no de gestión de cuentas. Ver Q-08 en el README.

---

## E01-11 — El acervo histórico queda fuera del sistema, y el Alcance no lo dice 🟡

**Severidad:** Media · **Ubicación:** Alcance · **Fuente:** entrevista P19, PG, respuesta directa del equipo · **Estado:** Pendiente

**Dice la entrevista (P19):**
> «De videos acumulados, tienen aproximadamente **80 a 100 videos desde hace 10-12 años**, todos ya analizados manualmente, que podrían usarse para entrenar y probar el sistema.»

**Y PG:**
> «Están localizando los archivos de Excel donde los alumnos capturaron los análisis manuales **para empatar archivo con video**.»

**Resuelto (respuesta directa del equipo, 2026-08-30):** «Quedan por fuera.» El acervo histórico
**no** se carga al sistema como experimentos regulares — se usa únicamente por fuera, como
material de entrenamiento y de conjunto de prueba para el clasificador. Sube de baja a media
porque ahora es una decisión de alcance tomada y confirmada, no una laguna sin resolver, y el
documento debe declararla explícitamente: un jurado puede preguntar directamente qué pasa con
esos 80–100 videos, y hoy el Alcance no lo contesta en ningún sentido.

**Corrección:** añadir un bullet en «Fuera del alcance» (cap. 1) del estilo: «Carga masiva del
acervo histórico: los 80 a 100 videos ya analizados manualmente que el laboratorio acumula
desde hace 10 a 12 años no se cargan al sistema como experimentos. Se usan exclusivamente,
fuera de la plataforma, como material de entrenamiento y de conjunto de prueba para el
clasificador.»

**Nota:** «empatar archivo con video» sigue siendo trabajo real —de anotación y correspondencia
entre los Excel históricos y sus videos—, pero ahora queda claro que es trabajo **externo al
sistema**, del lado del entrenamiento del modelo, no una funcionalidad de la plataforma web.
