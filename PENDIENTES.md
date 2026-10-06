# Pendientes del documento — capítulos 1 a 5

**Verificado contra el LaTeX el 2026-10-05**, ítem por ítem. Reemplaza como lista de
trabajo a `CORRECCIONES.md` (25-ago), `errores/0X/errores.md` (2-sep),
`errores/REVISION-AGENTES-2026-10-03.md` y los bloques B–D de `CAMBIOS-CAP5.md`. Esos
archivos se conservan como evidencia (citas de la entrevista, motivos); los IDs de aquí
apuntan a ellos.

Cada ítem lleva su fuente. Sin fuente de rango superior no se corrige (regla de `CLAUDE.md`).

Resumen: **5 bloqueados · 16 🔴 · 33 🟡 · 9 🟢 · 7 sin verificar**.

---

## 1. Bloqueado: no depende de editar

| # | Qué | Espera a |
|---|-----|----------|
| B-1 | **CLA-03:** escribir qué clasificador gana y su F1. Con eso se revisa el 0.80, si hay dos archivos de modelo (D-06) y la columna «DL» de la tabla comparativa del cap. 2 | Que termine el etiquetado y el entrenamiento |
| B-2 | **Métricas sin gold standard** (`CLAUDE.md`). Ligado a E04-06: RNF-02 y la justificación de umbrales (cap. 4, ~336-462) comparan «contra la anotación manual de analistas», justo lo que la regla evita | Confirmación del Dr. Sandino |
| B-3 | **CU-22:** revisión de casos de uso y notación con la Dra. Cordero | La revisión |
| B-4 | **D-52** (`INTERVALO`/`PRESENTA`) y **D-07** (recuadro y línea de agua a mano) | Decisión del equipo |
| B-5 | **CLA-04, parte BORIS:** caps. 1, 3 y 4 dicen que el laboratorio anota con BORIS (D-26) | Aclarar qué son los `*_mano.csv` de `fst_auto/etiquetas` |

---

## 2. 🔴 Alta — lo primero que vería un sinodal

| # | Dónde | Qué | Fuente |
|---|-------|-----|--------|
| A-1 | Caps. 2, 3 y 4; glosario; abreviaturas; figura del pipeline | **CLA-04:** CLAHE, fondo por **mediana** (`fst_auto` usa percentil 10) y línea de agua con EMA, cosas que el pipeline real no hace | Código de `fst_auto` |
| A-2 | Cap. 1: 11, 114, 212, 216; `resumen.tex:7` | **E01-06 / EF-02:** «dos evaluadores» y «se duplica» → son **tres analistas** y el tiempo se triplica | Entrevista P12 |
| A-3 | Cap. 1: 158, 271 | **E01-07:** el desglose por minuto se llama «opcional»; el laboratorio lo pidió como necesidad (y RF-20 lo exige) | Entrevista P9 |
| A-4 | Cap. 1: 59-66 y tabla `tab:grupos_experimentales` | **E01-05:** «tres grupos de entre 6 y 8» → hay tres **tipos** de grupo y 4 o más grupos por experimento | Entrevista PA, P19 |
| A-5 | Cap. 1: 157-198 | La **cuarta conducta** (conducta activa) no aparece en la propuesta ni en los objetivos; solo en la línea 281 | RN-13, D-29 |
| A-6 | Cap. 3: 62 | **E03-01:** criterio de escalamiento escrito «desde la vista cenital»; el sistema usa vista lateral | Equipo; el cap. 2 ya tiene el criterio lateral |
| A-7 | Cap. 3: 285-287 | **E03-03:** el marco teórico enumera tablas («usuarios, experimentos, sesiones de video, resultados por rata…») del modelo viejo | Modelo vigente (cap. 5) |
| A-8 | Cap. 5: ~293-303 | El párrafo del DER conceptual dice que incluye `ADMINISTRADOR`, `REPORTE` y `NOTIFICACION`; `esquema_conceptual.tex` no las dibuja | Contradicción figura–texto |
| A-9 | Cap. 5 (15 lugares) | Citas internas «D-04», «D-15», «D-16», «D-23»… que el lector de la tesis no puede resolver. Quitarlas o explicar la decisión en el texto | Agentes §3 |
| A-10 | `cu_paquete2.puml`, `cu_paquete5.puml` | **CU-01 / CU-03:** «:Sistema:» como actor de sí mismo | UML: un actor es externo |
| A-11 | `cu_vision_general.puml:26-27` | **CU-17:** el Administrador solo llega a P1 y P5 (no sube videos ni ve resultados), contra RF-04 y las fichas «Inv. / Admin.» | RF-04, D-08 |
| A-12 | Cap. 5: 1266 (CU-05) y 1618 (CU-08) | **CU-18 / CU-19:** CU-05 «Incluye: CU-07» debería ser extend (RF-15: monitorear es opcional); CU-08 «Extendido por: CU-07» está al revés | RF-15 |
| A-13 | `figures/mermaid/seq_perfil.png` | Figura de mayo sin fuente `.puml`: «obtiene nombre, correo y **rol**»; `USUARIO` no tiene rol. Rehacer en PlantUML | Modelo vigente |
| A-14 | `portada.tex:73`, `documento_tecnico.tex:32` | Fecha «Mayo 2026»; nombres distintos entre los dos archivos (acentos y orden) | Datos oficiales |
| A-15 | `esquema_fisico.puml:24-25` y `:90-92` | Encabezado viejo («16 relaciones, 74 atributos, 17 FK») y «tres valores en modo completo, dos en degradado» (son cuatro conductas). El PNG entra al cap. 5 | Modelo vigente |
| A-16 | Cap. 2: 64 y 189 | **E02-01:** la sección de DeepLabCut como clasificador del FST está duplicada (Sturman et al. dos veces) | Contradicción interna |

