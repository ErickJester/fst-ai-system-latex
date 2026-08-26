# Correcciones pendientes — TT 2026-B066

**Documento de control.** Cada ítem tiene ID, evidencia con archivo y línea, y acción concreta.
Marcar `[x]` conforme se apliquen. Actualizar la tabla de avance al cierre de cada sesión.

- **Rama de trabajo:** `modificaciones`
- **Fecha de la auditoría:** 2026-08-25
- **Origen de los hallazgos:** revisión del esquema relacional, los 5 diagramas de casos de uso,
  la entrevista del Anexo C y las notas manuscritas de revisión.

---

## Avance global

| Bloque | Ítems | Hechos | Estado |
|--------|-------|--------|--------|
| 1. Base de datos | 18 | 0 | 🔴 No iniciado |
| 2. Casos de uso y diagramas | 22 | 0 | 🔴 No iniciado |
| 3. Escala del sistema | 7 | 0 | 🔴 No iniciado |
| 4. Faltantes del documento | 12 | 1 | 🟡 En proceso |
| **Total** | **59** | **1** | |

**Prioridad máxima (🔴):** BD-14 (conductas como columnas fijas), CU-14 (agujero de autorización),
CU-17 (el Admin no puede subir videos), DOC-01 (diccionario de datos inexistente),
DOC-02 (sin capítulo de conclusiones).

---

# Bloque 1 — Base de datos

> **Diagnóstico:** el esquema declara normalización en el texto pero no la implementa en el modelo.
> No hay una sola restricción de dominio, longitud, nulidad, unicidad ni borrado en las 12 tablas.

## 1.1 Valores abiertos (dominio cerrado guardado como `VARCHAR` libre)

Los 11 campos siguientes solo pueden tomar un conjunto conocido y finito de valores,
pero están declarados como texto libre en [`diagramas/relacional.puml`](diagramas/relacional.puml).

- [ ] **BD-01** — `USUARIOS.rol` → FK a catálogo `ROLES`
  *(también resuelve la nota manuscrita «el tema de roles, es recomendable tener [tabla]»)*
- [ ] **BD-02** — `EXPERIMENTOS.tratamiento` → FK a catálogo `TRATAMIENTOS` (control / fluoxetina / experimental, con dosis y vía)
  *(nota manuscrita: «situación actual por el medicamento denota que no está en 3FN»)*
- [ ] **BD-03** — `EXPERIMENTOS.especie` → FK a catálogo `ESPECIES`
- [ ] **BD-04** — `EXPERIMENTOS.disposicion` → `CHECK` o catálogo (2×2, 1×4, …)
- [ ] **BD-05** — `VIDEOS.dia` → `CHECK (dia IN ('dia1','dia2'))`
- [ ] **BD-06** — `TRABAJOS.estado` → `CHECK` o catálogo `ESTADOS_TRABAJO` (en_cola, procesando, completado, error)
- [ ] **BD-07** — `TRABAJOS.etapa` → FK a catálogo `ETAPAS_PIPELINE` (4 etapas)
- [ ] **BD-08** — `REPORTES.formato` → `CHECK (formato IN ('PDF','CSV','XLSX'))`
- [ ] **BD-09** — `NOTIFICACIONES.tipo` → FK a catálogo `TIPOS_NOTIFICACION`
- [ ] **BD-10** — `CONFIGURACIONES_ANALISIS.nombre_modelo` y `version_pipeline` → FK a catálogo `MODELOS`
  *(conecta con la nota «sobre ResNet-18: sacarlo como tabla»)*

## 1.2 Restricciones ausentes en las 12 tablas

- [ ] **BD-11** — Declarar longitud en todos los `VARCHAR` (hoy ninguno tiene `(n)`)
- [ ] **BD-12** — Declarar `NOT NULL`, y añadir los 3 `UNIQUE` que faltan:
  - `USUARIOS.correo`
  - `SUJETOS (id_experimento, indice_rata)`
  - `VIDEOS (id_experimento, dia)`
  - `ROIS (id_video, id_sujeto)`
