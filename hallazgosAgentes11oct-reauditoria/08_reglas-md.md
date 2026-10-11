# 08 · Reglas escritas en `.md` frente al LaTeX y los diagramas (reauditoría, HEAD 975ec4c)

**Prefijo de IDs:** `MD-`. Pasada independiente primero; al final se contrastó con `hallazgosAgentes11oct/08_reglas-md.md` (campo «Previo»). No se copió ningún hallazgo anterior sin releer la línea en HEAD; los que ya no existen se listan al final.

## Alcance auditado

`CLAUDE.md`, `README.md`, `DISENO-BD.md`, `INSTRUCCIONES-WEB.md` (2986 líneas, por búsquedas dirigidas y lectura de §4, §8, §9, §11, A.9, A.11), `CAMBIOS-CAP5.md`, `PENDIENTES.md`, `PENDIENTES-VANESA.md`, `PENDIENTES-ERICK.md`, `CORRECCIONES.md`, `HISTORIAL.md`, `PREGUNTAS.md`, `MIGRACION-DIAGRAMAS.md`, `COMPARATIVA-FIGURAS-CAP5.md`, `angel.md`, `errores/README.md`, `errores/pendientes.md`, `errores/preguntas-doctor.md` (completo, D-01 a D-65, Q-A a Q-G), `errores/REVISION-AGENTES-2026-10-03.md`, `errores/0X/errores.md` y `errores/front/errores.md` (encabezados y conteos), y las copias de `para-notebooklm/`. Contraste contra `chapters/04_analisis.tex`, `chapters/05_diseno.tex`, `chapters/01–03`, `front/`, `back/apendice_C–D`, `diagramas/grafo_relacional_3_vigente.puml`, `esquema_fisico.puml`, `seq_analisis_automatico.puml` y `mockups/v2`.

## Conteos

| Severidad | Total | de ellas «pregunta abierta» |
|---|---|---|
| Alta | 4 | 0 |
| Media | 23 | 5 |
| Baja | 10 | 1 |
| **Total** | **37** | **6** |

## Verificado y sin hallazgo

- Filas D-57 a D-65: coinciden con `PENDIENTES-VANESA.md:218-222` (lista de temas y la nota «D-57 a D-60 no están aplicados a RN-04, RN-14, RF-32 ni al cap. 5»). RN-16 está en `04_analisis.tex:617-620` y se cita en CU-11 (`05_diseno.tex:1188`) y CU-17 (`:1931`). D-65: «F1 por conducta» ya está en `resumen.tex:29`, cap. 1 (`:179`, `:204`), cap. 2 (`:251`, `:264`), cap. 3 (`:346`) y cap. 4 (`:340`, `:445`). D-64 en CU-05 (`05_diseno.tex:1350`, `:1366-1368`). D-63 en CU-23 (`:2146`, «No pide nombre ni contraseña»).
- «Último segundo»: solo queda en `PENDIENTES-VANESA.md:45,54` como historia de lo revertido. RN-15 (`04_analisis.tex:597-615`) y D-53 coinciden. No quedan «Día 1 vs Día 2», «BORIS», «0.70», «CLAHE», `numeroRata` ni `CONFIGURACION` en los `.tex` de los caps. 1–5 y `front/`.
- Conteos de encabezado de `PENDIENTES.md:14-15`: Vanesa 13/17/4/4/1 y Erick 5/19/6/3/4 coinciden con las filas (cuentan ítems cerrados y abiertos por igual; ver MD-17). Conteos de `errores/README.md:56-61` coinciden con los encabezados `##` de cada `errores.md`.
- Rutas que los `.md` mencionan: existen, salvo archivos de repositorios externos (`fst_auto`, `fst-etiquetador`: `segundos.py`, `lib.py`, `etiquetar.py`, `revisor*.html`) y `worker_fake.py`/`nombre.puml` (futuros o ejemplos).
- `grafo_relacional_3_vigente.puml`: 15 relaciones, 17 llaves foráneas y 63 atributos; coincide con `DISENO-BD.md:282-284`. `VIDEO "1" --o "1" ANALISIS` (`:244`).
- D-57 a D-60 no se cuentan como hallazgo (decisión: pendientes de propagar); se menciona una vez en MD-06.

---

# Hallazgos de severidad Alta

### MD-01 — `INSTRUCCIONES-WEB.md` sigue diciendo que el Día 1 del grupo control se analiza (D-54 d lo descarta)
- Severidad: Alta
- Ubicación: `INSTRUCCIONES-WEB.md:424` (R-03); también `:385` (la ruta de subida «crea la tanda… y encola el análisis» para Día 1 o Día 2) y `:2133`; contraste: `errores/preguntas-doctor.md:279` (D-54 d), `DISENO-BD.md:278`, `diagramas/esquema_fisico.puml:72-73`
- Cita: «El Día 1 solo se analiza (sus primeros 5 min) si la tanda es del grupo **control**» vs «El **Día 1 solo confirma que ese video existe** y es de **habituación**… no se analiza ni conserva un recorte» (D-54)
- Fuente que decide: rango 1, D-54 (usuario, 6-oct). `DISENO-BD.md:286-293` declara D-54 «aplicado» en `INSTRUCCIONES-WEB.md`, pero R-03 no se tocó. El LaTeX también lo contradice (cap. 1 `:261` y `:321-323`; cap. 4 RF-09 `:107-110`; el apéndice C lo dice porque es literal), pero eso ya está registrado como pendiente en `PENDIENTES.md:8`; aquí solo se anota como «D-54 d pendiente de propagar».
- Destinatario: Erick (IW, cap. 4) / Vanesa (cap. 1)
- Previo: MD-01
- Corrección sugerida: R-03: «Una tanda tiene como máximo 2 videos: Día 1 (20 min) y Día 2 (5 min). Solo el Día 2 se analiza; el Día 1 solo confirma que existe el video de habituación (D-54).» Revisar `:385` y `:2133` para que no se encole el Día 1 (ver MD-24).

