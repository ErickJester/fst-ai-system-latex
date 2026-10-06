# Revisión con agentes — 3-oct-2026

> **Desactualizado como lista de trabajo (5-oct-2026).** Lo vigente, verificado contra el LaTeX, está en [`PENDIENTES.md`](../PENDIENTES.md). Este archivo queda como evidencia (fuentes y motivos de cada ítem).

Trece agentes de solo lectura revisaron la tesis: uno por capítulo (1 a 5), uno para los
capítulos 6 a 8, uno para `front/` y la bibliografía, y seis para los diagramas (base de
datos, casos de uso, secuencias, estados y flujo, clases, mockups). **No se editó nada.**

Cómo leerlo:
- **✔** = lo verifiqué yo con una búsqueda en el archivo. Sin marca = lo reportó un agente y
  no lo he comprobado.
- «posible» = el agente no estaba seguro.
- No incluye lo que ya se sabía: RF-16 («código de error»), `ANALISIS.confianza`, RF-18
  (mínimo de 3 s), los mockups con «animales», los PDF de `artifacts pdf/` y el título
  oficial con «RATA».
- El documento **compila sin errores** (171 páginas, sin referencias rotas).

---

## 1. Gravedad alta — corregir antes de entregar

### 1.1 Restos del modelo viejo en el texto
| Dónde | Qué dice | Debería |
|---|---|---|
| `05_diseno.tex:2480-2481` ✔ | «cada tanda aloja de tres a cuatro especímenes» | 2 a 4 (D-28) |
| `05_diseno.tex:1676` ✔ | CU-09 lee «ResultadoComportamiento» y «ComportamientoPorMinuto» | `OBSERVACION`, `INTERVALO`, `PRESENTA` y `SEGUNDO`; esas tablas no existen |
| `05_diseno.tex:755-756` ✔ | «aprobación de solicitudes de registro» | no hay autorregistro (RF-07, CU-12) |
| `05_diseno.tex:792` ✔ | «cuenta registrada y aprobada por el Administrador» | ídem |
| `05_diseno.tex:1214` ✔ | «según RN-15» | RN-15 no existe; el capítulo 4 termina en RN-14 |
| `front/glosario.tex:288` | «día 1: 15 min de nado» | 20 min (capítulos 1 y 3) |

### 1.2 Terminología prohibida
- **«cámara de celular»** ✔: `02_estado_arte.tex:21`, `03_marco_teorico.tex:76`,
  `04_analisis.tex:873-874`; y «teléfono o cámara actual» en `04_analisis.tex:930` ✔.
  Debe decir «cámara web».
- **«Gold standard» y «MAE»** ✔ siguen como entradas de `front/glosario.tex:181` y `:231`.
  Tu regla las elimina de todos los `.tex`; ningún capítulo las usa, así que son huérfanas.
- `back/apendice_C.tex:174,188,189` usa «ratas» y «por rata», y `:290-295` usa «ISRS»;
  `04_analisis.tex:1109` usa «animales» (describe la NOM-062).

### 1.3 Referencias cruzadas que apuntan al requerimiento equivocado
Capítulo 4 ✔ (verificadas todas las de esta tabla):

| Línea | Dice | Debe ser |
|---|---|---|
| 458 | umbral de 3 s «(ver RF-30)» | RF-18 |
| 528 (RN-06) | «Ver RF-25» | RF-26 |
| 539 (RN-08) | «RF-29» | RF-30 |
| 544 (RN-09) | «Ver RF-26» | RF-27 |
| 563 (RN-12) | «Ver RF-20» | RF-21 |
| 831 (R-06) | «ver RF-28» | RF-29 (y RF-25 para el borrado) |

Capítulo 5 (reportadas por agentes):

| Línea | Dice | Debe ser |
|---|---|---|
| 2154 (CU-23) | RF-26 | RF-27 |
| 1480 (CU-21) | RF-22 | RF-23 |
| 2120, 2291, 2543, 2566 | RF-23 para el aviso de 7 días | RF-24 |
| 2706, 2714 (pies de figura) | RF-20 y RF-19 | RF-21 y RF-20 |
| 2748 | «RF-05, RF-27, RF-28» | quitar RF-27 |
| 2396 | RNF-10 para disco | RNF-09 |
| 86 y 2616 | RF-12 y RF-10 | RF-15 y RF-08 |

