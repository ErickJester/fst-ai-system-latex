# Auditoría DR — diagramas relacionales y de clases

Fecha: 2026-10-11 · Agente DR (solo lectura) · Repo en HEAD `da96c00`.

## Alcance auditado

Leídos completos: `diagramas/grafo_relacional_3_vigente.puml` (base de verdad), `diagramas/clases.puml`,
`diagramas/esquema_fisico.puml`, `diagramas/relacional.puml`, `diagramas/esquema_conceptual.tex`,
cabeceras de `grafo_relacional_1_inicial.puml` y `_2_laboratorio.puml`,
`diagramas/diagram_design/clases_completo.md`, `clases_completo.html` (comparado texto a texto con el
generador), `generadores/gen_clases.py`, `back/apendice_D.tex` (completo), `chapters/05_diseno.tex`
(§ pipeline módulos 2–4 y § base de datos, normalización, diagrama de clases: líneas 160–300 y 340–655,
2538–2572). Además abrí como imagen `diagramas/clases.png`, `figures/mermaid/esquema_fisico.png`,
`diagramas/esquema_conceptual.pdf` y `diagramas/er.png`. Contexto: `DISENO-BD.md`, `PENDIENTES-ERICK.md`,
`PREGUNTAS.md`, filas D-23, D-24, D-28, D-29, D-35, D-40, D-53, D-54, D-55 de `errores/preguntas-doctor.md`.

### Conteos verificados (contando de verdad)

- Grafo vigente: **15 relaciones, 63 atributos, 17 FK lógicas** (7+5+5+4+3+6+6+3+3+1+3+4+1+5+7 = 63; FK: EXPERIMENTO 1, GRUPO 1, TANDA 1, ESPECIMEN 1, VIDEO 1, ANALISIS 1, OBSERVACION 2, INTERVALO 1, PRESENTA 2, SEGUNDO 2, ADMINISTRADOR 1, REPORTE 1, NOTIFICACION 2 = 17) y 17 aristas. Coincide con su cabecera.
- Físico: 63 + `ANALISIS.rutaDiagnostico` = **64 atributos, 17 FK** y 17 aristas. Apéndice D: 64 filas de columnas y 8 dominios; coincide con el `.puml`.
- Clases: 18 clases (coincide con `clases_completo.md`); 24 relaciones más la clase asociativa; `clases_completo.html` está en sincronía con `gen_clases.py` (mismas 161 etiquetas de texto, mismos miembros y multiplicidades) y con `clases.puml`.
- Cardinalidades D-28 y D-29 (Tanda–Espécimen 2..4, Video–Observación 2..4, Intervalo–Presenta 2..4, Grupo–Tanda 1..*): iguales en grafo, físico, clases, conceptual y apéndice D. La única discrepancia de sentido está en DR-02 (orden de la multiplicidad) y DR-03 (Experimento–Notificación).
- Ninguno de los nombres removidos (`numeroRata`, `idConfig`, `MODELO`, `CONFIGURACION`, `ANALISIS.confianza`, `SEGUNDO.clase`, `SEGUNDO.propuesta`, `idGrupo` en `ESPECIMEN`) sigue como columna en grafo vigente, físico, clases, conceptual, cap. 5 ni apéndice D; solo aparecen en comentarios históricos y en `relacional.puml` / `grafo_relacional_2` (históricos).
- «DER» se usa bien en el cap. 5 (L350, L366, solo para el conceptual); no hay «DER» mal aplicado a tablas con tipos.

## Resumen por severidad

| Alta | Media | Baja | Total | de ellas «pregunta abierta» |
|---|---|---|---|---|
| 1 | 9 | 3 | 13 | 2 (DR-04, DR-07) |

---

## Alta

