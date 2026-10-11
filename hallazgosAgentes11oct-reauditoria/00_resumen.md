# Reauditoría de consistencia — resumen general

**Fecha:** 2026-10-11 · **HEAD auditado:** `975ec4c` (rama `accesos-login`) · **Modo:** solo lectura. Nadie editó `.tex`, `.puml`, `.md` ni `.bib`; lo único nuevo es esta carpeta (`git status` solo la agrega, además de los archivos sin seguimiento que ya estaban).
**Alcance:** `chapters/01`–`05`, `front/`, `back/apendice_C` y `_D`, `diagramas/` (con `diagram_design/`), los `.md` de reglas y notas y `errores/`. Los caps. 6–8 están comentados en `main.tex` y no se auditaron.

**Carpeta aparte.** Se escribió en `hallazgosAgentes11oct-reauditoria/` y no en `hallazgosAgentes11oct/` porque esa carpeta ya existe, está en git (commit `00f045a`) y los IDs de la primera auditoría (C1-xx, DF-xx...) se citan en `PENDIENTES-VANESA.md`. Reemplazarla los habría roto. Cada hallazgo trae el campo `Previo`: ID anterior o «nuevo».

**Contexto de esta pasada.** Desde la primera auditoría se aplicaron los hallazgos de caps. 1–3, `front/`, `bib/` y casos de uso, y se registraron D-57 a D-65. D-57 a D-60 están registradas pero deliberadamente sin aplicar; los agentes las trataron como una sola nota «pendiente de propagar» (C5-17, una vez), no como hallazgo por cada ocurrencia.

---

## 1. Conteo por agente y severidad

| # | Agente | Alta | Media | Baja | Total | Preguntas abiertas (campo «Fuente») |
|---|--------|-----:|------:|-----:|------:|-----:|
| 01 | Cap. 1 (`C1-`) | 2 | 5 | 15 | 22 | 4 |
| 02 | Cap. 2 (`C2-`) | 0 | 1 | 7 | 8 | 3 |
| 03 | Cap. 3 (`C3-`) | 1 | 6 | 7 | 14 | 6 |
| 04 | Cap. 4 (`C4-`) | 4 | 10 | 14 | 28 | 7 |
| 05 | Cap. 5 (`C5-`) | 3 | 9 | 8 | 20 | 3 |
| 06 | Diagramas relacional y de clases (`DR-`) | 0 | 8 | 8 | 16 | 4 |
| 07 | Diagramas de flujo, CU y secuencia (`DF-`) | 2 | 13 | 5 | 20 | 2 |
| 08 | Reglas en `.md` (`MD-`) | 4 | 23 | 10 | 37 | 8 |
| 09 | Terminología y prohibiciones (`TT-`) | 1 | 5 | 10 | 16 | 3 |
| | **Total** | **17** | **80** | **84** | **181** | **40** |

Contados por mí contra los archivos (no solo con los totales de cada agente). Los agentes reportaron 38 preguntas abiertas en sus propios resúmenes; el número de arriba cuenta las entradas cuyo campo «Fuente que decide» dice «pregunta abierta» (dos de ellas, C2-05 y DR-05, no nombran destinatario). `06_diagramas-relacional.md` incluye además una sección «Conteos recontados del grafo vigente» que no es hallazgo: **15 relaciones, 63 atributos, 17 FK**, coinciden con el cap. 5, el apéndice D y `DISENO-BD.md`.

Los 181 son entradas de agente: **varios describen el mismo problema** (sección 4). Las 17 Altas se reducen a **11 problemas distintos**.

**Limpio en todos los agentes:** ningún resto de κ de Cohen, MAE ni «gold standard» en los `.tex`; ningún «último segundo» vigente; el grafo vigente cuadra con sus cifras; las filas D-57 a D-65 coinciden con `PENDIENTES-VANESA.md` y con los capítulos.

---

## 2. Los hallazgos de severidad Alta

Agrupados por problema, ordenados por impacto. Los marcados ✔ los verifiqué yo leyendo la línea citada.

