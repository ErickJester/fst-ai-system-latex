# Auditoría de consistencia — agente MD (reglas en los .md)

**Fecha:** 2026-10-11 · **HEAD auditado:** `da96c00` · **Modo:** solo lectura (no se tocó ningún otro archivo del proyecto).

## Alcance auditado (leído)

- Completos: `CLAUDE.md`, `DISENO-BD.md`, `PENDIENTES.md`, `PENDIENTES-VANESA.md`, `PENDIENTES-ERICK.md`, `CORRECCIONES.md`, `CAMBIOS-CAP5.md`, `HISTORIAL.md`, `PREGUNTAS.md`, `README.md`, `COMPARATIVA-FIGURAS-CAP5.md`, `MIGRACION-DIAGRAMAS.md`, `errores/README.md`, `errores/pendientes.md`, `errores/preguntas-doctor.md` (§1–6, D-01…D-56), `INSTRUCCIONES-WEB.md` (las 2986 líneas, cuerpo y anexos A, B y C).
- Cabeceras y muestreo: `errores/0X/errores.md`, `errores/front/errores.md`, `errores/REVISION-AGENTES-2026-10-03.md`, `diagramas/diagram_design/*.md` (leídos completos `flujo_sistema.md`, `pipeline_analisis.md`, `clases_completo.md`, `arquitectura_capas.md`, `despliegue.md`).
- Contrastados con: `chapters/04_analisis.tex` (completo), `chapters/05_diseno.tex` (líneas 1–745 y los pasajes citados), `back/apendice_D.tex` (completo), `diagramas/grafo_relacional_3_vigente.puml`, `esquema_fisico.puml`, `clases.puml`, `seq_analisis_automatico.puml`, `flujo_general.puml`, `esquema_conceptual.tex` (grep), `figures/mermaid/flujo_general.png` (vista), y greps transversales sobre `chapters/01`–`05`, `front/*`, `back/*`.
- Comprobaciones mecánicas hechas: cifras 15 relaciones / 63 atributos / 17 FK (lógico) y 64 atributos / 17 FK (físico) recontadas sobre los `.puml` (**coinciden** con DISENO-BD L282-284); existencia de D-01…D-56 en §6 (**todas existen**); enlaces markdown internos (sin enlaces rotos reales; solo placeholders `errores/0X/errores.md`, `puml/cu_paquete3.puml` abreviado y `fst_auto/…` externo); ausencia de «último segundo» en todo `.md`/`.puml`/`.tex` (**limpio**, solo se cita como historia en PENDIENTES-VANESA L45 y L54, correctamente marcado); ausencia de `numeroRata`, `MODELO/CONFIGURACION/idConfig`, `0.70` y BORIS vigentes en `chapters/`, `front/`, `back/apendice_*` y en los `.md` vigentes (los restos están en documentos históricos o en los hallazgos de abajo).

## Resumen de conteos

| Severidad | Total | de ellas «pregunta abierta» |
|-----------|-------|-----------------------------|
| Alta | 4 | 0 |
| Media | 22 | 6 |
| Baja | 9 | 1 |
| **Total** | **35** | **7** |

---

# Hallazgos de severidad Alta

### MD-01 — INSTRUCCIONES-WEB R-03 sigue diciendo que el Día 1 del grupo control se analiza
- Severidad: Alta
- Ubicación: `INSTRUCCIONES-WEB.md:424` (R-03); contraste: `errores/preguntas-doctor.md:279` (D-54 (d)), `PENDIENTES.md:8` y `:295`, `diagramas/esquema_fisico.puml:72-73`, `DISENO-BD.md:278`
- Cita: «El Día 1 solo se analiza (sus primeros 5 min) si la tanda es del grupo **control**» (IW R-03) vs «El Día 1 solo confirma que ese video existe y es de habituación…; no se analiza ni conserva un recorte» (D-54) y «el Dia 1 solo confirma que existe el video de habituacion; no se analiza, D-54» (esquema_fisico.puml)
- Fuente que decide: rango 1, D-54 (usuario, 6-oct). DISENO-BD L291 y PENDIENTES L295 declaran D-54 «aplicado» en `INSTRUCCIONES-WEB.md`, pero solo se actualizó el contrato del worker (L133, L158), no esta regla.
- Corrección sugerida: sustituir la segunda frase de R-03 por «El Día 1 solo confirma que existe el video de habituación y no se analiza ni se recorta; solo el Día 2 se analiza (D-54).» Revisar de paso `§4` paso 3 (L126: «Crea una fila en `ANALISIS`… del video») para que no encole el Día 1 (ver MD-24). El LaTeX (cap. 1 L251, cap. 4 L107-110) ya figura como pendiente del 6-oct y no se repite aquí.

### MD-02 — DISENO-BD.md deja P-08/D-03 «sin resolver» cuando D-03 está resuelto, aplicado y reforzado con UNIQUE
- Severidad: Alta
- Ubicación: `DISENO-BD.md:224` (árbol del modelo), `:405` (tabla de preguntas abiertas), `:483-497` (§8 «Errata estructural — sin resolver», «No aplicar todavía»); contraste: `errores/preguntas-doctor.md:215` (D-03), `diagramas/grafo_relacional_3_vigente.puml:244` y `:65-68`, `esquema_fisico.puml:339` y `:43-47` (D-24), `DISENO-BD.md:407` (D-05 «se disolvió con D-03»), `:418-420`
- Cita: «Análisis (1,N — un video se puede reanalizar · pendiente P-08/D-03)» y «**No aplicar todavía:** … falta cerrarlo formalmente» (DISENO-BD) vs «**Resuelto (equipo, 2026-09-13):** se reemplaza… `VIDEO — ANALISIS` queda en (1,1)» (D-03) y `VIDEO "1" --o "1" ANALISIS` (grafo vigente)
- Fuente que decide: rango 1, D-03 (equipo, 13-sep) y D-24 (15-sep).
- Corrección sugerida: en L224 poner «Análisis (1,1 — un video, un análisis vigente; D-03/D-24)»; en L405 marcar la fila P-08/D-03 como «Cerrada (equipo, 13-sep): se reemplaza»; reescribir §8 «Errata estructural» como «Resuelta por D-03: el reanálisis reemplaza; `OBSERVACION` sigue colgando de `VIDEO`», o borrarla y dejar un puntero a D-03. Es el archivo marcado como «punto de partida obligatorio» y hoy afirma lo contrario de la decisión.