### MD-02 — `DISENO-BD.md` deja P-08/D-03 «sin resolver» cuando D-03 está resuelto y aplicado
- Severidad: Alta
- Ubicación: `DISENO-BD.md:224` (árbol del modelo), `:405` (tabla de preguntas abiertas), `:483-497` (§8 «Errata estructural — sin resolver», «No aplicar todavía»); contraste: `errores/preguntas-doctor.md:215` (D-03), `diagramas/grafo_relacional_3_vigente.puml:244` y `:65-68`, `DISENO-BD.md:407` (D-05 «se disolvió con D-03»)
- Cita: «Análisis (1,N — un video se puede reanalizar · pendiente P-08/D-03)» y «**No aplicar todavía:** … falta cerrarlo formalmente» vs «**Resuelto (equipo, 2026-09-13):** se reemplaza… `VIDEO — ANALISIS` queda en (1,1)» y `VIDEO "1" --o "1" ANALISIS`
- Fuente que decide: rango 1, D-03 (equipo, 13-sep) y D-24 (`UNIQUE (idVideo)`). `DISENO-BD.md` se declara «punto de partida obligatorio» (`CLAUDE.md`) y afirma lo contrario.
- Destinatario: Erick
- Previo: MD-02
- Corrección sugerida: L224 «Análisis (1,1 — un video, un análisis vigente; D-03/D-24)»; L405 marcar «Cerrada (equipo, 13-sep): se reemplaza»; reescribir §8 como «Resuelta por D-03: el reanálisis reemplaza; `OBSERVACION` sigue colgando de `VIDEO`», o dejar un puntero a D-03. (Si D-60 cambia el reanálisis, anotarlo como «D-60 pendiente».)

### MD-03 — Cap. 5 describe procesamiento parcial si faltan cilindros; D-20 lo descarta (todo o nada)
- Severidad: Alta
- Ubicación: `chapters/05_diseno.tex:332-339` («Separación por espécimen», frase en `:336-338`); contraste: `errores/preguntas-doctor.md:231` (D-20) y `:126-145` (Q-G), `chapters/04_analisis.tex:568-571` (RN-11)
- Cita: «Si el número de cilindros detectados es menor al esperado, el sistema reporta cuáles especímenes pudo procesar y cuáles no, en lugar de abortar el análisis completo» vs «todo o nada, siguiendo RN-11… El comportamiento de "reporta cuáles especímenes pudo procesar" que describe el cap. 5 no se implementa» (D-20) y RN-11 «si… el pipeline no encuentra los cilindros, se detiene»
- Fuente que decide: rango 1, D-20 (equipo, 13-sep; «provisional» hasta confirmar Q-G). No figura en ningún `PENDIENTES*.md`.
- Destinatario: Erick
- Previo: MD-03
- Corrección sugerida: «Si no se encuentran los cilindros esperados de la tanda, el pipeline se detiene y genera el reporte de diagnóstico (ver RN-11); no se entregan resultados parciales.» Añadir el ítem a `PENDIENTES-ERICK.md`.

### MD-04 — Cap. 5 dice que el entrenamiento se alimenta de «anotación experta»
- Severidad: Alta
- Ubicación: `chapters/05_diseno.tex:99-102`; contraste: `CLAUDE.md` («Prohibición vigente — métricas de validación»), `errores/preguntas-doctor.md:241` (D-26) y `:281` (D-56)
- Cita: «de entrenamiento del modelo ---anotación experta, dataset y entrenamiento--- alimenta» vs «el clasificador se entrena con videos del laboratorio pero **sin** usar las anotaciones manuales del Dr. Sandino» (`CLAUDE.md`) y D-56 «las etiquetas… salen del **etiquetador del equipo**»
- Fuente que decide: rango 1 (D-26/D-56).
- Destinatario: Erick
- Previo: MD-04
- Corrección sugerida: «…el ciclo de entrenamiento del modelo ---etiquetado por el equipo con su etiquetador, dataset y entrenamiento--- alimenta al clasificador…». Agregarlo a `PENDIENTES-ERICK.md`.

---

# Hallazgos de severidad Media

### MD-05 — D-62, D-63 y D-64 solo están aplicados en la mitad del LaTeX; el cap. 5 se contradice dentro de sí mismo
- Severidad: Media
- Ubicación: eliminar experimento: `chapters/05_diseno.tex:2543` («La eliminación de un experimento no está en esta lista sino en su detalle») y `:2568-2569` («la acción pide escribir el nombre del experimento y la contraseña (RF-27, RN-09)») frente a `:2146` y `:2125-2130` (CU-23 «desde el dashboard o desde su detalle… No pide nombre ni contraseña»); `04_analisis.tex:247-250` (RF-27 «desde el dashboard… requiere confirmación explícita»), `:556-559` (RN-09); `mockups/v2/experimento.html:59` («pide escribir el nombre del experimento… y la contraseña de la cuenta»); `INSTRUCCIONES-WEB.md:429` (R-08), `:526`, `:2268` (confirmación explícita). Validación: `04_analisis.tex:561-566` (RN-10 «La validación de formato ocurre en el cliente», orientación «antes de intentar subirlo») frente a CU-05 `05_diseno.tex:1366-1368`. Despliegue: `04_analisis.tex:400-405` (RNF-10 «servidor institucional provisto por la ESCOM… proceso de despliegue»)
- Cita: «pide escribir el nombre del experimento y la contraseña» vs «No pide nombre ni contraseña» (D-63 / CU-23); «Despliegue documentado y verificado en al menos dos entornos» vs «El despliegue queda fuera del alcance y no se registra en el documento» (D-62)
- Fuente que decide: rango 1, D-62, D-63, D-64 (usuario, 11-oct). `errores/preguntas-doctor.md:287-289` y `PENDIENTES-VANESA.md:207-214` ya listan estos cabos como «Pendiente»; lo nuevo es que (a) el cap. 5 contradice su propia ficha CU-23 y (b) D-63 dice «desde el dashboard y desde el detalle» y el texto de la lista de experimentos dice lo contrario.
- Destinatario: Erick
- Previo: nuevo (decisiones del 11-oct)
- Corrección sugerida: `:2543` → «La eliminación de un experimento está en esta lista y en su detalle»; `:2568-2569` → «la acción pide solo un aviso de “¿está seguro?”»; RF-27/RN-09 → «aviso de “¿está seguro?”, sin pedir nombre ni contraseña»; mockup v2 igual; RN-10 → extensión en la interfaz, orientación y reproducibilidad en el servidor (y `seq_carga_video.puml`); RNF-10 → sin «servidor institucional/despliegue» o reformularlo como portabilidad. Registrar en `PENDIENTES-ERICK.md`.