| # | Problema | IDs de agente | Dónde | Fuente que decide |
|---|----------|---------------|-------|-------------------|
| 1 | El Día 1 del grupo control se sigue **analizando** (primeros 5 min) o aceptando como «referencia basal», pero D-54 (d) dice que el Día 1 solo confirma la habituación y no se analiza ✔ | C1-01, C4-01, MD-01 | `01_introduccion.tex:261,322`; `04_analisis.tex` RF-09 (`:104-110`); `INSTRUCCIONES-WEB.md:424` | D-54 (d), transcripción 02 §4.2 |
| 2 | Figura de arquitectura: muestra «corrección CLAHE», «Videos anotados _tracked.mp4», solo `.mp4` y SQL ✔ | C5-03, DF-02, TT-01 | `diagramas/arquitectura_software.puml:79,87,101,116` y su PNG (cap. 5:53) | D-16, CLA-04, D-30; cap. 5:158 |
| 3 | El cap. 5 dice que la «anotación experta» alimenta el entrenamiento del clasificador, contra la prohibición vigente y su propia figura ✔ | DF-01, MD-04 (+ C5-08 como Media) | `05_diseno.tex:99-102` | D-26, D-56, `CLAUDE.md` |
| 4 | El **despliegue** sigue registrado en RNF-10, otras menciones del cap. 4, y en el apartado «Arquitectura» y la portabilidad del cap. 5 ✔ | C4-02, C5-02 (+ TT-05, DF-15, C1-20 como Media/Baja) | `04_analisis.tex:350,401-406,698,880,904,1057`; `05_diseno.tex:22-31,93-95` | D-62 (11-oct) |
| 5 | La tabla de grupos dice que el control **no recibe nada**; el equipo decidió que recibe **placebo** el Día 2 ✔. Ningún capítulo menciona «placebo» | C1-02 | `01_introduccion.tex:74-77` | Transcripción 02 §4.1 (rango 1); contradice la entrevista PB (rango 2), cuya imprecisión el propio registro explica |
| 6 | La pantalla de eliminar experimento sigue pidiendo nombre y contraseña ✔ | C5-01 (+ C4-06) | `05_diseno.tex:2543-2569` frente a CU-23 | D-63 |
| 7 | **R-03** supone que el laboratorio entrega registros para entrenar y validar ✔ | C4-03 | `04_analisis.tex:806-810` | D-26 y la fila «Etiquetador del equipo» del mismo capítulo |
| 8 | La factibilidad dice «3 a 5» experimentos de «tres grupos» fijos y la cuenta de videos no cuadra con la entrevista (3–4, promedio 4 grupos, ~8 videos, 32–40 por semestre) ✔ | C4-04 (+ C1-06, C1-07, C3-02, MD-21) | `04_analisis.tex:926-932,1095-1097` | Entrevista P19, `PENDIENTES.md` |
| 9 | El cap. 5 describe procesamiento **parcial** si faltan cilindros («en lugar de abortar»); D-20 decidió todo o nada ✔ | MD-03 (+ C5-07 como Media) | `05_diseno.tex:336-339` | D-20, RN-11 |
| 10 | `DISENO-BD.md` deja P-08/D-03 «sin resolver / no aplicar todavía»; D-03 está resuelto y aplicado ✔ | MD-02 | `DISENO-BD.md:224,405,483-497` | D-03, D-24 |
| 11 | El glosario dice que el clasificador se entrena con fotogramas etiquetados «por el colaborador clínico» ✔ | C3-01 | `front/glosario.tex:50-51` | D-26, D-56 |

---

## 3. Lo que más pesa aunque no sea Alta

