# Diseño de la base de datos — punto de partida

**TT 2026-B066 · ESCOM-IPN** · Léeme antes de tocar nada relacionado con la base de datos.

Este archivo es la entrada al trabajo de diseño de la base de datos del sistema FST.
Si es tu primera sesión en este tema, lee este documento completo antes de abrir
cualquier `.tex`, cualquier diagrama o cualquier artifact.

---

## 1. Qué estamos haciendo

Estamos **rehaciendo el diseño de la base de datos desde cero**, siguiendo al pie de
la letra una metodología publicada, y documentando cada actividad de esa metodología
con su evidencia.

No es un refactor ni un ajuste. Es una derivación completa que parte del universo del
discurso (los requisitos del laboratorio) y llega al esquema lógico, pasando por el
esquema conceptual. El diseño de base de datos que hoy existe en el documento LaTeX
—capítulo 5 y los diagramas de `diagramas/`— **está mal y no se usa como insumo**.

### Por qué se rehace

Tres razones concretas:

1. **El capítulo 3 del TT declara un esquema lógico sin que exista un conceptual
   detrás.** Invierte el orden del método: primero aparecieron tablas, después nadie
   derivó las entidades. A esas tablas les faltan dos niveles enteros de la jerarquía
   (Grupo y Tanda).
2. **La palabra «experimento» se usa con dos significados incompatibles** en el
   documento: a veces es el estudio completo (4–6 grupos, 32–48 especímenes) y a veces
   es una sola grabación. Sin resolver eso, ningún esquema puede ser correcto.
3. **Los diagramas actuales tienen errores de construcción** señalados en la simulación
   de defensa, y la revisión con la Dra. Martha Rosa Cordero está pendiente.

### Qué queremos lograr

- Un **esquema conceptual** (modelo entidad-relación extendido) derivado con las ocho
  actividades del método, con su diccionario de datos y sus restricciones no
  estructurales documentadas.
- Un **esquema lógico** (modelo relacional) obtenido por transformación del anterior,
  validado con las formas normales.
- Que ese resultado **reemplace** el diseño de base de datos del capítulo 5 y los
  diagramas correspondientes, y que la defensa pueda explicar de dónde salió cada
  decisión.
- Que cada decisión sea **trazable a una fuente**: entrevista, respuesta del equipo o
  regla del libro. Nada por intuición.

---

## 2. En qué nos basamos

### 2.1 El libro — marco metodológico

> **Cardona, H.; Masso, J. E.; Mera, M. F.; Roa, S. M.; Ruano, E. F.; Torres, M. D.;
> Vidal, M. I.** *Diseño e Implementación de Bases de Datos desde una Perspectiva
> Práctica.* 1ª ed. Iniciativa Latinoamericana de Libros de Texto Abiertos (LATIn),
> marzo 2014. 147 págs. Licencia CC BY-SA 3.0.

**Ubicación del PDF:** `D:\Descargas\diseno-e-implementacion-de-bases-de-datos-desde-una-perspectiva-practica_copia.pdf`

> ⚠️ **Cómo leerlo.** La herramienta `Read` falla con este PDF (`pdftoppm` no está
> instalado en esta máquina). Extrae el texto primero:
> ```bash
> pdftotext -layout "/d/Descargas/diseno-e-implementacion-de-bases-de-datos-desde-una-perspectiva-practica_copia.pdf" libro.txt
> ```
> El archivo resultante son ~5,100 líneas. El sistema reporta 49 páginas pero **son
> 147**; no te fíes del conteo del visor.

**Secciones que importan:**

| Sección | Páginas | Contenido |
|---------|---------|-----------|
| §1.4 | 15–19 | La metodología completa: tres etapas con sus actividades numeradas |
| §1.4.2 | 16–17 | Diseño conceptual — 8 actividades |
| §1.4.3 | 17 | Diseño lógico — 7 actividades |
| §1.4.4 | 18 | Diseño físico — 6 actividades |
| §1.4.5 | 18–19 | Ejemplo del concesionario (el caso base que el libro desarrolla) |
| Cap. 2 | 21–39 | Modelo E/R: entidad fuerte y débil, atributo, dominio, cardinalidad, y el **EER** (§2.5): exclusividad, inclusividad, generalización y **agregación** |
| Cap. 3 | 41–47 | Modelo relacional: **reglas de transformación** (§3.2) y **normalización** (§3.3) |
| Apéndice A | 113+ | Caso completo (plan de manejo forestal) hasta el DDL en PostgreSQL |
| Apéndice B | — | Caso inmobiliaria: restricciones no estructurales y llaves compuestas |

