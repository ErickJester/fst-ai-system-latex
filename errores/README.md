# Catálogo de errores e inconsistencias — TT 2026-B066

Registro de contradicciones, imprecisiones y omisiones detectadas en el documento
LaTeX al contrastarlo contra las fuentes primarias del laboratorio.

**Última actualización:** 2026-08-30

---

## Jerarquía de fuentes de verdad

Cuando dos fuentes se contradicen, gana la de mayor rango. El documento LaTeX es
la fuente de **menor** autoridad: es el destino de las correcciones, no el árbitro.

| Rango | Fuente | Ubicación |
|-------|--------|-----------|
| 1 | Respuestas directas del equipo en sesión de trabajo | Registradas en este catálogo |
| 2 | Entrevista formal con el Dr. Sandino | `docs/entrevista_sandino.docx` |
| 3 | Transcripciones de reuniones informales | [`fuentes/transcripcion_01_no-formal.md`](fuentes/transcripcion_01_no-formal.md) |
| 4 | Retroalimentación de la simulación de defensa | `CLAUDE.md`, `docs/Retroalimentacion_*.docx` |
| 5 | Documento LaTeX | `chapters/`, `front/` |

> **Regla:** ninguna corrección se aplica al LaTeX sin que exista una fuente de rango
> superior que la respalde. Si no hay fuente, se registra como *pregunta abierta*, no
> como error.

## Documentos de trabajo

| Documento | Para qué sirve |
|-----------|----------------|
| [**preguntas-doctor.md**](preguntas-doctor.md) | Material para la próxima reunión con el Dr. Sandino: conceptos a validar, preguntas abiertas, datos nuevos y lo ya respondido. De ahí se formulan las preguntas de cada reunión |
| [fuentes/](fuentes/) | Transcripciones y fuentes primarias incorporadas al catálogo |

---

## Escala de severidad

| Nivel | Criterio |
|-------|----------|
| 🔴 **Alta** | Contradice una fuente primaria, o el documento se contradice a sí mismo en un hecho verificable. Afecta el diseño del sistema o la defensa. |
| 🟡 **Media** | Imprecisión, omisión de un dato que la fuente primaria sí declara, o inconsistencia de criterio. No invalida el diseño pero debilita el documento. |
| 🟢 **Baja** | Error de redacción, duplicación, typo o referencia cruzada rota. |

## Estados

`Pendiente` · `En revisión` · `Corregido` · `Descartado` · `Pregunta abierta`

---

## Índice

| Capítulo | Archivo | 🔴 | 🟡 | 🟢 | Total |
|----------|---------|----|----|----|-------|
| 1 · Introducción | [01_introduccion/errores.md](01_introduccion/errores.md) | 5 | 5 | 2 | 12 |
| 2 · Estado del arte | [02_estado_arte/errores.md](02_estado_arte/errores.md) | 0 | 2 | 3 | 5 |
| 3 · Marco teórico | [03_marco_teorico/errores.md](03_marco_teorico/errores.md) | 4 | 4 | 0 | 8 |
| 4 · Análisis | [04_analisis/errores.md](04_analisis/errores.md) | 4 | 3 | 0 | 7 |
| 5 · Diseño | [05_diseno/errores.md](05_diseno/errores.md) | — | — | — | *sin revisar* |
| 6 · Desarrollo | [06_desarrollo/errores.md](06_desarrollo/errores.md) | — | — | — | *sin revisar* |
| 7 · Pruebas y resultados | [07_pruebas_resultados/errores.md](07_pruebas_resultados/errores.md) | — | — | — | *sin revisar* |
| 8 · Conclusiones | [08_conclusiones/errores.md](08_conclusiones/errores.md) | — | — | — | *sin revisar* |
| Preliminares | [front/errores.md](front/errores.md) | 0 | 2 | 0 | 2 |

---

## Hallazgos transversales

Seis problemas atraviesan varios capítulos (uno ya resuelto, se conserva para trazabilidad).
Corregir uno sin los demás deja el documento inconsistente.

### T-01 · «Experimento» tiene dos significados incompatibles 🔴

El documento usa la misma palabra para el estudio completo (3 o más grupos, 32 a 48
especímenes) y para una sola grabación (unos pocos especímenes, uno o dos videos).
Falta un nivel intermedio en la jerarquía.

**Jerarquía correcta, derivada de la entrevista P19 y PA:**

