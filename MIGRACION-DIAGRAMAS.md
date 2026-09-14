# Migración de diagramas — viejo modelo → nuevo modelo

> **Documento temporal. Se borra cuando termine el bloque de diagramas del capítulo 5**
> (ver §6). No es un entregable del TT ni una fuente permanente — lo que sobreviva de
> valor duradero se mueve a [`CAMBIOS-CAP5.md`](CAMBIOS-CAP5.md) antes de borrar esto.

**Para qué sirve.** Cada diagrama nuevo se tiene que dibujar acorde a lo que el sistema
**necesita de verdad** (el modelo rediseñado en [`DISENO-BD.md`](DISENO-BD.md)), no a lo
que el diagrama viejo ya traía dibujado. El viejo modelo estaba mal — le faltaban dos
niveles enteros de la jerarquía (Grupo y Tanda) — así que copiar su estructura y solo
renombrar cosas reproduce el error. Este archivo reúne en un solo lugar lo que decía el
modelo viejo, lo que dice el nuevo, y una guía de preguntas por cada diagrama para que
la construcción parta de la necesidad real y no de la costumbre visual del diagrama
anterior.

**Cómo usarlo:** antes de tocar cualquier diagrama, abre su sección en el §3, contesta
el checklist, y solo entonces dibuja. Marca el estado en la bitácora del §5.

---

## 0. El modelo nuevo, de un vistazo

Fuente: [`diagramas/grafo_relacional_reconciliado.puml`](diagramas/grafo_relacional_reconciliado.puml)
— las 11 relaciones del esquema lógico definitivo más las 4 de soporte del sistema, ya
con la corrección de la reunión del 3-sep (`GRUPO.tratamiento` nunca nulo), más
`ADMINISTRADOR` (D-08, 13-sep): **16 relaciones en total**, no 15.

> **Verificado contra los artifacts, no solo contra los `.puml`.** Los `.puml`/`.tex` de
> `diagramas/` dicen derivarse de los artifacts, pero se comprobó línea por línea contra
> las versiones vivas: **Diseño Conceptual FST · Revisión 3-sep**
> (actualizado 2026-09-04) y **Diseño Lógico FST · Revisión 3-sep**
> (actualizado 2026-09-07, con la reconciliación del 6-sep). Son más recientes que los
> enlaces que cita `DISENO-BD.md` §4 — si necesitas volver a leerlos, búscalos por nombre
> con `Artifact action:"list"`, no por la URL vieja del `.md`.
>
> **Aviso de nomenclatura:** lo que `DISENO-BD.md` llama **P-08** (el reanálisis) es el
> mismo pendiente que el artifact lógico llama **D-03** — mismo problema, dos nombres en
> dos documentos. No son dos pendientes distintos.
>
> **Un pendiente que `CAMBIOS-CAP5.md` no tiene todavía** (salió de la
> reconciliación del 6-sep, es del equipo, no del laboratorio):
> - **Q-09** — ¿`NOTIFICACION.mensaje` lleva detalle por instancia o es plantilla por
>   tipo? Si es plantilla, `tipo → mensaje` sería transitiva y haría falta un catálogo
>   `TIPO_NOTIFICACION`.
>
> **D-05 y D-06, resueltos (equipo, 2026-09-13):** D-06 no cambia la relación
> `MODELO`↔`CONFIGURACION` — se queda en 1:N, lo que importa es el resultado, no la
> combinación exacta de modelos. Y D-05 (¿se puede correr dos veces la misma
> `CONFIGURACION` sobre el mismo video?) **se disolvió solo** al resolver D-03: si el
> reanálisis reemplaza en vez de conservar historial, un video nunca tiene más de un
> `ANALISIS` a la vez, así que la pregunta de si `(idVideo, idConfig)` se repite ya no
> aplica — no puede haber una segunda fila que compita con la primera.
>
> **Ocho decisiones más, todas del 13-sep, que tampoco están en `CAMBIOS-CAP5.md`
> todavía** (D-11 a D-18 — SGBD, seguridad, redundancia, tipos de dato, dominios y
> respaldo; detalle completo en `errores/preguntas-doctor.md` §6 y en el artifact de
> Diseño Físico). Son de la **etapa física**, no de la lógica — no tocan este archivo de
> migración de diagramas más que en un punto: D-08 (`ADMINISTRADOR`) sí es de la etapa
> lógica y ya está aplicado en el `.puml` (ver arriba y §3.2).
>
> **Cinco decisiones más, del 13-sep, que salieron de construir los diagramas de
> secuencia (§3.4), no de la etapa física:** D-19 (cómo infiere el sistema la Tanda al
> subir video), D-20 (todo o nada si no detecta los 4 cilindros — provisional, ver Q-G),
> D-21 (caché y regeneración de `REPORTE`), D-22 (porcentaje de avance aproximado por
> etapa) y D-23 (columna nueva `ANALISIS.rutaDiagnostico`). Detalle completo en
> `errores/preguntas-doctor.md` §6. **D-23 es la única que toca este `.puml`** — está
> **pendiente de aplicar** en `grafo_relacional_reconciliado.puml`, no se toca hasta que
> se pida explícitamente (ver §3.2).