- [ ] **BD-13** — Declarar comportamiento `ON DELETE` en las 14 claves foráneas.
  RN-09 dice que borrar un experimento elimina video, resultados y reportes → hace falta `CASCADE` explícito.

## 1.3 Problema estructural: conductas como columnas fijas

- [ ] **BD-14** — 🔴 **CRÍTICO.** `RESULTADOS_COMPORTAMIENTO` y `COMPORTAMIENTO_POR_MINUTO`
  guardan las tres conductas como columnas fijas (`nado_s`, `inmovil_s`, `escape_s`).

  **Contradice el RNF-11** ([`chapters/04_analisis.tex:368`](chapters/04_analisis.tex#L368)):
  > «El módulo de clasificación debe poder reconfigurarse para soportar paradigmas conductuales
  > distintos al FST sin modificar la plataforma web.»

  Con el diseño actual, analizar otro paradigma (p. ej. test de suspensión de cola) exige
  `ALTER TABLE`. **Acción:** catálogo `CONDUCTAS` + una fila por `(espécimen, conducta)`.
  Esto además hace la 1FN real y no solo declarativa.

## 1.4 Cardinalidades que contradicen las reglas de negocio

- [ ] **BD-15** — `EXPERIMENTOS "1" --o "0..*" VIDEOS` → debe ser `0..2`
  (RN-03: «Un experimento tiene como máximo dos videos»)
- [ ] **BD-16** — `ANIMALES "1" --o "0..*" RESULTADOS_COMPORTAMIENTO` → debe ser `1 --o 1`
  (un resultado por espécimen por trabajo; el desglose ya vive en `COMPORTAMIENTO_POR_MINUTO`)

## 1.5 Terminología y justificación

- [ ] **BD-17** — Renombrar la tabla `ANIMALES` → `ESPECIMENES_ANALIZADOS`.
  Quedan **12 ocurrencias** de «animal» en el cap. 5:
  [`05_diseno.tex`](chapters/05_diseno.tex) líneas 245, 301, 318, 326, 330, 367, 415, 477, 479, 2207.
  *Verificado el 2026-08-25:* la rama `claridad-documento` **sí está mergeada**; la corrección de
  terminología simplemente nunca alcanzó los nombres de entidad de base de datos del capítulo 5.
- [ ] **BD-18** — Justificar en el texto por qué `TRABAJOS.progreso_pct` se **almacena** en vez de
  calcularse (el frontend hace *polling* y necesita leerlo; llega a valor fijo 100 % al terminar).
  Hoy no está justificado, y ese silencio invita la pregunta del jurado.

---

# Bloque 2 — Casos de uso y diagramas

## 2.1 Fallas estructurales que atraviesan los 5 paquetes

- [ ] **CU-01** — El **«Sistema» aparece como actor de sí mismo** en P2 y P5
  ([`cu_paquete2.puml:12,25-26`](diagramas/puml/cu_paquete2.puml)).
  Un actor es externo al sistema por definición. Eliminar `:Sistema:` como actor.
- [ ] **CU-02** — **Descomposición funcional disfrazada de casos de uso.** No entregan valor
  observable a un actor y deben salir del diagrama de casos de uso:
  - `UC31`–`UC34` (las 4 etapas del pipeline) → pertenecen a un **diagrama de actividad**
  - `UC23`, `UC24` (validaciones internas)
  - `UC14` («Verificar rol y permisos»)
  - `UC55` («Conservar resultados indefinidamente») → es la regla de retención RN-06
- [ ] **CU-03** — **Catálogo de actores inconsistente.** Vista general usa INV/ADMIN/WRK;
  P1 inventa «Usuario autenticado»; P2 y P5 inventan «Sistema». Unificar a un solo catálogo.

## 2.2 Paquete 1 — Autenticación

- [ ] **CU-04** — El actor padre es imposible: `UA <|-- INV` con UA = «Usuario **autenticado**»,
  y luego `UA --> UC11 (Iniciar sesión)` ([`cu_paquete1.puml:11-14,26`](diagramas/puml/cu_paquete1.puml)).
  Nadie puede estar autenticado antes de autenticarse. → El padre debe ser «Usuario», a secas.
- [ ] **CU-05** — `UC17 (Crear cuenta) ..> UC15a (Cambiar contraseña al primer acceso) <<include>>`
  es incorrecto: otro actor, otro momento. Es una **postcondición**, no un include.
- [ ] **CU-06** — `UC15 ..> UC15b (Desactivar cuenta) <<include>>` es incorrecto:
  desactivar es opcional; `<<include>>` significa «siempre». → `<<extend>>` o caso de uso independiente.
- [ ] **CU-07** — **Falta el caso de uso de recuperación de contraseña.** RF-03 lo exige y existe
  `POST /auth/recover` en la tabla de la API ([`05_diseno.tex:533`](chapters/05_diseno.tex#L533)).
- [ ] **CU-08** — El ADMIN no tiene ruta a `UC16 (Actualizar perfil propio)`.
- [ ] **CU-09** — Los nombres de caso de uso llevan detalle de implementación
  («Iniciar sesión\ncorreo @ipn.mx + contraseña»). Deben ser verbo + objeto.

## 2.3 Paquete 2 — Experimentos y carga de video

- [ ] **CU-10** — **Cadena de includes con causalidad falsa:** `UC22 → UC23 → UC24 → UC25`
  ([`cu_paquete2.puml:27-29`](diagramas/puml/cu_paquete2.puml)) afirma que «Validar formato»
  *incluye* «Encolar análisis». Validar un formato no encola nada.
  → Los tres deben colgar directamente de `UC22`.
- [ ] **CU-11** — **Relación duplicada:** `UC26 ..> UC24 <<extend>>` aparece dos veces con
  condiciones distintas, y «formato inválido» pertenece a `UC23`, no a `UC24`.

## 2.4 Paquete 4 — Resultados y reportes

- [ ] **CU-12** — Solo existe «Descargar reporte PDF», pero **RF-21 exige CSV y XLSX**.
- [ ] **CU-13** — **RF-31 (estadísticos de grupo: media, desviación estándar, varianza)
  no tiene ningún caso de uso.**

## 2.5 Paquete 5 — Dashboard y administración

- [ ] **CU-14** — 🔴 **Agujero de autorización.** `INV --> UC53 (Eliminar experimento, permanente
  e irreversible)` ([`cu_paquete5.puml:29`](diagramas/puml/cu_paquete5.puml)).
  Combinado con RN-08 (todos ven todo), **cualquiera de los 4 usuarios puede destruir
  irreversiblemente los datos de otro** — y deja sin sentido el rol de Administrador.
- [ ] **CU-15** — **Alerta de disco invertida:** `UC57a (Notificar disco > 80 %) ..> UC57
  (Monitorear estado) <<extend>>` hace que la alerta solo exista si el admin está mirando el panel.
- [ ] **CU-16** — **Actor equivocado:** `WRK --> UC54 (Borrar video a los 30 días)`.
  RNF-08 dice que eso es un *cron job*, no el worker de análisis.

## 2.6 Contradicciones entre diagramas y fichas de caso de uso

> Las más peligrosas: el jurado tiene ambas cosas enfrente al mismo tiempo.

- [ ] **CU-17** — En [`cu_vision_general.puml:26-27`](diagramas/puml/cu_vision_general.puml)
  el ADMIN solo se conecta a P1 y P5 → **no puede subir videos ni ver resultados**.
  Pero RF-04 dice «mismos permisos que el Investigador, más…» y las fichas CU-05 y CU-08
  listan «Inv. / Admin.» como actores.
- [ ] **CU-18** — [`05_diseno.tex:1152`](chapters/05_diseno.tex#L1152): CU-05 «**Incluye:**
  CU-07 (Monitorear progreso)». `<<include>>` = siempre ocurre, pero **RF-15 dice que el análisis
  continúa aunque el investigador cierre la pestaña** → monitorear es opcional → `<<extend>>`.
- [ ] **CU-19** — [`05_diseno.tex:1496`](chapters/05_diseno.tex#L1496): CU-08 «**Extendido por:**
  CU-07» está al revés. CU-08 (descargar diagnóstico) **extiende** a CU-07, porque solo ocurre si hubo error.
- [ ] **CU-20** — **RF-04 contra RF-07:** RF-04 le da al Admin «la capacidad de **aprobar registros**»;
  RF-07 dice «**No existe** formulario público de autoregistro». Si nadie se registra, no hay nada que aprobar.
- [ ] **CU-21** — **Redundancia de paquetes:** `UC27` (P2), `UC35` (P3) y `UC51` (P5) son tres casos
  de uso para el mismo objetivo — «ver en qué va mi experimento».

## 2.7 Pendiente externo

- [ ] **CU-22** — Agendar revisión de los casos de uso corregidos con la **Dra. Martha Rosa Cordero López**
  (punto 6 de la retroalimentación de la simulación de defensa).

---

# Bloque 3 — Escala del sistema

> **La evidencia está en el propio Anexo C.** La entrevista al Dr. Sandino dice literalmente:
>
> «Bastaría con un rol de investigador en general; **no se necesitan permisos diferenciados** entre ellos.»
>
> «**Una persona a la vez**, seguramente. […] cuatro usuarios posibles, pero **no de forma simultánea**.»
>
> El documento construye, encima de eso, un sistema de escala empresarial.

- [ ] **ESC-01** — [`05_diseno.tex:87`](chapters/05_diseno.tex#L87): «permite **escalar el número de
  workers** de forma independiente si el volumen de análisis aumenta» → eliminar o reformular.
- [ ] **ESC-02** — RNF-01: «≤ 3 s en el **95 % de las solicitudes**» → un SLO percentil no tiene
  sentido con 1 usuario a la vez. Reformular como tiempo de respuesta objetivo simple.
- [ ] **ESC-03** — RNF-03: «24/7, **≥ 95 % de disponibilidad mensual medida**» → es un SLA que exige
  infraestructura de monitoreo que no se va a construir. Reformular.
- [ ] **ESC-04** — RNF-09: al 90 % de disco **borra automáticamente** los videos más antiguos →
  automatización destructiva excesiva para un laboratorio de 32–40 videos/semestre.
  Cambiar a bloqueo de cargas + aviso al administrador.
- [ ] **ESC-05** — RNF-13: prueba de carga con 4 sesiones concurrentes → contradice «no de forma
  simultánea» de la entrevista. Reformular el criterio de aceptación.
- [ ] **ESC-06** — Reformular la cola: con RN-04 (secuencial) lo que existe es **un ejecutor de un
  trabajo a la vez en segundo plano**, no una «cola de tareas asíncrona escalable».
  Es más honesto y más defendible.
- [ ] **ESC-07** — Revisar la justificación de **dos roles + RBAC** frente a la entrevista, que pidió
  un solo rol. Si se conservan dos roles, justificar por qué se decidió ir más allá de lo solicitado.

> ⚠️ **Lo que NO se toca:** la separación worker/backend está **bien justificada**
> ([`05_diseno.tex:26-32`](chapters/05_diseno.tex#L26)) — un video de 20 min bloquearía Flask.
> Ese argumento se queda tal cual. Lo que sobra es el lenguaje de escalado alrededor.

---

# Bloque 4 — Faltantes del documento

## 4.1 Promesas colgadas (el jurado las va a buscar)

- [ ] **DOC-01** — 🔴 [`05_diseno.tex:343`](chapters/05_diseno.tex#L343) promete: «El **diccionario de
  datos** completo con tipos, restricciones y descripciones de cada columna se incluye en los anexos.»
  Pero `back/apendice_A.tex` (195 bytes) y `back/apendice_B.tex` (213 bytes) son **stubs vacíos**
  y están **comentados** en [`main.tex:53-54`](main.tex#L53). **El diccionario de datos no existe.**
- [ ] **DOC-02** — 🔴 **No hay capítulo de conclusiones.** `main.tex` compila solo los capítulos 1–5
  más el anexo C. Para TT-I es un hueco grave, y es el punto 14 de la retroalimentación de defensa
  («alinear conclusiones con cada objetivo específico»).

## 4.2 Nomenclatura formal ausente (notas manuscritas)

- [ ] **DOC-03** — **Nivel de madurez de Richardson**: la API está en **nivel 2** de facto
  (recursos + verbos HTTP + códigos de estado, sin HATEOAS). Nunca se declara.
- [ ] **DOC-04** — **Definir SPA** (*Single Page Application*). El frontend es React + Vite,
  o sea una SPA, pero el término no aparece nunca en el documento.
- [ ] **DOC-05** — **Clasificar el patrón cliente-servidor**: hoy solo dice «cliente-servidor de tres
  capas» ([`05_diseno.tex:38`](chapters/05_diseno.tex#L38)). Falta decir de qué tipo
  (3 capas / N capas, cliente ligero).
- [ ] **DOC-06** — Nombrar **RBAC** explícitamente y separar conceptualmente
  **autenticación** (verificar identidad al iniciar sesión) de **autorización**
  (qué puede hacer cada rol una vez dentro).
- [ ] **DOC-07** — Declarar la **semántica de `PATCH`** (solo actualizaciones parciales).
  El uso actual es correcto; solo falta explicitarlo.
- [ ] **DOC-08** — **Definir cada norma citada** en su primera aparición
  (ISO/IEC 25010, ISO/IEC/IEEE 12207, ISO 31000, ISO 14064-1, ISO/IEC 19501, ISO/IEC/IEEE 42010, NOM-062).
  Hoy aparecen como número sin explicar qué son.

## 4.3 Sin justificar en el texto

- [ ] **DOC-09** — Convertir la cascada **ResNet-18 → ResNet-50 → heurística**
  ([`05_diseno.tex:169-179`](chapters/05_diseno.tex#L169)) de lista a **tabla comparativa**
  (nivel, modelo/regla, condición de activación, ventaja).
- [ ] **DOC-10** — Justificar el almacenamiento de `progreso_pct` *(duplicado de BD-18, marcar juntos)*.

## 4.4 Higiene del repositorio

- [x] **DOC-11** — ~~Mergear la rama `claridad-documento`.~~ **Resuelto el 2026-08-25:**
  se verificó que `claridad-documento` ya estaba contenida en `main`, y `modificaciones`
  se integró a `main` por *fast-forward*. Las tres ramas apuntan al mismo commit.
  El trabajo real que quedaba pendiente es BD-17, no un merge.
- [ ] **DOC-12** — Uniformar la bibliografía: el PDF local usa «y col.» y otra compilación usa
  «et al.». Fijar la configuración de `biblatex` para que sea estable.

---

# Orden de ataque recomendado

Los bloques 1 y 2 están **acoplados**: si el esquema cambia, las fichas de caso de uso que
mencionan `estado` y `etapa` también cambian. Conviene hacerlos en este orden.

| # | Paso | Bloques | Por qué en este orden |
|---|------|---------|-----------------------|
| 1 | Rediseñar el esquema relacional | BD-01 … BD-18 | Es la base de todo lo demás; toca `relacional.puml`, la sección de normalización del cap. 5 y el diagrama de clases |
| 2 | Reconstruir los 5 diagramas de casos de uso | CU-01 … CU-21 | Depende de los nombres de estado/etapa que fije el paso 1 |
| 3 | Bajar la escala del sistema | ESC-01 … ESC-07 | Independiente; se apoya en citar el Anexo C |
| 4 | Escribir el diccionario de datos | DOC-01 | Solo se puede escribir cuando el esquema esté cerrado (paso 1) |
| 5 | Escribir las conclusiones de TT-I | DOC-02 | Una conclusión por objetivo específico |
| 6 | Nomenclatura formal | DOC-03 … DOC-08 | Lo más rápido; se puede intercalar en cualquier momento |
| 7 | Revisión con la Dra. Cordero | CU-22 | Después del paso 2, con los diagramas ya corregidos |

---

# Bitácora

| Fecha | Ítems cerrados | Notas |
|-------|----------------|-------|
| 2026-08-25 | — | Auditoría inicial. 59 ítems identificados. |
| 2026-08-25 | DOC-11 | Reorganización del repositorio: material de trabajo movido a `docs/`, `scripts/`, `mockups/` y `diagramas/pdf/`. Presentaciones eliminadas del historial (628 MB → 34 MB). `modificaciones` integrada a `main`. |