### MD-03 — Cap. 5 describe procesamiento parcial si faltan cilindros; D-20 lo descarta (todo o nada)
- Severidad: Alta
- Ubicación: `chapters/05_diseno.tex:337-339` («Separación por espécimen»); contraste: `errores/preguntas-doctor.md:231` (D-20) y `:126-145` (Q-G), `chapters/04_analisis.tex:568-571` (RN-11), `chapters/05_diseno.tex:187-188` y `:303-306` (el propio cap. 5 dice que se detiene), `INSTRUCCIONES-WEB.md:134-137`
- Cita: «Si el número de cilindros detectados es menor al esperado, el sistema reporta cuáles especímenes pudo procesar y cuáles no, en lugar de abortar el análisis completo» (cap. 5) vs «todo o nada, siguiendo RN-11… El comportamiento de "reporta cuáles especímenes pudo procesar" que describe el cap. 5 no se implementa» (D-20) y «si no encuentra los cilindros, el pipeline se detiene y genera el reporte de diagnóstico» (cap. 5 L187-188)
- Fuente que decide: rango 1, D-20 (equipo, 13-sep, «provisional» hasta confirmar Q-G con el laboratorio). PENDIENTES no lo registra. Además se contradice dentro del mismo cap. 5 (L187-188 y L303-306 dicen «se detiene»).
- Corrección sugerida: sustituir el último período del párrafo por «Si no se encuentran los cilindros esperados de la tanda, el pipeline se detiene y genera el reporte de diagnóstico (ver RN-11); no se entregan resultados parciales.» Si el equipo prefiere conservar el comportamiento parcial, entonces hay que reabrir D-20 y RN-11 (decisión del equipo, no del LaTeX).

### MD-04 — Cap. 5 dice que el entrenamiento se alimenta de «anotación experta»; contradice la prohibición vigente, D-26/D-56 y la propia figura
- Severidad: Alta
- Ubicación: `chapters/05_diseno.tex:99-102` (texto antes de la Fig. flujo); contraste: `CLAUDE.md` (sección «Prohibición vigente — métricas de validación»), `errores/preguntas-doctor.md:241` (D-26) y `:281` (D-56), `figures/mermaid/flujo_general.png` (título del recuadro: «SIN anotación del Dr. Sandino, ni para entrenar ni para probar»), `diagramas/diagram_design/flujo_sistema.md:55-57`, `chapters/05_diseno.tex:250-256`
- Cita: «cómo el ciclo de entrenamiento del modelo ---anotación experta, dataset y entrenamiento--- alimenta al clasificador de conducta» (cap. 5) vs «el clasificador se entrena con videos del laboratorio pero **sin** usar las anotaciones manuales del Dr. Sandino» (CLAUDE.md) y «**Sin las anotaciones manuales del laboratorio**, ni para entrenar ni para probar» (flujo_sistema.md)
- Fuente que decide: rango 1 (CLAUDE.md / D-26 / D-56). El propio `flujo_sistema.md` (L55-57) ya detectó la contradicción y dejó «No se modificó»; ningún `PENDIENTES*.md` la registra.
- Corrección sugerida: reescribir esas líneas como «y cómo el ciclo de entrenamiento del modelo ---etiquetado por el equipo, entrenamiento y evaluación sobre un conjunto de prueba propio, sin las anotaciones del laboratorio--- alimenta al clasificador de conducta». Agregar el ítem a `PENDIENTES-ERICK.md` (cap. 5 es de Erick).

---

# Hallazgos de severidad Media

### MD-05 — INSTRUCCIONES-WEB A.11 (tareas programadas) contradice §8 y D-51 sobre `VIDEO.archivo` y la notificación del borrado por disco
- Severidad: Media
- Ubicación: `INSTRUCCIONES-WEB.md:2491-2494` y `:2508-2513` (A.11); contraste: `:468` y `:470` (§8), `:875-878` (§11.13), `errores/preguntas-doctor.md:276` (D-51 puntos 5 y 6), `esquema_fisico.puml:204`
- Cita: «VIDEO.archivo no se modifica. Resultados y reportes se conservan.» y «crea NOTIFICACION "alerta de disco" para quien creó ese experimento» (A.11) vs «Elimina el archivo… y su `archivo` queda en nulo» y «crea una `NOTIFICACION` tipo `video borrado` para el investigador de cada experimento afectado» (§8)
- Fuente que decide: rango 1, D-51 (usuario, 5-oct); el §8 ya está actualizado.
- Corrección sugerida: en A.11 cambiar la nota a «VIDEO.archivo queda en nulo; la fila se conserva» y la notificación del 90 % a tipo `video borrado` para el investigador de cada experimento afectado (la de `alerta de disco` va solo a los administradores, rama del 80 %); agregar el UPDATE de `archivo` en el bucle.

### MD-06 — INSTRUCCIONES-WEB A.9 trae una `seq_analisis_automatico` anterior a D-35/D-54, aunque se declara el «contrato» del worker
- Severidad: Media
- Ubicación: `INSTRUCCIONES-WEB.md:2166-2169` y `:2183-2194` (A.9); contraste: `:133-148` (§4, contrato), `:22-23` («si hay diferencia, manda el anexo»), `diagramas/seq_analisis_automatico.puml:73-86`
- Cita: «tu worker_fake debe escribir en la base exactamente estos cambios» y el bucle solo hace «guarda su observación… guarda sus 5 intervalos» (A.9) vs «escribe **una fila en `SEGUNDO` por cada segundo analizado**… se queda con los **últimos 300 segundos**… `analisis_{id}_cajas.json`… copia H.264» (§4 y el `.puml` real)
- Fuente que decide: rango 1, D-35, D-42, D-54.
- Corrección sugerida: sincronizar el bloque A.9 con `diagramas/seq_analisis_automatico.puml` (agregar el recorte a 300 s con renumeración, la escritura de `SEGUNDO`, el archivo de recuadros y la copia web). Mientras no se haga, la regla L22-23 («manda el anexo») produce un contrato incompleto para quien construya el `worker_fake`.

### MD-07 — INSTRUCCIONES-WEB sigue pidiendo el «disparador de `ESPECIMEN.idGrupo`» que D-55 eliminó
- Severidad: Media
- Ubicación: `INSTRUCCIONES-WEB.md:115` y `:915-916`; contraste: `errores/preguntas-doctor.md:280` (D-55 (3)), `DISENO-BD.md:276`, `diagramas/esquema_fisico.puml:40-42`, `INSTRUCCIONES-WEB.md:2623-2629` (Anexo B, sin disparador ni `idgrupo`)
- Cita: «SQL de creación (dominios, tablas, disparador, semillas)» y «disparador de `ESPECIMEN.idGrupo` y datos semilla de `CONDUCTA`» vs «desaparece el `idGrupo` redundante de `ESPECIMEN` y su disparador»
- Fuente que decide: rango 1, D-55.
- Corrección sugerida: L115 → «(dominios, tablas, restricciones, semillas)»; L915-916 → «dominios, 15 tablas, restricciones y datos semilla de `CONDUCTA`».