```
USUARIO ──registra──> EXPERIMENTO ──compone──> GRUPO ──agrupa──> ESPECIMEN
                                                   │
                                                   └──se graba en──> TANDA ──aloja──> ESPECIMEN
                                                                        └──produce──> VIDEO ──procesa──> ANALISIS
                                                                                                              │
                                              ESPECIMEN ──aparece en──┐                    CONFIGURACION ─────┤
                                              VIDEO ──contiene────────┴──> OBSERVACION           │
                                                                              └──se divide en──> INTERVALO
                                                                                                     └──presenta──> CONDUCTA [segundos]

EXPERIMENTO ──origina──> REPORTE
USUARIO / EXPERIMENTO ──origina──> NOTIFICACION
MODELO ──1:N──> CONFIGURACION
USUARIO ──subtipo (1,1)-(0,1)──> ADMINISTRADOR
```

**Dominio experimental (11 relaciones, lo que el laboratorio reconoce):** `USUARIO`,
`EXPERIMENTO`, `GRUPO`, `TANDA`, `ESPECIMEN`, `VIDEO`, `ANALISIS`, `OBSERVACION`,
`INTERVALO`, `CONDUCTA`, `PRESENTA`.

**Soporte de sistema (4 relaciones, el laboratorio no las nombra):** `MODELO`,
`CONFIGURACION`, `REPORTE`, `NOTIFICACION`.

**Subtipo de seguridad (1 relación, decidida el 13-sep, D-08):** `ADMINISTRADOR` — ni del
laboratorio ni del sistema en el mismo sentido que las cuatro de arriba; es un subtipo de
`USUARIO`, así que se cuenta aparte. Total: 11 + 4 + 1 = **16 relaciones**.

**Lo único que el sistema mide de verdad:** `segundos`, atributo de `PRESENTA`. Todo lo
demás es estructura para ubicarlo o metadato del análisis. Los totales por espécimen y
las comparaciones entre grupos se **derivan en consulta**, no se almacenan.

**Decisiones que sostienen el modelo** (detalle y fuentes en `DISENO-BD.md` §4):
1. La Tanda existe porque un grupo (6–8 especímenes) no cabe en un encuadre de máximo 4
   cilindros.
2. `OBSERVACION` es la entidad que junta un espécimen con el video en el que aparece —
   evita que un espécimen se empareje con el video de otra tanda.
3. `GRUPO.tratamiento` nunca es nulo: el control recibe placebo (mismo estrés de
   inyección en los tres grupos).
4. La rata **sí tiene identificador propio** (P-03, cerrada en la reunión del 3-sep):
   marca de plumón en la cola, numerada 1–8 **dentro de su grupo** — no es una clave de
   laboratorio. Lo que queda abierto no es si existe, sino cómo se garantiza que no se
   repita dentro del grupo una vez que `idGrupo` salió de `ESPECIMEN` por 3FN (**D-04**,
   ver §3.3).

> **D-02 resuelto (2026-09-12), renombre ejecutado (2026-09-13).** `USUARIO.idBoleta`
> estaba mal — corregido en `errores/preguntas-doctor.md` §6. **Nuevo esquema: un
> identificador institucional único** (`idInstitucional`), que acepta boleta
> (estudiantes) o número de empleado (personal), con una regla de formato/tipo pendiente
> de afinar para distinguir cuál es cuál — detalle menor, no bloquea. Ya renombrado en
> `diagramas/clases.puml`, `grafo_relacional_final.puml`, `grafo_relacional_reconciliado.puml`
> y `grafo_relacional_inicial.puml` — los cuatro compilan.

---

## 1. El modelo viejo, qué decía y por qué está mal

Fuente: `chapters/05_diseno.tex:235`–`501` (sección «Diseño de la base de datos» +
«Normalización») y `docs/diagramas.pdf` páginas 4–6 (DER conceptual, esquema físico,
diagrama de clases — todas construidas sobre las mismas 12 tablas).

**Las 12 tablas viejas:** `USUARIOS`, `EXPERIMENTOS`, `VIDEOS`, `SUJETOS`, `ROIS`,
`CONFIGURACIONES_ANALISIS`, `TRABAJOS`, `ANIMALES`, `RESULTADOS_COMPORTAMIENTO`,
`COMPORTAMIENTO_POR_MINUTO`, `REPORTES`, `NOTIFICACIONES`.

**Por qué está mal** (ver `DISENO-BD.md` §1):
- No existen `GRUPO` ni `TANDA`. `VIDEOS` cuelga directo de `EXPERIMENTOS` con un campo
  plano `dia` (`dia1`/`dia2`), como si un experimento fuera una sola grabación de ~4
  ratas — pero un experimento real son 3+ grupos de 6–8 ratas cada uno.