- **Una marca ✅ que no se cumple (MD-08, Media, pregunta abierta → tú y el usuario).** `PENDIENTES-VANESA.md` marca A-14 como hecho, pero `front/portada.tex:73` y `front/documento_tecnico.tex:32` siguen diciendo «Mayo 2026». La fecha de entrega no está en ninguna fuente. Algo parecido en MD-37: `zhang2022_bytetrack` sigue en `bib/referencias.bib:375` pese al ✅ L-5.
- **Decisiones del 11-oct solo a medias (MD-05, C4-05, C4-06, DF-10).** D-62, D-63 y D-64 están aplicadas en el cap. 1 y en los casos de uso, pero no en RN-09/RF-27, RN-10/RF-10, `seq_carga_video.puml` ni en las pantallas del cap. 5. El cap. 5 se contradice dentro de sí mismo.
- **`PENDIENTES.md` desactualizado (MD-06, MD-07, MD-36).** «Lo que ya está decidido» se declara vigente al 5-oct y dice que gana sobre decisiones posteriores; varios ítems siguen abiertos aunque están resueltos.
- **Tensión sobre el clasificador (DF-18 / MD-26, preguntas abiertas → equipo).** `diagram_design/pipeline_analisis.md` presenta la CNN de fusión como flujo principal; `PENDIENTES.md` dice «todavía no se elige». Hay que decidir cuál es la línea del proyecto antes de corregir cualquiera de los tres. El repositorio `fst-etiquetador` ya implementa la CNN de fusión.
- **El video del Día 1 en el modelo (DR-06 / MD-24 / MD-23, preguntas abiertas).** Si el Día 1 no se analiza, las cardinalidades Video–Análisis (1,1) y Video–Observación (2..4) y las columnas NOT NULL de `ANALISIS` no cuadran.
- **`clases.png` anterior a `clases.puml` (DR-01)** y notas con SQL y `D-xx` visibles en la figura del esquema físico (DR-10, TT-02, DF-05, DF-06).
- **Choque `CLAUDE.md` ↔ LaTeX sobre F1 (C1-21, C2-08, C3-07, TT-16).** Cuatro agentes lo reportaron: `CLAUDE.md` todavía dice «F1 por clase»; D-65 fija «por conducta».
- **Notificaciones por correo ausentes en figuras y alcance (C1-22, DF-07, DF-08).**

---

## 4. Contradicciones que aparecen en más de un agente

| Contradicción | Agentes / IDs | Comentario |
|---------------|---------------|------------|
| Día 1 «analizado» o «referencia basal» | C1-01, C4-01, MD-01 (+ DR-06, MD-24) | Una corrección en tres archivos; el efecto en el modelo es una pregunta abierta |
| Figura de arquitectura (CLAHE, `_tracked`, solo `.mp4`, SQL) | C5-03, DF-02, TT-01, C5-11 | Regenerar el PNG desde `arquitectura_software.puml` |
| «Anotación experta» alimenta el entrenamiento | DF-01, MD-04, TT-04, C5-08 | Un renglón en `05_diseno.tex:99-102` (TT-04 y C5-08 lo clasificaron Media) |
| Despliegue (D-62) | C4-02, C5-02, TT-05, DF-15, C1-20, MD-37 | C1-20 y MD-37 preguntan si «empaquetar con Docker Compose» cuenta como despliegue |
| Volumen de experimentos y videos | C4-04, C1-06, C1-07, C3-02, MD-21, MD-31 | Cinco capítulos/archivos, cuentas que no coinciden; la entrevista P19 decide |
| Eliminar experimento con nombre y contraseña | C5-01, C4-06 | D-63 pendiente de propagar |
| Validación de formato/orientación del video | C4-05, DF-10, C5-16 | D-64: extensión en la interfaz; orientación y reproducibilidad en el servidor |
| «Cuatro módulos» contra «tres etapas» | C5-04, TT-08, DF-19 | D-16 |
| Procesamiento parcial de cilindros | MD-03, C5-07 | D-20 contra el texto del cap. 5 |
| Dominio de `SEGUNDO.origen` (4 contra 6 valores) | C4-15, C5-06, DR-05 | Pregunta abierta → equipo/tú y el usuario |
| «Mismas columnas» en físico y lógico | C5-05, DR-03 | `ANALISIS.rutaDiagnostico` solo está en el físico |
| `PRESENTA` en la tabla de normalización | C5-12, DR-04 | |
| Fila 3FN de `USUARIO` mal rotulada | C5-12, DR-09 | |
| Número de rata | C5-15, TT-03 | `05_diseno.tex:416` y la nota de `esquema_fisico.puml` |
| `CU-21` inexistente | C5-13, DF-14, MD-09 | Debe decir CU-22 |
| Texto de figuras con SQL, `D-xx` y rutas HTTP | DF-05, DF-06, TT-02, DR-10 | |
| Tres conductas donde son cuatro | C1-10, C1-19, C2-06, C4-21, TT-15, DF-17 | La pregunta de fondo (¿la meta de F1 85 % aplica a conducta activa?) está en C3-14, C4-21 y TT-15 |
| «Tres grupos» fijos | C1-06, C4-04, DF-04, MD-21 | El modelo es de tres o más |
| Repetibilidad ausente de métricas y RNF | C3-05 (+ M-1c de `PENDIENTES-ERICK.md`) | Pendiente conocido |
| CNN de fusión como línea principal | DF-18, MD-26, C3-04 | Pregunta abierta → equipo |
| `README.md`, `MIGRACION-DIAGRAMAS.md`, `errores/pendientes.md` sin banner de obsolescencia | MD-18, MD-19, MD-20, MD-35 | |
| TT2 / TT-II | C4-24, TT-07 | Ninguno definido en abreviaturas |
| Cronograma y *stack* con Docker | C1-20, MD-37 | Ver despliegue |