### MD-08 — INSTRUCCIONES-WEB omite «Conducta activa» en las columnas de los reportes y en el resumen de resultados
- Severidad: Media
- Ubicación: `INSTRUCCIONES-WEB.md:448` y `:2426-2427` (columnas de CSV/XLSX), `:2368` (segundos sumados en la comparación); contraste: `:433` (R-12: «Los reportes deben mostrarla como una columna más»), `:621-623`, `chapters/04_analisis.tex:206-207` (RF-22: «`Nado`, `Escalamiento`, `Inmovilidad` y `Conducta activa`»), `chapters/01_introduccion.tex:281`
- Cita: «columnas `Tiempo (min:seg)`, `Nado`, `Escalamiento`, `Inmovilidad`, una fila por minuto» (IW) vs «`Tiempo (min:seg)`, `Nado`, `Escalamiento`, `Inmovilidad` y `Conducta activa`» (RF-22)
- Fuente que decide: rango 1, D-29 / RN-13 / RF-22.
- Corrección sugerida: añadir `Conducta activa` en L448, L2426-2427 y «conducta activa» en L2368. De paso, L711 (§9.8: «Conductas: "Nado activo", "Inmovilidad", "Escalamiento"») debe incluir «Conducta activa».

### MD-09 — INSTRUCCIONES-WEB: la secuencia de progreso todavía muestra un «código» de error
- Severidad: Media
- Ubicación: `INSTRUCCIONES-WEB.md:762`; contraste: `:584-586` (§9.4), `:865-866` (§11.10), `errores/preguntas-doctor.md:272` (D-47)
- Cita: «UI-->>I: código, descripción y botón de diagnóstico» vs «no hay columna de código ni de descripción de error» y «RF-16 deja de mostrar un código de error»
- Fuente que decide: rango 1, D-47 (usuario, 4-oct).
- Corrección sugerida: «mensaje armado con la etapa y botón de diagnóstico».

### MD-10 — INSTRUCCIONES-WEB define dos rutas distintas para la misma comparación entre grupos
- Severidad: Media
- Ubicación: `INSTRUCCIONES-WEB.md:389` (tabla principal) vs `:413` y `:2359` (secuencia); coincide con la tabla principal `chapters/05_diseno.tex:708`
- Cita: «`GET /experiments/{id}/results/groups`» vs «`GET /experiments/{id}/groups/comparison`»; además L2361 y L2383 hablan de «los tres grupos» (el experimento tiene 3 o más, L354).
- Fuente que decide: pregunta de contrato interno; el cap. 5 usa `/results/groups`.
- Corrección sugerida: eliminar la fila L413 y cambiar L2359 a `/results/groups`; decir «los grupos» en L2361, L2383 y L619.

### MD-11 — Apéndice D declara NOT NULL columnas de `ANALISIS` que el backend deja vacías al encolar (IW Anexo B las admite nulas)
- Severidad: Media
- Ubicación: `back/apendice_D.tex:174-180` (`etapa`, `nivelClasif`, `fechaAnalisis`: «No»); contraste: `INSTRUCCIONES-WEB.md:2650-2652` y `:850-851`, `:165-166`, `:149-150`
- Cita: «etapa… No», «nivelClasif… No», «fechaAnalisis… No» (apéndice D) vs «etapa etapa_analisis, -- nula mientras esta en cola», `nivelclasif nivel_clasif_analisis`, `fechaanalisis timestamptz, -- la fija el worker al terminar` (Anexo B) y «El backend nunca escribe `estado`, `etapa` ni `nivelClasif` salvo al crear el análisis en cola»
- Fuente que decide: pregunta abierta → equipo (ni `esquema_fisico.puml` ni D-xx fijan la nulidad de esas tres columnas; solo IW la propone, marcada `[PROPUESTA]`, §11 punto 4).
- Corrección sugerida: decidir y registrar (p. ej. D-57): si `etapa`, `nivelClasif` y `fechaAnalisis` son nulas hasta que el worker las llena, marcar «Sí» en el apéndice D (y en `esquema_fisico.puml`); si no, quitar la propuesta del Anexo B.

### MD-12 — Filas D-04, D-06 y D-14 sin marca de «sin objeto»; D-06 aparece con dos estados y las listas de pendientes todavía dependen de él
- Severidad: Media
- Ubicación: `errores/preguntas-doctor.md:217` (D-06 «si gana la fusión… esta pregunta se reabre»), `:218` (D-04), `:226` (D-14) vs `:276` (D-51: «Deja sin objeto a D-06 y D-14») y `:280` (D-55: «deja sin objeto a D-04»); `DISENO-BD.md:406-408` (sí marca «sin objeto»); `PENDIENTES-ERICK.md:19` (B-1: «D-06 (dos archivos de modelo si gana la fusión)»), `CAMBIOS-CAP5.md:277` (CLA-03)
- Cita: «esta pregunta se reabre» (D-06) y «revisar… D-06» (B-1) vs «Deja sin objeto a D-06 y D-14 (relación `MODELO`–`CONFIGURACION` y hash del modelo)» (D-51)
- Fuente que decide: D-51 (rango 1) dice sin objeto; pero la nota del 5-oct de D-06 plantea reabrirlo si gana la fusión de modelos → pregunta abierta → equipo (es una decisión que se vuelve a mirar cuando se elija el clasificador).
- Corrección sugerida: anotar en las filas D-04, D-06 y D-14 «Sin objeto desde D-55 / D-51»; en D-06 decir expresamente si se reabre (y entonces como pregunta nueva, no como D-06) o queda cerrada; quitar «D-06» de B-1 o reescribirlo como «si gana la fusión, decidir de nuevo dónde se documentan los dos archivos de modelo (cap. 6)».

