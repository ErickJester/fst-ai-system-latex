# Pendientes de Erick — cap. 4, cap. 5 (salvo casos de uso), modelo, diagramas y decisiones

Parte de [`PENDIENTES.md`](PENDIENTES.md), que tiene el reparto y las reglas de
coordinación. **Verificado contra el repositorio el 2026-10-14** (cada ítem, contra el LaTeX, los `.puml` y las figuras). Los IDs (A-, M-, L-, B-) son
los mismos de la lista original.

Marca aquí lo que termines (`✅`, fecha). Este archivo es solo tuyo: Vanesa no lo edita.

**Revisa también** la sección «Para Erick» al final de
[`PENDIENTES-VANESA.md`](PENDIENTES-VANESA.md): ahí te deja entradas de glosario o
abreviaturas y dudas.

---

## 1. 🔒 Bloqueado

| # | Qué | Espera a |
|---|-----|----------|
| ✅ B-1 | **CLA-03:** qué clasificador gana y su F1. Con eso: revisar el 0.80, D-06 (dos archivos de modelo si gana la fusión) y la columna «DL» de la tabla comparativa del cap. 2 (M-33) | Etiquetado y entrenamiento — **Actualizado (14-oct):** el clasificador ya está decidido (fusión). D-06 no se reabre: la fusión es una sola red (`fst_cnn.pt`), un solo archivo de modelo. Falta solo el F1 real tras entrenar. — **✅ Cerrado (14-oct):** ningún texto de los caps. 1–5 espera un F1 real (solo meta ≥ 85 %); el F1 medido va en el cap. 7, fuera del PDF. |
| ✅ B-2 | **Métricas sin gold standard** (`CLAUDE.md`). Ligado a E04-06: RNF-02 y la justificación de umbrales (cap. 4, ~336-462) comparan «contra la anotación manual de analistas» | Dr. Sandino — **✅ Cerrado (14-oct, D-104):** se quitó toda mención a anotaciones expertas (caps. 3, 4 y 5); el F1 se mide contra el conjunto de prueba propio. |
| ✅ B-4 | **D-52** (`INTERVALO`/`PRESENTA`) y **D-07** (recuadro y línea de agua a mano) | Decisión del equipo — **✅ Cerrado (14-oct):** D-52 resuelto; D-07 descartado (D-104): el recuadro solo se dibuja cuando el sistema pide corrección. |
| B-5 | ~~**CLA-04, parte BORIS:** caps. 1, 3 y 4 dicen que el laboratorio anota con BORIS (D-26)~~ **Resuelto (7-oct, D-56):** BORIS se quitó de todo el LaTeX; las etiquetas salen del etiquetador del equipo | — |

> Si una decisión tuya (D-52, CLA-03…) obliga a cambiar una **ficha de caso de uso** o
> algo de los caps. 1–3, avísale a Vanesa en vez de editarlo: esas zonas son suyas
> mientras trabaja (ver `PENDIENTES.md`).

## 2. 🔴 Alta

| # | Dónde | Qué | Fuente |
|---|-------|-----|--------|
| ✅ A-1 | Caps. 2, 3 y 4; glosario; abreviaturas; figura del pipeline | **CLA-04:** CLAHE, fondo por **mediana** (`fst_auto` usa percentil 10) y línea de agua con EMA, que el pipeline real no hace. En los caps. 2 y 3 toca **solo** esos párrafos: el resto es de Vanesa | Código de `fst_auto` — **✅ Cerrado (14-oct):** CLAHE y la línea de agua con EMA ya no aparecen; el fondo es el percentil 10 y la mediana solo se menciona como la alternativa descartada. |
| ✅ A-8 | Cap. 5: ~293-303 | El párrafo del DER conceptual dice que incluye `ADMINISTRADOR`, `REPORTE` y `NOTIFICACION`; `esquema_conceptual.tex` no las dibuja | Contradicción figura–texto — **✅ Cerrado (14-oct):** El párrafo ya dice que `ADMINISTRADOR`, `REPORTE` y `NOTIFICACION` aparecen en el esquema físico, no en el conceptual. |
| ✅ A-9b | Cap. 5 fuera de casos de uso: 242, 245, 248, 340, 371, 543, 601, 2435, 2504, 2645 | Citas internas «D-XX» que el lector no puede resolver (las de las fichas son de Vanesa) | Agentes §3 — **✅ Cerrado (14-oct):** No quedan citas «D-XX» en el cap. 5 (solo «R(2+1)D-18», que es otra cosa). |
| ✅ A-13 | `figures/diagramas/seq_perfil.png` | Mermaid de mayo sin fuente: «obtiene nombre, correo y **rol**» y `USUARIO` no tiene rol. Rehacer en PlantUML | Modelo vigente — **✅ Cerrado (14-oct):** `seq_perfil` se rehízo en PlantUML el 12-oct y ya no muestra el rol. |
| ✅ A-15 | `esquema_fisico.puml:24-25` y `:90-92` | Encabezado viejo («16 relaciones, 74 atributos, 17 FK») y «tres valores en modo completo, dos en degradado» (son cuatro conductas). El PNG entra al cap. 5 | Modelo vigente — **✅ Cerrado (14-oct):** El encabezado y las notas del esquema físico se actualizaron (D-52 y D-102); ya no hablan de «modo degradado». |