- `SUJETOS` + `ANIMALES` son un parche: dos tablas para simular el nivel que faltaba
  (espécimen dentro de una ejecución del pipeline), en vez de modelar la jerarquía real.
- `RESULTADOS_COMPORTAMIENTO` y `COMPORTAMIENTO_POR_MINUTO` guardan **totales
  calculados** como si fueran datos primarios, duplicando lo que ya está en el desglose
  por minuto — el nuevo modelo solo guarda `segundos` en `PRESENTA` y deriva el resto.
- `ROIS` guarda un recuadro `(x,y,w,h)` que el pipeline recalcula en cada corrida: es un
  derivado inestable, no un dato del universo del discurso.

---

## 2. Tabla de equivalencia — qué le pasa a cada tabla vieja

| Tabla vieja | Destino en el modelo nuevo | Veredicto |
|---|---|---|
| `USUARIOS` | `USUARIO` | Sobrevive. PK pasa de `id` autogenerado a `idInstitucional` (D-02, ver §0) — identificador único que acepta boleta o número de empleado |
| `EXPERIMENTOS` | `EXPERIMENTO` | Sobrevive, pero pierde `tratamiento`, `especie`, `disposicion` — esos bajan a `GRUPO` (el tratamiento es por grupo, no por experimento completo) |
| `VIDEOS` | `VIDEO` | Sobrevive, pero ahora cuelga de `TANDA`, no de `EXPERIMENTO`. `dia` → `sesion` |
| `SUJETOS` | `ESPECIMEN` | Sobrevive, pero cuelga de `TANDA`, no de `EXPERIMENTO`. `indice_rata`+`etiqueta` → `numeroRata`+`numeroCilindro` |
| `ROIS` | — | **Eliminada.** Es un derivado que el pipeline recalcula; no se almacena (ver §E de `CAMBIOS-CAP5.md`) |
| `CONFIGURACIONES_ANALISIS` | `CONFIGURACION` + `MODELO` | Se parte en dos por 3FN: `hashModelo → nombreModelo` es una dependencia transitiva real |
| `TRABAJOS` | `ANALISIS` | Renombrada. Ya no tiene `parametros` sueltos; referencia `CONFIGURACION` por FK |
| `ANIMALES` | — | **Desaparece como tabla de enlace.** El enlace espécimen↔video lo hace `OBSERVACION` |
| `RESULTADOS_COMPORTAMIENTO` + `COMPORTAMIENTO_POR_MINUTO` | `OBSERVACION` → `INTERVALO` → `PRESENTA` | Se funden. Solo se guarda `segundos` por intervalo de un minuto; los totales se derivan en consulta |
| `REPORTES` | `REPORTE` | Casi igual, FK sigue siendo a `EXPERIMENTO` |
| `NOTIFICACIONES` | `NOTIFICACION` | Casi igual, FK de usuario ahora es `idInstitucional` |

**Nuevo, sin equivalente en el modelo viejo:** `GRUPO`, `TANDA`, `OBSERVACION`,
`INTERVALO`, `CONDUCTA` (catálogo).

---

## 3. Guía diagrama por diagrama

No dibujes nada de una sección sin haber contestado su checklist.

### 3.1 DER conceptual (`fig:der` en el capítulo, hoy `figures/mermaid/entidadRelacion`)

**Estado:** 🟢 rehecho — [`diagramas/esquema_conceptual.tex`](diagramas/esquema_conceptual.tex).

Checklist de verificación (no de construcción, ya existe):
- [ ] Las 10 entidades son solo las que el laboratorio reconoce — nada de `MODELO`,
      `CONFIGURACION`, `REPORTE` ni `NOTIFICACION` (esas no las nombra el universo del
      discurso, son necesidad del sistema, van solo en el esquema lógico/físico)
- [ ] Cada cardinalidad (mín,máx) tiene una fuente citada en el `.tex` (P19, PA, reunión
      3-sep) — ninguna por intuición
- [ ] Sigue marcado como «Esquema Conceptual Inicial», no «Definitivo», hasta que pase la
      revisión de notación con la Dra. Cordero