### DR-01 — `diagramas/clases.png` (el que entra al cap. 5) quedó desactualizado frente a `clases.puml`
- Severidad: Alta
- Ubicación: `diagramas/clases.png` (último commit `1abb6f7`, 6-oct); `diagramas/clases.puml:90,96-109,123,182-183` (commit `a20d40e`, 8-oct); `chapters/05_diseno.tex:2568` (`\includegraphics{diagramas/clases}`); `chapters/05_diseno.tex:2561-2564`.
- Cita: imagen: clase `ROI` con solo «-x -y -w -h», sin nota, sin asociación con `Especimen`, `Observacion` sin miembros y «+clasificarConducta(especimen, frame) : String» vs `clases.puml`: «-numeroCilindro … -yAgua : Integer -yFondo : Integer», nota «No se guarda en la base de datos», «Especimen "1" --> "0..*" ROI», «+calcularBloques() : List<String>», «+clasificarConducta(especimen, roi, segundo) : String», «PipelineAnalisis ..> "2..4" ROI».
- Fuente que decide: rango 1 (cambios del 8-oct a partir de la revisión de quien construye el clasificador, commit `a20d40e`) y `grafo_relacional_3_vigente.puml:42-49` («ROIS … no entra»). El PNG publicado muestra a `ROI` con atributos `x, y, w, h` sin la nota que aclara que no es una tabla: sin respaldo en el grafo vigente. Además `clases_completo.png` sí está al día; solo `clases.png` no.
- Corrección sugerida: regenerar `diagramas/clases.png` desde `clases.puml` (`java -jar plantuml.jar -tpng diagramas/clases.puml`). Después, en el cap. 5 (L2561-2564) agregar una frase sobre `ROI` («objeto del pipeline que delimita el cilindro de cada espécimen; no se guarda en la base de datos») y sobre `Segundo`, que el texto de la figura omite.

---

## Media

### DR-02 — Multiplicidad `Intervalo 2..4 — Conducta` escrita al revés (UML) en clases, generador, HTML y PNG
- Severidad: Media
- Ubicación: `diagramas/clases.puml:196`; `diagramas/diagram_design/generadores/gen_clases.py:125`; `clases_completo.html` (mismas etiquetas `2..4` / `0..*`); `diagramas/clases.png` («2..4» junto a `Intervalo`, «0..*» junto a `Conducta`).
- Cita: «Intervalo "2..4" -- "0..*" Conducta : presenta» (clases.puml) vs «INTERVALO "1" --o "2..4" PRESENTA» y «CONDUCTA "1" --o "0..*" PRESENTA» (grafo vigente, L248-249); `esquema_conceptual.tex:166-167`: «Intervalo (2,4)» y «Conducta (0,N)» en notación Chen.
- Fuente que decide: D-29 («`INTERVALO–PRESENTA` pasa de (2,3) a (2,4)»); el grafo fija «un intervalo tiene de 2 a 4 conductas». En el mismo `clases.puml` las demás asociaciones usan la convención UML (el número junto a la clase de la que se cuenta el otro extremo, p. ej. `Tanda "1" *--> "2..4" Especimen`); esta línea copió el orden de Chen. Leída como UML dice que cada conducta aparece en 2 a 4 intervalos. `PENDIENTES-ERICK.md` M-25 lo marca como «dudosa»; aquí está verificado que es un error de orden.
- Corrección sugerida: `Intervalo "0..*" -- "2..4" Conducta : presenta`. En `gen_clases.py:125` cambiar a `PLAIN, '0..*', '2..4', ''`; regenerar `clases_completo.html/.png` y `clases.png`.

### DR-03 — Experimento–Notificación: `NOTIFICACION.idExperimento` es nulo, pero grafo y físico dibujan «1» y clases dibuja «0..1»
- Severidad: Media
- Ubicación: `diagramas/grafo_relacional_3_vigente.puml:228,255`; `diagramas/esquema_fisico.puml:315,333`; `diagramas/clases.puml:200`; `gen_clases.py:114-115`; `back/apendice_D.tex:247`.
- Cita: «idExperimento   [FK] (nulo)» + «EXPERIMENTO "1" --o "0..*" NOTIFICACION» (grafo); «idExperimento : integer <<FK>> (nulo)» + «EXPERIMENTO "1" --o "0..*" NOTIFICACION» (físico) vs «Experimento "0..1" --> "0..*" Notificacion : origina» (clases); apéndice D: «Nulo: Sí … Es nulo en la alerta de disco».
- Fuente que decide: el propio grafo, que en `SEGUNDO.conducta (nulo)` sí dibuja «CONDUCTA "0..1"» (L203, L252). Una FK que admite nulo implica extremo opcional (0..1).
- Corrección sugerida: `EXPERIMENTO "0..1" --o "0..*" NOTIFICACION` en `grafo_relacional_3_vigente.puml:255` y en `esquema_fisico.puml:333`; regenerar `figures/mermaid/esquema_fisico.png`. `clases.puml` ya está bien.

