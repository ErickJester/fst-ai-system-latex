# Diagramas para presentar el TT a los sinodales

Orden sugerido para una reunión que parte desde cero, porque los sinodales conocen el modelo
anterior. Va de lo general a lo técnico. Todos están hechos con el estilo de `diagram_design`
(HTML, con su PNG).

| # | Para qué sirve | Diagrama | Archivo |
|---|----------------|----------|---------|
| 1 | Qué es el sistema, de punta a punta | Flujo general | [flujo_sistema.html](flujo_sistema.html) |
| 2 | Quién hace qué | Casos de uso (visión general) | [casos_uso.html](casos_uso.html) |
| 3 | Cómo el video se vuelve conducta por segundo | Pipeline de análisis | [pipeline_analisis.html](pipeline_analisis.html) |
| 4 | Qué datos se guardan | Esquema conceptual | [esquema_conceptual.html](esquema_conceptual.html) |
| 5 | Qué pasa con un análisis y con un experimento | Estados | [estados_analisis.html](estados_analisis.html), [estados_experimento.html](estados_experimento.html) |
| 6 | Cuando algo sale mal: pausa y ajuste | Secuencia | [`../seq_pausa_y_ajuste.puml`](../seq_pausa_y_ajuste.puml) |
| 7 | Con qué está construido | Arquitectura por capas | [arquitectura_capas.html](arquitectura_capas.html) |

Respaldo, por si preguntan: [esquema_bd.html](esquema_bd.html) (las 12 tablas),
[clases_completo.html](clases_completo.html) y [contenedores.html](contenedores.html).

## Qué cambió respecto al modelo anterior

Lo que los sinodales ya conocen y ahora es distinto: el modelo de datos es de 12 tablas (sin totales guardados y con las conductas como dominio), la
conducta se decide por segundo, hay un worker aparte del backend, solo el video del Día 2 se
analiza y existe un flujo de pausa y ajuste del recuadro.

## Fuentes y generadores

| Diagrama nuevo | Fuente | Generador |
|----------------|--------|-----------|
| Casos de uso | `../puml/cu_vision_general.puml` y `../puml/cu_paquete1.puml` a `cu_paquete5.puml` | `generadores/gen_casos_uso.py` |
| Esquema conceptual | `../esquema_conceptual.tex` | `generadores/gen_conceptual.py` |

El esquema conceptual usa las posiciones y cardinalidades del `.tex`, con las del 12-oct
(Video–Análisis `(0,1)`, Video–Observación `(0,4)`) y, desde el 14-oct (D-52), sin
`Intervalo` ni `presenta`: 10 entidades y 11 interrelaciones. El PDF
`../esquema_conceptual.pdf` está recompilado.

## Diagramas de secuencia

Se quedan en PlantUML (`../seq_*.puml`); no se pasan a HTML.