> **Verificado contra Kendall & Kendall, *Análisis y Diseño de Sistemas*, cap. 2
> "Comprensión y modelado de los sistemas organizacionales" (pp. 32–33) y cap. 13
> "Diseño de bases de datos" (pp. 405–407).**
>
> - **Confirma la elección de Chen sobre pata de cuervo.** El libro solo cubre notación
>   de pata de cuervo para ER (cinco símbolos de línea: 1, 0..1, 0..*, 1..*). No tiene
>   forma de expresar `(3,4)`, `(6,N)`, `(2,3)` — la misma limitación que ya llevó a
>   elegir TikZ/Chen en `esquema_conceptual.tex`. Segunda fuente independiente que
>   confirma la justificación, no la cambia.
> - **Respaldo nuevo para `OBSERVACION` como entidad asociativa.** El libro la define
>   así: *"una entidad asociativa puede existir sólo si está conectada con por lo menos
>   otras dos entidades"* y da el ejemplo de `TRATAMIENTO`, agregada "porque no es
>   importante en el sistema por sí sola" — es la misma razón por la que existe
>   `OBSERVACION` (unir `ESPECIMEN` y `VIDEO`, sin atributos propios). Es un **segundo
>   libro, independiente del de Cardona**, que respalda la misma decisión.
> - **Pregunta para la revisión con la Dra. Cordero, no para resolver aquí:** en la
>   notación de pata de cuervo del libro, una entidad asociativa lleva un símbolo
>   distinto (diamante dentro del rectángulo). En Chen ese diamante ya significa
>   "interrelación", así que no se puede reutilizar sin ambigüedad — `Observación` hoy se
>   dibuja igual que cualquier otra entidad. Preguntarle a la Dra. Cordero si eso necesita
>   una marca visual propia en la notación Chen, o si está bien así.
> - Agregar Kendall & Kendall a `bib/referencias.bib` cuando se escriba la prosa de esta
>   sección (comparte el pendiente ya anotado en §3.3).

> **Nota para §3.2:** Kendall & Kendall cap. 13 trata la transformación M:N igual que
> Cardona ("se requieren tres tablas: una para cada entidad y una para la relación") —
> consistente con cómo ya se resolvió `PRESENTA`. Pero su normalización **llega solo
> hasta 3FN**, no cubre BCNF — no citarlo como respaldo de la validación BCNF del grafo
> relacional; ese respaldo sigue siendo Codd/Elmasri-Navathe/Cardona, ya citados en
> `chapters/05_diseno.tex`.

### 3.2 Esquema físico / grafo relacional (`fig:er`, hoy `figures/mermaid/er2`)

**Estado:** 🟡 insumo listo, falta compilar e insertar el par de evidencia.

Fuente: `diagramas/grafo_relacional_inicial.puml` (preliminar, con los 3 defectos
marcados) + `diagramas/grafo_relacional_final.puml` (validado, BCNF) +
`diagramas/grafo_relacional_reconciliado.puml` (+ 4 tablas de sistema + `ADMINISTRADOR`,
16 relaciones en total — este es el que de verdad sustituye a `fig:er`).

Antes de maquetar:
- [ ] Van los **tres** grafos, no solo uno: inicial y final son el par obligatorio que
      documenta el paso de validación (lo pidió el Prof. Israel Salas); el reconciliado es
      el candidato real a `fig:er`
- [ ] Al reconciliado le faltan tipos PostgreSQL y columnas de auditoría — eso es del
      **esquema físico**, no de este grafo lógico. La etapa física ya cerró sus 6
      decisiones (D-11 a D-18 — SGBD, seguridad, redundancia, tipos, dominios y respaldo;
      ver `errores/preguntas-doctor.md` §6 y el artifact de Diseño Físico), pero falta
      ejecutar el DDL real. Ese trabajo no toca este `.puml`, que se queda en BCNF
      estricta a propósito — la única redundancia física (D-04, `ESPECIMEN.idGrupo`) se
      declara solo en el DDL, nunca aquí
- [x] **P-08 / D-03 resuelto (equipo, 2026-09-13):** se reemplaza, no se conserva
      historial de reanálisis. `VIDEO—ANALISIS` baja de (1,N) a (1,1) — ya aplicado en
      `grafo_relacional_reconciliado.puml`, compila. `OBSERVACION` no necesita cambiar:
      sigue referenciando `idVideo` directo, porque con reemplazo nunca hay ambigüedad de
      cuál análisis corresponde a un video
- [x] **D-06 resuelto (equipo, 2026-09-13):** no cambia, se queda en 1:N. Lo que importa
      registrar es el resultado (F1, precisión, recall), no la combinación exacta de
      modelos que lo produjo — no hace falta la relación N:M
- [x] **D-02 ejecutado (2026-09-13):** `idInstitucional` ya es la PK de `USUARIO` en los
      tres grafos (ver §0)
- [x] **D-08 ejecutado (2026-09-13):** `ADMINISTRADOR(idInstitucional* [FK])` agregado a
      `grafo_relacional_reconciliado.puml` en relación (1,1)-(0,1) con `USUARIO` — pasa de
      15 a 16 relaciones, 16 a 17 llaves foráneas. Compila
- [ ] **D-23 pendiente de aplicar (13-sep):** columna nueva `ANALISIS.rutaDiagnostico`
      (nula salvo `estado = 'error'`), que salió de construir
      `diagramas/seq_consulta_progreso.puml` (§3.4) — ni `ANALISIS` ni `REPORTE` tenían
      dónde guardar la ruta del PDF de diagnóstico que genera el Worker. No se toca este
      `.puml` hasta que se pida explícitamente

### 3.3 Diagrama de clases (`diagramas/clases.puml`, `fig:clases` en `:2199`–`:2218`)