### 2.2 Las fuentes del universo del discurso

El «universo del discurso» de este proyecto está repartido entre varias fuentes que
**se contradicen entre sí**. Existe una jerarquía formal para resolver los conflictos,
definida en [`errores/README.md`](errores/README.md):

| Rango | Fuente | Dónde |
|-------|--------|-------|
| 1 | Respuestas directas del equipo en sesión | Registradas en `errores/` |
| 2 | Entrevista formal con el Dr. Sandino | `docs/entrevista_sandino.docx` |
| 3 | Transcripciones de reuniones informales | `errores/fuentes/transcripcion_01_no-formal.md` |
| 4 | Retroalimentación de la simulación de defensa | `CLAUDE.md`, `docs/Retroalimentacion_*.docx` |
| 5 | Documento LaTeX | `chapters/`, `front/` |

> **Regla dura:** el LaTeX es el **destino** de las correcciones, no el árbitro. Ninguna
> decisión de modelado se toma citando el LaTeX si una fuente de rango superior dice
> otra cosa. Si no hay fuente, se registra como *pregunta abierta*, no se inventa.

**Los `.docx` no se leen con `Read`.** Extráelos así:

```bash
python -c "import docx; d=docx.Document('docs/entrevista_sandino.docx'); [print(p.text) for p in d.paragraphs if p.text.strip()]"
```

### 2.3 Qué parte del LaTeX sí sirve

- **Capítulos 1 a 3** son el planteamiento del caso: de ahí salen los conjuntos, los
  dominios y las transacciones que el esquema debe soportar. La sección **Alcance del
  capítulo 1** es la principal fuente de dominios; el **Planteamiento del problema**
  declara las transacciones.
- **Capítulo 4** aporta atributos de `Usuario`, `Experimento` y `Análisis`, pero es la
  fuente con menos respaldo del laboratorio. Úsalo con reserva y márcalo.
- **Capítulo 5 y `diagramas/`: no se usan.** Están mal y son el objetivo a reemplazar.

---

## 3. La metodología del libro, actividad por actividad

Esto es el mapa de todo el trabajo. Las tres etapas son secuenciales y cada una
consume la salida de la anterior.

### Etapa 1 — Diseño conceptual (§1.4.2)

> Entrada: especificación de requisitos (universo del discurso) · Proceso: Modelo de
> Datos Conceptual · Salida: **Esquema Conceptual** · Independiente del SGBD.

1. Identificar los conceptos: **atributos** (el libro dice «generalmente adjetivos»),
   **conjuntos** (sustantivos) y **relaciones** (verbos).
2. Determinar los **dominios** de los atributos (por extensión o por intensión).
3. Determinar los **identificadores** de cada conjunto.
4. Seleccionar un **Modelo de Datos Conceptual** que modele *todos* los objetos.
5. Crear el **Esquema Conceptual**.
6. **Revisar** el esquema: sin redundancia, fiel a la semántica, que soporte las
   transacciones de los usuarios.
7. **Presentar al usuario** y corregir → Esquema Conceptual **Definitivo**.
8. **Documentar**: elementos no estructurales + **diccionario de datos**.

> El libro distingue explícitamente «Esquema Conceptual **Inicial**» de «Esquema
> Conceptual **Definitivo**». Mientras la actividad 7 no ocurra de verdad, lo que
> tenemos es el Inicial. Esta distinción importa para la defensa.

### Etapa 2 — Diseño lógico (§1.4.3)

> Entrada: Esquema Conceptual · Proceso: Modelo de Datos Lógico · Salida: **Esquema
> Lógico**.

1. Seleccionar el **Modelo Lógico** e identificar sus estructuras, reglas y
   restricciones.
2. **Transformar** el esquema conceptual según ese modelo.
3. Identificar las **restricciones** del universo del discurso (integridad, identidad).
4. Determinar los **elementos no estructurales** que pasan a la etapa física.
5. **Integrar vistas** de usuario, si hay varias.
6. **Validar** el esquema: semántica conservada, restricciones cumplidas, transacciones
   soportadas. Aquí entra la **normalización** (§3.3).
7. **Documentar** el esquema lógico y sus consideraciones no estructurales.

