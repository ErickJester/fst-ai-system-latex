# Transcripción 02 — Reunión de revisión del modelo de datos

**Rango de fuente:** 3 (transcripción de reunión) · ver jerarquía en [../README.md](../README.md)
**Fecha:** 2026-09-03 · **Duración:** 47:28 · **Modalidad:** virtual
**Participantes:** Dr. César Sandino · Prof. Israel Salas · Ángel Frausto · Vanesa Rodríguez
**Ausente:** Mtra. Martha Cordero — la revisión de notación sigue pendiente

> Transcripción completa en [`docs/reunion_sandino_2026-09-03.docx`](../../docs/reunion_sandino_2026-09-03.docx).
> Este archivo registra solo lo que la reunión **cambia** respecto a lo que ya sabíamos.

---

## 1 · Preguntas que quedaron cerradas

| Ref | Respuesta | Efecto |
|-----|-----------|--------|
| **P-03** | Marca física: plumón indeleble en la cola, con líneas. Identificación lógica: **número de rata del 1 al 8, dentro de su grupo** | ⚠️ No es un identificador de laboratorio único. Ver §3.1 |
| **P-04** | «Siempre utilizamos para cada video ratas que hayan recibido el mismo tratamiento» | ✅ La corrección de 3FN sobre `ESPECIMEN` se sostiene |
| **P-02** | «Sí, a veces las ponemos en el mismo orden»; confirmado después: «Así es, sí» | ✅ `numeroCilindro` se queda en `ESPECIMEN`. El «a veces» inicial deja una reserva menor |
| **P-05** | El laboratorio **no tiene palabra** para el nivel; identifica por número de rata. Pero sí llama **«sesión»** a cada una de las dos grabaciones | ✅ «Tanda» sigue siendo término nuestro. `sesion` coincide con su vocabulario |
| **P-06** | 8 es lo normal, 6 el mínimo útil, 12 el máximo habitual. **«Yo preferiría que fuera sin límite»** | ⚠️ La cardinalidad (6,8) está mal. Ver §3.2 |
| **P-08** | «Si hacemos alguna modificación, la que sea, nos quedaríamos con el análisis del video que estamos ejecutando al final» | ✅ **Reemplazar.** La errata estructural de `OBSERVACION` no hay que corregirla |
| **P-07** | Ni semestre ni bimestre: depende del avance del proyecto. 5–6 experimentos por proyecto, de 1 a 4 años | ⚠️ Debilita la cifra de «32–40 videos por semestre». Ver §4.3 |

---

## 2 · Hallazgos nuevos

### N-01 · Existe una segunda técnica de cuantificación: «por eventos» 🔴

**Minuto 10:00–11:32.** El laboratorio ha usado dos técnicas distintas:

- **Por segundo** (continua) — se contabiliza la duración de cada conducta. Es la que el
  sistema automatiza.
- **Por eventos** (muestreo instantáneo) — cada 5 segundos se registra qué conducta hace la
  rata *en ese instante exacto* y se suman los eventos. «Era para tratar de estandarizar lo
  más posible los eventos que estábamos viendo».

> «En algunos de esos videos se utilizó una técnica diferente para hacer la cuantificación.»

**Por qué importa:** los archivos de análisis manual **mezclan las dos técnicas**, y sus
salidas no son comparables entre sí — una produce segundos, la otra conteos. Antes de usar
cualquier Excel como conjunto de prueba hay que saber con qué técnica se hizo. Afecta
directamente a OE-5 y a RNF-02.

**Pregunta que abre:** el criterio de «episodio válido de 3 a 5 segundos» (entrevista P6),
¿pertenece a la técnica continua o es un residuo del muestreo cada 5 s? Que ambos números
ronden los 5 segundos es sospechoso y conviene confirmarlo.

### N-02 · No existe el empate entre los Excel y los videos 🔴

**Minuto 12:39.**

> «Lo que no tendría ahorita es el empate entre qué videos de los que tienen corresponden a
> qué tiempos de los de la tabla de Excel. ¿Sí me explico? No sé qué tanta utilidad vaya a
> ser tenerlos así.»