**Estado:** 🟢 sin pendientes de decisión — compila (verificado con PlantUML). D-08, D-09
y D-10 resueltos (2026-09-13): `Administrador` no es un tipo aparte, es `Investigador`
con permisos extra — `Investigador` se fusionó con `Usuario` (ya no abstracta) y
`Administrador` hereda de `Usuario`. El progreso del análisis vive solo en memoria de
`PipelineAnalisis`/`Worker`, no toca `Analisis`. `USUARIO` ganó `activo : Boolean`
(justificado con Kendall & Kendall p. 425-426 y Cardona Apéndice A p. 117-118) — ya
aplicado también en `grafo_relacional_final.puml` y `grafo_relacional_reconciliado.puml`.
Solo falta pulir el layout (`Observacion` se encima con el borde de P4 — cosmético) antes
de generar el PNG final para el capítulo.

Qué se recicla tal cual: paquete `P1_Autenticacion_y_usuarios` completo
(`Usuario`/`Investigador`/`Administrador`), las clases de sistema en `P3`
(`Worker`, `PipelineAnalisis`, y **`ROI` — se queda, transitoria**, ver nota abajo), y
`Notificacion` en `P5`.

Qué muere: `Sujeto`, `Animal`, `ResultadoComportamiento`, `ComportamientoPorMinuto` — no
existen como clases de dominio en el modelo nuevo.

> **Respaldo metodológico — Kendall & Kendall, *Análisis y Diseño de Sistemas*, cap. 10
> "Análisis y diseño de sistemas orientados a objetos mediante el uso de UML", pp.
> 298–300 ("Tipos de clases").** El libro divide las clases de un diagrama de clases en
> **cuatro** categorías: de entidad, de límite/interfaz, abstracta y de control. Las
> **clases de control** "controlan el flujo de actividades; actúan como coordinador... a
> menudo se derivan durante el diseño del sistema" (p. 299). Con esta fuente,
> `Worker` y `PipelineAnalisis` son clases de control — no es solo que el diagrama viejo
> ya las metiera así, el propio método las clasifica ahí. Al reconstruir el diagrama,
> usar el estereotipo `<<control>>` en vez del genérico `<<system>>` del diagrama viejo,
> para que la terminología sea la del libro citado.
>
> **Sobre `ROI` — no encaja en ninguna de las cuatro categorías del libro.** La
> definición del libro ata la clase de entidad al DER: "las clases de entidad son las
> entidades representadas en un diagrama de entidad-relación" (p. 299). Como `ROI` no
> está en el DER nuevo (no se persiste, ver `CAMBIOS-CAP5.md` §E), **no califica como
> clase de entidad** con esta fuente — y tampoco es de control, interfaz ni abstracta.
> **Se queda en el diagrama sin estereotipo**, como estructura de apoyo devuelta por
> `PipelineAnalisis.detectarCilindros()`; ponerle `<<entidad>>` sería una cita mal
> aplicada.
>
> **Pendiente — D-07 (idea sin decidir, ver `errores/preguntas-doctor.md` §6):** el
> equipo tiene la idea de que el usuario dibuje el recuadro sobre las 4 ratas antes del
> análisis, en vez de que el pipeline lo detecte solo. **No está confirmada.** Si se
> confirma algún día, `ROI` pasaría de derivado a dato del usuario y **sí calificaría**
> como clase de entidad (y necesitaría tabla en la BD) — revirtiendo la decisión de
> `CAMBIOS-CAP5.md` §E. No dibujar el diagrama de clases asumiendo esto todavía.
>
> **Pendiente de citar:** agregar Kendall & Kendall a `bib/referencias.bib` cuando se
> escriba la prosa del diagrama de clases en el capítulo 5 (todavía no está en el `.bib`).

Qué se agrega: `Grupo`, `Tanda`, `Especimen`, `Observacion`, `Intervalo`, `Conducta`
(ver §0). `Trabajo` se renombra a `Analisis` y cambia sus relaciones: procesa un `Video`
que cuelga de una `Tanda`, usa `Configuracion` (que a su vez referencia `Modelo`).

Checklist antes de dibujar:
- [ ] Cada clase de dominio nueva tiene exactamente los atributos de su relación en
      `grafo_relacional_final.puml` — no atributos inventados para que “se vea completo”
- [ ] Las multiplicidades coinciden con las del conceptual (§3.1), no con las que “se ven
      bien” en el diagrama
- [ ] Si después de editar sigue apareciendo `Sujeto` o `Animal` en cualquier paquete, es
      señal de que la migración quedó a medias
- [x] **D-02 ejecutado:** el atributo de la clase `Usuario` es `idInstitucional` (ver §0)

### 3.4 Diagramas de secuencia

**Estado:** 🟢 los cinco diagramas del dominio experimental están rehechos. Fuente de
cada uno y decisiones que salieron de construirlos, abajo.