### MD-06 — `PENDIENTES.md` «Lo que ya está decidido» quedó vieja y dice que gana sobre las decisiones nuevas
- Severidad: Media
- Ubicación: `PENDIENTES.md:60` («Vigente al 2026-10-05»; incluye D-56 del 7-oct), `:53-58` («Si algo de esta lista choca con lo que vas a escribir, gana esta lista»), `:81-82`, `:91-93`, `:96-97`; contraste: `errores/preguntas-doctor.md:279-290` (D-53 a D-65)
- Cita: «el investigador no lo inicia, pausa, cancela ni reinicia (RN-04). Reanalizar **reemplaza** (D-03)» y «**Sin vista en vivo**» y «los resultados se muestran también en bloques de 5 s (D-49)» vs D-60 «El usuario sí puede reiniciar el análisis… RN-04 y D-03 deben ajustarse», D-59 (pausa 5 min con notificación) y D-53 (cada bloque toma la conducta con más segundos). La sección no menciona D-61 (Administrador activo), D-62 (despliegue fuera), D-63, D-64 ni D-65.
- Fuente que decide: rango 1, D-53 y D-57 a D-65. D-57 a D-60 están registradas pero **no aplicadas** a propósito; se anota una sola vez como «D-5x pendiente de propagar», no por ocurrencia.
- Destinatario: Erick (la sección es suya, `PENDIENTES.md:94`)
- Previo: nuevo
- Corrección sugerida: fechar «Vigente al 2026-10-11», añadir las reglas D-53 (mayoría y desempates), D-61, D-62, D-63, D-64 y D-65, y una línea «D-57 a D-60: registradas, sin aplicar; no corregir RN-04 ni el LaTeX todavía».

### MD-07 — Las listas de pendientes siguen mostrando como abiertos ítems ya resueltos
- Severidad: Media
- Ubicación: `PENDIENTES-ERICK.md:32` (A-1), `:34` (A-9b), `:36` (A-15, primera mitad), `:63` (M-26), `:22` (B-5 tachado pero contado), `PENDIENTES.md:14-15` (conteos), `PENDIENTES.md:28`, `PENDIENTES-VANESA.md:29`
- Cita: A-1 «CLAHE, fondo por **mediana**… y línea de agua con EMA, que el pipeline real no hace» y A-9b «Citas internas “D-XX” que el lector no puede resolver» vs el LaTeX actual
- Verificación: `grep` de `CLAHE|EMA` en caps. 1–5, `front/` y `back/`: 0 resultados; la «mediana» aparece solo como opción descartada (`04_analisis.tex:662`, `05_diseno.tex:151`; el fondo usa percentil bajo). `grep \bD-[0-9]{2}\b` y `CLA-0` en `chapters/01–05`, `front/`, `back/`: 0 resultados (solo «R(2+1)D-18»). `esquema_fisico.puml` ya dice «15 tablas, 17 llaves foraneas» (`:8`) y no contiene `fn_sincronizar…`; queda solo «tres valores… dos en modo degradado» (`:91-94`, mitad de A-15).
- Fuente que decide: verificación contra el LaTeX y `PENDIENTES-VANESA.md:36-43` (Erick quitó los `D-xx` el 7-oct).
- Destinatario: Erick
- Previo: MD-16
- Corrección sugerida: marcar ✅ A-1, A-9b, M-26 y la primera mitad de A-15 (queda la nota de «tres valores»); sacar B-5 de los 🔒; recalcular `PENDIENTES.md:14-15` (Erick pasaría a 3 🔴 y 3 🔒); en `PENDIENTES.md:28` y `PENDIENTES-VANESA.md:29` dejar solo «preprocesamiento y clasificador son de Erick», sin CLAHE ni EMA.

### MD-08 — Ítem ✅ A-14 de `PENDIENTES-VANESA.md` no se cumple: la fecha sigue siendo «Mayo 2026»
- Severidad: Media
- Ubicación: `PENDIENTES-VANESA.md:100` (✅ 5-oct); `front/portada.tex:73` y `front/documento_tecnico.tex:32`
- Cita: «Fecha “Mayo 2026” → la de entrega» (✅) vs `Mayo 2026` en ambos archivos. Los nombres sí se unificaron (`portada.tex:48`, `documento_tecnico.tex:57`).
- Fuente que decide: pregunta abierta → tú y el usuario (la fecha de entrega no figura en ninguna fuente; si «Mayo 2026» es la correcta, se retira la marca; si no, se corrige).
- Destinatario: Vanesa
- Previo: nuevo
- Corrección sugerida: poner la fecha real de entrega, o reformular el ítem como «la fecha “Mayo 2026” se conserva (confirmado)». No marcar ✅ mientras tanto.

### MD-09 — Cap. 5 cita CU-21, que ya no existe
- Severidad: Media
- Ubicación: `chapters/05_diseno.tex:320`; contraste: `PENDIENTES-VANESA.md:145` («CU-21 ya no existe… cámbialo a “ver CU-22, RF-23”… Es tu zona, no la mía»)
- Cita: «(ver CU-21, RF-23)» vs «CU-21 ya no existe (se fusionó en CU-22, 5-oct)»
- Fuente que decide: `PENDIENTES-VANESA.md:145` y las fichas (`05_diseno.tex:2060`, CU-22 «Consultar dashboard»). La nota lleva seis días sin atenderse y no está en `PENDIENTES-ERICK.md`.
- Destinatario: Erick
- Previo: nuevo
- Corrección sugerida: «(ver CU-22, RF-23)» y pasar el ítem a la lista de Erick o cerrarlo.

### MD-10 — `DISENO-BD.md` §4 «El modelo, en corto» se contradice dentro de la misma sección
- Severidad: Media
- Ubicación: `DISENO-BD.md:213-215` y `:238-239` vs `:244-247`, `:248-251`, `:252-256`, `:257-258`
- Cita: «ninguna entidad es débil y la agregación desapareció» vs «**Observación es una agregación, no una relación ternaria**… La agregación cierra primero el par válido»; «la rata tiene identificador propio» vs «El espécimen no tiene identidad propia… única identidad es geométrica»; «16 interrelaciones… → 16 relaciones» vs «**15 relaciones**» (`:282`); «Un grupo tiene 6–8 especímenes… el encuadre admite máximo 4» vs D-28 «un grupo tiene **2 o más** especímenes, sin tope»; «Los otros 26 atributos» vs 63 atributos
- Fuente que decide: rango 1: D-28, D-35, D-51, D-55 y las cifras vigentes de `DISENO-BD.md:282-284` (verificadas contra el grafo).
- Destinatario: Erick
- Previo: MD-14
- Corrección sugerida: dejar un solo relato: decisión 1 «un grupo tiene 6–8 especímenes típicos, sin tope; la tanda aloja de 2 a 4»; decisión 2 «el espécimen se identifica por su posición (`numeroCilindro`, D-55)»; decisión 3 «`OBSERVACION` es una entidad asociativa»; L238-239 «15 relaciones»; decisión 4 «la medida de fondo es la conducta de cada segundo (`SEGUNDO`); `PRESENTA` es su resumen por minuto».

