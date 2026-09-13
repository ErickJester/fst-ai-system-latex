# Cambios al capítulo 5 — Diseño

**Documento de control.** Qué se le tiene que cambiar a `chapters/05_diseno.tex` para
que refleje el diseño de base de datos rehecho, qué está ya hecho y qué falta.

- **Archivo destino:** [`chapters/05_diseno.tex`](chapters/05_diseno.tex) (2 400+ líneas)
- **Rama de trabajo:** `diagramas-plantuml`
- **Origen del trabajo:** los dos artifacts de diseño conceptual y lógico, revisión del 3-sep
- **Léelo junto con:** [`DISENO-BD.md`](DISENO-BD.md) (el porqué y la metodología) ·
  [`CORRECCIONES.md`](CORRECCIONES.md) (auditoría del documento completo) ·
  [`errores/README.md`](errores/README.md) (jerarquía de fuentes)

> **Regla heredada del catálogo de errores:** ninguna corrección se aplica al LaTeX sin
> fuente de rango superior. Todo lo de aquí se apoya en los artifacts, la entrevista formal
> o la reunión del 3-sep.

---

## Avance

| Bloque | Ítems | Hechos | Estado |
|--------|-------|--------|--------|
| A. Diagramas nuevos | 4 | 4 | 🟢 Hecho |
| B. Prosa y figuras del capítulo | 8 | 0 | 🔴 No iniciado |
| C. Bloqueados por decisión | 4 | 0 | ⚫ En espera |
| D. Infraestructura de build | 3 | 0 | 🔴 No iniciado |

**Nada se ha tocado todavía en `05_diseno.tex`.** Los diagramas existen como archivos
nuevos y no pisan a los viejos.

---

## A. Hecho — los diagramas nuevos

Los cuatro compilan y su render está verificado.

| Archivo | Qué es | Sustituye a |
|---------|--------|-------------|
| [`diagramas/esquema_conceptual.tex`](diagramas/esquema_conceptual.tex) | ER conceptual, TikZ, notación Chen con cardinalidades (mín,máx) | `figures/mermaid/entidadRelacion.png` |
| [`diagramas/grafo_relacional_inicial.puml`](diagramas/grafo_relacional_inicial.puml) | Esquema Lógico Preliminar · 11 rel · 46 attr · 12 FK | — (no existía) |
| [`diagramas/grafo_relacional_final.puml`](diagramas/grafo_relacional_final.puml) | Esquema Lógico Definitivo · 11 rel · 46 attr · 11 FK · BCNF | `diagramas/relacional.puml` |
| [`diagramas/grafo_relacional_reconciliado.puml`](diagramas/grafo_relacional_reconciliado.puml) | Esquema reconciliado con las tablas de sistema · 15 rel · 71 attr · 16 FK · BCNF | base para `esquema_fisico.puml` |

### Por qué el par inicial/final y no solo el final

El método produce **dos** entregables en la etapa lógica: un esquema preliminar y uno
definitivo, separados por la validación. El Prof. Israel Salas lo pidió explícitamente en
la reunión: presentar solo el final deja sin evidencia el paso de validación, y los
sinodales lo van a pedir.

### Por qué TikZ y no PlantUML en el conceptual

Las cardinalidades del modelo son `(3,4)`, `(5,5)`, `(6,N)`, `(2,3)`, `(1,2)`. PlantUML
solo dibuja notación de pata de gallo, que distingue 0/1/muchos y **no puede expresar esos
rangos**. Convertirlo a PlantUML perdería información del universo del discurso.

### El pase de normalización, ya hecho

Cuatro defectos, no tres. Los tres primeros vienen de los artifacts; el cuarto salió al
reconciliar con las tablas de sistema.

| # | Relación | Defecto | Corrección |
|---|----------|---------|------------|
| 1 | `USUARIO` | `nombre` es dominio compuesto (1FN) | Se parte en `nombre` + `apellidos` |
| 2 | `ESPECIMEN` | `idEspecimen → idTanda → idGrupo` (3FN) | Se elimina `idGrupo`; se alcanza por la tanda |
| 3 | `VIDEO` | `sesion → duracion` nominal (3FN) | `duracion` pasa a ser la real del archivo |
| 4 | `CONFIGURACION` | `hashModelo → nombreModelo` (3FN) | Se extrae `MODELO (hashModelo, nombreModelo)` |

Determinantes examinados y **descartados**: `tipo → mensaje` en `NOTIFICACION`,
`estado → etapa` en `ANALISIS`, `tipo → tratamiento` en `GRUPO`. `ruta → formato` en
`REPORTE` sí se cumple, pero `ruta` es clave candidata, así que no viola BCNF.

**Resultado: las 15 relaciones quedan en BCNF**, verificadas una por una.

---

## B. Por hacer en `chapters/05_diseno.tex`

### C5-01 — §«Diseño de la base de datos», prosa completa 🔴