**Reglas de transformación del libro (§3.2)** — solo cubren relaciones **binarias entre
entidades**:

| Cardinalidad | Caso | Regla |
|--------------|------|-------|
| 1:1 | ambos extremos obligatorios | fusionar en una sola tabla |
| 1:1 | un extremo opcional | la PK de una pasa a la otra como FK → 2 tablas |
| 1:1 | ambos opcionales | tercer caso previsto |
| 1:N | lado 1 es (1,1) | la PK del lado 1 pasa al lado N como FK, junto con los atributos de la relación |
| 1:N | lado 1 es (0,1) | la relación se vuelve tabla con PK compuesta |
| N:M | siempre | la relación se vuelve tabla, conserva atributos, recibe ambas PK como FK y PK |

> ⚠️ **El libro no da regla para entidades débiles ni para agregación** en el capítulo
> de transformación. Los patrones se deducen de sus apéndices (p. ej. la tabla
> `JURIDICA_TELEFONOS` del apéndice A, con PK `(Identificacion, Telefono)` donde
> `Identificacion` es a la vez FK). Cuando apliques esos patrones, **dilo
> explícitamente**: es extrapolación, no letra del método.

### Etapa 3 — Diseño físico (§1.4.4)

Aún no empezada. Seis actividades, desde elegir el SGBD hasta documentar. Aquí es donde
el método **sí admite «redundancia controlada»** para rendimiento — lo que en la etapa
conceptual estaba prohibido.

---

## 4. Dónde está el trabajo hecho

Dos artifacts publicados. **Son la fuente de verdad del diseño**, por encima del LaTeX.

| Artifact | URL | Cubre | Estado |
|----------|-----|-------|--------|
| **Diseño Conceptual FST** | https://claude.ai/code/artifact/441abfbd-3944-4412-8dca-0c40ab3964ba | Actividades 1–8 de la etapa conceptual | 7 de 8 hechas; la 7 está *preparada*, no ejecutada |
| **Diseño Lógico FST** | https://claude.ai/code/artifact/0f0abf49-bb77-4424-b5e8-6ea88a578143 | Actividades 1–2 de las 7 de la etapa lógica | 2 de 7 |

Cada artifact está organizado por actividad, y cada actividad muestra tres cosas: qué
pide el método, cómo lo resuelve el ejemplo del concesionario del libro, y qué resultó
en este proyecto. El conceptual incluye además una **bitácora** con la trazabilidad de
cada decisión.

**Para leerlos:** `Artifact` con `action: "read"` y la URL. Para actualizarlos, pasa la
misma URL como parámetro `url` — si publicas sin `url` creas un artifact nuevo en vez
de actualizar el existente.

### El modelo, en corto

```
Usuario ──registra──> Experimento
                          └── Grupo          (débil · etiqueta)   tipo ∈ {control, referencia, tratamiento}
                                └── Tanda    (débil · ordinal)    nCilindros ∈ {3,4}
                                      ├── Espécimen  (débil · posición del cilindro)
                                      └── Video      (débil · sesión ∈ {Día 1, Día 2})
                                                └── Análisis  (1,N — un video se puede reanalizar)

     Observación = AGREGACIÓN( Espécimen ──aparece en──> Video )
           └── Intervalo (débil · minuto 1..5)
                 └──presenta──> Conducta     [ segundos ]  ← el único dato medido del sistema
```

**9 entidades + 1 agregación + 9 interrelaciones → 11 relaciones** en el esquema lógico.

### Las cuatro decisiones que sostienen el modelo

1. **La Tanda existe.** Un grupo tiene 6–8 especímenes (entrevista PA) y el encuadre
   admite máximo 4 cilindros (respuesta del equipo). No caben: el grupo se graba en dos
   tandas. Ese nivel **no estaba nombrado en ninguna fuente**; se dedujo de la
   aritmética y se comprobó contra P19 (4 grupos × 2 tandas = 8 videos de Día 2).
2. **El espécimen no tiene identidad propia.** Ninguna fuente le da arete, número ni
   peso. Su única identidad es **geométrica**: la posición del cilindro en el encuadre.
   Eso funciona solo porque el laboratorio garantiza que la cámara y los cilindros no se
   mueven entre el Día 1 y el Día 2. Toda la comparación entre sesiones descansa ahí.