### MD-11 — `DISENO-BD.md` conserva instrucciones y listas de «lo que falta» de septiembre
- Severidad: Media
- Ubicación: `DISENO-BD.md:19-20` y `:116` («Capítulo 5 y `diagramas/`: no se usan. Están mal»), `:387-395` («Reescribir el cap. 5 del LaTeX | No iniciado»; «Próxima reunión: lunes 2026-09-21»), `:422-435` («El LaTeX todavía no refleja el modelo nuevo… RF-14 fija “los cuatro cilindros”; el dominio correcto es 3 ó 4… “Cámara de celular”…»), `:474-477`; contraste: `DISENO-BD.md:286-293` («Aplicado (6-oct)… cap. 1, 4 y 5»), `04_analisis.tex:148-150`, `chapters/05_diseno.tex` (reescrito: §5, §6, §7), D-28 (2 a 4)
- Cita: «El diseño de BD del capítulo 5 y los diagramas de `diagramas/` está mal y no se usa como insumo» vs «Aplicado (6-oct): `grafo_relacional_3_vigente.puml`, `esquema_fisico.puml`, `clases.puml`… cap. 1, 4 y 5»
- Fuente que decide: rango 1 (los cambios de oct) y `PENDIENTES.md:3-8`.
- Destinatario: Erick
- Previo: MD-13
- Corrección sugerida: marcar esas secciones como «histórico (septiembre)» o reescribirlas; la lista de lo que falta es `PENDIENTES.md`. Quitar «3 ó 4 cilindros» (D-28: 2 a 4) y la fecha pasada del 21-sep.

### MD-12 — `INSTRUCCIONES-WEB.md` A.11 contradice §8 y D-51 sobre `VIDEO.archivo` y el aviso del borrado por disco
- Severidad: Media
- Ubicación: `INSTRUCCIONES-WEB.md:2492` y `:2508-2513`; contraste: `:468` y `:470` (§8), `:875-878` (§11.13), `errores/preguntas-doctor.md:276` (D-51 puntos 5 y 6)
- Cita: «VIDEO.archivo no se modifica. Resultados y reportes se conservan.» y «crea NOTIFICACION “alerta de disco” para quien creó ese experimento» vs «`archivo` queda en nulo» y «`NOTIFICACION` tipo `video borrado`»
- Fuente que decide: rango 1, D-51 (usuario, 5-oct); §8 ya está actualizado.
- Destinatario: Erick
- Previo: MD-05
- Corrección sugerida: en A.11, «VIDEO.archivo queda en nulo; la fila se conserva», y la notificación del 90 % de tipo `video borrado` para el investigador de cada experimento afectado (la de `alerta de disco` va solo a los administradores, rama del 80 %).

### MD-13 — `INSTRUCCIONES-WEB.md` A.9 es anterior a D-35/D-42/D-54 aunque se declara «el contrato» del worker
- Severidad: Media
- Ubicación: `INSTRUCCIONES-WEB.md:2183-2194` (A.9); contraste: `:22-23` («si hay diferencia, manda el anexo»), `:133-148` (§4), `diagramas/seq_analisis_automatico.puml:73-86`
- Cita: «guarda su observación de este video / guarda sus 5 intervalos, con los segundos por conducta de cada uno» (A.9) vs «escribe **una fila en `SEGUNDO` por cada segundo analizado**… se queda con los **últimos 300 segundos**» (§4 y el `.puml`)
- Fuente que decide: rango 1, D-35, D-42, D-54.
- Destinatario: Erick
- Previo: MD-06
- Corrección sugerida: sincronizar A.9 con `seq_analisis_automatico.puml` (recorte a 300 s con renumeración, escritura de `SEGUNDO`, `analisis_{id}_cajas.json`, copia H.264). Mientras no, la regla L22-23 produce un contrato incompleto.

### MD-14 — `INSTRUCCIONES-WEB.md` sigue pidiendo el «disparador de `ESPECIMEN.idGrupo`» que D-55 eliminó
- Severidad: Media
- Ubicación: `INSTRUCCIONES-WEB.md:115` y `:915-916`; contraste: `errores/preguntas-doctor.md:280` (D-55 (3)), `DISENO-BD.md:276`
- Cita: «SQL de creación (dominios, tablas, disparador, semillas)» y «disparador de `ESPECIMEN.idGrupo` y datos semilla de `CONDUCTA`» vs «desaparece el `idGrupo` redundante de `ESPECIMEN` y su disparador»
- Fuente que decide: rango 1, D-55.
- Destinatario: Erick
- Previo: MD-07
- Corrección sugerida: L115 «(dominios, tablas, restricciones, semillas)»; L915-916 «dominios, 15 tablas, restricciones y datos semilla de `CONDUCTA`».

### MD-15 — `INSTRUCCIONES-WEB.md` omite «Conducta activa» en las columnas de los reportes y en la comparación
- Severidad: Media
- Ubicación: `INSTRUCCIONES-WEB.md:448` y `:2426-2427` (columnas CSV/XLSX), `:2368` (segundos sumados); contraste: `:433` (R-12 «Los reportes deben mostrarla como una columna más»), `chapters/04_analisis.tex` RF-22, `chapters/01_introduccion.tex:291`
- Cita: «columnas `Tiempo (min:seg)`, `Nado`, `Escalamiento`, `Inmovilidad`, una fila por minuto» vs «Tiempo (min:seg), Nado activo, Escalamiento, Inmovilidad y Conducta activa» (cap. 1)
- Fuente que decide: rango 1, D-29 / RN-13 / RF-22.
- Destinatario: Erick
- Previo: MD-08
- Corrección sugerida: añadir `Conducta activa` en L448, L2426-2427 y «conducta activa» en L2368 (y en la lista de conductas de §9.8).

### MD-16 — `INSTRUCCIONES-WEB.md` muestra un «código» de error que D-47 quitó
- Severidad: Media
- Ubicación: `INSTRUCCIONES-WEB.md:762`; contraste: `:584-586` (§9.4), `:865-866` (§11.10), `errores/preguntas-doctor.md:272` (D-47)
- Cita: «UI-->>I: código, descripción y botón de diagnóstico» vs «RF-16 deja de mostrar un código de error: muestra la descripción, armada a partir de la etapa»
- Fuente que decide: rango 1, D-47.
- Destinatario: Erick
- Previo: MD-09
- Corrección sugerida: «mensaje armado con la etapa y botón de diagnóstico».