**Siguen reciclables sin cambio** (no tocan entidades del dominio experimental): registro
de usuario por admin, login, logout, cambio de contraseña, gestión de usuarios, perfil,
notificaciones.

**Ya no son reciclables — se rehicieron:**

- **Carga de video** → [`diagramas/seq_carga_video.puml`](diagramas/seq_carga_video.puml),
  reemplaza a `seq_carga`. El video ahora cuelga de `Tanda` dentro de `Grupo`, no del
  experimento directo. La pregunta abierta de este mismo §3.4 (¿el sistema pide Grupo+Tanda
  o los infiere?) se resolvió como **D-19**: el investigador escribe el nombre del
  grupo/tratamiento con autocompletado: si coincide con un grupo del mismo experimento, el
  sistema infiere la siguiente tanda (letra A, B, C... en pantalla) y pre-llena un campo
  editable, pero pide confirmación explícita antes de guardar.

- **Análisis automático** →
  [`diagramas/seq_analisis_automatico.puml`](diagramas/seq_analisis_automatico.puml),
  reemplaza a `seq_analisis`. No nombraba `SUJETOS`/`ANIMALES` de forma literal, pero sí
  tenía el participante "Pipeline IA" (término prohibido, ver `CLAUDE.md`) y decía "rastrea
  a los animales" — corregido. Se le agregó el curso alterno de error que le faltaba
  (RN-11, confianza de detección < 0.70) y el registro del nivel de clasificación (D-17).
  Al revisarlo contra `chapters/05_diseno.tex:225-232` salió **D-20**: ese capítulo describe
  procesamiento parcial si detecta menos cilindros de los esperados, pero el equipo decidió
  todo-o-nada (si falla la detección de los 4 cilindros, es error completo) — queda como
  **Q-G**, pendiente de confirmar con el laboratorio.

- **Consulta de progreso** (+ **descarga del reporte de diagnóstico**, fusionado) →
  [`diagramas/seq_consulta_progreso.puml`](diagramas/seq_consulta_progreso.puml),
  reemplaza a `seq_progreso` **y** a `seq_error`. El diagrama viejo de progreso leía
  "estado, etapa y porcentaje" de la base de datos, pero D-09 ya había resuelto que el
  progreso vive solo en memoria del Worker — `ANALISIS` no tiene columna de porcentaje.
  **D-22** resuelve que el porcentaje se aproxima por etapa (25% fijo por cada una de las 4
  etapas de D-16), sin que el Worker comparta memoria con nadie. El viejo `seq_error`
  mezclaba tres cosas que hoy viven cada una en su lugar correcto: que el Worker detecte el
  error (`seq_analisis_automatico.puml`), que el investigador se entere (rama de error de
  este diagrama) y la descarga del PDF de diagnóstico (agregada a esa misma rama en vez de
  vivir en un archivo aparte — CU-08 está marcado "Secundario" en el `.tex`, y Kendall &
  Kendall cap. 10, p. 295-296, dice que los escenarios de menor importancia no siempre
  necesitan su propio diagrama de secuencia; separarlo obligaba a una nota de precondición
  que solo repetía lo que ya pasa en este mismo diagrama). De ahí salió **D-23**: ni
  `ANALISIS` ni `REPORTE` tenían dónde guardar la ruta del PDF de diagnóstico — se agrega
  `ANALISIS.rutaDiagnostico`, pendiente de aplicar al grafo relacional (ver §3.2).

