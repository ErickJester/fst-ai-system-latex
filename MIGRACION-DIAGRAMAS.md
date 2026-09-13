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
con la corrección de la reunión del 3-sep (`GRUPO.tratamiento` nunca nulo).

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
> **Tres pendientes que `CAMBIOS-CAP5.md` no tiene todavía** (salieron de la
> reconciliación del 6-sep, son del equipo, no del laboratorio — ver §3.2 y §4):
> - **D-05** — ¿el sistema permite correr dos veces la misma `CONFIGURACION` sobre el
>   mismo video? Decide si `(idVideo, idConfig)` es clave alterna de `ANALISIS`.
> - **D-06** — el pipeline usa más de un modelo (YOLOv8 + ResNet-18/50), pero
>   `CONFIGURACION` solo guarda un `hashModelo`. Puede necesitar que
>   `MODELO`↔`CONFIGURACION` sea N:M en vez de 1:N — **revisar antes de dar el grafo
>   relacional por definitivo** (§3.2).
> - **Q-09** — ¿`NOTIFICACION.mensaje` lleva detalle por instancia o es plantilla por
>   tipo? Si es plantilla, `tipo → mensaje` sería transitiva y haría falta un catálogo
>   `TIPO_NOTIFICACION`.

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
```

**Dominio experimental (11 relaciones, lo que el laboratorio reconoce):** `USUARIO`,
`EXPERIMENTO`, `GRUPO`, `TANDA`, `ESPECIMEN`, `VIDEO`, `ANALISIS`, `OBSERVACION`,
`INTERVALO`, `CONDUCTA`, `PRESENTA`.

**Soporte de sistema (4 relaciones, el laboratorio no las nombra):** `MODELO`,
`CONFIGURACION`, `REPORTE`, `NOTIFICACION`.

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

> **D-02 resuelto (2026-09-12).** `USUARIO.idBoleta` estaba mal — confirmado y ya
> corregido en `errores/preguntas-doctor.md` §6. **Nuevo esquema: un identificador
> institucional único** (nombre de atributo propuesto: `idInstitucional`), que acepta
> boleta (estudiantes) o número de empleado (personal), con una regla de formato/tipo
> pendiente de afinar para distinguir cuál es cuál — detalle menor, no bloquea el §3.2 ni
> el §3.3. **Falta ejecutar el renombre** en `diagramas/grafo_relacional_final.puml` y
> `diagramas/grafo_relacional_reconciliado.puml` (hoy siguen con `idBoleta`); hacerlo
> cuando se toquen esos archivos, junto con el diagrama de clases nuevo.

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
| `USUARIOS` | `USUARIO` | Sobrevive. PK pasa de `id` autogenerado a `idBoleta` — **pero ver el hallazgo de §0**: D-02 (rango 1) ya dijo que la boleta no sirve para personal con nombramiento. Nombre de la PK probablemente cambia |
| `EXPERIMENTOS` | `EXPERIMENTO` | Sobrevive, pero pierde `tratamiento`, `especie`, `disposicion` — esos bajan a `GRUPO` (el tratamiento es por grupo, no por experimento completo) |
| `VIDEOS` | `VIDEO` | Sobrevive, pero ahora cuelga de `TANDA`, no de `EXPERIMENTO`. `dia` → `sesion` |
| `SUJETOS` | `ESPECIMEN` | Sobrevive, pero cuelga de `TANDA`, no de `EXPERIMENTO`. `indice_rata`+`etiqueta` → `numeroRata`+`numeroCilindro` |
| `ROIS` | — | **Eliminada.** Es un derivado que el pipeline recalcula; no se almacena (ver §E de `CAMBIOS-CAP5.md`) |
| `CONFIGURACIONES_ANALISIS` | `CONFIGURACION` + `MODELO` | Se parte en dos por 3FN: `hashModelo → nombreModelo` es una dependencia transitiva real |
| `TRABAJOS` | `ANALISIS` | Renombrada. Ya no tiene `parametros` sueltos; referencia `CONFIGURACION` por FK |
| `ANIMALES` | — | **Desaparece como tabla de enlace.** El enlace espécimen↔video lo hace `OBSERVACION` |
| `RESULTADOS_COMPORTAMIENTO` + `COMPORTAMIENTO_POR_MINUTO` | `OBSERVACION` → `INTERVALO` → `PRESENTA` | Se funden. Solo se guarda `segundos` por intervalo de un minuto; los totales se derivan en consulta |
| `REPORTES` | `REPORTE` | Casi igual, FK sigue siendo a `EXPERIMENTO` |
| `NOTIFICACIONES` | `NOTIFICACION` | Casi igual, FK de usuario ahora es `idBoleta` |

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
`diagramas/grafo_relacional_reconciliado.puml` (+ 4 tablas de sistema, este es el que de
verdad sustituye a `fig:er`).

Antes de maquetar:
- [ ] Van los **tres** grafos, no solo uno: inicial y final son el par obligatorio que
      documenta el paso de validación (lo pidió el Prof. Israel Salas); el reconciliado es
      el candidato real a `fig:er`
- [ ] Al reconciliado le faltan tipos PostgreSQL y columnas de auditoría — eso es etapa
      física, todavía no arranca (`DISENO-BD.md` §5 «Lo que falta»)
- [ ] Revisar **P-08 / D-03** (mismo pendiente, ver §0) antes de compilar como definitivo:
      si el laboratorio quiere conservar historial de reanálisis, `OBSERVACION` debe
      referenciar `idAnalisis` en vez de `idVideo`, y `VIDEO—ANALISIS` se queda en (1,N)
      tal como está; si no, baja a (1,1) y el esquema es más simple. El laboratorio ya dijo
      que se queda con el último análisis — falta cerrarlo formalmente
- [ ] Revisar **D-06**: si `CONFIGURACION` necesita referenciar más de un `MODELO` (el
      pipeline usa YOLOv8 + ResNet-18/50), la relación `MODELO`↔`CONFIGURACION` del grafo
      podría ser N:M y no 1:N. No dibujar la cardinalidad como cerrada sin resolver esto
- [ ] **D-02 resuelto:** usar `idInstitucional` en vez de `idBoleta` como PK de `USUARIO`
      al regenerar este grafo (ver §0)

### 3.3 Diagrama de clases (`diagramas/clases.puml`, `fig:clases` en `:2199`–`:2218`)

**Estado:** 🟡 borrador hecho, compila (verificado con PlantUML 2026-09-12). Falta pulir
el layout (`Observacion` se encima con el borde de P4 — cosmético) y cerrar D-08/D-09
antes de generar el PNG final para el capítulo.

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
- [ ] **D-02 resuelto:** el atributo de la clase `Usuario` se llama `idInstitucional`, no
      `idBoleta` (ver §0)

### 3.4 Diagramas de secuencia

**Reciclables sin cambio** (no tocan entidades del dominio experimental): registro de
usuario por admin, login, logout, cambio de contraseña, gestión de usuarios, perfil,
notificaciones, manejo de error de calidad de video, consulta de progreso.

**Necesitan revisión:**

- **Carga de video** (`seq_carga`, pág. 14 del PDF viejo). Hoy sube el video "para ese
  día" directo al experimento. En el modelo nuevo el video pertenece a una `Tanda` dentro
  de un `Grupo`. Pregunta antes de rehacerlo: ¿la pantalla le pide Grupo+Tanda al
  investigador, o el sistema los infiere del orden de carga? Si no hay fuente que lo
  responda, es pregunta abierta, no se inventa.

- **Consulta de resultados** (`seq_resultados`, pág. 18). Hoy es "por animal", comparando
  Día 1 vs Día 2. La comparación real que pide el protocolo es **entre grupos**
  (control/fluoxetina/tratamiento) usando solo el Día 2 — ver
  [`errores/preguntas-doctor.md`](errores/preguntas-doctor.md) sección "Ya respondido":
  *"Qué se compara — Los 5 minutos del Día 2, entre los tres grupos"*. Reescribir la
  secuencia sobre esa comparación, no sobre día1-vs-día2 por animal.

- **Análisis automático** (`seq_analisis`). Revisar si nombra `SUJETOS`/`ANIMALES`
  explícitamente. Si solo habla de `Video`/`Trabajo` en abstracto, sobrevive con
  renombrar `Trabajo` → `Análisis`.

- **Descarga de reportes** (`seq_reportes`). Cambio menor: `REPORTE` sigue colgando de
  `EXPERIMENTO`, no hay impacto de fondo.

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

- [ ] **Página 1 (arquitectura por capas):** el contenedor `Docker: db` lista las 12
      tablas viejas (`USUARIOS EXPERIMENTOS VIDEOS TRABAJOS...`). Sustituir por las 15
      nuevas o quitar la lista y remitir a la figura del esquema físico.
- [x] **Página 3 (pipeline) — verificado a fondo el 2026-09-12**, no solo por inspección
      visual: se leyó completo `chapters/05_diseno.tex:102`–`234` (los 5 módulos +
      "Separación por espécimen"). Los módulos describen procesamiento de video cuadro a
      cuadro (contraste, cilindros, tracking YOLOv8/ByteTrack, clasificación ResNet en
      cascada) — nunca dependieron de `Grupo`/`Tanda`/`Experimento`, y "Separación por
      espécimen" asigna por posición espacial del cilindro, no por estructura de grupo.
      **Confirmado: no requiere cambio — pero solo mientras D-07 siga sin decidir.**
      Los métodos de `PipelineAnalisis` en `diagramas/clases.puml` (§3.3) se verificaron
      contra estos 5 módulos uno a uno. **Contingencia real, no hipotética:** D-07 no es
      solo el recuadro — también cubre que el usuario ajuste a mano la línea de agua del
      Módulo 2 (ver `errores/preguntas-doctor.md` §6). Si se confirma cualquiera de las
      dos, el Módulo 2 deja de describir detección 100% automática, y hay que rehacer:
      la prosa de `chapters/05_diseno.tex:127`–`134`, el diagrama de esta página, y los
      métodos `detectarCilindros()` / la estimación de línea de agua en
      `PipelineAnalisis`. No es trabajo perdido si eso pasa — es la razón por la que D-07
      sigue abierto en vez de cerrado en falso.
- Página 2 (flujo general): no nombra tablas, no requiere cambio (sin verificación tan
  exhaustiva como la página 3, pero es un diagrama de bloques genérico sin prosa propia
  que auditar).

---

## 4. Checklist transversal — antes de dar cualquier diagrama por "definitivo"

- [ ] ¿Cada entidad/tabla tiene una fuente de rango ≤3 en la jerarquía de
      [`errores/README.md`](errores/README.md), o está marcada como pregunta abierta?
- [ ] ¿"Experimento" se usa solo para el estudio completo, nunca para una sola grabación?
- [ ] ¿Aparecen `Grupo` y `Tanda` en todo lo que hable de cómo se organizan ratas/videos?
- [ ] ¿Nada dice "cámara de celular", "animales" ni "inteligencia artificial" a secas, y
      nada reintroduce κ de Cohen, MAE o "gold standard"? (ver `CLAUDE.md`)
- [ ] Si es conceptual: ¿está en lenguaje natural, sin SQL ni tipos de dato?
- [ ] ¿Se revisó contra los pendientes abiertos (P-08/D-03, D-02, D-04, D-05, D-06, Q-08,
      Q-09, revisión de la Dra. Cordero) antes de llamarlo "definitivo"?

---

## 5. Bitácora de esta sesión de migración

| Diagrama | Estado | Nota |
|---|---|---|
| DER conceptual | 🟢 hecho | verificar checklist §3.1 antes de dar por cerrado |
| Grafo relacional (inicial+final+reconciliado) | 🟡 insumo listo | falta compilar a PNG e insertar en el `.tex` |
| Diagrama de clases | 🟡 borrador compila | pendiente: layout + D-08/D-09 (ver `PREGUNTAS.md`) |
| Secuencia — Carga de video | 🔴 no iniciado | pregunta abierta: ¿UI pide Grupo+Tanda o los infiere? |
| Secuencia — Consulta de resultados | 🔴 no iniciado | cambiar a comparación entre grupos, Día 2 |
| Secuencia — Análisis automático | ⚪ sin auditar | revisar si nombra SUJETOS/ANIMALES |
| Secuencia — Descarga de reportes | ⚪ sin auditar | cambio menor esperado |
| Casos de uso | 🟢 casi listo | solo 3 retoques, ver §3.5 |
| Mockups de UI | ⚪ sin auditar | |
| Arquitectura pág. 1 (`docs/diagramas.pdf`) | 🔴 no iniciado | lista de tablas desactualizada |
| `idBoleta` en `USUARIO` (D-02) | 🟢 resuelto | renombrar a `idInstitucional` al tocar §3.2 y §3.3 |

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