### MD-17 — `INSTRUCCIONES-WEB.md` define dos rutas para la misma comparación entre grupos
- Severidad: Media
- Ubicación: `INSTRUCCIONES-WEB.md:389` (tabla principal, `/results/groups`) vs `:413` y `:2359` (`/groups/comparison`); coincide con la tabla principal `chapters/05_diseno.tex` (API); `:413` y `:2361` hablan de «los tres grupos» (el experimento tiene 3 o más)
- Cita: «`GET /experiments/{id}/results/groups`» vs «`GET /experiments/{id}/groups/comparison`»
- Fuente que decide: contrato interno; el cap. 5 usa `/results/groups`.
- Destinatario: Erick
- Previo: MD-10
- Corrección sugerida: eliminar la fila L413, cambiar L2359 a `/results/groups` y decir «los grupos» donde dice «los tres grupos».

### MD-18 — `README.md` describe el proyecto de febrero (IA, TensorFlow, anotaciones expertas, cap. 5 «a reemplazar», sin `PENDIENTES.md`)
- Severidad: Media
- Ubicación: `README.md:17`, `:19-21`, `:22`, `:41`, `:7-13`, `:58`, `:81-93`, `:133`; contraste: `CLAUDE.md` (terminología y prohibición), `chapters/04_analisis.tex:685-702` (PyTorch/scikit-learn, R(2+1)D-18)
- Cita: «sistema web asistido por inteligencia artificial (IA)… clasificar automáticamente conductas como: Nado activo, Inmovilidad, Intentos de escape» y «**Inteligencia Artificial:** OpenCV, TensorFlow y Scikit-learn» y «comparando los resultados automáticos con anotaciones expertas» y «El diseño de BD del capítulo 5 y los diagramas actuales están desactualizados y son el objetivo a reemplazar» y «Última actualización: Febrero 2026» vs «visión por computadora… aprendizaje supervisado», cuatro conductas, sin gold standard
- Fuente que decide: rango 1 (`CLAUDE.md`). El título «asistido por IA» es el registrado (D-65) y puede quedar en el título del README; el resto no.
- Destinatario: ambos
- Previo: MD-18
- Corrección sugerida: stack «Visión por computadora y aprendizaje supervisado: OpenCV, PyTorch y scikit-learn»; «nado activo, inmovilidad, escalamiento y conducta activa»; quitar «anotaciones expertas» (usar «métricas de clasificación sobre un conjunto de prueba propio»); sustituir L7-13 por un puntero a `DISENO-BD.md`/`PENDIENTES.md`; añadir `PENDIENTES*.md` al árbol; actualizar la fecha.

### MD-19 — `MIGRACION-DIAGRAMAS.md` presenta como vigentes cifras y decisiones ya revertidas, sin banner
- Severidad: Media
- Ubicación: `MIGRACION-DIAGRAMAS.md:26`, `:96`, `:156` (`numeroRata`), `:344` y `:450` (umbral 0.70), `:369` («Día 1 vs Día 2»), `:424-428` (BORIS), `:432` (YOLOv8/ByteTrack/ResNet); cabecera `:3-5` solo dice «Documento temporal»
- Cita: «**16 relaciones en total**, no 15» y «confianza de detección < 0.70» vs 15 relaciones (`grafo_relacional_3_vigente.puml:13`) y D-32/D-47; los otros trackers viejos llevan «Desactualizado como lista de trabajo (5-oct-2026)» y este no
- Fuente que decide: rango 1 (D-32, D-44, D-47, D-51, D-55, D-56).
- Destinatario: Erick
- Previo: MD-19
- Corrección sugerida: copiar el banner de `CAMBIOS-CAP5.md:3` o borrarlo, como prevé su §6.

### MD-20 — `errores/pendientes.md` sin banner: «mínimo 3» y cap. 5 «sin revisar» como vigentes
- Severidad: Media
- Ubicación: `errores/pendientes.md:6`, `:15`, `:27`; contraste: `errores/preguntas-doctor.md:245` (D-28), `chapters/05_diseno.tex` (reescrito)
- Cita: «El número es variable, mínimo 3 y máximo 4» y «**Ahora hay que reescribirlo completo**» vs «una tanda tiene de **2 a 4** especímenes» (D-28)
- Fuente que decide: rango 1, D-28.
- Destinatario: Erick
- Previo: MD-21
- Corrección sugerida: añadir el banner de `errores/README.md:3` y cambiar T-02 a «de dos a cuatro».

### MD-21 — Cap. 4 «Factibilidad operativa» describe tres grupos y 6–9 videos por experimento; ningún ítem pendiente lo cubre
- Severidad: Media
- Ubicación: `chapters/04_analisis.tex:927-928`; contraste: `PENDIENTES.md:64-69` («tres o más grupos (en promedio 4)… un tipo puede repetirse»), `PENDIENTES-VANESA.md:67` (A-4, solo cap. 1)
- Cita: «cada uno con tres grupos (control, referencia y tratamiento experimental) de entre 6 y 8 especímenes cada uno. Cada experimento genera entre 6 y 9 videos» vs «tres o más grupos (en promedio 4)»
- Fuente que decide: rango 1 (lista «Lo que ya está decidido», D-28, entrevista PA/P19).
- Destinatario: Erick
- Previo: MD-22
- Corrección sugerida: «tres tipos de grupo, tres o más grupos por experimento (en promedio 4), 6–8 especímenes por grupo como valor típico, una o más tandas por grupo»; agregar a `PENDIENTES-ERICK.md`.

### MD-22 — Filas D-04, D-06 y D-14 sin marca de «sin objeto»; D-06 sigue pidiendo reabrirse
- Severidad: Media
- Ubicación: `errores/preguntas-doctor.md:217` (D-06 «esta pregunta se reabre»), `:218` (D-04), `:226` (D-14) vs `:276` (D-51 «Deja sin objeto a D-06 y D-14») y `:280` (D-55 «deja sin objeto a D-04»); `PENDIENTES-ERICK.md:19` (B-1 «D-06»), `CAMBIOS-CAP5.md:277`; `DISENO-BD.md:406-408` sí lo marca
- Cita: «si gana la fusión de los dos, el sistema vuelve a tener dos archivos de modelo y esta pregunta se reabre» (D-06) vs «Deja sin objeto a D-06 y D-14» (D-51)
- Fuente que decide: D-51 dice sin objeto, pero la nota del 5-oct plantea reabrirlo si gana la fusión → pregunta abierta → equipo (sigue la elección del clasificador, CLA-03).
- Destinatario: Erick
- Previo: MD-12
- Corrección sugerida: anotar «Sin objeto desde D-51/D-55» en D-04, D-06 y D-14; en B-1 quitar «D-06» o reescribirlo como «si gana la fusión, decidir dónde se documentan los dos archivos de modelo».