Sin esa correspondencia, los análisis manuales **no sirven como conjunto de prueba**: hay
tiempos, pero no se sabe de qué video son. Es el insumo con el que se pensaba medir el F1.
Materializa parcialmente el riesgo R-03 y compromete el criterio de aceptación de TT-II.

### N-03 · Solo hay 6 videos disponibles 🟡

**Minuto 22:45.** El equipo tiene seis videos; la carpeta de Drive es de 2016 y el resto está
«en la otra computadora, en la oficina». La entrevista formal (P19) hablaba de 80 a 100 videos
acumulados en 10–12 años. El Dr. Sandino se comprometió a subir una carpeta «nado forzado».
Hasta que eso ocurra, el riesgo R-02 (dataset insuficiente) sube de nivel.

### N-04 · Un experimento puede repetirse por varianza alta 🟡

**Minuto 05:43.** «Llegamos a repetir el experimento con otras ocho cuando no tenemos
resultados que nos den una baja varianza entre la conducta de los primeros ocho.» Refuerza el
«sin límite» y sugiere que un grupo puede crecer después de haberse creado.

### N-05 · Aparece un nivel «proyecto» ⚪ SIN PRIORIDAD

**Minuto 06:24.** «En un proyecto podemos tener 5 o 6 experimentos diferentes, y ese proyecto
puede durar entre 1 año y 4 años.» Es un nivel por encima de `Experimento` que el modelo no tiene.

**Decisión tomada:** no se modela, y **no se menciona en el LaTeX** hasta confirmar a qué se
refiere exactamente. Queda registrado aquí y como pregunta sin prioridad.

> **Nota de vocabulario.** El resto de los términos del laboratorio **ya coinciden** con el modelo:
> él usa «experimento» para el estudio de tres grupos (nuestro `Experimento`), «grupo» para el
> grupo (`Grupo`) y «sesión» para cada una de las dos grabaciones (`sesion`). El único término
> inventado por nosotros sigue siendo «tanda», para el que el laboratorio no tiene palabra.

### N-06 · Instrucción del director sobre el documento

**Minuto 40:08.** Prof. Israel Salas: «Todos los cambios que hagan en el modelo deben estar
justificados y representados en el documento, porque los evaluadores o sinodales se los van a
pedir.» Es requisito explícito para la reescritura del cap. 5.

---

## 3 · Cambios obligados en el modelo

### 3.1 · `idLaboratorio` estaba mal modelado 🔴

Lo modelamos como clave alterna **única en todo el laboratorio**, con la idea de poder seguir
a la misma rata entre experimentos. La realidad es otra: el número va **del 1 al 8 dentro de
su grupo** y se reinicia en cada grupo. La marca física —plumón en la cola— es temporal.

**Consecuencias:**

1. Renombrar `idLaboratorio` → **`numeroRata`**, dominio entero, unicidad **relativa al grupo**.
2. La transacción «seguir a la misma rata entre experimentos distintos», que la actividad 6 del
   conceptual declaraba soportada, **no es posible**. Hay que retirarla.
3. **Problema estructural:** la clave alterna pasa a ser `(idGrupo, numeroRata)`, pero `idGrupo`
   se eliminó de `ESPECIMEN` por 3FN. Una restricción de unicidad no puede atravesar una
   reunión de tablas.

**Salidas para el punto 3**, en orden de preferencia:

| Opción | Costo |
|--------|-------|
| Disparador que valide la unicidad recorriendo `ESPECIMEN → TANDA → GRUPO` | Lógica fuera del esquema, más difícil de defender |
| Reintroducir `ESPECIMEN.idGrupo` como **redundancia controlada** | Rompe la 3FN a propósito, pero el método lo admite en la etapa física y ya estaba identificado como el candidato natural |

La respuesta del laboratorio convierte esa «candidata a redundancia controlada» en la opción
casi obligada. Conviene decidirlo antes de reescribir el cap. 5.