---

## 3. 🟡 Media

### Caps. 1 a 3
| # | Dónde | Qué | Fuente |
|---|-------|-----|--------|
| M-1 | Caps. 1, 2 y 4 | **E01-08 / E02-02 / E04-05:** falta el criterio de **repetibilidad** (variabilidad ≤ 5–10 % entre corridas del mismo video): en la justificación, como criterio del estado del arte y como RNF | Entrevista P13, P8 |
| M-2 | Cap. 1, «Fuera del alcance» (~304) | **E01-11:** no dice que el acervo histórico (80–100 videos) no se carga al sistema | Entrevista P19, PG |
| M-3 | Cap. 1 | **E01-04:** el capítulo nunca nombra la **tanda**; «experimento» sigue sin el nivel intermedio | Entrevista P19 |
| M-4 | `resumen.tex:4` | **EF-01:** «entre una y dos horas» (el cuerpo dice hora y media a dos); ISO e IEEE sin expandir | Cap. 1 |
| M-5 | Cap. 3: 55-56 | **E03-04:** «los antidepresivos tipo antidepresivos como la fluoxetina» (edición mal cerrada) | Terminología `CLAUDE.md` |
| M-6 | Cap. 3, protocolo | **E03-05:** no describe grupos ni tandas (6–8 especímenes por grupo, 3–4 experimentos por semestre) | Entrevista PA |
| M-7 | Cap. 3, protocolo | **E03-08:** falta el valor de referencia de iluminación | Ver `errores/03_marco_teorico/errores.md` |
| M-8 | Cap. 3: 276 | La portabilidad se atribuye a la ISO/IEC/IEEE 12207; es atributo de la ISO/IEC 25010 | Norma |

### Cap. 4
| # | Dónde | Qué | Fuente |
|---|-------|-----|--------|
| M-9 | RF-09 (104-108) | «Ambos son opcionales individualmente»: una tanda podría quedar sin videos | D-28 |
| M-10 | RF-22 (201-205) | Las columnas del CSV no incluyen espécimen ni grupo | Entrevista P9 |
| M-11 | RN-04 (533-536) | **E04-07:** no distingue reiniciar (prohibido) de reanalizar (D-03) | D-03 |
| M-12 | RNF-01 (333) y RNF-03 (350) | **ESC-02 / ESC-03:** SLO del 95 % y disponibilidad mensual medida, para 1 usuario a la vez | Entrevista, «una persona a la vez» |
| M-13 | RF-04 / línea 69 | **ESC-07:** «dos roles con permisos distintos» sin justificar contra la entrevista («bastaría con un rol»); D-08 da el argumento | Entrevista P1/P18, D-08 |
| M-14 | Cap. 4: 1137 | ISO 14064-1 (gases de efecto invernadero) citada para consumo de energía | Norma |