**Ubicación:** `:238`–`:343` · **Estado:** Pendiente

La prosa entera describe el modelo viejo: entidades `USUARIOS`, `EXPERIMENTOS`, `VIDEOS`,
`TRABAJOS`, `ANIMALES`, y los cuatro grupos funcionales de tablas (`:274`–`:340`). Nada de
eso sobrevive.

Falta: reescribirla sobre las 15 relaciones, con los niveles `GRUPO` y `TANDA` que el
modelo viejo no tenía, y con `OBSERVACION` como entidad asociativa.

### C5-02 — Figura `fig:der` no es conceptual 🔴

**Ubicación:** `:253`–`:258` · **Estado:** Pendiente

El documento la titula «diagrama entidad-relación **conceptual**», pero su fuente
(`diagramas/DiagramaEntidadRelacion.svg`) contiene `VARCHAR`, `INTEGER`, `PK` y `FK`: es el
esquema físico dibujado por segunda vez. La figura conceptual y la física muestran lo mismo.

Falta: sustituirla por `esquema_conceptual.pdf` y reescribir el pie.

### C5-03 — Figura `fig:er` (esquema físico) 🔴

**Ubicación:** `:267`–`:272` · **Estado:** Bloqueado (ver C-02 y C-03)

`figures/mermaid/er2.png` viene de `diagramas/esquema_fisico.puml`, con las 12 tablas
viejas. El punto de partida para rehacerlo es `grafo_relacional_reconciliado.puml`, más los
tipos PostgreSQL y las columnas de auditoría, que son de la etapa física.

### C5-04 — Insertar el par de grafos relacionales 🔴

**Ubicación:** nueva, entre `:265` y `:346` · **Estado:** Pendiente

Faltan dos figuras que hoy no existen en el documento: el grafo relacional inicial y el
final, con sus `\ref` y sus pies. Van juntas; son la evidencia del paso de validación.

### C5-05 — §«Normalización», reescritura completa 🔴

**Ubicación:** `:346`–`:500` · **Estado:** Pendiente · **Desbloqueado**

Hoy argumenta sobre las 12 tablas viejas (`:365`–`:369`) y llega solo hasta 3FN. Hay que
sustituirla por el pase del bloque A: cuatro defectos, determinantes descartados, veredicto
**BCNF**, y la tabla resumen de `:455`–`:500` rehecha.

**Lo que sí se recicla tal cual:**

- El argumento de 1FN sobre los parámetros del pipeline (`:379`–`:388`): cada umbral en su
  columna, sin campo JSON. Aplica igual a `CONFIGURACION`.
- El argumento de 3FN sobre extraer los hiperparámetros de `TRABAJOS` (`:428`–`:440`). Es el
  mismo caso, ahora entre `ANALISIS` y `CONFIGURACION`.
- El argumento de clave sustituta en `USUARIOS` (`:442`–`:448`).

**Un ejemplo nuevo que conviene aprovechar:** la clave natural de `CONFIGURACION` son **ocho
columnas** (el modelo más los siete parámetros). Es el mejor argumento del esquema a favor
de las llaves subrogadas, mejor que cualquiera de los que ya estaban.

### C5-06 — Diccionario de datos 🔴

**Ubicación:** `:342`–`:343` · **Estado:** Pendiente · **Cruza con DOC-01 de `CORRECCIONES.md`**

La prosa promete «El diccionario de datos completo con tipos, restricciones y descripciones
de cada columna se incluye en los anexos». `CORRECCIONES.md` lo marca como prioridad máxima
con la nota «diccionario de datos inexistente».

Material disponible: la actividad 8 del artifact conceptual trae el diccionario de `Grupo`,
`Espécimen` y `Video`; la actividad 7 del lógico trae el de las relaciones que la revisión
tocó. **Faltan las demás.**

### C5-07 — Diagrama de clases 🟡

**Ubicación:** `:2199`–`:2218` · **Estado:** Pendiente

`diagramas/clases.puml` tiene `Sujeto`, `Trabajo`, `ROI`, `Animal`,
`ResultadoComportamiento` y `ComportamientoPorMinuto` — todas del modelo viejo. No tiene
`Grupo`, `Tanda`, `Observacion`, `Intervalo` ni `Conducta`.

Solo la capa de dominio cambia; los paquetes P1–P5 y las clases de sistema (`Worker`,
`PipelineAnalisis`) se quedan.

### C5-08 — Casos de uso 🟢

**Ubicación:** `:581`–`:2042` · **Estado:** Pendiente menor

Los artifacts casi no los tocan. Solo tres retoques:

- Retirar la transacción «seguir a la misma rata entre experimentos» — imposible: el número
  se reinicia en cada grupo y las ratas se sacrifican al terminar.
- El Día 1 es **opcional** para cualquier grupo, no exclusivo del control.
- El grupo **no tiene tope** de especímenes (el laboratorio lo pidió explícitamente).