### DR-04 — Video de Día 1 sin análisis ni observaciones (D-54 d) contra cardinalidades «1» y «2..4» (pregunta abierta)
- Severidad: Media
- Ubicación: `diagramas/grafo_relacional_3_vigente.puml:244-246`; `diagramas/esquema_fisico.puml:71-73,339-342`; `diagramas/esquema_conceptual.tex:135-137,143-144,147-148,153`; `diagramas/clases.puml:176,189-190`; `back/apendice_D.tex:159,172,191`; `chapters/05_diseno.tex:356-358` y `:2549-2550`.
- Cita: «VIDEO "1" --o "1" ANALISIS», «VIDEO "1" --o "2..4" OBSERVACION», «ESPECIMEN "1" --o "1..2" OBSERVACION» (grafo); «(1,2): una por sesión. Mínimo 1 porque el Día 1 es opcional» (conceptual, L147); «Un video tiene un solo análisis vigente» y «Cada video tiene de 2 a 4 observaciones» (apéndice D); «cada video se procesa mediante un análisis» (cap. 5) vs D-54 (d): «El Día 1 solo confirma que ese video existe y es de habituación … no se analiza ni conserva un recorte» y `esquema_fisico.puml:72-73` «el Dia 1 solo confirma que existe el video de habituacion; no se analiza, D-54».
- Fuente que decide: pregunta abierta → equipo. La fila D-54 dice que la cobertura de (a) y (d) «no se aplica hasta que se pida» en caps./artifacts, pero nadie registró el efecto sobre el modelo: si `VIDEO` (Día 1) no tiene `ANALISIS` ni `OBSERVACION`, entonces `VIDEO–ANALISIS` es (0,1), `VIDEO–OBSERVACION` (0,4) (o 2..4 solo para Día 2) y `ESPECIMEN–OBSERVACION` queda en (1,1) (solo Día 2). Hoy el modelo promete un análisis y de 2 a 4 observaciones por cada video, incluido el de Día 1. No consta en `PENDIENTES.md`, `PENDIENTES-ERICK.md` ni `PREGUNTAS.md`.
- Corrección sugerida: decidir una de dos: (i) el video de Día 1 se guarda en `VIDEO` sin análisis: cambiar las cardinalidades a `VIDEO "1" --o "0..1" ANALISIS` y `VIDEO "1" --o "0..4" OBSERVACION` (o separar el Día 1 de las reglas), y ajustar `ANALISIS.idVideo` UNIQUE/NOT NULL no cambia; (ii) el Día 1 también genera `ANALISIS` pero marcado de otra forma (contradice D-54 d). Hasta decidir, no tocar los diagramas; registrar como D-xx en `errores/preguntas-doctor.md` §6.

### DR-05 — `clases_completo.md` dice que el documento «no tiene» los valores de `origen` `humano_ciego` y `sin_revisar`; el apéndice D y el físico los definen
- Severidad: Media
- Ubicación: `diagramas/diagram_design/clases_completo.md:88-92`; `back/apendice_D.tex:65`; `diagramas/esquema_fisico.puml:83-85`; `chapters/05_diseno.tex:446-448`.
- Cita: «ni los valores de `origen` `humano_ciego` y `sin_revisar`, que el documento no tiene» (md) vs «`sin_revisar`: el usuario lo etiquetó sin llegar a verlo en el video. `humano_ciego`: etiquetado en el modo de revisión que oculta la conducta del sistema» (apéndice D, Tabla de dominios) y «'humano_corrige','humano_duda','sin_revisar','humano_ciego')» (físico). Cap. 5 L448 resume el origen como «del sistema, confirmada, corregida o dudosa» (4 de los 6 valores).
- Fuente que decide: rango 1, D-35 y D-40 aplicados en `esquema_fisico.puml` y apéndice D (6 valores del dominio `origen_segundo`).
- Corrección sugerida: en `clases_completo.md` reemplazar la frase por «el atributo `origen` de `Segundo` es una cadena; sus seis valores (`maquina`, `humano_confirma`, `humano_corrige`, `humano_duda`, `sin_revisar`, `humano_ciego`) están en el apéndice D». En el cap. 5 L448 completar: «(del sistema, confirmada, corregida, dudosa, sin revisar o etiquetada a ciegas)».