### MD-23 — Pregunta abierta: `back/apendice_D.tex` declara NOT NULL tres columnas de `ANALISIS` que `INSTRUCCIONES-WEB.md` deja vacías al encolar
- Severidad: Media (pregunta abierta)
- Ubicación: `back/apendice_D.tex:174-180` (`etapa`, `nivelClasif`, `fechaAnalisis`: «No»); contraste: `INSTRUCCIONES-WEB.md` Anexo B (`etapa… -- nula mientras esta en cola`, `fechaanalisis… la fija el worker al terminar`) y §11 punto 4 `[PROPUESTA]`
- Cita: «`etapa` … No» y «`fechaAnalisis` … No» vs «nula mientras está en cola» / «la fija el worker al terminar»
- Fuente que decide: pregunta abierta → equipo (ningún D-xx fija la nulidad de esas tres columnas).
- Destinatario: Erick
- Previo: MD-11
- Corrección sugerida: decidir y registrar un D-66: si son nulas hasta que el worker las llena, «Sí» en apéndice D y `esquema_fisico.puml`; si no, quitar la propuesta del Anexo B y fijar un valor inicial.

### MD-24 — Pregunta abierta: qué hace el Día 1 en el modelo si D-54 d dice que no se analiza (y para qué sirve)
- Severidad: Media (pregunta abierta)
- Ubicación: `errores/preguntas-doctor.md:279` (D-54 d), `:269` (D-44 «el Día 1 solo verifica el nivel de estrés»), `:190` (§5); `chapters/04_analisis.tex:575-579` (RN-12 «El Día 1 solo verifica que los especímenes lleguen con el mismo nivel de estrés»); `diagramas/grafo_relacional_3_vigente.puml:243-246`; `INSTRUCCIONES-WEB.md:126`, `:358`, `:432` (R-11), `:541`
- Cita: «El Día 1 solo confirma que ese video existe y es de habituación… no se analiza» (D-54) vs «El Día 1 solo verifica que los especímenes lleguen con el mismo nivel de estrés» (RN-12, D-44) y `VIDEO "1" --o "1" ANALISIS`, `VIDEO "1" --o "2..4" OBSERVACION`
- Fuente que decide: pregunta abierta → tú y el usuario. Si el Día 1 no se analiza, no puede «verificar» el estrés con datos del sistema, un video de Día 1 no tendría `ANALISIS` ni `OBSERVACION`, y las cardinalidades (1,1) y (2,4) dejan de ser ciertas.
- Destinatario: ambos
- Previo: MD-24
- Corrección sugerida: decidir una de: (a) el Día 1 no genera `VIDEO` ni `ANALISIS`; (b) genera `VIDEO` con `VIDEO–ANALISIS` en (0,1); (c) se analiza y D-54 d se retira. Registrar como D-66 y propagar solo cuando se pida. Aclarar de paso el texto de RN-12 sobre el estrés.

### MD-25 — Pregunta abierta: quién borra los videos a los 30 días (worker o tarea del backend)
- Severidad: Media (pregunta abierta)
- Ubicación: `INSTRUCCIONES-WEB.md:468-470` y `:2481` (A.11 «Tarea programada (en el backend)»); `chapters/05_diseno.tex:2245` y `:2258` («El *Worker* ejecuta diariamente una tarea programada…»); `diagramas/clases.puml:84` (`Worker.borrarVideosExpirados()`); `CORRECCIONES.md` (CU-16: RNF-08 «es un *cron job*, no el worker de análisis»)
- Cita: «lo hace una **tarea programada del backend**» (IW) vs «El *Worker* ejecuta diariamente una tarea programada que elimina los archivos de video» (cap. 5)
- Fuente que decide: pregunta abierta → equipo.
- Destinatario: Erick
- Previo: MD-25
- Corrección sugerida: decidir quién la ejecuta y alinear IW, CU-14 del cap. 5, `clases.puml` y `cu_paquete5.puml`.

### MD-26 — Pregunta abierta: `pipeline_analisis.md` presenta la CNN de fusión como clasificador principal; `PENDIENTES.md` dice «todavía no se elige»
- Severidad: Media (pregunta abierta)
- Ubicación: `diagramas/diagram_design/pipeline_analisis.md:11-13`; contraste: `PENDIENTES.md:87-88`, `PENDIENTES-ERICK.md:19` (B-1), `chapters/05_diseno.tex:194-200` y `:258-266`
- Cita: «Esta versión describe la CNN de fusión… No es lo que describe hoy el cap. 5» vs «**Clasificador: todavía no se elige.** Candidatos: *gradient boosting* sobre rasgos y R(2+1)D-18»
- Fuente que decide: pregunta abierta → equipo. Si la descripción ya es decisión, actualizar `PENDIENTES.md` y B-1; si no, marcar el diagrama como «propuesta» y no insertarlo en el cap. 5.
- Destinatario: Erick
- Previo: MD-26
- Corrección sugerida: ver arriba.

### MD-27 — Pregunta abierta: `DISENO-BD.md` da dos juegos de URLs para los mismos tres artifacts
- Severidad: Media (pregunta abierta)
- Ubicación: `DISENO-BD.md:189` (`claude.ai/artifact/Y7uJ7Mje…`, `FJtL6wbw…`, `972fCkz4…`) vs `:193-195` (`claude.ai/code/artifact/fc01fd30-…`, `73df37d9-…`, `41a09816-…`) y `:197` («se verificaron… el 2026-09-14»)
- Cita: «Actualizados el 2026-10-06… Conceptual https://claude.ai/artifact/Y7uJ7…» vs «Diseño Conceptual FST v4 | https://claude.ai/code/artifact/fc01fd30-…»
- Fuente que decide: pregunta abierta → tú y el usuario (no se verificaron las URLs en vivo).
- Destinatario: Erick
- Previo: MD-15
- Corrección sugerida: dejar una sola URL por artifact (la del 6-oct) y marcar las otras como anteriores.

---

# Hallazgos de severidad Baja

