# Auditoría de consistencia — resumen general

**Fecha:** 2026-10-11 · **HEAD auditado:** `da96c00` · **Modo:** solo lectura (nadie editó `.tex`, `.puml`, `.md` ni `.bib`; `git status` solo muestra la carpeta nueva `hallazgosAgentes11oct/`, además del PDF sin seguimiento que ya estaba).
**Alcance:** `chapters/01`–`05`, `front/`, `back/apendice_C` y `_D`, `diagramas/` (incluido `diagram_design/`) y los `.md` de reglas y notas. Los caps. 6–8 están comentados en `main.tex` y no se auditaron.

Los 9 documentos están en esta carpeta (`01_cap1.md` … `09_terminologia.md`). Cada hallazgo trae ubicación `archivo:línea`, cita, fuente que decide y corrección sugerida. **Nada de lo sugerido está aplicado.**

---

## 1. Conteo por agente y severidad

| # | Agente | Alta | Media | Baja | Total | Preguntas abiertas |
|---|--------|-----:|------:|-----:|------:|-------------------:|
| 01 | Cap. 1 (`C1-`) | 2 | 7 | 13 | 22 | 7 |
| 02 | Cap. 2 (`C2-`) | 0 | 7 | 7 | 14 | 6 |
| 03 | Cap. 3 (`C3-`) | 1 | 5 | 6 | 12 | 3 |
| 04 | Cap. 4 (`C4-`) | 1 | 6 | 12 | 19 | 7 |
| 05 | Cap. 5 (`C5-`) | 3 | 10 | 8 | 21 | 5 |
| 06 | Diagramas relacional y de clases (`DR-`) | 1 | 9 | 3 | 13 | 2 |
| 07 | Diagramas de flujo, CU y secuencia (`DF-`) | 5 | 10 | 10 | 25 | 3 |
| 08 | Reglas en `.md` (`MD-`) | 4 | 22 | 9 | 35 | 7 |
| 09 | Terminología y prohibiciones (`TT-`) | 2 | 5 | 9 | 16 | 3 |
| | **Total** | **19** | **81** | **77** | **177** | **43** |

Los 177 son entradas de agente: **varios describen el mismo problema** (sección 4). Contados por problema distinto, las 19 Altas se reducen a **13**.

**Limpio en todos los agentes:** ningún resto de κ de Cohen, MAE ni «gold standard» en los `.tex`; ningún «último segundo» vigente en `.tex`, `.puml` ni `.md` (solo aparece como historia marcada en `PENDIENTES-VANESA.md`); ninguna clave `\cite` sin entrada en el `.bib` (incluidas `detke1995` y `craft2010`); los `\ref` existen; las 48 rutas de `\includegraphics` del cap. 5 existen; los conteos 15 relaciones / 63 atributos / 17 FK (lógico) y 64 atributos / 17 FK (físico) cuadran contando en los archivos.

---

## 2. Los hallazgos de severidad Alta

Agrupé por problema (los 19 de agente → 13 problemas) y ordené por impacto. Los 10 primeros son «los 10 Altos»; los 3 últimos también son Alta y van aparte.