3. **Observación es una agregación, no una relación ternaria.** Una ternaria entre
   Espécimen, Video y Conducta permitiría emparejar un espécimen con el video de otra
   tanda. Es el error que el libro documenta en §2.5.3 con el ejemplo de las audiciones
   que no generan grabación. La agregación cierra primero el par válido y clasifica
   después.
4. **Todo el sistema mide un solo dato:** `segundos`, en la interrelación *presenta*.
   Los otros 26 atributos son estructura para ubicarlo o metadato del análisis. Los
   totales y los estadísticos de grupo se **derivan**, no se almacenan (actividad 6:
   sin redundancia).

---

## 5. Estado actual y qué sigue

### Etapa conceptual

| # | Actividad | Estado |
|---|-----------|--------|
| 1–6 | Conceptos, dominios, identificadores, modelo, esquema, revisión | ✅ Hechas |
| 7 | Presentación al usuario | ⏳ **Preparada, no ejecutada** — faltan dos reuniones |
| 8 | Documentación y diccionario | ✅ Hecha (27 atributos) |

La actividad 7 requiere **dos revisiones distintas**:
- **Dr. César Sandino** — que el modelo refleje el protocolo real. Llevar la jerarquía
  Experimento → Grupo → Tanda → Espécimen, el nombre del nivel «Tanda» (es un nombre de
  trabajo, el laboratorio no tiene término propio) y las preguntas abiertas Q-06 y Q-07.
- **Dra. Martha Rosa Cordero** — que los diagramas estén bien construidos. Llevar la
  agregación, las entidades débiles y las cardinalidades.

Material de apoyo: [`errores/preguntas-doctor.md`](errores/preguntas-doctor.md).

### Etapa lógica

| # | Actividad | Estado |
|---|-----------|--------|
| 1 | Selección del modelo lógico (relacional, PostgreSQL) | ✅ Hecha |
| 2 | Transformación → 11 relaciones | ✅ Hecha, en dos versiones |
| 3 | Restricciones de integridad e identidad | ⏳ Se puede adelantar para las 7 relaciones estables |
| 4 | Elementos no estructurales para la etapa física | ✅ Ya existen — salen de la actividad 8 del conceptual |
| 5 | Integración de vistas | ➖ No aplica: una sola vista, sin permisos diferenciados |
| 6 | Validación con formas normales | 🔴 **Esperar** — normalizar cuatro tablas cuya llave va a cambiar es trabajo que se tira |
| 7 | Documentación | ⏳ Después de la 6 |

### La decisión abierta más importante: llaves naturales vs. subrogadas

La transformación al pie de la letra produce una cadena de seis entidades débiles donde
las llaves se acumulan: `PRESENTA` termina con una **llave primaria de siete
componentes** y una sola columna de dato. Ambas versiones están documentadas y
comparadas en el artifact lógico.

**No decidas esto por tu cuenta.** Depende de si la rata resulta tener un identificador
propio (pregunta P-01 al Dr. Sandino): si lo tiene, la cadena se acorta sola y el
problema pierde gravedad; si no, la llave subrogada pasa de conveniencia a necesidad.
Es la misma pregunta la que resuelve las dos cosas.

> Nota: al pasar a llaves subrogadas **se pierde algo real**. Con llaves naturales, las
> FK de `OBSERVACION` hacia `ESPECIMEN` y `VIDEO` comparten sus tres primeras columnas,
> y ese solapamiento garantiza *por estructura* que ambos sean de la misma tanda. Con
> subrogadas esa restricción deja de ser estructural y pasa a `CHECK` o disparador.

### Preguntas abiertas que bloquean

| ID | Pregunta | Qué bloquea |
|----|----------|-------------|
| **P-01** | ¿La rata tiene un identificador propio (arete, marca, número de jaula)? | Si `Espécimen` es entidad débil o fuerte. Reescribe 4 de las 11 relaciones. **La de mayor impacto.** |
| Q-06 | ¿3–4 experimentos por semestre o por bimestre? | Cadencia de datos, factibilidad |
| Q-07 | ¿Algún grupo ha superado los 8 especímenes? | Si siempre son 2 tandas por grupo |
| Q-08 | ¿Autoregistro con aprobación (cap. 1) o solo el Admin crea cuentas (cap. 4, RF-07)? | Si `Usuario` necesita atributo discriminante o especialización |
| — | Identificador de `Experimento`: ninguna fuente declara clave natural | Decidir entre subrogada o la pareja (nombre, fecha) |