### MD-13 — DISENO-BD.md sigue diciendo que el cap. 5 y `diagramas/` «están mal y no se usan», y que reescribir el cap. 5 «no está iniciado»
- Severidad: Media
- Ubicación: `DISENO-BD.md:19-20`, `:116`, `:387-395` (tabla «Lo que falta»: L389 «Próxima reunión: lunes 2026-09-21»; L391 «Reescribir el cap. 5 del LaTeX | No iniciado»), `:422-435` («El trabajo grande que falta en el documento»: L429 «RF-14 fija "los cuatro cilindros"; el dominio correcto es 3 ó 4»), `:474-477`; contraste: `DISENO-BD.md:286-295` («Aplicado (6-oct)… cap. 1, 4 y 5»), `PENDIENTES.md:3-8`, `CLAUDE.md` («`grafo_relacional_3_vigente.puml`» como grafo vigente), `chapters/04_analisis.tex:148` (RF-14 «de dos a cuatro»)
- Cita: «Capítulo 5 y `diagramas/`: no se usan. Están mal y son el objetivo a reemplazar» y «Lo que NO debes hacer… tomar el capítulo 5, `diagramas/`… como referencia» vs «Aplicado (6-oct): … `grafo_relacional_3_vigente.puml`, `esquema_fisico.puml`, `clases.puml`… cap. 1, 4 y 5»
- Fuente que decide: rango 1 (los propios cambios del 5-6 oct y `PENDIENTES.md`).
- Corrección sugerida: marcar §1 (L19-20), §2.3 (L116), §7 (L474-477) y §5 «Lo que falta» / «trabajo grande» como «histórico (septiembre)» o reescribirlos: los `.puml` vigentes y el cap. 5 reescrito **sí** son referencia (el cap. 5 ya no es objetivo a reemplazar); la lista de lo que falta es `PENDIENTES.md`. Quitar la fecha 21-sep (pasada) y la frase de «los cuatro cilindros… 3 ó 4».

### MD-14 — DISENO-BD.md §4 «El modelo, en corto» se contradice dentro de la misma sección
- Severidad: Media
- Ubicación: `DISENO-BD.md:213-215` y `:238-239` vs `:248-251`, `:252-256`, `:257-258`
- Cita: «ninguna entidad es débil y la agregación desapareció» (L213-215) vs «**Observación es una agregación**… La agregación cierra primero el par válido» (L252-256); «la rata tiene identificador propio» (L213) vs «El espécimen no tiene identidad propia… única identidad es geométrica» (L248-251); «16 interrelaciones… → 16 relaciones» (L238-239) vs «15 relaciones» (L282-284); «Todo el sistema mide un solo dato: `segundos`… Los otros 26 atributos» (L257-258) vs 63 atributos y `SEGUNDO.conducta` como dato por segundo
- Fuente que decide: rango 1, D-55 (cambia la premisa de P-01), D-35, D-51; cifras vigentes en L282-284 (verificadas contra los `.puml`).
- Corrección sugerida: dejar un solo relato: decisión 2 → «el espécimen se identifica por su posición (`numeroCilindro`, D-55); no guarda número de rata»; decisión 3 → «`OBSERVACION` es una entidad asociativa» (como dice MC-01 y el artifact conceptual); L238-239 → «15 relaciones»; decisión 4 → «la medida de fondo es la conducta de cada segundo (`SEGUNDO`); `PRESENTA` es su resumen por minuto (D-35)».

### MD-15 — DISENO-BD.md da dos juegos distintos de URLs para los mismos tres artifacts
- Severidad: Media
- Ubicación: `DISENO-BD.md:189` (`claude.ai/artifact/Y7uJ7Mje…`, `FJtL6wbw…`, `972fCkz4…`) vs `:193-195` (`claude.ai/code/artifact/fc01fd30-…`, `73df37d9-…`, `41a09816-…`) y `:197-199` («verificaron… 2026-09-14»)
- Cita: «Actualizados el 2026-10-06… Conceptual https://claude.ai/artifact/Y7uJ7…» vs tabla «Diseño Conceptual FST v4 | https://claude.ai/code/artifact/fc01fd30-…»
- Fuente que decide: pregunta abierta → tú y el usuario (no verifiqué las URLs en vivo; `CLAUDE.md` pide no propagar a artifacts sin pedirlo).
- Corrección sugerida: dejar una sola columna de URL (la de 6-oct) y borrar las de septiembre, o marcar las de la tabla como «anteriores». La nota de L197-199 sobre «`441abfbd…`, `0f0abf49…` OBSOLETO» sigue siendo válida.

### MD-16 — `PENDIENTES-ERICK.md` / `PENDIENTES-VANESA.md` / `PENDIENTES.md` listan como pendientes ítems ya resueltos (y los conteos los incluyen)
- Severidad: Media
- Ubicación: `PENDIENTES-ERICK.md:34` (A-9b), `:32` (A-1), `:36` (A-15), `:63` (M-26), `:22` (B-5); `PENDIENTES-VANESA.md:129` (A-9a) vs `:36-43`; `PENDIENTES.md:14-15` (conteos), `:28`
- Cita: A-9b «Citas internas "D-XX" que el lector no puede resolver» y A-9a «Quitar las citas internas "D-XX"» (siguen como 🔴) vs `PENDIENTES-VANESA.md:36-39` («Erick quitó los códigos `D-xx` del cap. 5 (7-oct, commit `6a2b98a`)»); A-1 «CLAHE, fondo por **mediana**… línea de agua con EMA» vs el LaTeX actual
- Verificación: `grep` de `D-[0-9]{2}`, `Q-[A-G]`, `CLA-0` en `chapters/01-05`, `front/`, `back/apendice_C-D` → **0 resultados** (solo «R(2+1)D-18»); `grep CLAHE` en todos los `.tex`/`.bib` → 0 (cap. 4 L652-658 y cap. 5 L148-156 ya usan percentil 10); `esquema_fisico.puml` ya dice «15 tablas, 17 llaves foraneas» (L8) y no contiene `fn_sincronizar…` (A-15 primera mitad y M-26 resueltos; queda solo «tres valores… dos en degradado», L91-94). B-5 está tachado pero se cuenta entre los «4 🔒».
- Fuente que decide: rango 1 (los propios commits `6a2b98a`, `9de519f`) y verificación contra el LaTeX.
- Corrección sugerida: marcar ✅ A-9a/A-9b (retirar de los conteos), A-1 (en `PENDIENTES.md:28` y `PENDIENTES-VANESA.md:29` dejar solo «el preprocesamiento y el clasificador son de Erick», sin CLAHE ni EMA), M-26 y la primera mitad de A-15; recalcular `PENDIENTES.md:14-15` (Erick pasaría de «5 🔴 / 4 🔒» a «3 🔴 / 3 🔒» si se cierran A-1, A-9b y se descuenta B-5; Vanesa de 13 a 12 🔴).