| # | Problema | IDs de agente | Dónde | Fuente que decide |
|---|----------|---------------|-------|-------------------|
| 1 | El cap. 5 dice que la «anotación experta» alimenta el entrenamiento del clasificador. Es la prohibición vigente (el entrenamiento no usa las anotaciones del Dr. Sandino) y la propia figura `flujo_general` dice lo contrario. **Lo vieron 4 agentes**; `C5-11` lo clasificó Media, los otros tres Alta | DF-01, MD-04, TT-02, C5-11 | `chapters/05_diseno.tex:99-102` | `CLAUDE.md`, D-26, D-56 |
| 2 | El cap. 5 sigue prometiendo la comparación «Día 1 vs. Día 2» (intro del Paquete 4 y curso alterno 5 de CU-09). **Lo vieron 4 agentes** | C1-02, C5-01, DF-04, MD-23 | `chapters/05_diseno.tex:808` y `:1758` | D-44, RN-12 |
| 3 | «Rata» y «animal» en el cuerpo y en una figura: `documento_tecnico.tex:79` («comportamiento animal»), `05_diseno.tex:416` y la nota visible de `esquema_fisico.puml:194-196` (que sale en el PNG) | TT-01 (+ C5-14, C5-10, TT-14) | ver ubicación | `CLAUDE.md` (terminología) |
| 4 | CU-07, curso alterno 4: «el sistema muestra alerta con código y descripción del error» en fallos del análisis | C5-02, DF-05 (+ MD-09 en `INSTRUCCIONES-WEB`) | `chapters/05_diseno.tex:1646` | D-47, RF-16 |
| 5 | Figura `arquitectura_software.png`: muestra «corrección CLAHE», solo `.mp4` y `_tracked.mp4`, lo que contradice el texto (cap. 5:158) y D-30 | C5-03, DF-02 (+ DF-15, DR-12) | `diagramas/arquitectura_software.puml:87` y su PNG | D-30, texto cap. 5 |
| 6 | `diagramas/clases.png` (el que entra al cap. 5) es anterior a `clases.puml` (cambios del 8-oct): sin `ROI` completo, sin `Especimen–ROI`, sin `calcularBloques()`, con la firma vieja de `clasificarConducta` | DR-01, C5-04 | `diagramas/clases.png` vs `diagramas/clases.puml` | `grafo_relacional_3_vigente.puml`, commit `a20d40e` |
| 7 | Cap. 5 describe procesamiento parcial si faltan cilindros («reporta cuáles especímenes pudo procesar … en lugar de abortar»); D-20 decidió todo o nada, y el propio cap. 5 se contradice en L187-188 y L303-306 | MD-03 (Alta), C5-12 (Media, pregunta abierta) | `chapters/05_diseno.tex:337-339` | D-20 (equipo, provisional, Q-G) |
| 8 | El cap. 3 presenta la CNN como el clasificador y nunca menciona el *gradient boosting*; la lista vigente dice «clasificador sin elegir» con dos candidatos | C3-01 (ver tensión con DF-13/MD-26, sección 4) | `chapters/03_marco_teorico.tex` (sección del clasificador) | `PENDIENTES.md` (CLA-03) |
| 9 | R-03 (riesgos) supone que el laboratorio entrega registros conductuales para entrenar y validar el clasificador | C4-01 | `chapters/04_analisis.tex:800-805` | D-26, D-56, fila «Etiquetador del equipo» del mismo cap. |
| 10 | «La propuesta original del sistema se conserva» al describir la revisión segundo a segundo; D-53 quitó `SEGUNDO.propuesta` y el grafo solo guarda `conducta` y `origen` | C1-01 | `chapters/01_introduccion.tex:286-287` | D-53, `grafo_relacional_3_vigente.puml` |
| 11 | `seq_consulta_resultados` define «agrupado» como «dos conductas» y omite la conducta activa | DF-03 | `diagramas/seq_consulta_resultados.puml:25,32` | D-29, D-41, RN-13 |
| 12 | `INSTRUCCIONES-WEB.md` R-03: «El Día 1 solo se analiza (sus primeros 5 min) si la tanda es del grupo control» | MD-01 | `INSTRUCCIONES-WEB.md:424` | D-54(d) (el Día 1 solo confirma la habituación; los últimos 300 s) |
| 13 | `DISENO-BD.md` deja P-08/D-03 «sin resolver / no aplicar todavía»; D-03 está resuelto, aplicado en el grafo y reforzado con UNIQUE (D-24) | MD-02 | `DISENO-BD.md` L224, L405, §8 (L483-497) | D-03, D-24 |

**Verificado por mí contra los archivos** (los que uso como evidencia central): #1, #2, #3, #4, #7, #9, #10, #11 y #12 (leí la línea citada). Los demás los di por buenos con la verificación del agente.

---

## 3. Lo que más pesa aunque no sea Alta