### 1.4 Contradicciones entre figura y texto
- **Normalización (BCNF).** El capítulo afirma que las 17 relaciones cumplen FNBC, pero la
  figura del esquema físico incluye `ESPECIMEN.idGrupo`, redundante a propósito (D-04). El
  capítulo no menciona ni D-04 ni `idGrupo`. Es lo primero que un sinodal puede señalar.
- **Estados del experimento** (`estados_experimento.puml`): la transición «con_error →
  procesando» contradice la precedencia del capítulo 5 (error > procesando).
- **Análisis automático** (`seq_analisis_automatico.puml`): el Worker genera el PDF de
  diagnóstico pero nunca lo guarda ni escribe `ANALISIS.rutaDiagnostico`; el diagrama de
  progreso lee justo esa ruta.
- **Consulta de resultados** (`seq_consulta_resultados.puml`): compara solo los tres grupos
  en Día 2 y no usa las rutas de la tabla de la API; CU-09 y la API siguen describiendo el
  modelo viejo (tabla por espécimen y comparación Día 1 vs Día 2).
- **Cierre de sesión.** `05_diseno.tex:2332` dice «invalida el token en el cliente»; CU-02 y
  el diagrama dicen que se invalida en el servidor. Tu decisión de hoy (el cliente descarta
  el token, sin lista de bloqueo) **no está en la tesis**.

### 1.5 Mockups con contenido contradictorio
- **Confianza 0.70** ✔ (3 apariciones) en `mockup_progreso_analisis.html`: «umbral 0.70» y
  «confianza máxima del detector 0.18».
- **Botón «Reintentar análisis»** ✔ en el dashboard con experimentos en error: RN-04 lo
  prohíbe.
- **Dashboard**: dice «Solo puedes ver experimentos de tu propia cuenta (RN08)»; RN-08 dice
  lo contrario.
- **Subida (5 mockups)**: piden «Número esperado de animales» con valor 4 (por experimento,
  cuando RF-11 lo captura por tanda), el validador acepta 1 a 8, y solo aceptan `.mp4`.
- **Fallos de captura**: `ui_nuevo_exito` está en blanco; `ui_resultados_comparacion` y
  `ui_resultados_minutos` son idénticas a `ui_resultados_dia2`, así que no muestran lo que
  dicen sus pies de figura.

### 1.6 Datos oficiales de la portada
- Los nombres difieren entre `portada.tex` y `documento_tecnico.tex` (acentos y orden de
  apellidos: «Ángel Alí» frente a «Angel Ali»).
- La fecha dice «Mayo 2026» en ambos.

---

## 2. Gravedad media

### Capítulos 1 a 4
- **Cap. 1**
  - La cuarta conducta no aparece en la propuesta ni en los objetivos (líneas 157-158,
    180-181, 197-198).
  - El desglose por minuto se llama «opcional» (158, 269) pero se exporta siempre (279) y se
    recalcula al corregir (285).
  - Con dos evaluadores: «se revisa dos veces más» (11-12) frente a «se duplica» (212).
  - Cola «para hasta cuatro análisis» (290) confunde los 4 usuarios de RNF-13 con 4 análisis.
  - Grupos «de 6 a 8 especímenes» (59-60) se lee como regla frente a D-28.
- **Cap. 2**
  - La tabla comparativa contradice el texto: el texto dice que los de código abierto no usan
    aprendizaje profundo, y la tabla marca DeepLabCut y YOLO-Behaviour como abiertos y con DL.
  - **posible:** YOLO-Behaviour parece detectar la conducta con YOLO en una sola etapa; el
    texto lo presenta como el origen de la arquitectura de dos etapas del proyecto. Conviene
    verificarlo contra el artículo.
  - La cita `armario2021` (revisión conceptual del FST) respalda una afirmación sobre
    descriptores de visión; hay cifras de YOLOv8 y de «cientos de miles de imágenes» sin
    cita directa.
- **Cap. 3**
  - «Desde la vista cenital» (62) contradice la vista lateral de todo el documento.
  - «Con los cuadros etiquetados del laboratorio» (254-255) contradice D-26.
  - Atribuye la portabilidad a la ISO 12207 (es atributo de la 25010).
  - Habla de 3 salidas y 3 clases donde ya son 4.