---

## C. Bloqueados por una decisión

| ID | Decisión | Bloquea | Quién decide |
|----|----------|---------|--------------|
| **P-08** | ¿El reanálisis reemplaza al anterior, o se conserva historial? | C5-03, C5-04. Si se conserva historial, `OBSERVACION` debe referenciar `idAnalisis` en vez de `idVideo` — ver [`DISENO-BD.md`](DISENO-BD.md) §8 «Errata estructural» | Laboratorio |
| **D-04** | Disparador vs. reintroducir `ESPECIMEN.idGrupo` como redundancia controlada | C5-03 | Equipo |
| **Q-08** | ¿Autoregistro con aprobación, o solo el administrador crea cuentas? El cap. 1 y el cap. 4 se contradicen | C5-08, atributos de `USUARIO` | Equipo |
| **Rev. 2** | Revisión de notación con la **Dra. Martha Rosa Cordero** | Todo el bloque A, si cambia convenciones | Directora |

> **P-08 es el de mayor peso.** Mientras `VIDEO—ANALISIS` siga en `(1,N)`, los resultados
> cuelgan de `VIDEO` y no del análisis que los produjo: desde una fila de `PRESENTA` no se
> puede saber cuál análisis la escribió. Con `(1,1)` el esquema es consistente tal como está.

---

## D. Infraestructura de build

| ID | Qué | Estado |
|----|-----|--------|
| **INF-01** | `diagramas/puml/gen_pngs.sh` solo genera los `cu_*`. Faltan los tres `.puml` nuevos | Pendiente |
| **INF-02** | No hay regla para compilar `esquema_conceptual.tex` (TikZ → PDF) | Pendiente |
| **INF-03** | `gen_pngs.sh` tiene rutas absolutas a `/home/vane/` y `/tmp/plantuml.jar`. No corre en otra máquina | Pendiente |

Versión de PlantUML con la que se verificaron los diagramas: **1.2026.8**.

---

## E. Lo que deliberadamente NO cambia

### `ROIS` no vuelve como tabla

El pipeline **calcula** el recuadro en cada corrida (Módulo 2, `:129`–`:131`) y lo único que
conserva es el orden espacial, que ya está guardado como `ESPECIMEN.numeroCilindro`
(«Separación por espécimen», `:227`–`:230`). Guardar `(x, y, w, h)` sería almacenar un
derivado inestable: si se reprocesa con otro modelo de fondo, el recuadro cambia.

**Reserva:** el día que exista una pantalla para corregir a mano un cilindro mal detectado,
el recuadro pasa a ser dato del usuario y entonces sí necesitaría tabla.

### `OBSERVACION` se queda sin atributos propios

Es una relación asociativa legítima, no una tabla vacía por error.

---

## G. `protocolo_fst.tex` — desincronizado, encontrado el 2026-09-12 🔴

**Ubicación:** `protocolo_fst.tex` (raíz del repo) + `Protocolo_FST_paso_a_paso.pdf`.
Documento independiente, no es uno de los 8 capítulos, pero se usa como material de
apoyo para la revisión con el laboratorio y con la Dra. Cordero.

**Problema:** el commit `8b26dd6` (3-sep, 17:59) quedó escrito con el modelo **de antes**
de que la reunión de esa misma tarde cerrara las correcciones. Nadie lo resincronizó
después.

| Ahí dice | Debe decir |
|---|---|
| `ESPECIMEN(idEspecimen, idLaboratorio, numeroCilindro, idTanda*)` | `numeroRata` en vez de `idLaboratorio` — ya no es clave global, es relativa al grupo |
| `Grupo → agrupa (6,8 / 1,1) → Espécimen` | `(6,N)` — sin tope, el laboratorio lo pidió explícitamente |
| «`UNIQUE idLaboratorio` (alcance por confirmar, P-03)» | P-03 ya está cerrada — marca de plumón, numerada 1–8 dentro del grupo |
| `ANALISIS(..., etapaActiva, ..., nivelClasificacion, ...)` | Reconciliar nombres contra `grafo_relacional_final.puml`, que usa `etapa` y `nivelClasif` |

**Cómo se descubrió:** al leer el diff completo del commit `8b26dd6` tras el `git pull`
de esta sesión (regla nueva en `CLAUDE.md` — leer commits completos, no solo el
resumen). El `git log --stat` que se revisó al principio no mostraba nada de esto.

---

## F. Nota sobre `DISENO-BD.md`

Su §8 dice que hay que corregir la nota «Sobre los nulos» porque declara dos atributos
nulables. **Ya está corregido en el artifact lógico** (revisión del 3-sep): solo
`EXPERIMENTO.notas` admite nulo. `DISENO-BD.md` quedó desactualizado en ese punto —
su última actualización es del 2026-09-02 y el artifact se republicó después.

---

*Creado: 2026-09-06*