- **C4-02 (Media, pregunta abierta → laboratorio) toca el último commit.** RN-15 dice que el laboratorio ya usó la técnica de predominancia («la ha usado en parte de sus análisis manuales»); la transcripción (N-01) y Q-A describen un **muestreo instantáneo cada 5 s**, y Q-A sigue sin respuesta. La regla de mayoría (D-53, `e51eaa8`) no se cuestiona: lo dudoso es la atribución al laboratorio y la frase de que los bloques «se pueden comparar con el análisis manual» (RF-18, justificación de umbrales). Relacionado: C4-06 (RN-15 no cubre todos los empates ni cómo cuenta la conducta activa).
- **D-54(d) deja una laguna en el modelo (DR-04 y MD-24, pregunta abierta).** Si el Día 1 no se analiza, un video de Día 1 no tendrá `ANALISIS` ni `OBSERVACION`, pero las cardinalidades Video–Análisis (1,1) y Video–Observación (2,4) siguen en todos los diagramas y en el apéndice D. Ningún pendiente lo registra.
- **Regla de calidad de la figura.** Tres agentes (C5-10, DF-08, TT-04) y DR-10 coinciden: varias figuras que entran al cap. 5 (esquema físico, estados, secuencias) muestran códigos `D-xx`, fechas internas, SQL y «rata» dentro de la imagen. Incumple la regla de diagramas («sin SQL ni código») y la de no dejar `D-xx` en el documento.
- **Bibliografía (C2-01, C2-02, C2-03).** Según el agente del cap. 2, que consultó Crossref, los autores de `chan2025_yolo`, `della_valle2025` y `meng2024_dsaan` en el `.bib` no coinciden con los de los artículos. **No lo re-verifiqué**; confírmalo antes de corregir.
- **Citas dudosas (pregunta abierta, ninguna verificada):** `cryan2005` es sobre la suspensión de la cola pero se cita para el nado forzado (C3-03, también en caps. 1 y 4); ResNet y el gradiente que se desvanece (C3-04); `armario2021` (C2-13); Pressman para los umbrales de disco (C4-16); atributos de ISO 12207 y 25010:2023 (C1-16, C4-15).
- **Choque de reglas entre `CLAUDE.md` y el LaTeX (TT-06).** `CLAUDE.md` fija «F1 por clase» (OE-5, RNF-02), pero RNF-02 dice «por conducta» y D-53 pide «conducta». Es decisión tuya, no de los agentes.
- **Portada (TT-03).** El título en portada y documento técnico usa «IA» y «RATA». `CLAUDE.md` los prohíbe en el documento, pero el título puede ser el registrado ante la escuela; pregunta abierta para equipo y directores.

---

## 4. Contradicciones que aparecen en más de un agente

| Contradicción | Agentes / IDs | Comentario |
|---------------|---------------|------------|
| «Anotación experta» alimenta el entrenamiento | DF-01, MD-04, TT-02, C5-11 (+ `flujo_sistema.md` ya lo detectó) | La severidad no coincide entre agentes (Media vs Alta). Es Alta: viola una prohibición vigente |
| Día 1 vs Día 2 en cap. 5 | C1-02, C5-01, DF-04, MD-23 | Una sola corrección en dos líneas |
| Código de error en CU-07 | C5-02, DF-05, MD-09 | MD-09 es el mismo resto en `INSTRUCCIONES-WEB` (secuencia de progreso) |
| Figura de arquitectura vieja (CLAHE, solo `.mp4`, `_tracked`) | C5-03, DF-02, DF-15, DR-12 | DR-12 es el comentario de cabecera con «16 relaciones» |
| `clases.png` desactualizado | DR-01, C5-04 | Regenerar el PNG desde `clases.puml` |
| Cap. 5 L595: «las mismas columnas» en físico y lógico | C5-05, DR-06 | `ANALISIS.rutaDiagnostico` solo está en el físico (hueco ya registrado en `DISENO-BD.md`; lo nuevo es la frase) |
| Códigos `D-xx`, fechas y SQL visibles en figuras | C5-10, DF-08, TT-04, DR-10, TT-16 | Seis `.puml` más con `D-xx` en el texto fuente |
| DSAAN: ¿una o tres conductas? | C1-03, C2-05 (C2-04 afín) | Cap. 1 y cap. 2 se contradicen; se resuelve leyendo a Meng et al. 2024 |
| Tres grupos fijos / «tres o más (en promedio 4)» | C4-05, DF-07, MD-22 | Afecta la cuenta de videos de la factibilidad operativa |
| «Cuatro módulos» del pipeline vs «tres etapas» | C5-15, DF-23 (+ observación de C3) | Cap. 5 L119 y la figura del pipeline |
| Listas de conductas con tres valores donde son cuatro | C3-02, C4-19, C5-16, DF-22, TT-12, C4-18 | RNF-02 incluida |
| OE-5 citado sin objetivos rotulados | C1-09, TT-07 | Cap. 5 L266 cita «OE-5» y el cap. 1 no rotula |
| Detección parcial de cilindros | MD-03, C5-12 | Decisión D-20 vs texto del cap. 5 |
| D-54(d) y el video de Día 1 en el modelo | DR-04, MD-24, MD-01 | MD-01 es el efecto en `INSTRUCCIONES-WEB` |
| CNN de fusión como flujo principal vs «clasificador sin elegir» | DF-13, MD-26 vs C3-01 | **Tensión entre agentes:** `pipeline_analisis.md` (11-oct) la presenta como principal; el cap. 3 solo menciona la CNN; `PENDIENTES.md` dice «todavía no se elige». Hay que decidir cuál es la línea antes de corregir cualquiera de los tres |
| Dominio de `SEGUNDO.origen` (4 valores vs 6) | C5-06, DR-05 | Cap. 5 y RF-32 dicen 4; apéndice D y físico, 6 |
| Dónde se valida el formato/orientación del video | C4-10, DF-11 | RN-10 / RF-08 (cliente, antes de subir) vs diagramas y RF-10 (backend) |
| ANY-maze sin cita | C1-19, C2-12 | |
| «Sprint 6» sin definir | C1-22, C3-08 | |
| TT1/TT2 vs TT-I/TT-II | C4-12, TT-05 | Ninguno definido |
| Vista cenital (cap. 3) vs lateral (vigente) | C2-06 (+ A-6 ya registrado) | |
| Borrado adelantado sin notificación en RF-33 / correo ausente en figuras | C4-03, DF-10 | RN-05, RF-25, RNF-09 y D-45 lo piden |
| Quién borra los videos a los 30 días | MD-25 (cap. 5: worker; `INSTRUCCIONES-WEB`: backend) | Pregunta abierta |
| `README.md`, `MIGRACION-DIAGRAMAS.md`, `errores/pendientes.md` y `DISENO-BD.md` presentan como vigente lo revertido | MD-13, MD-14, MD-18, MD-19, MD-20, MD-21 | Faltan banners de obsolescencia |