## 3. 🟡 Media

### Cap. 4
| # | Dónde | Qué | Fuente |
|---|-------|-----|--------|
| ✅ M-1c | RNF nuevo | **E04-05:** RNF de **repetibilidad** (variabilidad ≤ 5–10 % entre corridas del mismo video). Vanesa lo agrega a los caps. 1 y 2 con la misma cifra | Entrevista P13, P8 — **✅ Cerrado (14-oct):** RNF-14 de repetibilidad y su subsección en el cap. 3 (D-74). |
| ✅ M-9 | RF-09 (104-108) | «Ambos son opcionales individualmente»: una tanda podría quedar sin videos | D-28 — **✅ Cerrado (14-oct):** D-99. |
| ✅ M-10 | RF-22 (201-205) | Las columnas del CSV no incluyen espécimen ni grupo | Entrevista P9 — **✅ Cerrado (14-oct):** D-99. |
| ✅ M-11 | RN-04 (533-536) | **E04-07:** no distingue reiniciar (prohibido) de reanalizar (D-03) | D-03 — **✅ Cerrado (14-oct):** RN-04 distingue reiniciar (permitido; borra el resultado) de un análisis nuevo por cambio de video o de modelo. |
| ✅ M-12 | RNF-01 (333), RNF-03 (350) | **ESC-02 / ESC-03:** SLO del 95 % y disponibilidad mensual medida, para un usuario a la vez | Entrevista — **✅ Cerrado (14-oct):** D-99. |
| ✅ M-13 | RF-04 / línea 69 | **ESC-07:** «dos roles» sin justificar contra la entrevista («bastaría con un rol»); D-08 da el argumento | Entrevista P1/P18, D-08 — **✅ Cerrado (14-oct):** D-99. |
| ✅ M-14 | Línea 1137 | ISO 14064-1 (gases de efecto invernadero) citada para consumo de energía | Norma — **✅ Cerrado (14-oct):** D-99. |

### Cap. 5 (fuera de casos de uso)
| # | Dónde | Qué | Fuente |
|---|-------|-----|--------|
| ✅ M-15 | Línea 97 | **ESC-01:** «escalar el número de workers de forma independiente» | Entrevista — **✅ Cerrado (14-oct):** D-99. |
| ✅ M-16 | Arquitectura (38) y API (~607-692) | **DOC-03 a DOC-07:** nivel 2 de Richardson, definir SPA, tipo de cliente-servidor, nombrar RBAC y separar autenticación de autorización, semántica de `PATCH` | Simulación de defensa — **✅ Cerrado (14-oct):** D-99 (nivel 2 de Richardson, SPA, RBAC y `PATCH`; DOC-03 a DOC-07). |
| ✅ M-17b | Caps. 4 y 5 | **DOC-08:** definir en su primera aparición las normas que aparecen por primera vez aquí (31000, 14064-1, 19501, 42010, 12207 si no salió antes) | Simulación de defensa — **✅ Cerrado (14-oct):** ISO 31000, 19501, 42010 y 12207 se definen donde aparecen; la 14064 se quitó (D-99). |

### Diagramas (no de casos de uso)
| # | Dónde | Qué |
|---|-------|-----|
| ✅ M-24 | `grafo_relacional_3_vigente.puml` | `ANALISIS.idVideo` sin `[AK]` (es UNIQUE, D-24); falta `ANALISIS.rutaDiagnostico` (D-23) — **✅ Cerrado (14-oct):** D-99. |
| ✅ M-25 | `clases.puml` | Falta la asociación `Segundo → Conducta`; `Analisis` sin `rutaDiagnostico`; tipos `Float` contra el «nunca real/double» del físico; multiplicidad `Intervalo 2..4 — Conducta` dudosa — **✅ Cerrado (14-oct):** D-99; además `Conducta` pasó a enumeración (D-102) y se agregó `Estadisticas` (D-103). |
| ✅ M-26 | `esquema_fisico.puml` (notas) | Nombres de función (`fn_sincronizar_grupo_especimen()`) e historial de sesión dentro de la figura; regla de lenguaje natural — **✅ Cerrado (14-oct):** Las notas de la figura del esquema físico ya no traen nombres de función ni historial. |
| ✅ M-27 | `esquema_fisico.puml`, `esquema_conceptual.tex` | `PRESENTA` dibujada (2,4) pero siempre guarda 4 filas; el conceptual dice «todas fuertes» y `Segundo` no tiene identificador propio. **Depende de D-52** — **✅ Cerrado (14-oct):** `PRESENTA` ya no existe (D-52) y `Segundo` se dibuja ahora como entidad débil (doble borde, con su interrelación identificadora), en el `.tex`, el HTML y el PNG; el cap. 5 lo dice. |
| ✅ M-28 | `seq_gestion_usuarios.puml:46,75` | `/admin/usuarios` contra `/admin/users` de la API — **✅ Cerrado (14-oct):** `seq_gestion_usuarios` ya no usa `/admin/usuarios`; la API usa `/admin/users`. |
| ✅ M-29 | `figures/diagramas/seq_notificaciones.png`, `seq_cambio_pass_inv.png` | Mermaid de mayo sin fuente: revisar y rehacer en PlantUML — **✅ Cerrado (14-oct):** `seq_notificaciones` y `seq_cambio_pass_inv` se rehicieron en PlantUML el 12-oct. |
| ✅ M-32 | `seq_*` | Falta la transición preprocesamiento → error; el fallo de apertura del video aparece después de la detección — **✅ Cerrado (14-oct):** `seq_analisis_automatico` separa el fallo al abrir el video (preprocesamiento) del de los cilindros; el diagrama de estados ya tenía la transición. |
| ✅ M-33 | Cap. 2, tabla comparativa | Texto contra tabla en «abierto / DL». **Depende de B-1** — **✅ Cerrado (14-oct):** el clasificador es la fusión (CNN 3D + rama de 22 medidas), que ya dicen los caps. 3, 4 y 5 y es la versión 5 de `fst_auto`; «DL = Sí» es correcto. |