### MD-17 — PREGUNTAS.md conserva una pregunta ya respondida y con «primeros 300 s»
- Severidad: Media
- Ubicación: `PREGUNTAS.md:3-4` (regla «Al responder, se borra de aquí») y `:15-18` (pregunta 2); contraste: `INSTRUCCIONES-WEB.md:891-897` (§11.16 «Resuelto (usuario, 3-oct-2026)»), `errores/preguntas-doctor.md:279` (D-54: «últimos»), `INSTRUCCIONES-WEB.md:904-907` (§11.18, la pregunta 1 sí sigue abierta)
- Cita: «una copia en formato compatible (H.264) de los primeros 300 s. ¿La genera el worker…?» vs «el worker genera con `ffmpeg`… una copia en H.264 de los últimos 300 s» (resuelto)
- Fuente que decide: rango 1 (respuesta del usuario 3-oct) + D-54.
- Corrección sugerida: borrar la pregunta 2 de `PREGUNTAS.md` (la respuesta ya persiste en IW §11.16); dejar la 1, que coincide con IW §11.18 [ABIERTO].

### MD-18 — README.md describe un proyecto anterior (IA, TensorFlow, anotaciones expertas, cap. 5 «a reemplazar», sin PENDIENTES)
- Severidad: Media
- Ubicación: `README.md:1`, `:17`, `:22`, `:41`, `:7-13`, `:58`, `:87-93`, `:133`; contraste: `CLAUDE.md` (terminología y prohibición vigente), `chapters/04_analisis.tex:690-702` (PyTorch, scikit-learn), `PENDIENTES.md`
- Cita: «sistema web asistido por inteligencia artificial (IA)», «**Inteligencia Artificial:** OpenCV, TensorFlow y Scikit-learn», «comparando los resultados automáticos con anotaciones expertas para validar», «El diseño de BD del capítulo 5 y los diagramas actuales están desactualizados y son el objetivo a reemplazar», «`CORRECCIONES.md` | Registro versionado… referencia con el detalle completo», «Última actualización: Febrero 2026»
- Fuente que decide: rango 1 (CLAUDE.md: «visión por computadora»/«aprendizaje supervisado»; prohibición de gold standard; PENDIENTES.md como lista vigente). El título «ASISTIDO POR IA» sí es el oficial (portada) y puede quedar.
- Corrección sugerida: cambiar la viñeta de stack a «Visión por computadora y aprendizaje supervisado: OpenCV, PyTorch y scikit-learn», quitar «TensorFlow» y la frase de «anotaciones expertas» (por «métricas de clasificación sobre un conjunto de prueba propio»), reemplazar L7-13 por un puntero a `DISENO-BD.md`/`PENDIENTES.md` sin decir que el cap. 5 está mal, agregar `PENDIENTES.md` al árbol y actualizar la fecha.

### MD-19 — MIGRACION-DIAGRAMAS.md presenta como vigentes cifras y decisiones ya revertidas (sin aviso de obsolescencia)
- Severidad: Media
- Ubicación: `MIGRACION-DIAGRAMAS.md:26`, `:96` («16 relaciones en total, no 15»), `:156` (`numeroRata`), `:158` y `:309` (`MODELO`/`CONFIGURACION`), `:344` y `:450` (umbral 0.70), `:355` (25 % por cada una de 4 etapas), `:416` (`rat.pt`, `resnet*_fst.pt`), `:425-428` (BORIS), `:342` («Pipeline IA»), `:390` («El Día 1 es opcional para **cualquier** grupo»); cabecera L3-5 solo dice «Documento temporal»
- Cita: «**16 relaciones en total**, no 15» vs «15 relaciones» (PENDIENTES.md, grafo vigente); «confianza de detección < 0.70» vs D-32/D-47; «25% fijo por cada una de las 4 etapas de D-16» vs D-22 revisado (tres etapas, un tercio)
- Fuente que decide: rango 1 (D-22, D-32, D-47, D-51, D-55, D-56). Los otros trackers viejos llevan el banner «Desactualizado como lista de trabajo»; este no. `D-56` (L281) lo llama «historial de decisiones».
- Corrección sugerida: copiar en la cabecera el mismo banner de `CAMBIOS-CAP5.md` («Desactualizado… lo vigente está en `PENDIENTES.md`/`DISENO-BD.md`; evidencia histórica»). O borrarlo, como su §6 prevé.

### MD-20 — COMPARATIVA-FIGURAS-CAP5.md afirma que ninguna figura está insertada en el cap. 5
- Severidad: Media
- Ubicación: `COMPARATIVA-FIGURAS-CAP5.md:43-46`, `:3-4`, `:50-51`; contraste: `chapters/05_diseno.tex` (`\includegraphics` en L53, 106, 125, 313, 327, 365, 380, 760-828, 2408-2535, 2568)
- Cita: «**Ninguna de las 19 "listas" está insertada todavía en `05_diseno.tex` como figura** — la inserción… sigue sin empezar» vs el cap. 5 inserta `arquitectura_software`, `flujo_general`, `pipeline`, `esquema_conceptual`, `esquema_fisico`, `cu_*`, `seq_*` y `clases`
- Fuente que decide: verificación contra el LaTeX (rango 5 como hecho verificable) y `CAMBIOS-CAP5.md` banner.
- Corrección sugerida: banner de «desactualizado (septiembre)» y quitar la frase, o reescribir la tabla con el estado de octubre (5.3 «Sin tocar» ya no es cierto: `pipeline.puml` se rehízo en CLA-02).

### MD-21 — `errores/pendientes.md` sin banner: T-02 «mínimo 3» y cap. 5 «sin revisar» presentados como vigentes
- Severidad: Media
- Ubicación: `errores/pendientes.md:6`, `:15`, `:27`; contraste: `errores/preguntas-doctor.md:245` (D-28), `PENDIENTES.md:70-72`, `chapters/05_diseno.tex` (reescrito)
- Cita: «El número es variable, mínimo 3 y máximo 4» y «Sin revisar… **Ahora hay que reescribirlo completo**» vs «de **2 a 4** especímenes» (D-28) y cap. 5 ya reescrito con el diseño nuevo
- Fuente que decide: rango 1, D-28 (equipo, 3-oct).
- Corrección sugerida: añadir el mismo banner que `errores/README.md:3` y cambiar T-02 a «de dos a cuatro».