### MD-28 — `CLAUDE.md` y `HISTORIAL.md`: punteros y cifras desfasadas
- Severidad: Baja
- Ubicación: `CLAUDE.md:120` (siglas «FST, CLAHE, BORIS, IEEE…»), `:127-134` («F1 por clase» en OE-5 y RNF-02), `CLAUDE.md` tabla «Dónde está cada cosa» («Los 22 ítems de la simulación de defensa»; filas hacia `CAMBIOS-CAP5.md`, `CORRECCIONES.md`, `errores/README.md`, los tres con banner de desactualizado); `HISTORIAL.md:60-62` («32–40 videos/semestre, 200+ horas-persona»; «RF-01 a RF-31, RNF-01 a RNF-13 y RN-01 a RN-13»), `:90` («`preguntas-doctor.md` §4 (Ya respondido)»)
- Cita: «F1 ≥ 85 % por clase» (`CLAUDE.md`) vs «F1 $\geq 85$ % por conducta» (`04_analisis.tex:340`, `:344`); «Los 22 ítems» vs 18 (`HISTORIAL.md:24-51`); «§4» vs «Ya respondido» es el §5 (`preguntas-doctor.md:179`); «32–40 videos/semestre» vs `01_introduccion.tex:111` «32 a 40 videos, aunque no tiene un calendario fijo»; RF hasta RF-33 y RN hasta RN-16
- Fuente que decide: D-65 (a) para «por conducta» (discrepancia `CLAUDE.md` ↔ LaTeX, no error del LaTeX); CLAHE y BORIS ya no están en el documento (CLA-04, D-56). `PENDIENTES-VANESA.md:215` ya avisa lo de «por clase».
- Destinatario: Erick
- Previo: MD-30
- Corrección sugerida: «F1 por conducta»; quitar CLAHE y BORIS de las siglas; «Los 18 ítems»; apuntar los punteros viejos a `PENDIENTES*.md`; `HISTORIAL.md:90` a «§5»; marcar las cifras de `HISTORIAL.md:60-62` como históricas.

### MD-29 — `errores/preguntas-doctor.md` §1–5: premisas superadas sin nota y cabecera vieja
- Severidad: Baja
- Ubicación: `:3` («Última actualización: 2026-09-03»; llega a 2026-10-11), `:42-44` (Q-A «RF-18… fijado en 3 segundos continuos»), `:128-145` (Q-G con «0.70»), `:183-205` (§5 «Ya respondido — no volver a preguntar»: «Formato de video: Siempre MP4», «Conductas: Tres», «Roles de usuario: Un solo rol… sin permisos diferenciados», «Tamaño de grupo… 6 el mínimo», «Reanálisis… solo el más reciente»)
- Cita: «Siempre MP4» vs D-30 «`.mp4` y `.mov`»; «Tres» vs D-29 «cuatro»; «Un solo rol» vs D-08/D-12; «6 el mínimo» vs D-28 «desde 2»; «0.70» vs D-32/D-47 «se elimina el umbral»; «3 segundos continuos» vs D-49
- Fuente que decide: rango 1. Las filas de §5 registran lo que dijo el laboratorio (rango 2/3); el problema es que están bajo «no volver a preguntar» sin indicar que el equipo las modificó.
- Destinatario: Erick
- Previo: MD-29
- Corrección sugerida: añadir al encabezado de §5 «respuestas del laboratorio; el equipo las modificó en D-08, D-28, D-29, D-30», anotar en Q-A y Q-G «RF-18 y el 0.70 ya no existen (D-49, D-32)» y actualizar la fecha.

### MD-30 — Notas de aplicación caducadas en filas de §6 (D-03, D-26, D-31, D-54, D-61)
- Severidad: Baja
- Ubicación: `errores/preguntas-doctor.md:215` (D-03 «Pendiente de aplicar en `grafo_relacional_3_vigente.puml` (hoy dice `"1" --o "1..*"`)»), `:241` (D-26 «en BORIS»), `:251` (D-31 «solo los primeros 300 s»), `:279` (D-54 «La cobertura… no se aplica hasta que se pida»), `:286` (D-61 «Falta en la pantalla de administración»)
- Cita: D-03 vs `grafo_relacional_3_vigente.puml:244` (`"1" --o "1"`); D-26 vs D-56; D-31 vs D-54 («últimos»); D-61 vs `05_diseno.tex:2749-2750` («el sistema impide dejar sin ningún Administrador activo»)
- Fuente que decide: rango 1; el propio §6 contiene la corrección en otra fila.
- Destinatario: Erick
- Previo: MD-28 (D-61 es nuevo)
- Corrección sugerida: añadir «(ya aplicado)», «→ ver D-56», «→ cambiado por D-54» y quitar «Falta en la pantalla de administración» de D-61.

### MD-31 — D-52: cifras que no cuadran con su propia aritmética
- Severidad: Baja
- Ubicación: `errores/preguntas-doctor.md:277`
- Cita: «15 → 13 relaciones, 66 → 60 atributos, 18 → 16 llaves foráneas lógicas»
- Fuente que decide: recuento sobre `grafo_relacional_3_vigente.puml`: hoy 15 relaciones, 63 atributos, 17 llaves foráneas; quitar `INTERVALO` (3 atributos, 1 FK) y `PRESENTA` (3 atributos, 2 FK) deja 13 relaciones, 57 atributos, 14 FK.
- Destinatario: Erick
- Previo: MD-27
- Corrección sugerida: «15 → 13 relaciones, 63 → 57 atributos, 17 → 14 llaves foráneas lógicas».

### MD-32 — Números de línea y atribuciones desfasadas en `PENDIENTES*.md`
- Severidad: Baja
- Ubicación: `PENDIENTES.md:33` y `PENDIENTES-VANESA.md:28` («hoy 693–2333»; real: `\section{Diseño de casos de uso}` en `05_diseno.tex:740`, `\section{Diagramas de secuencia}` en `:2285`); `PENDIENTES-ERICK.md:34` (A-9b), `:45-49` (RF-22, RN-04, RNF-01/03, `1137`→`1155`), `:79` (`1148`→`1166`), `PENDIENTES-VANESA.md:65` («la 455 del cap. 4» → `449`); `PENDIENTES.md:140` («ESC-04 (el borrado al 90 % se queda: RN-05, **D-51**)» → la decisión es **D-39**)
- Fuente que decide: verificación contra el LaTeX actual.
- Destinatario: ambos
- Previo: MD-31
- Corrección sugerida: citar sección/RF en vez de línea o renumerar con `grep -n`; D-39 en ESC-04.

### MD-33 — `INSTRUCCIONES-WEB.md` detalles menores
- Severidad: Baja
- Ubicación: `INSTRUCCIONES-WEB.md:684` (tecla `0` como «no se ve»; D-40 fusionó «no se ve» y «dudosa» en una sola opción y D-53 conserva «no se ve» solo en el CSV) y `:2985` («Última actualización: 5 de octubre de 2026»; recoge D-53 a D-55 del 6-oct); `:1450` (`duracion : Float`, frente a «nunca float» de `:308`)
- Fuente que decide: D-40, D-53, D-55.
- Destinatario: Erick
- Previo: MD-32
- Corrección sugerida: rotular `0` según la pantalla vigente (9.7), actualizar la fecha.