### DR-06 — El cap. 5 afirma que físico y lógico tienen «las mismas columnas»; el físico tiene una más (`ANALISIS.rutaDiagnostico`)
- Severidad: Media
- Ubicación: `chapters/05_diseno.tex:595-596`, `:648`, `:426-428`; `diagramas/grafo_relacional_3_vigente.puml:164-172`; `diagramas/clases.puml:111-117`; `diagramas/esquema_fisico.puml:219`; `back/apendice_D.tex:182`.
- Cita: «El esquema físico tiene las mismas columnas que el lógico, sin columnas repetidas» (cap. 5) vs 63 atributos del grafo (sin `rutaDiagnostico`) y 64 del físico/apéndice D.
- Fuente que decide: D-23 (columna vigente, «pendiente de aplicar» en el grafo) y D-53 (6) (se mantiene). El hueco del grafo y de `clases.puml` ya está registrado (`DISENO-BD.md` §5 y `PENDIENTES-ERICK.md` M-24/M-25); lo nuevo es que el texto del cap. 5 lo contradice de forma explícita y el cap. 5 L426-428 sí describe la ruta del diagnóstico.
- Corrección sugerida: o bien aplicar D-23 al grafo (cuando el equipo lo pida) y subir a 64 atributos, o bien reescribir L595-596: «El esquema físico agrega la columna `ANALISIS.rutaDiagnostico` y los tipos de dato; por lo demás tiene las mismas columnas que el lógico. Con ello también cumple FNBC.» Ajustar L648 igual.

### DR-07 — El cap. 5 nombra «el esquema lógico» pero nunca lo muestra ni lo introduce (pregunta abierta)
- Severidad: Media
- Ubicación: `chapters/05_diseno.tex:370-376`, `:593`, `:595`.
- Cita: «A partir del DER se derivó el esquema físico aplicando las reglas de conversión al modelo relacional» y «las quince relaciones del esquema lógico cumplen FNBC» / «El esquema físico tiene las mismas columnas que el lógico». Ninguna figura ni tabla del documento muestra el grafo relacional; el único `\input` de esquemas son `fig:der` y `fig:er`.
- Fuente que decide: pregunta abierta → equipo. `DISENO-BD.md` §6 dice que «el grafo relacional es el entregable propio de la etapa lógica» y el método (§1.4.3) exige la etapa lógica entre la conceptual y la física. El documento salta de DER a esquema físico y luego habla del lógico como si el lector lo conociera.
- Corrección sugerida: incluir `grafo_relacional_3_vigente.puml` (con PNG; hoy no existe ningún PNG de ese grafo en el repo) como figura del cap. 5, o al menos una frase que defina «esquema lógico» (el mismo conjunto de 15 relaciones y 63 atributos del esquema físico, sin tipos).

### DR-08 — Tabla de normalización: la lista de excepciones a la clave subrogada omite a `PRESENTA`
- Severidad: Media
- Ubicación: `chapters/05_diseno.tex:618-623`; también `:526-528`; `diagramas/grafo_relacional_3_vigente.puml:192-197`; `back/apendice_D.tex:221-223`.
- Cita: «Clave subrogada autogenerada, salvo `USUARIO`/`ADMINISTRADOR` (`idInstitucional`), `CONDUCTA` (`nombre`) y `SEGUNDO` (clave compuesta …)» vs «El caso compuesto del esquema es `PRESENTA`, cuya clave primaria es el par (`idIntervalo`, `conducta`)» (misma sección, L526) y grafo/apéndice D: `PRESENTA` PK = (`idIntervalo`, `conducta`), sin identificador autogenerado.
- Fuente que decide: grafo vigente y apéndice D.
- Corrección sugerida: «… `CONDUCTA` (`nombre`), `PRESENTA` (clave compuesta `idIntervalo`, `conducta`) y `SEGUNDO` (clave compuesta `idObservacion`, `segundo`)».