### MD-22 — Cap. 4 «Factibilidad operativa» describe tres grupos y 6–9 videos por experimento; ningún ítem pendiente lo cubre
- Severidad: Media
- Ubicación: `chapters/04_analisis.tex:921-927`; contraste: `PENDIENTES.md:64-69` («**tres o más grupos** (en promedio 4)… un tipo puede repetirse»), `PENDIENTES-VANESA.md:67` (A-4, que solo toca el cap. 1), `INSTRUCCIONES-WEB.md:354-358`
- Cita: «del orden de 3 a 5, cada uno con tres grupos (control, referencia y tratamiento experimental) de entre 6 y 8 especímenes cada uno. Cada experimento genera entre 6 y 9 videos… (uno por tanda, con dos o tres tandas por grupo)» vs «tres o más grupos (en promedio 4)… Grupo: una o más tandas»
- Fuente que decide: rango 1 (lista «Lo que ya está decidido», D-28). Es zona de Erick (cap. 4) y A-4 es de Vanesa/cap. 1: nadie lo tiene asignado.
- Corrección sugerida: agregar a `PENDIENTES-ERICK.md` un ítem: «cap. 4 L921-927: tres tipos de grupo, tres o más grupos por experimento (en promedio 4), 6–8 especímenes es lo típico, 1 o más tandas por grupo».

### MD-23 — D-44 figura «aplicado en CU-09», pero el cap. 5 conserva dos menciones de «comparación Día 1 vs. Día 2»
- Severidad: Media
- Ubicación: `chapters/05_diseno.tex:808` (intro del Paquete 4) y `:1758` (curso alterno 5 de la ficha de resultados); contraste: `errores/preguntas-doctor.md:269` (D-44 «Aplicado (4-oct) en RF-21, RN-12, CU-09, cap. 1…»), `PENDIENTES.md:104-105` («**No existe** comparación Día 1 contra Día 2»), `INSTRUCCIONES-WEB.md:432` (R-11 eliminada)
- Cita: «comparación Día~1 vs.\ Día~2 (cuando ambos videos están disponibles)» y «la comparación Día~1 vs.\ Día~2 no está disponible» vs «se **quita toda mención** de la comparación Día 1 vs Día 2» (D-44)
- Fuente que decide: rango 1, D-44 (usuario, 4-oct). Ambas líneas están en la zona de casos de uso (Vanesa).
- Corrección sugerida: L808 → «comparación entre grupos con el Día 2»; L1758 → «Hay especímenes cuyo Día 2 aún no está analizado: se señalan como faltantes y no entran al promedio (RN-12).» Anotarlo en «Para Vanesa» o en su lista.

### MD-24 — Pregunta abierta: cómo queda el video del Día 1 en el modelo si D-54 dice que no se analiza
- Severidad: Media
- Ubicación: `errores/preguntas-doctor.md:279` (D-54 (d)); `diagramas/grafo_relacional_3_vigente.puml:243-246`, `esquema_fisico.puml:337-345`; `INSTRUCCIONES-WEB.md:126` (§4: se crea un `ANALISIS` por cada video subido), `:358` («`VIDEO` tiene… un análisis»), `:541` (el formulario permite subir Día 1)
- Cita: «El Día 1 solo confirma que ese video existe… no se analiza» vs `VIDEO "1" --o "1" ANALISIS`, `VIDEO "1" --o "2..4" OBSERVACION`, `ESPECIMEN "1" --o "1..2" OBSERVACION`
- Fuente que decide: pregunta abierta → tú y el usuario. Si el Día 1 no se analiza, un video de Día 1 no tendría `ANALISIS` ni `OBSERVACION`, y las cardinalidades (1,1) y (2,4) de `VIDEO` y (1,2) de `ESPECIMEN` dejan de ser ciertas; además el backend no debería encolarlo.
- Corrección sugerida: decidir una de tres: (a) el Día 1 no genera `VIDEO` ni `ANALISIS` (solo un indicador a nivel `TANDA`); (b) genera `VIDEO` pero `VIDEO–ANALISIS` pasa a (0,1) y `VIDEO–OBSERVACION` a (0,4); (c) se analiza igual y D-54 (d) se retira. Registrar como D-57 y propagar a grafo, físico, apéndice D, IW §4/§7 y cap. 5 cuando se pida.

### MD-25 — Pregunta abierta: quién borra los videos a los 30 días (worker o tarea del backend)
- Severidad: Media
- Ubicación: `INSTRUCCIONES-WEB.md:1804-1806` (nota), `:468-470` (§8), `:2481` (A.11 «Tarea programada (en el backend)»); `chapters/05_diseno.tex:2343` y `:2356` («El *Worker* ejecuta diariamente una tarea programada…»), `diagramas/clases.puml:84` (`Worker.borrarVideosExpirados()`), `diagramas/diagram_design/arquitectura_capas.md` y `despliegue.md` («el worker… borra los videos a los 30 días»); `CORRECCIONES.md:97-98` (CU-16: «RNF-08 dice que eso es un *cron job*, no el worker de análisis»)
- Cita: «lo hace una **tarea programada del backend**» (IW) vs «El *Worker* ejecuta diariamente una tarea programada que elimina los archivos de video» (cap. 5, CU)
- Fuente que decide: pregunta abierta → equipo. IW reconoce la divergencia en una nota; CORRECCIONES CU-16 la consideraba un error del diagrama de casos de uso, pero el cap. 5 la sostiene y los diagramas nuevos de `diagram_design/` la repiten.
- Corrección sugerida: decidir quién ejecuta el borrado y alinear los cuatro lugares (IW, cap. 5 CU-24, `clases.puml`, `cu_paquete5.puml`/UC54).

### MD-26 — Pregunta abierta: `pipeline_analisis.md` (11-oct) presenta la CNN de fusión como clasificador principal; PENDIENTES dice «todavía no se elige»
- Severidad: Media
- Ubicación: `diagramas/diagram_design/pipeline_analisis.md:13-14` y `:25-36`, `:70-84`; contraste: `PENDIENTES.md:87-88`, `PENDIENTES-ERICK.md:19` (B-1), `chapters/05_diseno.tex:194-200` y `:258-266`, `CAMBIOS-CAP5.md:277` (CLA-03)
- Cita: «Esta versión describe la CNN de fusión (una sola red decide…)… Aquí la red es el flujo principal y decide cada segundo» vs «**Clasificador: todavía no se elige.** Candidatos: *gradient boosting* sobre rasgos y R(2+1)D-18… No escribir ResNet-50 ni Random Forest»
- Fuente que decide: pregunta abierta → equipo. El `.md` documenta su propia discrepancia con el LaTeX, pero la regla de PENDIENTES («gana esta lista») dice que nadie escriba cuál clasificador gana.
- Corrección sugerida: si la descripción del 8-oct ya es decisión, actualizar `PENDIENTES.md` («Lo que ya está decidido») y B-1; si no, marcar el diagrama como «propuesta» y no insertarlo en el cap. 5 todavía.