```
Experimento            estudio independiente · 3–4 por semestre
  └── Grupo            4–6 por experimento · 6–8 especímenes
                       tipo ∈ {control, referencia, tratamiento experimental}
        └── Tanda      2 por grupo · especímenes grabados juntos · n ∈ {3, 4}
              ├── Espécimen   n por tanda · identificado por posición del cilindro
              └── Video       1 o 2 · Día 1 (20 min) y/o Día 2 (5 min)
```

Comprobación con las cifras de P19: 4 grupos × 8 especímenes = 32 especímenes; 8 especímenes ÷ 4
por cuadro = 2 tandas por grupo; 4 grupos × 2 tandas = **8 videos de Día 2**, que es la cifra que
el investigador reporta por experimento.

Afecta: cap. 1, cap. 3, cap. 4.

### T-02 · El número de cilindros no es cuatro 🔴

**Respuesta directa del equipo (2026-08-29):**
> «Los videos pueden mostrar menos o más cilindros pero siempre más de dos. En ambos días
> siempre serán el mismo número de cilindros al de su respectivo día anterior.»
>
> «Lo máximo que se verá a cuadro son 4 cilindros.»

El dominio correcto es **n ∈ {3, 4}**, variable. El error del documento no es el valor máximo
—cuatro es correcto— sino tratarlo como **constante** en lugar de como tope de un rango.

**Consecuencia estructural.** Con 6 a 8 especímenes por grupo (entrevista PA) y máximo 4 por
cuadro, **un grupo no cabe en una sola grabación**: ocupa dos tandas. Eso confirma que Tanda es
un nivel propio de la jerarquía y no un sinónimo de Grupo.

Afecta: cap. 1 (4 ocurrencias), cap. 3 (1), cap. 4 (3).

### T-03 · El tiempo de anotación manual está inflado 🔴

Entrevista P12: **~30 min por rata**, **~2 h por video completo**, con **3 analistas**
independientes. El cap. 1 atribuye las 2 h a un solo espécimen y habla de 2 evaluadores.

`front/resumen.tex` tiene la cifra correcta («por video»), lo que hace que el resumen
y el cap. 1 se contradigan entre sí.

