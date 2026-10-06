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
| C. Bloqueados por decisión | 4 | 3 | 🟡 Solo falta Rev. 2 (Cordero, en curso) |
| D. Infraestructura de build | 3 | 0 | 🔴 No iniciado |

**Nada se ha tocado todavía en `05_diseno.tex`.** Los diagramas existen como archivos
nuevos y no pisan a los viejos. Las tres decisiones del equipo que bloqueaban el bloque B
ya se cerraron (13-sep) — ver bloque C.

---

## A. Hecho — los diagramas nuevos

Los cuatro compilan y su render está verificado.

| Archivo | Qué es | Sustituye a |
|---------|--------|-------------|
| [`diagramas/esquema_conceptual.tex`](diagramas/esquema_conceptual.tex) | ER conceptual, TikZ, notación Chen con cardinalidades (mín,máx) | `figures/mermaid/entidadRelacion.png` |
| [`diagramas/grafo_relacional_1_inicial.puml`](diagramas/grafo_relacional_1_inicial.puml) | Esquema Lógico Preliminar · 11 rel · 46 attr · 12 FK | — (no existía) |
| [`diagramas/grafo_relacional_2_laboratorio.puml`](diagramas/grafo_relacional_2_laboratorio.puml) | Esquema Lógico Definitivo · 11 rel · 46 attr · 11 FK · BCNF | `diagramas/relacional.puml` |
| [`diagramas/grafo_relacional_3_vigente.puml`](diagramas/grafo_relacional_3_vigente.puml) | Esquema reconciliado con las tablas de sistema · 15 rel · 71 attr · 16 FK · BCNF | base para `esquema_fisico.puml` |

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
viejas. El punto de partida para rehacerlo es `grafo_relacional_3_vigente.puml`, más los
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

### C5-06 — Diccionario de datos 🟢

**Ubicación:** `:342`–`:343` · **Estado:** ✅ Hecho (5-oct): `back/apendice_D.tex`, armado
desde `esquema_fisico.puml` (17 tablas, con D-29, D-35 y D-47) y no desde los artifacts,
que siguen en 16 relaciones · 
**Cruza con DOC-01 de `CORRECCIONES.md`**

La prosa promete «El diccionario de datos completo con tipos, restricciones y descripciones
de cada columna se incluye en los anexos». `CORRECCIONES.md` lo marca como prioridad máxima
con la nota «diccionario de datos inexistente».

**Ya no falta material.** La actividad 8 del artifact conceptual (v4) trae el diccionario
completo de las 10 entidades; la actividad 7 del lógico (v5) trae el de las 16 relaciones.
Lo único pendiente es trasladarlo a los anexos del `.tex` — es trabajo de redacción, no de
investigación.

### C5-07 — Diagrama de clases 🟢

**Ubicación:** `:2199`–`:2218` · **Estado:** El `.puml` ya está rehecho, falta actualizar
la prosa del capítulo que lo describe

`diagramas/clases.puml` se reescribió por completo (commit `f43c0da`, 12-sep): ya tiene
`Grupo`, `Tanda`, `Observacion`, `Intervalo`, `Conducta`, `Modelo`, `Configuracion`,
`Reporte`, `Notificacion` y `Administrador` — nada de `Sujeto`/`Trabajo`/`Animal` del
modelo viejo. Lo que queda pendiente es que la prosa de `05_diseno.tex` en `:2199`–`:2218`
describa este diagrama nuevo, no el viejo.

### C5-08 — Casos de uso 🟢

**Ubicación:** `:581`–`:2042` · **Estado:** Pendiente menor

Los artifacts casi no los tocan. Solo tres retoques:

- Retirar la transacción «seguir a la misma rata entre experimentos» — imposible: el número
  se reinicia en cada grupo y las ratas se sacrifican al terminar.
- El Día 1 es **opcional** para cualquier grupo, no exclusivo del control.
- El grupo **no tiene tope** de especímenes (el laboratorio lo pidió explícitamente).

---

## C. Bloqueados por una decisión

**Actualizado 2026-09-15: las tres decisiones del equipo ya se cerraron el 13-sep.** Solo
queda la revisión de la directora, y no bloquea empezar a escribir.

| ID | Decisión | Bloqueaba | Estado |
|----|----------|---------|--------------|
| ~~**P-08**~~ | ¿El reanálisis reemplaza al anterior, o se conserva historial? | C5-03, C5-04 | **Cerrada como D-03 (equipo, 13-sep):** reemplaza, no se conserva historial. `VIDEO—ANALISIS` baja de (1,N) a (1,1) — ya aplicado en `grafo_relacional_3_vigente.puml` y en `clases.puml` |
| ~~**D-04**~~ | Disparador vs. reintroducir `ESPECIMEN.idGrupo` como redundancia controlada | C5-03 | **Cerrada (equipo, 13-sep):** redundancia controlada — `idGrupo` reingresa a `ESPECIMEN` como columna redundante con `UNIQUE (idGrupo, numeroRata)`. Solo en el esquema físico |
| ~~**Q-08**~~ | ¿Autoregistro con aprobación, o solo el administrador crea cuentas? | C5-08, atributos de `USUARIO` | **Cerrada como D-01 (equipo, 13-sep):** solo el administrador crea cuentas. El cap. 1 queda mal, hay que corregirlo al RF-07 |
| **Rev. 2** | Revisión de notación con la **Dra. Martha Rosa Cordero** | Convenciones del bloque A, si cambian | **En curso** (2026-09-15) — directora del TT, sin cambios grandes esperados |

> Con las tres primeras cerradas, **nada estructural sigue bloqueando el bloque B.** El
> esquema es consistente en `(1,1)` tal como está en los artifacts vigentes (v4/v5).

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
| `ANALISIS(..., etapaActiva, ..., nivelClasificacion, ...)` | Reconciliar nombres contra `grafo_relacional_2_laboratorio.puml`, que usa `etapa` y `nivelClasif` |

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