### El trabajo grande que falta en el documento

El LaTeX **todavía no refleja el modelo de los artifacts**. Los capítulos 1 y 4 siguen
usando la noción vieja y plana donde «experimento» = una grabación de ~4 ratas con ≤2
videos. Los puntos concretos:

- **RF-09, RF-11, RN-03, RF-31** (cap. 4) están escritos con la semántica equivocada de
  «experimento» y hay que reescribirlos con los niveles Grupo y Tanda.
- **RF-14** fija «los cuatro cilindros»; el dominio correcto es 3 ó 4, variable.
  Igual en cap. 1 (4 ocurrencias) y cap. 3 (1).
- **«Cámara de celular»** aparece en caps. 2, 3 y 4. Es **cámara web** (respuesta del
  equipo, Q-04).
- **§3.4 del cap. 3** describe las tablas de la BD sin Grupo ni Tanda.
- **RN-04 y RF-16** implican que un video no se reanaliza nunca; el modelo dice (1,N).
  Hay que distinguir reinicio manual del investigador (prohibido) de reanálisis
  administrativo (permitido).

Detalle completo por capítulo en [`errores/`](errores/).

---

## 6. Reglas de trabajo

Además de las de `CLAUDE.md`, que aplican siempre:

- **Terminología.** Lo que tiene tablas, tipos y llaves foráneas es **esquema físico** o
  **modelo relacional**, nunca «DER». «Diagrama entidad-relación» se reserva para el
  modelo conceptual, sin tipos ni FK. El **grafo relacional** (nodos = relaciones,
  aristas = FK) es el entregable propio de la etapa lógica.
- **Diagramas en lenguaje natural.** Sin SQL, sin nombres de función, sin código. Es
  requisito del TT.
- **No reintroducir** κ de Cohen, MAE ni «gold standard» sin confirmación explícita del
  usuario. Ver `CLAUDE.md`.
- **Nunca «inteligencia artificial»** a secas: siempre «visión por computadora» y
  «aprendizaje supervisado».
- **«Espécimen» o «rata»**, nunca «animales».
- **Los dominios del conceptual son conceptuales.** No hay `VARCHAR2` ni `NUMBER` hasta
  la etapa física.
- Si encuentras una contradicción sin fuente que la resuelva, va a `errores/` como
  **pregunta abierta**. No la resuelvas tú.

---

## 7. Cómo empezar una sesión nueva

1. Lee este archivo entero. ✔ (lo estás haciendo)
2. Lee [`errores/README.md`](errores/README.md) — jerarquía de fuentes y hallazgos
   transversales T-01 a T-06.
3. Extrae y lee del libro las secciones §1.4.2 y §1.4.3 (págs. 16–17), y del capítulo 3
   la sección §3.2 (págs. 41–44). Son ~150 líneas en total.
4. Lee los dos artifacts con `Artifact` / `action: "read"`.
5. Extrae `docs/entrevista_sandino.docx`. Las respuestas clave son **P19** (qué es un
   experimento), **PA** (grupos y especímenes), **P4/PC** (sesiones), **P9** (qué datos
   necesita), **P7** (conductas), **P1/P18** (usuarios y permisos).
6. Solo entonces, abre los `.tex` que necesites — capítulos 1 a 4 únicamente.

> **Lo que NO debes hacer al empezar:** tomar el capítulo 5, `diagramas/` o
> `docs/EsquemaFisicoBD_*.docx` como referencia de cómo es la base de datos. Están
> desactualizados respecto a los artifacts y contienen los errores que este trabajo
> corrige.

---

## 8. Erratas conocidas en los artifacts

Detectadas en revisión y **pendientes de corregir**:

**Diseño Conceptual**
- Actividad 1 dice «10 relaciones»; son **9**.
- Actividad 8 dice «26 atributos» en tres lugares; el conteo real y el recuadro de
  totales dicen **27**.
- Actividad 6, tabla de transacciones: dice «por animal» → debe ser «por espécimen».
- El enlace compartido muestra una **versión anterior fijada**, no la actual.

**Diseño Lógico**
- El pie dice `30-08-2026`; la última actualización fue el 02-09.
- La tabla «Qué es provisional» lista 6 filas pero el recuadro dice 4 provisionales
  (las 2 últimas tienen reserva menor, pero no llevan distintivo en las tarjetas).

---

*Última actualización: 2026-09-01*