---

## 5. Hallazgos por destinatario

La asignación a Vanesa o a Erick sale de las zonas de `PENDIENTES.md` (caps. 1–3, `front/` de portada y resumen y `bib/` son de Vanesa; la sección de casos de uso del cap. 5, líneas ~693–2333, y `diagramas/puml/cu_*` también; todo lo demás es de Erick). Es una heurística por la ubicación citada: **un hallazgo que cita archivos de las dos zonas aparece con ambos dueños**, por eso los totales de Vanesa y Erick suman más de 177.

### Vanesa (75 hallazgos)

- **Alta (8):** C1-01, C1-02, C3-01, C5-01, C5-02, DF-04, DF-05, TT-01
- **Media (29):** C1-03, C1-04, C1-05, C1-06, C1-07, C1-08, C1-09, C2-01, C2-02, C2-03, C2-04, C2-05, C2-06, C2-07, C3-02, C3-03, C3-04, C3-05, C3-06, C4-07, C5-07, C5-08, DF-09, DF-11, MD-08, MD-10, MD-23, TT-03, TT-06
- **Baja (38):** C1-10, C1-11, C1-12, C1-13, C1-14, C1-15, C1-16, C1-17, C1-18, C1-19, C1-20, C1-21, C1-22, C2-08, C2-09, C2-10, C2-11, C2-12, C2-13, C2-14, C3-07, C3-08, C3-09, C3-10, C3-11, C3-12, C4-10, C5-16, C5-17, C5-19, DF-19, DF-20, DF-22, DF-25, TT-08, TT-09, TT-10, TT-13

### Erick (143 hallazgos)