## H. El clasificador del cap. 5 no es el que se construyó — encontrado el 2026-10-04 🔴

Las secciones del clasificador (`05_diseno.tex`, alrededor de las líneas 170-212, y la
mención «ResNet» de la arquitectura, línea ~46) describen una cascada ResNet-18 →
ResNet-50 y un suavizado por voto mayoritario de cuadros en ventanas de **1 s**. El
etiquetador real (`C:\Users\Samsung\Desktop\proyectos\fst_auto`) hace otra cosa:

- Mide **15 rasgos** por fotograma y decide con el **modelo de bloques**
  (`modelo_fst.joblib`), entrenado con bloques de 5 s; además hay una CNN 3D fusionada con
  rasgos y reglas (commit `ee7c9a8`, 26-sep).
- **Segundo a segundo** (`segundos.py`, commit `4eb1f46`, 30-sep): para el segundo *k* mide
  los rasgos en una **ventana deslizante de 4 s** centrada en *k*; detecta conductas de unos
  **2 s**. Regla de tres pasos que da «conducta activa» cuando no decide.
- Valida juntando los segundos de cada bloque de 5 s por mayoría contra los bloques hechos
  a mano.

| ID | Qué | Estado |
|----|-----|--------|
| **CLA-01** | Reescribir la descripción del clasificador del cap. 5 según el etiquetador real (rasgos, modelo de bloques, CNN, ventana deslizante de 4 s) | ✅ Hecho (4-oct): Módulo 4 reescrito (rasgos, Random Forest con regla de tres pasos, ventana deslizante de 4 s, entrenamiento en bola de nieve, CNN R(2+1)D en desarrollo). Sin cifras de desempeño: la evaluación queda para TT-II con precisión, recall y F1. Bibliografía: `breiman2001`, `tran2018`. **Corregido (5-oct):** el clasificador nunca fue un Random Forest; `fst_auto` usa `HistGradientBoostingClassifier` desde su primer commit. El cap. 5 (~185) ya lo dice, y `breiman2001` se cambió por `friedman2001` y `ke2017`. Los umbrales de `CONFIGURACION` quedan en D-50, pendiente de aplicar |
| **CLA-02** | Revisar la arquitectura (línea ~46: «YOLOv8, ByteTrack, ResNet»), el Módulo 3 (seguimiento con YOLOv8 + ByteTrack) y los modelos que monta el worker (`rat.pt`, `resnet18_fst.pt`, `resnet50_fst.pt`) contra lo real | ✅ Hecho (5-oct). El usuario lo separó de lo que depende del clasificador: `fst_auto` no usa YOLO, ByteTrack ni ningún *tracker* (detecta por sustracción de fondo, un espécimen por cilindro), así que eso sale sin importar qué clasificador gane. Quitados YOLOv8, ByteTrack, CSRT, Kalman/IoU, `rat.pt` y los `resnet*_fst.pt` de caps. 1–5, glosario y abreviaturas (CSRT, IoU, MOT, SORT). YOLO queda solo como trabajo revisado en el cap. 2. El pipeline pasa a tres etapas (D-16 y D-22 revisados). Figura del pipeline rehecha en `diagramas/pipeline.puml` (la vieja era Mermaid sin fuente). Los caps. 6 y 7 (`tracker.py`, «Resultados del módulo de seguimiento») no se tocaron: están comentados en `main.tex` y se reescriben cuando se retomen |
| **CLA-03** | ResNet-18/50 como clasificador del proyecto sigue en otros capítulos: cap. 1 (líneas ~366, 466, 488), cap. 2 (~272-289), cap. 3 (sección «ResNet y conexiones residuales», ~261-281, y ~333), cap. 4 (tabla de tecnologías ~693-708, viabilidad ~882-886 y ~909), glosario (~62, 81, 190, 261, 287-290, 315) y abreviaturas | 🟡 Parte hecha (5-oct): ResNet-50 quitado en todos lados. ResNet-18 queda solo como base de la R(2+1)D-18 («una ResNet-18 para video»); los caps. 1–4 y el glosario ya presentan dos candidatos, *gradient boosting* sobre rasgos y R(2+1)D-18, igual que el cap. 5. **Falta (cuando termine el etiquetado y el entrenamiento):** escribir cuál gana y su F1; volver a revisar D-50 (el 0.80 de `umbralConfianza` viene de la regla de tres pasos del *gradient boosting*), D-06 (si gana la fusión hay dos archivos de modelo) y si «rasgos» se vuelve etapa (D-16); la columna «DL» de la tabla comparativa del cap. 2 dice «Sí» y dejaría de ser cierto si gana el *gradient boosting* |
| **CLA-04** | Lo que el cap. 5 y el marco teórico dicen del preprocesamiento y que `fst_auto` no hace: CLAHE (cap. 4 R-01, cap. 5 Módulo 1, glosario, abreviaturas, figura del pipeline), línea de agua con EMA (cap. 3, glosario, abreviaturas) y fondo por **mediana** (caps. 2, 3 y 4; `fst_auto` usa el **percentil 10** y dice que la mediana no sirve, `lib.py:218`). D-26 sigue diciendo BORIS (caps. 1, 3 y 4): espera a aclarar qué son los `*_mano.csv` de `fst_auto/etiquetas` | Pendiente (5-oct): fuera del paso 1, sin decidir |

**Fuente:** el código y los commits de `fst_auto` (rango 1, el equipo). D-49 solo quita la
liga del suavizado con la duración mínima de episodio; la reescritura completa es CLA-01.

---

*Creado: 2026-09-06*