---

# Hallazgos de severidad Baja

### MD-27 — D-52: cifras que no cuadran ni con su propia aritmética ni con las vigentes
- Severidad: Baja
- Ubicación: `errores/preguntas-doctor.md:277`
- Cita: «15 → 13 relaciones, 66 → 60 atributos, 18 → 16 llaves foráneas lógicas»
- Fuente que decide: recuento sobre `grafo_relacional_3_vigente.puml`: hoy 15 relaciones, **63** atributos, **17** FK; quitar `INTERVALO` (3 atrib., 1 FK) y `PRESENTA` (3 atrib., 2 FK) deja 13 relaciones, **57** atributos, **14** FK.
- Corrección sugerida: reemplazar por «15 → 13 relaciones, 63 → 57 atributos, 17 → 14 llaves foráneas lógicas».

### MD-28 — Filas de §6 con notas de aplicación caducadas (D-03, D-26, D-31, D-54)
- Severidad: Baja
- Ubicación: `errores/preguntas-doctor.md:215` (D-03: «Pendiente de aplicar en `grafo_relacional_3_vigente.puml` (hoy dice `"1" --o "1..*"`)»), `:241` (D-26: «en BORIS»), `:251` (D-31: «solo los primeros 300 s»), `:279` (D-54: «La cobertura… por (a) y (d) **no se aplica** hasta que se pida»)
- Cita: D-03 vs `grafo_relacional_3_vigente.puml:244` (ya `"1" --o "1"`); D-26 vs D-56 (BORIS fuera); D-31 vs D-54 («últimos»); D-54 vs `DISENO-BD.md:291-295` y `esquema_fisico.puml:72-73` (ya aplicado)
- Fuente que decide: rango 1; el propio §6 contiene la corrección en otra fila.
- Corrección sugerida: añadir «→ ver D-56», «→ cambiado por D-54», «aplicado» y «(1,1) ya aplicado» al final de cada fila.

### MD-29 — `preguntas-doctor.md` §1–5: premisas superadas sin nota y fecha de cabecera vieja
- Severidad: Baja
- Ubicación: cabecera `:3` («Última actualización: 2026-09-03», el archivo llega a 2026-10-07); `:42-44` (Q-A: «RF-18… lo tiene fijado en 3 segundos continuos»), `:133-145` (Q-G: «0.70»), `:186-196` (§5 «Ya respondido»: «Tamaño de grupo… 6 el mínimo», «Formato de video: Siempre MP4», «Conductas: Tres», «Roles de usuario: Un solo rol»); contraste: D-49, D-32, D-28, D-30, D-29, D-08
- Cita: «Siempre MP4» vs D-30 «`.mp4` y `.mov`»; «6 el mínimo» vs D-28 «desde 2»; «Tres» vs D-29 «cuatro»; «0.70» vs D-32 «se elimina el umbral»
- Fuente que decide: rango 1. Las filas de §5 son registro fiel de lo que dijo el laboratorio (rango 2/3) y no es error mantenerlas; el problema es que están bajo «no volver a preguntar» sin indicar que el equipo las modificó.
- Corrección sugerida: añadir al encabezado de §5 «Estas respuestas son las del laboratorio; el equipo las modificó en D-08, D-28, D-29, D-30», actualizar la fecha de cabecera y anotar en Q-A/Q-G «RF-18 y el 0.70 ya no existen (D-49, D-32)».

### MD-30 — CLAUDE.md: punteros a documentos que se declaran desactualizados y menciones de CLAHE/BORIS
- Severidad: Baja
- Ubicación: `CLAUDE.md:170-174` (tabla «Dónde está cada cosa»), `:120` (siglas), `:132` (cita de RNF-02); `HISTORIAL.md:90`
- Cita: «Qué falta cambiar en el capítulo 5 | `CAMBIOS-CAP5.md`», «Correcciones pendientes… | `CORRECCIONES.md`», «Contradicciones detectadas en el LaTeX | `errores/README.md`» (los tres con banner «Desactualizado como lista de trabajo (5-oct-2026)»); «Aplica a FST, CLAHE, BORIS, IEEE, ISO, IEC» (CLAHE y BORIS ya no aparecen en el documento: D-56 y CLA-04); «RNF-02 usa «F1 ≥ 85 % por clase»» vs RNF-02 real «F1 ≥ 85 % por conducta» (`chapters/04_analisis.tex:340`, `:344`); HISTORIAL L90 «`errores/preguntas-doctor.md` §4 (Ya respondido)» vs «Ya respondido» es el **§5** (`preguntas-doctor.md:179`); «Los 22 ítems de la simulación de defensa | `HISTORIAL.md`» (HISTORIAL lista 18; los 4 de terminología ya aplicados se quitaron, `HISTORIAL.md:19-20`)
- Fuente que decide: rango 1 (los propios banners de esos archivos y `PENDIENTES.md`).
- Corrección sugerida: apuntar las tres filas a `PENDIENTES.md`/`PENDIENTES-VANESA.md`/`PENDIENTES-ERICK.md` (los viejos como «evidencia»), quitar CLAHE y BORIS de la lista de siglas (D-56), decir «F1 ≥ 85 % por conducta» (D-53) y cambiar HISTORIAL L90 a «§5». *(No toco CLAUDE.md; es sugerencia.)*

### MD-31 — Números de línea y citas desfasadas en PENDIENTES*.md
- Severidad: Baja
- Ubicación: `PENDIENTES.md:33` y `PENDIENTES-VANESA.md:28` («hoy 693–2333»; real: `\section{Diseño de casos de uso}` en `05_diseno.tex:740` y `\section{Diagramas de secuencia}` en `:2381`); `PENDIENTES-ERICK.md:45` (RF-22 «201-205» → 203-211), `:46` (RN-04 «533-536» → 527-530), `:47` (RNF-01/03 «333, 350» → 329, 347), `:49` («1137» → 1150), `:79` (L-1 «1148» → 1161), `PENDIENTES-VANESA.md:65` («la 455 del cap. 4» → 449); `PENDIENTES.md:60` («Vigente al 2026-10-05» pero incluye D-53…D-56 del 6-7 oct); `PENDIENTES.md:140` («ESC-04 (el borrado al 90 % se queda: RN-05, **D-51**)» → la decisión que lo mantiene es **D-39**)
- Fuente que decide: verificación contra el LaTeX actual.
- Corrección sugerida: renumerar con `grep -n` al cerrar cada ítem, o citar la sección/RF en lugar de la línea; fechar «Vigente al 2026-10-11»; cambiar D-51 por D-39 en ESC-04.