- **Cap. 4**
  - RNF-09 borra «los videos más antiguos» al 90 % de disco, contra RN-05 (30 días) y
    RF-24; el mockup de administración repite la misma regla.
  - RF-09 dice que ambos videos son opcionales: una tanda podría quedar con cero.
  - RF-22 (columnas del CSV) no incluye espécimen ni grupo.
  - RNF-02 mide F1 sin la conducta activa.
  - RNF-02 compara «contra la anotación manual de analistas»: choca con tu regla de no usar
    anotaciones de un solo anotador.
  - Falta decir en qué punto se rechaza un video vertical (RF-10 y RN-10 no coinciden).
  - «Pruebas preliminares» respaldadas con una cita ajena (870-875); umbrales 80/90 % citados a
    un libro de ingeniería de software; la ISO 14064 (gases de efecto invernadero) citada para
    consumo de energía.
- **Resumen** (`front/resumen.tex`): «entre una y dos horas» (el cuerpo dice 1.5 a 2); solo
  tres conductas; dice «reemplazar» cuando el capítulo 5 dice que la revisión humana corrige
  sin sustituir; ISO e IEEE sin expandir.

### Capítulo 5 y diagramas
- **Inconsistencias entre fichas** (CU-04 «incluye» CU-05 pero CU-05 dice «extendido por
  CU-04»; CU-05 y CU-07; CU-09 y CU-10): se contradicen entre sí y con el diagrama de casos
  de uso.
- **Casos de uso**
  - Las fichas CU-06 y CU-08 no tienen caso de uso dibujado.
  - Hay nombres distintos entre diagrama y ficha (por ejemplo UC14 contra CU-15).
  - El diagrama del paquete 2 hace que «Notificar rechazo» extienda a «Validar video
    reproducible» cuando la ficha CU-20 dice que extiende a CU-05.
  - El administrador solo hereda del investigador en el paquete 1.
- **Esquemas de base de datos**
  - El encabezado de `esquema_fisico.puml` (líneas 24-25) sigue diciendo «16 relaciones, 74
    atributos».
  - Siguen mencionándose «tres valores en modo completo, dos en modo degradado» (90-93).
  - **Cardinalidad:** `PRESENTA` se dibuja (2,4) pero se guardan siempre cuatro filas; sería
    (4,4).
  - Una sola arista cubre las dos llaves `clase` y `propuesta`.
  - El conceptual no dibuja la relación de `propuesta`.
  - El conceptual dice «todas las entidades fuertes» pero `Segundo` no tiene identificador
    propio (sería débil).
  - `ANALISIS.idVideo` es `UNIQUE` en el físico y no aparece como clave alterna en el grafo.
  - El capítulo 5 (281-293) presenta `ADMINISTRADOR`, `REPORTE`, `NOTIFICACION`,
    `CONFIGURACION` y `MODELO` como parte del DER conceptual, pero ese diagrama no las tiene.
  - Las notas dentro del esquema físico tienen nombres de función y código
    (`fn_sincronizar_grupo_especimen()`, `hashlib…`) e historial de sesión («15-sep», «a
    petición del usuario»).
- **Clases**: la multiplicidad `Intervalo 2..4 — Conducta` parece invertida; falta la
  asociación `Segundo` → `Conducta`; `versionPipeline` es entero y en el físico es texto; los
  tipos `Float` contradicen el «nunca real/double» del físico; faltan métodos de CU-03, CU-18,
  CU-22 y CU-25; `validarFormatoMp4()` no coincide con RF-08; `Notificacion.marcarComoLeida()`
  no tiene ficha.
- **Secuencias**
  - Rutas `/admin/usuarios` contra `/admin/users` de la API.
  - El autocompletado de grupo y la tanda sugerida no tienen ruta.
  - El fallo de apertura del video está después de la detección.
  - La revisión lee recuadros y una copia de video que ningún diagrama guarda.
  - No tiene el curso alterno de «no se puede guardar».
  - `seq_perfil.png` (incluido en el capítulo) muestra un «rol» en `USUARIO` que ya no existe;
    `seq_login.png` registra una «última conexión» sin columna.
- **Estados y flujo**
  - Falta la transición preprocesamiento → error.
  - `flujo_general.puml` omite la cuarta conducta y habla de «anotación experta».
  - `pipeline.png` y `arquitectura_software.png` dicen solo `.mp4` y no muestran 300 s ni la
    rama de error.
  - Hay 3, 4 y 5 etapas en distintas figuras.