**Confirmación (transcripción informal, rango 3):** el propio Dr. Sandino describe el
mecanismo completo sin ambigüedad — «es rata por rata… en su computadora cada uno lleva su
video y analiza una rata a la vez… por cada rata nos tardamos cerca de 30 minutos… en un
video que tiene cuatro ratas nos tardamos como 2 horas», y lo hacen «por triplicado». El
costo real es 3 analistas × 2 h = **6 horas-persona por video**, no 2. Ver
[`fuentes/transcripcion_01_no-formal.md`](fuentes/transcripcion_01_no-formal.md#n-02--mecánica-exacta-del-análisis-manual-confirmada-explícitamente).

Afecta: cap. 1, front.

### T-04 · Falta el criterio de repetibilidad, y ahora hay línea base para exigirlo 🔴

Entrevista P13: *«Lo ideal sería que el mismo video analizado múltiples veces arroje
siempre el mismo resultado, con una variabilidad máxima de entre el 5 y el 10 %.»*
Y P8: *«El objetivo principal no es tanto la velocidad sino reducir la variabilidad
del factor humano.»*

El documento solo lleva el criterio de concordancia con el analista humano (≥ 85 %).
El criterio de repetibilidad del propio sistema no aparece en ningún capítulo, pese a
que el usuario lo declaró como prioritario por encima del tiempo de procesamiento.

**Dato nuevo (transcripción informal, rango 3):** el Dr. Sandino cuantifica la variabilidad
humana actual — *«cada uno va a tener una variabilidad, anda por ahí del 15 % en cada una de
las conductas, un poquito más, 20 % de diferencia en tiempos»* — frente a la meta declarada
del sistema (5–10 %). Deja de ser un criterio sin sustento: hay una línea base humana
documentada (15–20 %) contra la que el 5–10 % objetivo se justifica directamente. Ver
[`fuentes/transcripcion_01_no-formal.md`](fuentes/transcripcion_01_no-formal.md#n-01--variabilidad-humana-de-línea-base-15–20-).
Por esto sube de severidad media a alta.

Afecta: cap. 1, cap. 2, cap. 3, cap. 4.

### T-05 · El «otro equipo» es un paradigma distinto, no un competidor — resuelto 🟢

**Transcripción informal, rango 3** (minuto 12:46–13:36): *«Lo que estamos haciendo con el
otro equipo es que el mismo video lo analizan varias veces para ver si el entrenamiento
genera datos diferentes… con videos que no se usaron para entrenar.»*

**Respuesta directa del equipo (2026-08-30):** «Es un equipo que trabaja con ansiolíticos y
un experimento diferente (laberinto T elevado).»

Resuelto: no es un trabajo comparable sobre FST — el laberinto T elevado mide ansiedad, no
depresión, y usa fármacos ansiolíticos en vez de antidepresivos. No pertenece a la tabla
comparativa del cap. 2. Sí es relevante para **RNF-11** («el módulo de clasificación debe
poder reconfigurarse para soportar paradigmas conductuales distintos al FST»): confirma que ya
existe, dentro de la misma institución, una necesidad real de extender esta metodología a otro
paradigma. Vale la pena mencionarlo como contexto de colaboración en la metodología (cap. 1),
no como estado del arte.

Afecta: cap. 1 (opcional, como contexto), cap. 2 (ya no requiere corrección).

### T-06 · El reanálisis de un video está confirmado, pero el documento no lo distingue del reinicio manual 🟡

**Respuesta directa del equipo (2026-08-30):** a la pregunta de si un video puede volver a
analizarse más de una vez (por ejemplo tras mejorar el modelo), la respuesta fue «sí, se puede
volver a hacer.»

**Esto no contradice RN-04** («El investigador no puede iniciarlo, pausarlo, cancelarlo ni
reiniciarlo desde la interfaz») si se entiende que RN-04 restringe únicamente el reinicio
manual por el investigador desde la interfaz, mientras que el reanálisis administrativo o
automatizado —tras actualizar el modelo, por ejemplo— es un caso distinto y permitido. Pero el
documento **no hace esa distinción en ningún lugar**, y tal como está redactado un lector
puede entender que ningún video se reanaliza jamás.

**Consecuencia estructural para el esquema conceptual:** la relación Video–Análisis deja de
ser (1,1) y pasa a **(1,N)** — un video puede tener más de un registro de análisis a lo largo
del tiempo. Esto afecta el esquema publicado en la actividad 5 (sección «Lo que queda
abierto», ítem «Reanálisis de un video»).

Afecta: cap. 4 (RN-04, RF-16), esquema conceptual.

---

## Preguntas abiertas

Registradas aquí porque **no son errores**: son huecos sin fuente que los resuelva.

| ID | Pregunta | Bloquea |
|----|----------|---------|
| ~~Q-01~~ | ~~¿Una tanda corresponde siempre a un grupo experimental completo?~~ — **Resuelta.** Respuesta directa del equipo (2026-08-29): «Sí, la tanda grabada son siempre de un grupo experimental completo.» | — |
| ~~Q-02~~ | ~~¿Los 80–100 videos históricos entran al sistema?~~ — **Resuelta.** Respuesta directa del equipo (2026-08-30): «Quedan por fuera.» Se usan solo externamente para entrenar/probar el modelo; no se cargan al sistema como experimentos. | — |
| ~~Q-03~~ | ~~¿El desglose por minuto se almacena en segundos o en porcentaje?~~ — **Resuelta.** Respuesta directa del equipo (2026-08-30): «Segundos.» | — |
| ~~Q-04~~ | ~~¿Cuál es el dispositivo de captura real?~~ — **Resuelta.** Respuesta directa del equipo (2026-08-30): «Cámara web.» No es celular (cap. 3) ni la Mac en sí — es una webcam, cuyo video la Mac procesa y guarda como MP4 (consistente con la entrevista P5). | — |
| ~~Q-05~~ | ~~¿Quién es «el otro equipo»?~~ — **Resuelta.** Respuesta directa del equipo (2026-08-30): «Es un equipo que trabaja con ansiolíticos y un experimento diferente (laberinto T elevado).» No es un trabajo comparable sobre FST — paradigma distinto. Ver T-05, revisado. | — |
| Q-06 | ¿Son 3–4 experimentos por **semestre** o por **bimestre**? **El equipo no lo sabe** (respuesta directa, 2026-08-30: «eso no sé») — hay que preguntarlo directamente al Dr. Sandino. | Cadencia real de generación de datos, relevante para factibilidad y planeación de TT-II |
| Q-07 | ¿Algún grupo experimental ha superado los 8 especímenes? **El equipo no lo sabe** (respuesta directa, 2026-08-30: «eso no sé») — hay que preguntarlo directamente al Dr. Sandino. | Si siempre son 2 tandas por grupo o a veces más |
| Q-08 | ¿Cómo se crea una cuenta: autoregistro con aprobación del administrador (cap. 1) o solo el Administrador las crea (cap. 4, RF-07)? Los dos capítulos se contradicen y la entrevista no lo resuelve. | Si `Usuario` necesita un atributo o especialización que distinga al administrador. Ver E01-12 |