### Cap. 5: texto
| # | Dónde | Qué | Fuente |
|---|-------|-----|--------|
| M-15 | Cap. 5: 97 | **ESC-01:** «escalar el número de workers de forma independiente» | Entrevista |
| M-16 | Cap. 5, arquitectura y API | **DOC-03 a DOC-07:** declarar nivel 2 de Richardson; definir SPA; tipo de cliente-servidor (38); nombrar RBAC y separar autenticación de autorización; semántica de `PATCH` | Notas de la simulación de defensa |
| M-17 | Caps. 1–5 | **DOC-08:** definir cada norma en su primera aparición (25010, 12207, 31000, 14064-1, 19501, 42010, NOM-062) | Simulación de defensa |

### Diagramas de casos de uso
| # | Dónde | Qué |
|---|-------|-----|
| M-18 | P1 | **CU-05:** `UC17 ..> UC15a <<include>>` (es postcondición). **CU-06:** `UC15 ..> UC15b <<include>>` (desactivar es opcional) |
| M-19 | P1, P2, P3, P5 | **CU-02:** descomposición funcional como casos de uso: UC31–UC34 (etapas del pipeline), UC23/UC24 (validaciones), UC14 (verificar rol), UC55 (conservar resultados) |
| M-20 | P2 | **CU-10:** cadena falsa `UC22 → UC23 → UC24 → UC25`. **CU-11:** `UC26 ..> UC24` duplicado, y «formato inválido» va en UC23 |
| M-21 | P4 | **CU-12:** solo «Descargar reporte PDF»; RF-22 pide CSV y XLSX |
| M-22 | P5 | **CU-15:** la alerta de disco extiende a «Monitorear» (solo existiría si el admin mira el panel) |
| M-23 | P2, P3, P5 | **CU-21:** UC27, UC35 y UC51 son el mismo objetivo («ver en qué va mi experimento») |

### Otros diagramas
| # | Dónde | Qué |
|---|-------|-----|
| M-24 | `grafo_relacional_3_vigente.puml` | `ANALISIS.idVideo` sin `[AK]` (es UNIQUE por D-24); falta `ANALISIS.rutaDiagnostico` (D-23) |
| M-25 | `clases.puml` | Falta la asociación `Segundo → Conducta`; `Analisis` sin `rutaDiagnostico`; tipos `Float` contra el «nunca real/double» del físico; multiplicidad `Intervalo 2..4 — Conducta` dudosa |
| M-26 | `esquema_fisico.puml` (notas) | Nombres de función (`fn_sincronizar_grupo_especimen()`) e historial de sesión («15-sep», «a petición del usuario») dentro de la figura; regla de diagramas en lenguaje natural |
| M-27 | `esquema_fisico.puml`, `esquema_conceptual.tex` | `PRESENTA` dibujada (2,4) pero siempre se guardan 4 filas (sería 4,4). El conceptual dice «todas fuertes» y `Segundo` no tiene identificador propio |
| M-28 | `seq_gestion_usuarios.puml:46,75` | `/admin/usuarios` contra `/admin/users` de la tabla de la API |
| M-29 | `figures/mermaid/seq_notificaciones.png`, `seq_cambio_pass_inv.png` | Mermaid de mayo sin fuente; revisar contra el modelo vigente y rehacer en PlantUML |
| M-30 | `INF-01` a `INF-03` | `gen_pngs.sh` solo genera los `cu_*`, tiene rutas absolutas y no compila `esquema_conceptual.tex` |
| M-31 | Apéndice C: 174, 188-189, 290-295 | «ratas», «por rata», «ISRS». **Decidir** si se toca: es la transcripción de la entrevista |
| M-32 | `seq_*` (agentes §2) | Falta la transición preprocesamiento → error; el fallo de apertura del video aparece después de la detección |
| M-33 | Cap. 2, tabla comparativa | El texto dice que las herramientas abiertas no usan aprendizaje profundo y la tabla marca DeepLabCut y YOLO-Behaviour como abiertos y con DL |