- **Mockups**: el progreso muestra 5 etapas (RF-13 dice 4) con «escape» en lugar de
  escalamiento y sin conducta activa; los resultados no tienen conducta activa, XLSX ni
  estadísticas por grupo; las cifras del panel de administración no suman (67.2 + 2.1 + 18.8 ≠
  100 GB); los códigos «FST-2024-0xx» llevan fecha 2025; el nombre y apellido del modal de
  edición están invertidos. No hay acceso a la revisión desde progreso ni resultados.
- **Capítulo 6**: describe como respaldo del seguimiento a CSRT en unas partes y a un «detector
  clásico» en otras; las líneas citadas en los «puntos clave» no coinciden con los listados;
  la tabla de condiciones de activación (GPU) no coincide con el código.

---

## 3. Gravedad baja (resumen)

- Siglas sin definir en primera aparición: OMS, ENMyH/IPN, BORIS, TT1/TT2, IoU, ROI, GMM, ML,
  ECCV; términos en inglés sin cursiva o sin traducción (*time behaviour*, *transfer
  learning*, *recall*, *trade-off*).
- Erratas: «dejaran», «la rata aparezca duplicado» (y otros de concordancia), «diagnostico» sin
  tilde, `kingma2014` con año 2015 y `bradski2000` con 2008.
- Bibliografía: `abadi2016`, `henriques2015` y `lauer2022_madlc` nunca se citan; queda un
  bloque de comentario residual («INSTRUCCIONES: Pegar estas entradas…»).
- Abreviaturas: FN, FP, HTTPS y SQL no se usan; faltan CU, MXN, FNBC, GMM y DeepSORT.
- Glosario: «cola de tareas» como estructura FIFO (el diseño es sondeo a la base);
  Corticosterona y Dopaminérgico sin uso.
- Capítulo 5: 13 citas internas «D-08, D-12, D-14, D-15…» que un lector de la tesis no puede
  resolver; falta `MODELO` y `PRESENTA` en la fila de claves de la tabla de normalización; CU-14
  borra el archivo dos veces; «rastreo» donde D-16 pide «seguimiento».
- Archivos huérfanos con el modelo viejo (no se usan en el documento): `ciclo_vida_experimento.puml`
  ✔ (todavía dice «confianza ≥ 0.70», «Iniciar Análisis» y «reintento»), `seq_analisis.png`,
  `seq_registro.png`, `seq_carga.png`, `figures/mermaid/clases.png`, `figures/mermaid/casos_uso.png`
  y los `cu_*.png` de `diagramas/`.
- Comentarios de las fuentes de diagramas con las palabras «ratas», «IA» y «animales» (no se
  ven en las imágenes).
- Legibilidad: etiquetas amontonadas en el diagrama de clases cerca de `Observacion`.

---

## 4. Huecos del modelo que los agentes encontraron (son decisiones tuyas)

1. **«Último acceso»** de cada usuario: aparece en RF-28, CU-11 y `seq_login.png`, pero
   `USUARIO` no tiene esa columna.
2. **Identificador institucional** al crear cuenta: es la llave primaria y el formulario
   (RF-05, CU-12) solo pide nombre y correo; `apellidos` tampoco se captura.
3. **Cierre de sesión**: la tesis dice servidor; tu decisión fue cliente.
4. **Borrado automático al 90 % de disco** (RNF-09, mockup de administración): ¿se queda o se
   quita?
5. **«No se ve» frente a «dudosa»** en la revisión: ambas dejan el segundo sin conducta.
6. **Ramas «preciso / agrupado»** en `seq_consulta_resultados` y `nivelClasif`: siguen
   pendientes desde D-29.
7. **Dónde se guardan el PDF de diagnóstico, los recuadros y la copia de video para
   reproducir**: ningún diagrama de secuencia los escribe.
8. **Quién puede eliminar un experimento ajeno** (RF-27 contra RN-08).

---

## 5. Lo que esta revisión NO hizo

- No verificó las citas bibliográficas contra los artículos.
- No compiló ni probó el SQL ni el código de ejemplo.
- Los hallazgos sin ✔ son afirmaciones de los agentes y pueden contener errores.