### MD-34 — Ortografía inconsistente: «autoregistro» / «autorregistro»
- Severidad: Baja
- Ubicación: «autoregistro» en `chapters/04_analisis.tex:91`, `chapters/05_diseno.tex:1958`, `INSTRUCCIONES-WEB.md:452` y `:857`, `DISENO-BD.md:409`; «autorregistro» en `PENDIENTES.md:108`, `chapters/05_diseno.tex:2301`
- Fuente que decide: RAE (autorregistro).
- Destinatario: Erick
- Previo: MD-33
- Corrección sugerida: unificar en «autorregistro», empezando por los `.tex`.

### MD-35 — Copias y documentos de apoyo con contenido superado
- Severidad: Baja
- Ubicación: `para-notebooklm/preguntas-doctor.md` (301 líneas; `diff` con `errores/preguntas-doctor.md` = 10 líneas distintas, copia del 6-oct); `COMPARATIVA-FIGURAS-CAP5.md:43-46` («Ninguna de las 19 “listas” está insertada todavía en `05_diseno.tex`»; el cap. 5 inserta `arquitectura_software`, `pipeline`, `esquema_conceptual`, `esquema_fisico`, `cu_*`, `seq_*` y `clases`); `protocolo_fst.tex:224-234`, `:277` (`idLaboratorio`, «detección baja de 0.70»), que `CAMBIOS-CAP5.md` §G ya señala y `PENDIENTES*.md` no recoge
- Fuente que decide: rango 1 (D-32, D-55, D-56) y verificación contra el LaTeX.
- Destinatario: Erick
- Previo: MD-20 y MD-34
- Corrección sugerida: regenerar la copia desde `errores/`; poner banner de «desactualizado (septiembre)» a `COMPARATIVA-FIGURAS-CAP5.md`; marcar `protocolo_fst.tex` como histórico.

### MD-36 — `PENDIENTES-VANESA.md` §7: la lista «Pendiente de decidir» ya está respondida debajo y los conteos incluyen lo cerrado
- Severidad: Baja
- Ubicación: `PENDIENTES-VANESA.md:166-173` («❓ Pendiente de decidir (preguntas abiertas)»: C1-03, C2-04, C2-10, C3-03, C3-04, C2-13, C1-16, C1-19, C1-05, C1-08, C1-12, C1-14, C1-22, C2-14, TT-03, TT-06, DF-09, DF-11, C5-08) vs `:179-203` («Decisiones del 11-oct»: las respondidas, una por una); `:146` («BORIS en la tabla de cronograma del cap. 1»; D-56 lo quitó); `PENDIENTES.md:14` (los conteos «13 🔴 · 17 🟡…» incluyen los 34 ítems ✅ y no los de §7)
- Fuente que decide: `PENDIENTES-VANESA.md:179-203` (rango 1) y D-56.
- Destinatario: Vanesa
- Previo: nuevo
- Corrección sugerida: marcar cada ID de `:166-173` como ✅ (11-oct) o moverlos a «Resueltos»; quitar «BORIS» de `:146`; aclarar en `PENDIENTES.md:14` que los conteos son del total de ítems originales y añadir los pendientes que realmente quedan abiertos.

### MD-37 — `referencias.bib` conserva `zhang2022_bytetrack` pese al ✅ L-5; y el cronograma conserva «Empaquetado con Docker Compose»
- Severidad: Baja (el segundo punto es pregunta abierta)
- Ubicación: `PENDIENTES-VANESA.md:104` (L-5 ✅ «quitar las entradas que nadie cita: … `zhang2022_bytetrack`…») vs `bib/referencias.bib:375` (la clave sigue; solo la cita `chapters/06_desarrollo.tex:75`, comentado en `main.tex`); D-62 (`errores/preguntas-doctor.md:287`, «Aplicado en el cap. 1: alcance, responsabilidades, cronograma y stack») vs `chapters/01_introduccion.tex:413` («Entorno Flask / PostgreSQL / Docker») y `:434` («Empaquetado con Docker Compose, manuales y material de defensa»)
- Cita: «Quitar las entradas que nadie cita» vs la entrada sigue en el `.bib`; «El despliegue queda fuera del alcance y no se registra» vs «Empaquetado con Docker Compose»
- Fuente que decide: L-5: verificación contra el documento (no se cita en caps. 1–5); Docker: pregunta abierta → tú y el usuario (¿«empaquetar» cuenta como despliegue?).
- Destinatario: Vanesa
- Previo: nuevo
- Corrección sugerida: quitar `zhang2022_bytetrack` del `.bib` (o anotar que se conserva para el cap. 6); decidir si «Empaquetado con Docker Compose» queda en el cronograma.

---

## Hallazgos anteriores que ya no existen en HEAD (no se repiten)

- **MD-17 (previo), PREGUNTAS.md:** el archivo quedó en «Sin preguntas abiertas» y registra D-57 a D-61; la pregunta con «primeros 300 s» ya no está.
- **MD-23 (previo), «Día 1 vs Día 2» en el cap. 5:** `grep` de `Día~1 vs`/`contra`/`frente` en `chapters/01–05` da 0 resultados; ya está corregido.
- **A-9b/A-1/M-26 como pendientes:** tratados en MD-07 (siguen listados, pero resueltos).

## Cobertura y límites

- Se leyeron completos: `errores/preguntas-doctor.md`, `PENDIENTES.md`, `PENDIENTES-VANESA.md`, `PENDIENTES-ERICK.md`, `CLAUDE.md`, `HISTORIAL.md`, `PREGUNTAS.md`, `README.md`, `errores/README.md`, `errores/pendientes.md`, `CAMBIOS-CAP5.md` y `DISENO-BD.md`. `INSTRUCCIONES-WEB.md` se revisó por búsquedas dirigidas (R-01 a R-14, §4, §8, §9.4–9.5, §11, A.9, A.11, Anexo B), no línea por línea. `CORRECCIONES.md`, `MIGRACION-DIAGRAMAS.md`, `COMPARATIVA-FIGURAS-CAP5.md`, `angel.md`, `errores/REVISION-AGENTES-2026-10-03.md` y los `errores/0X/errores.md` solo por encabezados, banners, conteos y búsquedas de términos prohibidos.
- Se verificó con script que las rutas entre comillas de los `.md` existen (salvo repositorios externos). No se verificaron las URLs de artifacts ni se abrió ningún `.docx`; por eso **no se repite el hallazgo anterior MD-35** (nombre de la directora en el `.docx` de la simulación), que queda como pregunta abierta sin re-verificar.
- No se auditaron en detalle los mockups v2 (solo `experimento.html:59`) ni los diagramas, salvo `grafo_relacional_3_vigente.puml`, `esquema_fisico.puml` y `seq_analisis_automatico.puml`; eso corresponde a otros agentes.
- Los números de línea corresponden a HEAD 975ec4c con finales CRLF ignorados.