- **Alta (17):** C1-01, C4-01, C5-01, C5-02, C5-03, DF-01, DF-02, DF-03, DF-04, DF-05, DR-01, MD-01, MD-02, MD-03, MD-04, TT-01, TT-02
- **Media (70):** C1-04, C1-05, C1-06, C1-08, C1-09, C2-02, C2-03, C3-02, C3-03, C3-05, C4-02, C4-03, C4-04, C4-05, C4-06, C4-07, C5-04, C5-05, C5-06, C5-07, C5-08, C5-09, C5-10, C5-11, C5-12, C5-13, DF-06, DF-07, DF-08, DF-10, DF-11, DF-12, DF-13, DF-14, DF-15, DR-02, DR-03, DR-04, DR-05, DR-06, DR-07, DR-08, DR-09, DR-10, MD-05, MD-06, MD-07, MD-08, MD-09, MD-10, MD-11, MD-12, MD-13, MD-14, MD-15, MD-16, MD-17, MD-18, MD-19, MD-20, MD-21, MD-22, MD-23, MD-24, MD-25, MD-26, TT-04, TT-05, TT-06, TT-07
- **Baja (56):** C1-12, C1-14, C2-14, C3-08, C3-09, C3-12, C4-08, C4-09, C4-10, C4-11, C4-12, C4-13, C4-14, C4-15, C4-16, C4-17, C4-18, C4-19, C5-14, C5-15, C5-16, C5-17, C5-18, C5-19, C5-20, C5-21, DF-16, DF-17, DF-18, DF-19, DF-20, DF-21, DF-22, DF-23, DF-24, DF-25, DR-11, DR-12, DR-13, MD-27, MD-28, MD-30, MD-31, MD-32, MD-33, MD-34, MD-35, TT-08, TT-09, TT-10, TT-11, TT-12, TT-13, TT-14, TT-15, TT-16

### Preguntas abiertas por destinatario

**Laboratorio (Dr. Sandino) — 1:**

- C4-02 (M) — RN-15 afirma que el laboratorio usó la técnica de predominancia de Detke; la transcripción describe muestreo instantáneo

**Equipo (Erick y Vanesa; directores si aplica) — 32:**

- C1-05 (M) — «Despliegue ESCOM» en el cronograma contra «despliegue institucional fuera del alcance»
- C1-12 (B) — «En minutos genera un reporte» sin respaldo en los requisitos
- C1-14 (B) — «Flujo óptico» en el cronograma del baseline sin respaldo en el pipeline
- C1-22 (B) — Cap. 3 habla de «Sprint 6»; la metodología del cap. 1 no numera sprints
- C2-04 (M) — Descripción de YOLO-Behaviour como «detección + clasificador independiente» (pregunta abierta)
- C2-05 (M) — «Los de aprendizaje profundo más recientes sí clasifican las tres conductas» contradice la tabla y arrastra al cap. 1
- C2-12 (B) — ANY-maze descrito sin cita (EthoVision sí la tiene)
- C2-13 (B) — `armario2021` citada para un descriptor que ese artículo (revisión conceptual del FST) probablemente no respalda (pregunta abierta)
- C2-14 (B) — Métrica de tiempo del cap. 2 no aparece en el cap. 4
- C3-06 (M) — La relación de tiempo de análisis está invertida respecto al cap. 2
- C4-06 (M) — RN-15 no cubre todos los casos de empate ni indica cómo cuenta la conducta «activa» por segundo; además la frase central es ambigua
- C4-07 (M) — «PDF final», «resumen ejecutivo» y «reporte en PDF» nombran (¿o no?) lo mismo
- C4-14 (B) — Criterio de tiempo: R-04 remite a RNF-02, que dice que el tiempo no es criterio; la factibilidad operativa sí fija un tope
- C4-15 (B) — Atribuciones a normas dudosas: «atributo de portabilidad» de ISO/IEC/IEEE 12207 y nombres de atributos de ISO/IEC 25010:2023
- C4-16 (B) — Pressman citado como respaldo de los umbrales de 80/90 % de disco
- C4-19 (B) — RNF-02 lista solo tres conductas en la métrica; el resto del capítulo tiene cuatro
- C5-06 (M) — Dominio de `SEGUNDO.origen`: el cap. 5 y RF-32 dicen cuatro valores, apéndice D y esquema físico seis (pregunta abierta)
- C5-08 (M) — La eliminación de un experimento: CU-23 dice «desde el dashboard», la pantalla dice «en su detalle» y pide nombre y contraseña (pregunta abierta)
- C5-12 (M) — Detección parcial de cilindros: el cap. 5 dice «no aborta», RF-14/RN-11/CU-07 dicen «se detiene» (pregunta abierta)
- C5-17 (B) — Regla «siempre al menos un Administrador activo» sin RF ni RN (pregunta abierta)
- C5-18 (B) — El panel de administración muestra «el modelo del clasificador en uso»; ningún RF lo pide (pregunta abierta)
- DF-13 (M) — `diagram_design/pipeline_analisis` presenta la CNN de fusión como flujo principal y deja fuera la conducta activa; contradice cap. 5, `pipeline.puml` y «el clasificador no se elige todavía»
- DF-14 (M) — «Video anotado»: unas figuras lo guardan y otra dice que se quitó porque el código no lo genera
- DR-04 (M) — Video de Día 1 sin análisis ni observaciones (D-54 d) contra cardinalidades «1» y «2..4» (pregunta abierta)
- DR-07 (M) — El cap. 5 nombra «el esquema lógico» pero nunca lo muestra ni lo introduce (pregunta abierta)
- MD-11 (M) — Apéndice D declara NOT NULL columnas de `ANALISIS` que el backend deja vacías al encolar (IW Anexo B las admite nulas)
- MD-12 (M) — Filas D-04, D-06 y D-14 sin marca de «sin objeto»; D-06 aparece con dos estados y las listas de pendientes todavía dependen de él
- MD-25 (M) — Pregunta abierta: quién borra los videos a los 30 días (worker o tarea del backend)
- MD-26 (M) — Pregunta abierta: `pipeline_analisis.md` (11-oct) presenta la CNN de fusión como clasificador principal; PENDIENTES dice «todavía no se elige»
- MD-35 (B) — Pregunta abierta: el .docx de la simulación nombra a otra directora distinta de la que cita HISTORIAL
- TT-03 (M) — Título del TT con «IA» y «RATA» (portada y documento técnico)
- TT-15 (B) — Apéndice C: transcripción con «animal», «rata», «ISRS», «celular» y el nombre viejo del laboratorio