---

## 5. Hallazgos por destinatario

Conteo según el campo «Destinatario» de cada hallazgo (el agente lo asigna por el archivo citado; un hallazgo que cita archivos de las dos zonas aparece como «ambos»).

| Destinatario | Alta | Media | Baja | Total |
|--------------|-----:|------:|-----:|------:|
| Erick | 13 | 63 | 43 | 119 |
| Vanesa | 1 | 6 | 25 | 32 |
| Ambos | 3 | 11 | 14 | 28 |
| Sin indicar (C5-17, TT-16) | 0 | 0 | 2 | 2 |
| **Total** | **17** | **80** | **84** | **181** |

### Vanesa (32)

- **Alta (1):** C1-02.
- **Media (6):** C1-03, C1-04, C2-01, DF-12, DF-13, MD-08.
- **Baja (25):** C1-08, C1-10, C1-11, C1-12, C1-13, C1-14, C1-16, C1-17, C1-19, C1-22, C2-02, C2-03, C2-04, C2-05, C2-06, C2-07, C2-08, C3-08, C3-09, C3-12, C3-14, MD-36, MD-37, TT-13, TT-14.

### Ambos (28), donde Vanesa tiene su parte

- **Alta (3):** C1-01, C4-01, MD-01.
- **Media (11):** C1-05, C1-07, C3-02, C3-05, DR-06, DR-08, DF-14, MD-18, MD-24, TT-02, TT-05.
- **Baja (14):** C1-09, C1-15, C1-18, C1-20, C3-10, C3-11, C3-13, DR-15, DF-16, DF-19, MD-32, TT-09, TT-10, TT-11.

### Erick (119)

Todo lo demás: caps. 4 y 5 fuera de casos de uso, `.puml`, figuras, `.md` y apéndices. Incluye 13 de las 17 Altas.

### Preguntas abiertas por destinatario (40)

**Laboratorio (Dr. Sandino) — 3:**

- C1-07 (M) — Cuántos experimentos y videos hay por semestre; tres cuentas distintas en los caps. 1, 3 y 4
- C3-02 (M) — Mismo tema, desde el cap. 3
- C4-10 (M) — RN-15 atribuye al laboratorio la técnica de conducta predominante; la transcripción describe un muestreo instantáneo (Q-A sin responder)

**Equipo (Erick y Vanesa; directores si aplica) — 21:**

- C1-12 (B) — ¿El *sprint* es mensual o semanal?
- C3-04 (M) — ¿La versión fusionada de la CNN es parte del diseño del TT?
- C3-08 (B), C3-10 (B) — Afirmaciones técnicas que la bibliografía no respalda del todo
- C4-11 (M) — RN-15: redacción ambigua y casos de empate sin regla
- C4-13 (M) — RNF-03: 95 % de disponibilidad sin fuente
- C4-14 (M) — «PDF final» y «resumen ejecutivo»: ¿qué entregable es?
- C4-21 (B) / TT-15 (B) — ¿La meta de F1 85 % aplica a conducta activa?
- C4-25 (B) — Pressman como respaldo de umbrales de disco
- C5-07 (M) — Detección parcial de cilindros: ¿qué pasa con menos cilindros que `TANDA.nCilindros`?
- C5-10 (M) — Panel de administración muestra «el modelo del clasificador en uso»
- DR-05 (M) — `clases_completo.md` contra el documento sobre `humano_ciego` y `sin_revisar`
- DR-06 (M), DR-08 (M) — Video de Día 1 contra cardinalidades; `PRESENTA (2..4)` contra cuatro filas siempre
- DR-16 (B) — `Grupo agrupa Espécimen (2,N)` del conceptual
- MD-22 (M) — Filas D-04, D-06 y D-14 sin marca de «sin objeto»
- MD-23 (M) — NOT NULL de `ANALISIS` frente a `INSTRUCCIONES-WEB.md`
- MD-25 (M) — Quién borra los videos a los 30 días
- MD-26 (M) — La CNN de fusión como clasificador principal
- TT-14 (B) — «animal(es)» en trabajos relacionados del cap. 2

