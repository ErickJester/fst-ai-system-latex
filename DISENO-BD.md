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
| 4 | Retroalimentación de la simulación de defensa | `HISTORIAL.md`, `docs/Retroalimentacion_*.docx` |
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

## 5. Estado actual

**Las dos etapas están cerradas.** Conceptual: 8 de 8 actividades. Lógica: 7 de 7.
Resultado: 11 relaciones en BCNF, 11 llaves foráneas de una columna, 29 restricciones
documentadas (11 referenciales, 8 de identidad, 10 semánticas).

La respuesta a **P-01** —la rata sí tiene identificador propio— cerró la decisión que
estaba bloqueando todo: desapareció la cadena de seis entidades débiles, las diez
entidades quedaron fuertes, la agregación se volvió innecesaria y la llave más larga bajó
de siete componentes a dos.

La validación encontró **tres defectos reales**, así que el esquema definitivo no es igual
al preliminar:

| Forma | Dónde | Corrección |
|-------|-------|-----------|
| 1FN | `USUARIO` | `nombre` era dominio compuesto → se partió en `nombre` y `apellidos` |
| 3FN | `ESPECIMEN` | `idGrupo` era derivable de la tanda → columna eliminada |
| 3FN | `VIDEO` | `duracion` dependía de la sesión → ahora es la duración real del archivo |

### Lo que falta

| Qué | Estado |
|-----|--------|
| Revisión del protocolo con el Dr. Sandino | Reunión del 3-sep. Material: `Reunion_Sandino_2026-09-03.pdf` |
| Revisión de notación con la Dra. Cordero | Misma reunión — es directora del TT |
| Reescribir el cap. 5 del LaTeX | No iniciado. Es el trabajo grande |
| Etapa de diseño físico | Arranca cuando cierren las dos revisiones |

Hasta que ocurran esas dos revisiones, en los términos del método lo que existe es el
**Esquema Conceptual Inicial**, no el Definitivo.

### Preguntas que siguen abiertas

| ID | Pregunta | Qué decide |
|----|----------|-----------|
| P-03 | ¿Con qué se identifica físicamente a la rata: arete, jaula, código? | El dominio de `idLaboratorio` y el alcance de su unicidad. Único atributo del diccionario sin cerrar |
| P-04 | ¿Una grabación puede mezclar ratas de dos grupos? | Sostiene la corrección de 3FN sobre `ESPECIMEN` |
| P-02 | ¿La rata usa el mismo cilindro los dos días? | Si `numeroCilindro` vive en `ESPECIMEN` o en `OBSERVACION` |
| P-05 | ¿Cómo llama el laboratorio a la «tanda»? | El nombre en documento, diagrama e interfaz |
| P-08 | Al reanalizar un video, ¿se conservan ambos resultados? | Ver la errata estructural de la sección 8 |
| Q-08 | ¿Autoregistro con aprobación (cap. 1) o solo el Admin (cap. 4, RF-07)? | Si `USUARIO` necesita atributo discriminante |

### El trabajo grande que falta en el documento

El LaTeX **todavía no refleja el modelo nuevo**. Los capítulos 1 y 4 usan la noción vieja
y plana donde «experimento» = una grabación de ~4 ratas con ≤2 videos:

- **RF-09, RF-11, RN-03, RF-31** (cap. 4): escritos con la semántica equivocada de
  «experimento». Reescribir con los niveles Grupo y Tanda.
- **RF-14** fija «los cuatro cilindros»; el dominio correcto es 3 ó 4. Igual en cap. 1
  (4 ocurrencias) y cap. 3 (1).
- **«Cámara de celular»** en caps. 2, 3 y 4 → es **cámara web**.
- **§3.4 del cap. 3** describe tablas sin Grupo ni Tanda.
- **RN-04 y RF-16** implican que un video no se reanaliza nunca; el modelo dice (1,N).

Detalle por capítulo en [`errores/`](errores/).

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

## 8. Pendientes conocidos en los artifacts

### Errata estructural — sin resolver

`OBSERVACION` cuelga de `VIDEO`, pero la cardinalidad Video–Análisis es (1,N): un video
puede analizarse varias veces. Como `OBSERVACION` es única por el par (espécimen, video),
**un reanálisis con resultado distinto no tiene dónde escribirse**, y desde una fila de
`PRESENTA` no se puede saber qué análisis la produjo ni con qué nivel de clasificación.

**Corrección propuesta:** que `OBSERVACION` referencie `idAnalisis` en lugar de `idVideo`,
con unicidad sobre (espécimen, análisis). El video se alcanza por `ANALISIS → VIDEO`. No
cambia el número de relaciones ni rompe BCNF.

**No aplicar todavía:** depende de la respuesta a P-08. Si el laboratorio prefiere que el
reanálisis reemplace al anterior, el esquema se queda como está.

### Publicación

Los enlaces compartidos de ambos artifacts muestran **versiones anteriores fijadas**, no
la actual. Si alguien externo va a abrirlos, hay que mover el anclaje de compartición.

---

*Última actualización: 2026-09-02*