**Tú y el usuario (conversación) — 10:**

- C1-03 (M) — El cap. 1 dice que DSAAN clasifica tres conductas; el cap. 2 dice que no
- C1-08 (M) — «Gráficas de barras de distribución por conducta» no existe en RF-21 ni en el cap. 5
- C1-16 (B) — Los requisitos mínimos de calidad de video se atribuyen a *performance efficiency*
- C2-10 (B) — Sturman et al. y DeepLabCut descritos dos veces casi textualmente
- C3-03 (M) — `cryan2005` es un artículo sobre la prueba de suspensión de la cola en ratón, citado para el FST
- C3-04 (M) — Explicación de ResNet: atribuye la degradación al gradiente que se desvanece, lo que el artículo citado descarta
- DF-09 (M) — CU-11 y CU-12 están en el Paquete 1 del diagrama, pero sus fichas y la introducción del paquete 5 los tratan como del Paquete 5
- MD-15 (M) — DISENO-BD.md da dos juegos distintos de URLs para los mismos tres artifacts
- MD-24 (M) — Pregunta abierta: cómo queda el video del Día 1 en el modelo si D-54 dice que no se analiza
- TT-06 (M) — «F1 por clase» vs «F1 por conducta»

### Ítems que ninguna lista de dueño cubre y requieren decisión de quien coordina

- **TT-06** (F1 por clase / por conducta) y **TT-03** (título con «IA» y «RATA»): reglas de `CLAUDE.md` frente a lo escrito.
- **Tensión DF-13 / MD-26 / C3-01** (¿la CNN de fusión ya es la línea del proyecto?).
- **DR-04 / MD-24** (modelo vs Día 1 sin análisis).
- **MD-30, MD-17:** `CLAUDE.md` apunta a documentos que se declaran desactualizados, y `PREGUNTAS.md` conserva una pregunta ya respondida con «primeros 300 s». No toqué ninguno.

---

## 6. Límites de esta auditoría

- Es lectura y búsqueda; **no se compiló LaTeX ni PlantUML**. Las comparaciones PNG vs `.puml` se hicieron abriendo las imágenes que cada agente indica en su sección de cobertura; los `seq_*.png`, `cu_paquete*.png` y los mockups v2 no se abrieron todos.
- Los datos externos (Crossref, DOI, ISO, cifras de artículos) los comprobó cada agente por su cuenta o los dejó como «no verificado» en su sección de cobertura. No los repetí.
- El agente de reglas `.md` leyó del cap. 5 solo L1–745 más los pasajes citados; los caps. 1–3 los revisó por búsqueda de reglas. Esos tramos los cubren los agentes de capítulo.
- La severidad la asignó cada agente con el criterio del brief; hubo al menos una discrepancia (`C5-11`).
- No hice preguntas sueltas ni toqué `PREGUNTAS.md`. Mi única duda de método (partes cortadas del encargo) la dejé en el chat.