---

## 4. 🟢 Baja

| # | Dónde | Qué |
|---|-------|-----|
| L-1 | Cap. 4: 1148 | «dejaran» → «dejarán» |
| L-2 | `abreviaturas.tex` | Sobran FN, FP, HTTPS y SQL (no se usan); faltan CU, MXN, FNBC y GMM |
| L-3 | `glosario.tex` | Corticosterona y Dopaminérgico sin uso; «Cola de tareas» definida como FIFO (el diseño es sondeo a la tabla) |
| L-4 | `referencias.bib:293` | Comentario sobrante «INSTRUCCIONES: Pegar estas entradas…» |
| L-5 | `referencias.bib` | Sin citar: `abadi2016`, `henriques2015`, `lauer2022_madlc`, `lukezic2017`, `zhang2022_bytetrack`, `bewley2016_sort`, `wojke2017_deepsort` (los de seguimiento quedaron huérfanos con CLA-02). Con `biblatex` no salen en el PDF; es limpieza |
| L-6 | Caps. 1–5 | Siglas sin definir en primera aparición (OMS, ENMyH, TT1/TT2, ROI, ML…) y términos en inglés sin cursiva o sin traducción (*time behaviour*, *recall*, *trade-off*). Revisar uno por uno |
| L-7 | Bibliografía | **DOC-12:** «y col.» contra «et al.» según la compilación |
| L-8 | `clases.puml` | Faltan métodos de algunos CU; `validarFormatoMp4()` no cubre `.mov`; etiquetas amontonadas cerca de `Observacion` |
| L-9 | Fuentes `.puml` | Comentarios con «ratas», «IA», «animales» (no se ven en las imágenes) |

---

## 5. Sin verificar (los reportaron los agentes; no se pudo confirmar con búsqueda)

- `estados_experimento.puml`: transición «con_error → procesando» contra la precedencia del cap. 5.
- `seq_consulta_resultados.puml`: si usa las rutas de la tabla de la API.
- Fichas de CU que se contradicen entre sí: CU-04/CU-05, CU-05/CU-07, CU-09/CU-10.
- Nombres distintos entre diagrama y ficha (p. ej. UC14 contra CU-15); fichas CU-06 y CU-08 sin caso de uso dibujado.
- YOLO-Behaviour: si de verdad es de dos etapas como dice el cap. 2 (verificar contra el artículo).
- Cifras de YOLOv8 y «cientos de miles de imágenes» sin cita directa (cap. 2).
- Mockups v2: revisar contra el modelo vigente (los hallazgos de los agentes eran de los mockups viejos).

---

## 6. Ya resueltos (para cerrar en los trackers viejos)

- **errores/:** E01-01, 02, 03, 09 (D-49), 10, 12 · E02-03, 04, 05 · E03-02, 06 (D-49), 07 · E04-01, 02, 03, 04.
- **CORRECCIONES:** CU-04, 07, 08, 09, 13, 14 (D-43), 16, 20 · ESC-04 (el borrado al 90 % se queda: RN-05, D-51), ESC-05, ESC-06 · DOC-01 (apéndice D), DOC-09 y DOC-10 (sin objeto) · DOC-11.
- **Agentes §1:** todo §1.1 a §1.3; terminología prohibida en capítulos; BCNF y D-04 ya explicados en el cap. 5; cierre de sesión; huecos §4.1–4.3 y §4.6–4.8 (D-37, D-41, D-42, D-43).

---

## 7. Fuera de «hasta el cap. 5»

- **DOC-02:** no hay capítulo de conclusiones (caps. 6–8 comentados en `main.tex`).
- **D-51 sin aplicar:** `INSTRUCCIONES-WEB.md` (DDL y semilla), comentario de `seq_analisis_automatico.puml`, artifacts y cap. 6.
- Archivos huérfanos con el modelo viejo que no entran al documento (`ciclo_vida_experimento.puml`, `seq_analisis.png`, `seq_registro.png`, `figures/mermaid/clases.png`, `casos_uso.png`, `cu_*.png` de `diagramas/`).