### Decidir
| # | Qué |
|---|-----|
| ✅ M-31 | Apéndice C (174, 188-189, 290-295): «ratas», «por rata», «ISRS». Es la transcripción de la entrevista: ¿se toca? — **✅ Cerrado (14-oct):** se queda literal, decisión del usuario. |

## 4. 🟢 Baja

| # | Dónde | Qué |
|---|-------|-----|
| ✅ L-1 | Cap. 4: 1148 | «dejaran» → «dejarán» — **✅ Cerrado (14-oct):** Corregido: «dejarán». |
| ✅ L-2 | `abreviaturas.tex` | Sobran FN, FP, HTTPS y SQL; faltan CU, MXN, FNBC y GMM — **✅ Cerrado (14-oct):** Se quitaron DLC, HTTPS y MB (sin uso) y se agregaron FNBC y MXN. FN, FP y SQL se quedan: los usa el glosario (precisión, *recall* y la nota de SQL). |
| ✅ L-3 | `glosario.tex` | Corticosterona y Dopaminérgico sin uso; «Cola de tareas» como FIFO (el diseño es sondeo a la tabla) — **✅ Cerrado (14-oct):** Se quitaron las entradas sin uso (corticosterona, dopaminérgico) y «cola de tareas» ya no dice FIFO: es la tabla de análisis, consultada por sondeo. |
| ✅ L-6b | Caps. 4 y 5 | Siglas en primera aparición y términos en inglés en cursiva (Vanesa hace caps. 1–3) — **✅ Cerrado (14-oct):** «pipeline», «frontend» y «backend» van en cursiva en los caps. 4 y 5 (62 apariciones). |
| ✅ L-8 | `clases.puml` | Faltan métodos de algunos CU; `validarFormatoMp4()` no cubre `.mov`; etiquetas amontonadas cerca de `Observacion` — **✅ Cerrado (14-oct):** `validarFormato()` cubre `.mov` y a `Usuario` se le agregaron los métodos de CU-03 (`recuperarContrasena`), CU-18 (`actualizarPerfil`) y CU-22 (`consultarDashboard`); la figura se regeneró. |
| ✅ L-9 | Fuentes `.puml` (no `cu_*`) | Comentarios con «ratas», «IA», «animales» — **✅ Cerrado (14-oct):** Sin objeto: los comentarios que quedan nombran las tablas del modelo viejo (`ANIMALES`, `TRABAJOS`) solo para decir qué reemplaza cada diagrama; `relacional.puml` es un archivo obsoleto con aviso. |

## 5. ❓ Sin verificar

**✅ Verificado el 14-oct, ya no queda nada aquí:**
- `estados_experimento.puml`: `error` no tiene transiciones de salida; la precedencia del cap. 5 coincide.
- `seq_consulta_resultados.puml`: no usa rutas de la API; habla en lenguaje natural.
- Mockups v2 contra el modelo vigente: puestos al día el 14-oct (eliminar sin contraseña, sin texto del modelo, reporte de resultados, «en espera del Día 2», pausa y cancelado, selector de vista).

## 6. Mantenimiento

- **Cuando resuelvas una decisión que toque el texto**, actualiza «Lo que ya está decidido» de `PENDIENTES.md` en el mismo commit: es lo que Vanesa usa para no contradecir nada.
- Cerrar en los trackers viejos los ítems ya resueltos (lista en `PENDIENTES.md` §Resueltos).
- **D-51:** ✅ el comentario de `seq_analisis_automatico.puml` se corrigió el 14-oct. Queda solo el cap. 6, que está comentado en `main.tex`. (Los tres artifacts se actualizaron el 14-oct con D-52, D-102 y lo anterior.)

## 7. Resumen del 14-oct

**Nada abierto en los caps. 1–5.** Lo único que espera el entrenamiento es llenar el cap. 7 (resultados), que está comentado en `main.tex`.

**Todo lo demás está cerrado.**