### 3.2 · Las cardinalidades de tamaño de grupo están mal 🔴

| Dónde | Estaba | Debe ser |
|-------|--------|----------|
| `Grupo — agrupa — Espécimen` | (6,8) | **(6,N)** — sin límite superior, a petición explícita |
| `TANDA.ordinal` | entero 1..2 | **entero ≥ 1** — con 12 ratas son 3 tandas |
| `Grupo — se graba en — Tanda` | (2,N) | ✅ sigue bien: con 6 ratas ya son 2 tandas |

La aritmética que presentamos —4 grupos × 8 ratas = 32 especímenes = 8 videos— **es un ejemplo,
no una regla**. En la reunión el Dr. Sandino describió el diseño canónico con **tres** grupos.

### 3.3 · La cardinalidad Video–Análisis cambia

Con «nos quedaríamos con el análisis del video que estamos ejecutando al final», la relación
pasa de **(1,N) a (1,1)** en la práctica. La alternativa —conservar historial marcando cuál está
vigente— ya no tiene respaldo del usuario. **Lo bueno:** la errata estructural de `OBSERVACION`
frente al reanálisis, registrada en `DISENO-BD.md` §8, queda cerrada sin tocar el esquema.

---

## 4 · Contradicciones con fuentes anteriores

La entrevista formal es rango 2 y esta transcripción rango 3, así que entre esas dos gana la
entrevista. La primera ya quedó resuelta por una respuesta del equipo, que es rango 1; las otras
dos siguen abiertas y hay que volver a preguntarlas.

### 4.1 · El grupo control sí recibe placebo ✅ RESUELTO

| Fuente | Dice |
|--------|------|
| Entrevista formal, PB (rango 2) | «Solo se mete al cilindro… **sin ningún tratamiento, fármaco ni placebo**» |
| Esta reunión, 35:40 (rango 3) | «Al día siguiente les damos el tratamiento: **placebo al control**, fármaco estándar a la referencia…» |
| **Equipo, sesión de trabajo (rango 1)** | **Sí hay placebo.** El acto de inyectar genera estrés por sí mismo, así que los tres grupos deben recibir el mismo estrés de inyección |

**Resuelto a favor del placebo**, por rango 1 de la jerarquía de fuentes. La respuesta de la
entrevista formal fue imprecisa: se preguntó por «fármaco o placebo» y se contestó pensando en
principio activo.

**El razonamiento importa y conviene que esté en el documento:** la inyección —manejo, sujeción,
piquete— es un estresor. En un modelo donde lo que se mide es precisamente la respuesta al
estrés, ese factor tiene que ser idéntico en los tres grupos; si solo se inyectara a los tratados,
una diferencia conductual podría atribuirse al piquete y no a la molécula. Es control de una
variable confusora.

**Reparto por día, ya firme:**

| | Día 1 (20 min) | Día 2 (5 min) |
|---|---|---|
| Control | Nada | Placebo / vehículo |
| Referencia | Nada | Fármaco de referencia (fluoxetina) |
| Tratamiento experimental | Nada | Molécula en evaluación |

**Qué cambia:**

- `GRUPO.tratamiento` **nunca es nulo**. Se elimina la restricción semántica «`tratamiento` es
  nulo si y solo si `tipo` = control».
- `EXPERIMENTO.notas` queda como **el único atributo que admite nulo** en todo el esquema. La
  nota «Sobre los nulos» de la etapa lógica, que menciona dos, hay que corregirla.
- La tabla de grupos experimentales del cap. 1 dice que el control va «sin tratamiento
  farmacológico». Debe decir que recibe placebo, y explicar por qué.

### 4.2 · Qué se analiza del Día 1 ✅ RESUELTO

Resuelto por el equipo (rango 1): **cada grupo puede tener o no su Día 1.** Cuando existe, sirve
para verificar que todas las ratas lleguen igual de estresadas al Día 2 — no es dato de
comparación del efecto del tratamiento.

**Qué cambia:**