### DR-09 — Fila 3FN de `USUARIO` mal rotulada y razonamiento inexacto sobre el correo
- Severidad: Media
- Ubicación: `chapters/05_diseno.tex:639-643` y `:564-570`; contraste con `:621-622`.
- Cita: «Clave sustituta en lugar de dato de negocio como clave primaria … `idInstitucional` como primaria» (L640-642) vs «salvo `USUARIO`/`ADMINISTRADOR` (`idInstitucional`)» (L621: `idInstitucional`, boleta o número de empleado, es dato de negocio, no clave sustituta). Además L566-568: «`nombre`, `apellidos`, `activo` y `cambioRequerido` dependen directamente de `idInstitucional`, no del correo»; como `correo` es clave alterna (grafo L115 `[AK]`), esas columnas también dependen de él: no hay violación porque `correo` es clave candidata.
- Fuente que decide: grafo vigente (`idInstitucional` PK, `correo` AK) y la definición de FNBC del propio cap. 5 (L574-579).
- Corrección sugerida: rotular la fila «Elección de la clave primaria entre claves candidatas» y la observación «`USUARIO` tiene dos claves candidatas (`idInstitucional` y `correo`); se elige `idInstitucional` como primaria porque el correo puede cambiar sin tocar las llaves foráneas». En L566-568 sustituir «no del correo» por «y, como el correo es clave candidata, también del correo; por eso no hay dependencia transitiva».

### DR-10 — La figura del esquema físico (PNG del cap. 5) lleva SQL, siglas de decisiones internas e historial de sesión en las notas
- Severidad: Media
- Ubicación: `diagramas/esquema_fisico.puml:146-151, 193-196, 222-233, 277, 281-286, 295, 339`; renderizado en `figures/mermaid/esquema_fisico.png`.
- Cita: «D-10: activo evita el DELETE. Contraseña con bcrypt + sal (RNF-05, ya resuelto en el .tex)»; «CK segundo BETWEEN 1 AND 300»; «Su PK es la misma FK, asi que PostgreSQL la indexa sola al declarar el PRIMARY KEY»; «Aplicado aqui por primera vez a peticion del usuario (15-sep)»; «D-24 (15-sep): idVideo UNIQUE fuerza la cardinalidad…»; etiqueta de arista «· UK, D-24».
- Fuente que decide: `CLAUDE.md` («lenguaje natural obligatorio: sin SQL ni código dentro de los diagramas») y `DISENO-BD.md` §6. El PNG es el que entra al documento (cap. 5, `fig:er`). `PENDIENTES-ERICK.md` M-26 y A-9b ya cubren parte (nombres de función, citas «D-XX»); sigue presente: una expresión SQL (`BETWEEN 1 AND 300`), palabras clave SQL, referencias al `.tex` y a «petición del usuario».
- Corrección sugerida: reescribir las notas sin identificadores de decisión ni fechas de sesión (p. ej. «`activo` evita borrar usuarios; la contraseña se guarda con bcrypt y sal», «`segundo` va de 1 a 300», «la llave primaria de `ADMINISTRADOR` es a la vez llave foránea»), quitar `D-24` de la etiqueta de arista («UK») y regenerar el PNG.

---

## Baja

### DR-11 — Encabezado del grafo vigente cuenta mal sus relaciones de «dominio experimental»
- Severidad: Baja
- Ubicación: `diagramas/grafo_relacional_3_vigente.puml:8-11` y `:107`; `diagramas/grafo_relacional_2_laboratorio.puml:3-5`.
- Cita: «Las 11 relaciones del esquema lógico definitivo más las dos … REPORTE y NOTIFICACION. Más ADMINISTRADOR» (= 14) y «DOMINIO EXPERIMENTAL - las 11 del esquema logico definitivo» vs la sección contiene 13 clases (`SEGUNDO` y `ADMINISTRADOR` incluidas) y el total es 15. `_2_laboratorio` dice que el vigente es «este mas las tablas del sistema», omitiendo `SEGUNDO` (D-35) y la baja de `numeroRata` (D-55: `_2` aún tiene `numeroRata [AK]`, L115, lo cual es correcto por ser paso intermedio).
- Fuente que decide: conteo real del grafo (15 / 63 / 17, verificado).
- Corrección sugerida: en L8-11: «Las 11 relaciones del esquema lógico original, más SEGUNDO (D-35), REPORTE, NOTIFICACION y ADMINISTRADOR (D-08)»; en L107 «las 13 del dominio experimental»; en `_2` L4-5 aclarar «este, más SEGUNDO, las tablas del sistema y sin `numeroRata` (D-55)».

### DR-12 — Comentario de `arquitectura_software.puml` dice 16 relaciones
- Severidad: Baja
- Ubicación: `diagramas/arquitectura_software.puml:36`.
- Cita: «repetir aquí las 16 relaciones del modelo nuevo» vs 15 relaciones vigentes.
- Fuente que decide: grafo vigente y D-51.
- Corrección sugerida: «las 15 relaciones del modelo vigente».