### MD-32 — INSTRUCCIONES-WEB: detalles menores desfasados
- Severidad: Baja
- Ubicación: `INSTRUCCIONES-WEB.md:671` y `:684` (tecla `0` rotulada «Dudosa» en la pantalla y «"no se ve"» en la lista de teclas; D-40 dejó una sola opción «dudosa», y L699-702 aclara que no existe botón «No se ve»); `:2985` («Última actualización: 5 de octubre de 2026» pero recoge D-53/D-54/D-55 del 6-oct); `:1472-1477` y `:1488-1489` (A.5 `ROI` sin `numeroCilindro`, `yAgua`, `yFondo` ni `calcularBloques()`, que `diagramas/clases.puml:~90-140` incorporó el 8-oct); `:1450` (`duracion : Float` frente a «nunca float» de L308; ya listado como M-25 de PENDIENTES-ERICK)
- Fuente que decide: D-40, D-55, `clases.puml` (rango 1/5).
- Corrección sugerida: rotular `0` como «Dudosa» en L684; actualizar la fecha; sincronizar A.5 con `clases.puml` si el anexo ha de seguir siendo «el que manda».

### MD-33 — Ortografía inconsistente: «autoregistro» / «autorregistro»
- Severidad: Baja
- Ubicación: «autoregistro» en `chapters/04_analisis.tex:91`, `INSTRUCCIONES-WEB.md:452` y `:857`, `DISENO-BD.md:409`, `CORRECCIONES.md:114`; «autorregistro» en `PENDIENTES.md:108` y `chapters/05_diseno.tex:2397`
- Fuente que decide: RAE (autorregistro, con rr).
- Corrección sugerida: unificar en «autorregistro» en los `.tex` que entran al documento (cap. 4 RF-07) y, de paso, en los `.md` vigentes.

### MD-34 — Copias y documentos de apoyo fuera de la lista, con contenido ya superado
- Severidad: Baja
- Ubicación: `para-notebooklm/preguntas-doctor.md` (copia del 7-oct 19:18: falta la fila D-56 y conserva D-26 «en BORIS»; `diff` con `errores/preguntas-doctor.md` = solo esa fila); `protocolo_fst.tex:224-234` y `:277` (`idLaboratorio`, «detección baja de 0.70»), señalado por `CAMBIOS-CAP5.md:225-244` §G pero ausente de `PENDIENTES*.md` (no entra a `main.tex`)
- Fuente que decide: rango 1 (D-55, D-32, D-56).
- Corrección sugerida: regenerar la copia de `para-notebooklm/` desde `errores/` y registrar `protocolo_fst.tex` como «histórico» o añadirlo a una lista de pendientes si se sigue usando para reuniones con el laboratorio/Dra. Cordero.

### MD-35 — Pregunta abierta: el .docx de la simulación nombra a otra directora distinta de la que cita HISTORIAL
- Severidad: Baja
- Ubicación: `docs/Retroalimentacion_Simulacion_TT2026-B066_v2.docx` (encabezado y §1: «Dra. Alicia Marcela Ramírez Guzmán»; punto de acciones: «Dra. Martha Rosa Cordero López») vs `HISTORIAL.md:11` («Directores: Dr. Israel Salas Ramírez · Dra. Martha Rosa Cordero López»), `CLAUDE.md`
- Cita: «Participaron los dos directores (Dr. Israel Salas Ramírez y Dra. Alicia Marcela Ramírez Guzmán)» (docx, rango 4) vs «Dra. Martha Rosa Cordero López» (HISTORIAL)
- Fuente que decide: pregunta abierta → equipo (confirmar si es el mismo nombre/persona o un error del docx; no afecta al LaTeX, pero HISTORIAL copia el nombre al revés de la fuente).
- Corrección sugerida: si el docx tiene un error, anotarlo en `HISTORIAL.md` («el .docx dice Alicia Marcela Ramírez en el encabezado»); si fueron dos personas distintas, corregir L11.

---

## Cobertura y límites

- **No verifiqué en vivo** las URLs de los artifacts (MD-15) ni abrí los `.docx` salvo `Retroalimentacion_Simulacion…_v2.docx`; `entrevista_sandino.docx` no se releyó (las fuentes de rango 2 se tomaron de las citas ya transcritas en `errores/`).
- **Ya conocido y no repetido** (según el brief): «Pendiente del 6-oct» (LaTeX sin la aclaración completa de D-54 en cap. 1/4/5 y apéndice D, incluido el análisis del Día 1 de control en cap. 4 L107-110 y cap. 1 L251), «D-51 sin aplicar» en el comentario de `seq_analisis_automatico.puml` (L25-26, L40) y cap. 6, M-24/M-25/M-27/M-28 de `PENDIENTES-ERICK.md` (comprobé que M-24 y M-25 siguen ciertos en `grafo_relacional_3_vigente.puml` y `clases.puml`), y A-8 (comprobé que `esquema_conceptual.tex` no dibuja `ADMINISTRADOR`, `REPORTE` ni `NOTIFICACION`).
- **No audité** los `.tex` salvo para contrastar reglas de los `.md` (los reparten otros agentes): del cap. 5 solo leí L1–745 y los pasajes citados (casos de uso L740-2380, secuencias y mockups no revisados línea a línea); caps. 1–3 solo por `grep` de las reglas.
- `errores/0X/errores.md`, `errores/front/errores.md` y `REVISION-AGENTES-2026-10-03.md`: solo cabeceras y los puntos citados. Esos archivos (excepto el de REVISION y el `README.md`) **no llevan el banner «Desactualizado»** y conservan «Estado: Pendiente» en ítems que `PENDIENTES.md:139` ya da por resueltos (E01-01, 02, 03, 09, 10, 12; E04-01…04); el propio PENDIENTES lo registra como tarea de mantenimiento (`PENDIENTES-ERICK.md:95`), por eso no se reporta aparte.
- Cifras recontadas (15/63/17 y 64/17) y correspondencia D-xx ↔ §6 correctas; no encontré D-xx citados que no existan ni numeración RN/RF citada que no exista en el cap. 4 (RF-01…RF-33, RNF-01…RNF-13, RN-01…RN-15). La numeración propia de `INSTRUCCIONES-WEB.md` (R-01…R-14, distinta de RN-xx y de los riesgos R-xx del cap. 4) es una convención interna del archivo, no un error.
- `MEMORY.md` (memoria del usuario) no se auditó; su «Pendiente grande: reescribir el cap. 5» ya no es cierto y conviene actualizarlo.