- La cardinalidad `Tanda — produce — Video (1,2)` **se confirma**: 1 video si solo se grabó el
  Día 2, 2 si se grabaron ambos.
- Se retira la restricción no estructural «del Día 1 solo se analiza el grupo control». El Día 1
  es opcional para **cualquier** grupo.
- El alcance del cap. 1 está mal: hoy restringe el Día 1 al grupo control. Debe decir que es
  opcional para cualquier grupo y que su propósito es verificar la línea base.

### 4.3 · La cifra de volumen del cap. 1 pierde respaldo 🟡 SE PREGUNTA DE NUEVO

El cap. 1 justifica el proyecto con «en un semestre con entre 32 y 40 videos… más de 200
horas-persona», cifra que venía de la entrevista P19. En la reunión dijo que **no hay cadencia por
calendario**: los experimentos dependen del avance del proyecto, y un proyecto dura de 1 a 4 años.

Queda como pregunta **Q-C** en [`../preguntas-doctor.md`](../preguntas-doctor.md), reformulada para
no volver a chocar con el marco del calendario: cuántos experimentos corrieron en el último año,
cuántos videos tienen guardados en total, y cuánto tardan en analizarlos.

**Hacia dónde apunta la corrección:** reformular la justificación **por experimento** en vez de por
semestre. Ocho videos de Día 2 × ~2 h × 3 analistas ≈ 48 horas-persona por experimento. Ese número
aguanta cualquier cadencia.

## 5 · Errores y artefactos de la transcripción

| Dónde | Qué pasa |
|-------|----------|
| 00:54 | «Regresan al bioterio» no responde a la pregunta de identificación. Parece la cola de una respuesta anterior o audio recortado |
| 04:25 / 04:53 · 15:10 / 15:20 · 16:10 | Marcas de tiempo solapadas o desordenadas, y un bloque con dos hablantes. Artefacto de la separación automática de hablantes, no del contenido |
| 12:39 | «Tengo un **video** que se llama Resultados de videos» — por contexto está buscando tablas de Excel; debería decir «archivo» o «carpeta» |
| 06:04–06:14 | Hueco de audio: Ángel pide que repita y la respuesta se repite. No cambia el sentido |
| 03:14 | «Le llamamos sesiones a los 5 minutos… o bueno, a la primera sesión de 20 minutos» — autocorrección al hablar. Sentido final: sesión = cada una de las dos grabaciones |
| Nombres | «Vanessa Rodríguez» → en el TT es **Vanesa**. «Prof. Israel Salas» y «Mtra. Martha» → en el documento aparecen como **Dr.** Israel Salas Ramírez y **Dra.** Martha Rosa Cordero López. Si el tratamiento correcto es Mtra., hay que corregirlo en el TT, no aquí |

---

## 6 · Pendientes que deja la reunión

**Del laboratorio**

- [ ] Subir a Teams la carpeta «nado forzado» con los videos faltantes
- [ ] Compartir el artículo de Porsolt — describe cómo se interpreta cada conducta
- [ ] Buscar el video de protocolos que explica conducta por conducta
- [x] Presentación subida a Teams › Compartidos › «Sesión Depresión»
- [x] Acceso a Teams para Ángel y Vanesa

**Del equipo**

- [ ] Recordarle al Dr. Sandino por la mañana lo de los videos y los artículos
- [x] ~~Preguntar de nuevo lo de §4.1 (placebo)~~ — resuelto por el equipo, rango 1
- [x] ~~Preguntar lo de §4.2 (Día 1)~~ — resuelto por el equipo, rango 1
- [ ] Llevar al lunes las preguntas Q-A (técnicas de cuantificación), Q-B (videos por
      experimento) y Q-C (volumen real), formuladas en [`../preguntas-doctor.md`](../preguntas-doctor.md)
- [ ] Decidir cómo se resuelve la unicidad de `numeroRata` (§3.1)
- [ ] Reunión presencial en ESCOM, lunes o viernes 14:00–16:00, sujeta a la Mtra. Martha Cordero