### DR-13 — `relacional.puml` y `er.png` conservan el modelo descartado sin marca de obsoleto
- Severidad: Baja
- Ubicación: `diagramas/relacional.puml:1-197` (12 tablas); `diagramas/er.png` (commit del 1-may); `diagramas/DiagramaEntidadRelacion.svg`; uso: `scripts/gen_presentacion.py:944` (`er.png` como «Diagrama ER» de la presentación).
- Cita: tablas y columnas sin respaldo en el grafo vigente: `SUJETOS`, `ROIS`, `CONFIGURACIONES_ANALISIS`, `TRABAJOS`, `ANIMALES`, `RESULTADOS_COMPORTAMIENTO`, `COMPORTAMIENTO_POR_MINUTO`; `USUARIOS.rol`, `ultimo_acceso` (D-37), `SUJETOS.indice_rata`, `TRABAJOS.progreso_pct`, `EXPERIMENTOS.tratamiento/especie/disposicion`. El encabezado dice solo «Diagrama Relacional — Base de datos FST»; `er.png` rotula «Diagrama Entidad-Relación» a un esquema con tipos y llaves (contra la regla de «DER»). El cap. 5 no los incluye (verificado con grep), pero `grafo_relacional_2_laboratorio.puml:21` y `CORRECCIONES.md:34` ya dicen que se descartó.
- Fuente que decide: `CLAUDE.md` (regla de diagramas) y D-51/D-55; no hay fuente que mande sobre qué hacer con el archivo (archivar o marcar).
- Corrección sugerida: agregar a `relacional.puml` un banner «OBSOLETO — modelo descartado; el vigente es grafo_relacional_3_vigente.puml» (o moverlo a una carpeta de históricos), y revisar que la presentación de defensa (`gen_presentacion.py`) no muestre `er.png`.

---

## Ya registrados que siguen presentes (no cuentan como hallazgos nuevos)

- `PENDIENTES-ERICK.md` A-8: el cap. 5 (L359-361) presenta `ADMINISTRADOR`, `REPORTE` y `NOTIFICACION` junto a la figura del DER, que no las dibuja (`esquema_conceptual.tex` solo tiene 11 entidades; verificado en el PDF).
- A-15: `esquema_fisico.puml:91-94` todavía dice «tres valores en modo completo, dos en modo degradado / D-17» (son cuatro conductas, D-29); es comentario, no sale en el PNG.
- M-24: `ANALISIS.idVideo` sin `[AK]` en el grafo (L167) aunque físico y apéndice D lo declaran UNIQUE (D-24); y falta `rutaDiagnostico` (D-23).
- M-25: `clases.puml` sin asociación `Segundo → Conducta` (el atributo `Segundo.conducta` es `String`), `Analisis` sin `rutaDiagnostico`, `Float` para `segundos`/`duracion` frente a `numeric` del físico.
- L-8: `Video.validarFormatoMp4()` no cubre `.mov` (`clases.puml:74`).
- D-51 sin aplicar: comentario de `seq_analisis_automatico.puml:40` sobre `idConfig`.

## Cobertura y límites

- No revisé los diagramas de secuencia, de casos de uso, de estados, `pipeline.puml` ni `flujo_general.puml` (otras áreas), salvo búsquedas cruzadas de nombres de columna.
- El comentario de `esquema_conceptual.tex:20` («los atributos son 34») no pude verificarlo: el conceptual no dibuja atributos y la cuenta depende de qué identificadores se consideren; con los atributos propios del grafo vigente (sin FK ni claves subrogadas) salen 29. Si el dato va a citarse, conviene recontarlo con el equipo.
- No compilé PlantUML ni LaTeX; las comprobaciones de PNG/PDF fueron visuales (`clases.png`, `esquema_fisico.png`, `esquema_conceptual.pdf`, `er.png`). No abrí `diagramas/pdf/*.pdf`, `docs/DiagramaClases_PlantUML_TT2026B066.docx` ni `figures/mermaid/clases.png` (4-oct, no entra al documento).
- Del cap. 5 no audité los casos de uso, secuencias, API ni interfaz web, salvo menciones de tablas/columnas.
- El número de figura («Figura 5.5», `esquema_fisico.puml:7`) no se comprobó sin compilar.