- **Consulta de resultados** →
  [`diagramas/seq_consulta_resultados.puml`](diagramas/seq_consulta_resultados.puml),
  reemplaza a `seq_resultados`. Ya no es "por animal" comparando Día 1 vs Día 2 — ahora es
  la comparación real que pide el protocolo, **entre los tres grupos** usando solo el Día 2
  (ver [`errores/preguntas-doctor.md`](errores/preguntas-doctor.md) sección "Ya
  respondido"). Al construirlo salieron dos preguntas de laboratorio, no de equipo —
  **Q-E** (¿se compara por promedio o por total del grupo?) y **Q-F** (¿qué hacer si un
  grupo mezcla especímenes "preciso" y "agrupado", D-17?) — ambas con una decisión
  provisional (promedio; mostrar separado con aviso) documentada en el propio `.puml`.

- **Descarga de reportes** →
  [`diagramas/seq_descarga_reportes.puml`](diagramas/seq_descarga_reportes.puml),
  reemplaza a `seq_reportes`. `REPORTE` sigue colgando de `EXPERIMENTO`, sin cambio de
  fondo en el modelo, pero CU-10 ya insinuaba caché ("el sistema genera o recupera el
  archivo") sin decir cómo se invalida — **D-21** resuelve que se regenera solo si hubo un
  análisis más reciente que el reporte guardado (reanálisis, D-03).

### 3.5 Diagramas de casos de uso (`:581`–`:2042`)

**Estado:** 🟢 casi no cambian (ver `CAMBIOS-CAP5.md` C5-08). Tres retoques, no diagramas
nuevos:
- [ ] Retirar la transacción "seguir a la misma rata entre experimentos" — imposible, el
      número se reinicia por grupo y las ratas se sacrifican al terminar
- [ ] El Día 1 es opcional para **cualquier** grupo, no exclusivo del control
- [ ] El grupo no tiene tope superior de especímenes (lo pidió el laboratorio en la
      reunión del 3-sep)

### 3.6 Mockups de UI (`ui_resultados_*`, `ui_nuevo_*`, `ui_admin_*`)

**Estado:** ⚪ sin auditar. Pendiente revisar si muestran resultados "por animal" en vez
de por espécimen dentro de un grupo, y si el formulario de "nuevo experimento" pide
Grupo+Tanda o sigue asumiendo un experimento = una grabación. No bloquea los diagramas de
datos; auditar por separado cuando toque la sección de interfaz.

### 3.7 `docs/diagramas.pdf` páginas 1–3 (arquitectura, flujo general, pipeline)

Mayormente genéricas y reciclables — no nombran entidades de dominio salvo la página 1.

- [x] **Página 1 (arquitectura por capas) — rehecha (13-sep):**
      [`diagramas/arquitectura_software.puml`](diagramas/arquitectura_software.puml). El
      contenedor `Docker: db` ya no lista las 12 tablas viejas — remite al diagrama de
      esquema físico en vez de repetir las 16 relaciones aquí. De paso, al revisar el
      archivo completo (no solo la lista de tablas) salió un segundo problema que no
      estaba en este pendiente: el diagrama tenía un contenedor `Docker: redis` con cola
      de mensajes que **no existe en ningún capítulo** — `05_diseno.tex:38-39` dice
      explícitamente "tres capas... frontend, backend y base de datos. Un cuarto
      contenedor —el worker—" (cuatro contenedores, nunca cinco), y el mecanismo real,
      confirmado en CU-07, es *polling* del Worker a la tabla de análisis, sin cola de
      mensajes aparte. Se quitó Redis y se agregó el volumen de modelos entrenados
      (`rat.pt`, `resnet18_fst.pt`, `resnet50_fst.pt`) que `05_diseno.tex:47-49` sí
      menciona y el diagrama viejo no tenía.
- [x] **Página 2 (flujo general) — rehecha (13-sep):**
      [`diagramas/flujo_general.puml`](diagramas/flujo_general.puml) (no había fuente
      editable, solo la imagen). El bloque "Referencia y validación" encadenaba
      Anotación experta (conjunto de prueba) → Dataset de referencia → Entrenamiento del
      modelo — es decir, alimentaba el entrenamiento con la anotación del Dr. Sandino
      guardada como "conjunto de prueba", que es un gold standard con otro nombre.
      Corregido dos veces: la primera versión seguía usando BORIS como conjunto de
      prueba (insuficiente); la versión final no usa BORIS/anotación experta en ningún
      punto — entrenamiento y prueba propia salen de los mismos clips inequívocos, según
      la "Prohibición vigente" de `CLAUDE.md`. Sigue marcado "provisional" porque esa
      prohibición depende de una pregunta abierta sin confirmar con el Dr. Sandino.
- [x] **Página 3 (pipeline) — verificado a fondo el 2026-09-12**, no solo por inspección
      visual: se leyó completo `chapters/05_diseno.tex:102`–`234` (los 5 módulos +
      "Separación por espécimen"). Los módulos describen procesamiento de video cuadro a
      cuadro (contraste, cilindros, tracking YOLOv8/ByteTrack, clasificación ResNet en
      cascada) — nunca dependieron de `Grupo`/`Tanda`/`Experimento`, y "Separación por
      espécimen" asigna por posición espacial del cilindro, no por estructura de grupo.
      **Confirmado: no requiere cambio de fondo — pero solo mientras D-07 siga sin
      decidir.** Los métodos de `PipelineAnalisis` en `diagramas/clases.puml` (§3.3) se
      verificaron contra estos 5 módulos uno a uno. **Contingencia real, no hipotética:**
      D-07 no es solo el recuadro — también cubre que el usuario ajuste a mano la línea
      de agua del Módulo 2 (ver `errores/preguntas-doctor.md` §6). Si se confirma
      cualquiera de las dos, el Módulo 2 deja de describir detección 100% automática, y
      hay que rehacer: la prosa de `chapters/05_diseno.tex:127`–`134`, el diagrama de
      esta página, y los métodos `detectarCilindros()` / la estimación de línea de agua
      en `PipelineAnalisis`. No es trabajo perdido si eso pasa — es la razón por la que
      D-07 sigue abierto en vez de cerrado en falso.
  - [ ] **Pendiente sin resolver (13-sep) — revisar el texto de la imagen, no solo el
        contenido.** Esta página no tiene fuente editable (era raster puro, a diferencia
        de las páginas 1 y 2, que ya se recrearon en `.puml`), así que lo de abajo no se
        pudo corregir directamente, solo se deja anotado:
        1. El nodo "¿Confianza ResNet-18?" / "¿Confianza ResNet-50?" se ve como un umbral
           ya decidido, igual que el 0.70 de RN-11 (detección de cilindros) — pero
           `05_diseno.tex:162-163` dice que ese umbral de la cascada de clasificación
           "se definirá durante la fase de validación en TT-II", **todavía no existe**.
           Falta una nota visual que distinga ambos casos.
        2. Las etiquetas en inglés "swim / immobile / escape" (ResNet-18) y "swim s,
           immobile s, escape s" (etapa de Resultados) no coinciden con los nombres de
           columna que el propio capítulo 5 usa para lo mismo — `nado_s`, `inmovil_s`,
           `escape_s` (`05_diseno.tex:211-212`) — ni con la terminología en español del
           resto del documento (nado activo, inmovilidad, escalamiento). Quedaron así
           porque nunca se recreó esta página como `.puml`; hace falta rehacerla (no solo
           retocar el texto de la imagen) para corregirlo.

---

## 4. Checklist transversal — antes de dar cualquier diagrama por "definitivo"

- [ ] ¿Cada entidad/tabla tiene una fuente de rango ≤3 en la jerarquía de
      [`errores/README.md`](errores/README.md), o está marcada como pregunta abierta?
- [ ] ¿"Experimento" se usa solo para el estudio completo, nunca para una sola grabación?
- [ ] ¿Aparecen `Grupo` y `Tanda` en todo lo que hable de cómo se organizan ratas/videos?
- [ ] ¿Nada dice "cámara de celular", "animales" ni "inteligencia artificial" a secas, y
      nada reintroduce κ de Cohen, MAE o "gold standard"? (ver `CLAUDE.md`)
- [ ] Si es conceptual: ¿está en lenguaje natural, sin SQL ni tipos de dato?
- [ ] ¿Se revisó contra los pendientes abiertos (P-08/D-03, D-02, D-04, D-05, D-06, D-19 a
      D-23, Q-08, Q-09, Q-E, Q-F, Q-G, revisión de la Dra. Cordero) antes de llamarlo
      "definitivo"?

---

## 5. Bitácora de esta sesión de migración

| Diagrama | Estado | Nota |
|---|---|---|
| DER conceptual | 🟢 hecho | verificar checklist §3.1 antes de dar por cerrado |
| Grafo relacional (inicial+final+reconciliado) | 🟡 insumo listo | falta compilar a PNG e insertar en el `.tex`. Reconciliado ya con `ADMINISTRADOR` (16 relaciones); pendiente D-23 (`rutaDiagnostico`), no se aplica hasta que se pida |
| Diagrama de clases | 🟢 sin pendientes de decisión | solo falta pulir layout cosmético |
| Secuencia — Carga de video | 🟢 hecho | `seq_carga_video.puml`, inferencia de tanda por D-19 |
| Secuencia — Análisis automático | 🟢 hecho | `seq_analisis_automatico.puml`, todo-o-nada por D-20 (provisional, ver Q-G) |
| Secuencia — Consulta de progreso + diagnóstico | 🟢 hecho | `seq_consulta_progreso.puml` (fusiona el viejo `seq_progreso` y `seq_error`), % por etapa (D-22), `rutaDiagnostico` (D-23) |
| Secuencia — Consulta de resultados | 🟢 hecho | `seq_consulta_resultados.puml`, comparación entre grupos, Día 2; promedio/nivel mixto provisional (Q-E, Q-F) |
| Secuencia — Descarga de reportes | 🟢 hecho | `seq_descarga_reportes.puml`, caché con invalidación por reanálisis (D-21) |
| Casos de uso | 🟢 casi listo | solo 3 retoques, ver §3.5 |
| Mockups de UI | ⚪ sin auditar | |
| Arquitectura pág. 1 (`docs/diagramas.pdf`) | 🟢 hecho | `arquitectura_software.puml`: quitó las 12 tablas viejas y el contenedor Redis inexistente (era polling), agregó el volumen de modelos entrenados |
| `idBoleta` → `idInstitucional` en `USUARIO` (D-02) | 🟢 ejecutado | renombrado en los 3 grafos + `clases.puml`, compilan |

---

## 6. Cuándo borrar este archivo

Borrar cuando las tres condiciones se cumplan:
1. Los diagramas de datos del capítulo 5 (§3.1–3.3) están regenerados y reflejan el
   modelo nuevo.
2. `CAMBIOS-CAP5.md` tiene los ítems C5-02, C5-03, C5-04 y C5-07 en 🟢.
3. Ya no hace falta consultar la tabla de equivalencia (§2) porque el `.tex` está
   reescrito y es la referencia directa.

Si el trabajo se detiene a medias, mueve lo que siga siendo útil a `CAMBIOS-CAP5.md`
antes de borrar — este archivo no es la fuente permanente, es el andamiaje.