**Tú y el usuario (conversación) — 16:**

- C1-18 (B) — OE-6 y alcance contra RNF-11 (¿requisito o trabajo futuro?)
- C1-20 (B), MD-37 (B) — ¿«Empaquetar con Docker Compose» cuenta como despliegue?
- C2-01 (M) — DSAAN: verificar contra el artículo (DOI 10.1016/j.jneumeth.2024.110212)
- C2-05 (B), C2-06 (B) — Atributos de ISO 25010 como «del mismo nivel»; «tres conductas» sin la cuarta
- C3-05 (M) — Repetibilidad ausente de las métricas
- C3-14 (B) — Nombre del laboratorio abreviado y «cada conducta es una clase»
- C4-20 (B) — RN-16: ¿«modificar» una cuenta puede quitar el rol de Administrador?
- C5-06 (M) — Dominio de `SEGUNDO.origen`
- DF-09 (M) — Qué guarda realmente el worker (salidas del módulo 4)
- DF-18 (B) — Descripción del 8-oct de la CNN de fusión sin D-xx
- MD-08 (M) — Fecha de entrega para portada y documento técnico
- MD-24 (M) — Qué hace el Día 1 en el modelo
- MD-27 (M) — Dos juegos de URLs de los artifacts en `DISENO-BD.md`
- TT-05 (M) — Despliegue en requisitos, costos y figura (D-62)

(3 + 21 + 16 = 40. DR-05 no nombra destinatario y lo puse en «equipo»; C2-05 tampoco y lo puse en «tú y el usuario».)

### Ítems que ninguna lista de dueño cubre y requieren decisión de quien coordina

- **Placebo (C1-02):** hay que decidir cómo se redacta la fila del control en el cap. 1, que contradice la entrevista de rango 2.
- **Marcas ✅ que no se cumplen (MD-08, MD-37, MD-07):** conviene reabrirlas en `PENDIENTES-VANESA.md`.
- **Línea del clasificador (DF-18 / MD-26 / C3-04):** hay que decidir si la CNN de fusión ya es la línea del proyecto.
- **`CLAUDE.md` (C1-21, C2-08, C3-07, TT-16, MD-28):** F1 «por conducta» y punteros desactualizados. No lo toqué.
- **D-57 a D-60:** siguen sin aplicar; cambian RN-04, RN-14, RF-32 y la pantalla de revisión.

---

## 6. Límites de esta auditoría

- Lectura y búsqueda; **no se compiló LaTeX ni PlantUML.** Las comparaciones PNG contra `.puml` se hicieron abriendo las imágenes que cada agente indica en su sección de cobertura. No se abrieron todos los `seq_*.png`, `cu_paquete*.png` ni los mockups v2; en esos casos se asumió que el PNG refleja su fuente por tener fecha de git igual o posterior.
- `INSTRUCCIONES-WEB.md` se revisó por búsquedas dirigidas, no línea por línea; `CORRECCIONES.md`, `MIGRACION-DIAGRAMAS.md`, `COMPARATIVA` y `errores/0X` solo por encabezados, banners, conteos y términos prohibidos. No se abrió ningún `.docx`.
- Los datos externos (artículos, DOI, ISO) los comprobó cada agente por su cuenta o los dejó como «no verificado». No los repetí.
- `03_cap3.md` cambió en disco después de que su agente lo escribió y no lo releyó; recontaré sus totales contra las entradas (1 Alta, 6 Media, 7 Baja) y coinciden.
- Verifiqué por mi cuenta, leyendo la línea citada, los 11 problemas de severidad Alta de la sección 2. No re-verifiqué las Medias ni las Bajas.
- La severidad la asignó cada agente con el criterio del brief; hay diferencias entre agentes para el mismo problema (p. ej. «anotación experta»: Alta en DF-01 y MD-04, Media en TT-04 y C5-08).
- No hice preguntas sueltas ni toqué `PREGUNTAS.md`.
