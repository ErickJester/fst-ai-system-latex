# Material para la próxima reunión con el Dr. Sandino

**Última actualización:** 2026-08-30
**Propósito:** acumular lo que hay que validar y preguntar. De aquí se formulan las preguntas de cada reunión.

> **Cómo usar este documento.** La sección 1 son **conceptos que entendimos y hay que confirmar** —se le leen al doctor tal cual—. La sección 2 son **preguntas directas**. La sección 3 registra datos nuevos que aún no llegan al documento. La sección 4 lista lo ya respondido, para no volver a preguntarlo.
>
> Jerarquía de fuentes y catálogo de errores: ver [README.md](README.md).

---

# 1 · Conceptos a validar

Cosas que dedujimos al modelar la base de datos y que **hay que confirmar con el laboratorio** antes de fijarlas en el documento del TT.

## 1.1 · Qué estamos llamando «tanda»

> **Para leerle al doctor.** El objetivo es que confirme si entendimos bien, y sobre todo si el laboratorio ya tiene una palabra propia para esto.

### El problema que la hizo aparecer

Al modelar la base de datos encontramos que la palabra **«experimento»** se estaba usando para dos cosas distintas:

- **El estudio completo** — 4 grupos, entre 32 y 48 ratas, alrededor de 8 videos
- **Una sola grabación** — las 3 o 4 ratas que salen juntas en un mismo video

Son cosas distintas y hacía falta un nombre para la segunda. Le pusimos **«tanda»** de forma provisional.

### Qué llamamos tanda

> Una **tanda** es el conjunto de ratas que se graban **juntas en el mismo video**, es decir, las que comparten encuadre.

Como en el encuadre caben **máximo 4 cilindros** y un grupo tiene entre **6 y 8 ratas**, un grupo no cabe en una sola grabación: **necesita dos tandas**.

### Ejemplo concreto

```
Experimento «Molécula X»  (el estudio completo)
│
├── Grupo control            8 ratas
│     ├── Tanda 1   →  4 ratas  →  video Día 1  +  video Día 2
│     └── Tanda 2   →  4 ratas  →  video Día 1  +  video Día 2
│
├── Grupo fluoxetina         8 ratas
│     ├── Tanda 1   →  4 ratas  →  video Día 1  +  video Día 2
│     └── Tanda 2   →  4 ratas  →  video Día 1  +  video Día 2
│
├── Grupo tratamiento A      8 ratas   → 2 tandas
└── Grupo tratamiento B      8 ratas   → 2 tandas
                                        ─────────────
                              8 tandas  →  8 videos de Día 2
```

Eso cuadra con lo que el doctor declaró en la entrevista: *«promedio de 4 grupos y 32 a 48 especímenes, lo que genera alrededor de 8 videos por experimento»*.

### Lo que ya está confirmado sobre la tanda

| Afirmación | Estado |
|---|---|
| Las ratas de una tanda son **siempre del mismo grupo** experimental | ✅ confirmado |
| La **misma tanda** se graba los dos días, con las mismas ratas en los mismos cilindros | ✅ confirmado |
| El encuadre y la posición de los cilindros **no cambian** entre el Día 1 y el Día 2 | ✅ confirmado |
| Caben entre **3 y 4 cilindros** a cuadro, nunca más de 4 | ✅ confirmado |

### Lo que falta preguntar

**¿El laboratorio ya tiene una palabra para esto?** «Tanda» es un nombre que inventamos nosotros. Puede que ustedes le digan *corrida*, *lote*, *sesión de grabación*, *bloque* o algo más.

**Por qué importa el nombre:** va a aparecer en el documento escrito del TT, en el diagrama de la base de datos y en la interfaz del sistema. Es mucho mejor usar el término que el laboratorio ya usa que imponer uno inventado.

---

# 2 · Preguntas abiertas

Ordenadas por impacto en el diseño. Las tres primeras cambian el modelo de datos.

## P-01 · ¿Cómo se identifica a una rata individualmente? 🔴

**Por qué se pregunta.** Hasta ahora, en todo el material disponible, la única forma de distinguir una rata de otra es **la posición del cilindro en el encuadre**. Ninguna fuente menciona arete, tatuaje, marca, número ni peso.

**Qué preguntar concretamente:**
- ¿Cada rata tiene algún identificador propio? ¿Arete, marca con plumón, tatuaje, número de jaula?
- ¿Ese identificador se anota en algún lado —bitácora, Excel— junto con el video?
- ¿Se puede saber, viendo un video, cuál rata es cuál más allá de su posición?

**Qué cambia según la respuesta:**

| Si la respuesta es… | Consecuencia en el modelo |
|---|---|
| **No hay identificador** — solo la posición | Se queda como está: la rata es una «entidad débil» que solo existe dentro de su tanda, y todo depende de que el encuadre no cambie |
| **Sí hay identificador** | La rata pasa a ser una entidad con identidad propia. El modelo mejora: deja de depender del encuadre, y se podría seguir a la misma rata entre experimentos distintos |

**La segunda opción es mejor**, así que vale la pena insistir en esta pregunta.

## P-02 · ¿Cómo le dicen ustedes a lo que llamamos «tanda»? 🟡

Ver la explicación completa en la sección 1.1. Se trata de adoptar el término del laboratorio en vez del que inventamos.

## P-03 · ¿El sistema usará número de boleta como identificador de usuario? 🟡

**Contexto.** Se decidió que cada usuario del sistema tenga un identificador único: el **número de boleta**.

**El problema.** En el IPN la boleta es de **estudiantes**. Los profesores e investigadores tienen **número de empleado**, no boleta. Y según la entrevista (P14), los usuarios del sistema serían *«máximo tres personas más el doctor»* — es decir, el Dr. Sandino **es usuario del sistema**.

**Qué preguntar:**
- ¿El doctor tiene número de boleta, o su identificador institucional es otro?
- ¿Los usuarios serán siempre tesistas y estudiantes, o también personal con nombramiento?

**Por qué importa:** si algunos usuarios no tienen boleta, el identificador no puede ser la boleta a secas. Habría que usar un identificador institucional más general, o una clave propia del sistema.

## P-04 · ¿Los experimentos son por semestre o por bimestre? 🟡

**Contexto.** En la grabación de la entrevista el doctor dice *«por bimestre se pueden realizar entre tres y cuatro experimentos independientes»*, pero cierra la cuenta con *«por semestre estaríamos hablando de entre 32 y 40 videos»*.

Las dos cifras solo cuadran si son **por semestre**: con «bimestre» saldrían más de 70 videos por semestre, que no coincide con lo que él mismo reportó.

**Qué preguntar:** ¿cuántos experimentos independientes se realizan por semestre? Probablemente fue un lapsus al hablar, pero conviene confirmarlo porque afecta la planeación de TT-II.

## P-05 · ¿Algún grupo experimental ha tenido más de 8 ratas? 🟡

**Por qué se pregunta.** Con 6–8 ratas por grupo y máximo 4 por encuadre, salen siempre **dos tandas por grupo**. Si algún grupo puede tener más de 8, serían tres o más tandas y el modelo tiene que admitirlo.

**Qué preguntar:** ¿el rango de 6 a 8 ratas por grupo es fijo, o alguna vez han trabajado con grupos más grandes?

## P-06 · ¿Cómo se crea una cuenta en el sistema? 🟡

**Por qué se pregunta.** El documento del TT se contradice a sí mismo:

| Fuente | Dice |
|---|---|
| Capítulo 1 | «registro de usuario **con aprobación del administrador**» → el usuario se registra solo y alguien aprueba |
| Capítulo 4 (RF-07) | «Solo el Administrador puede crear cuentas. **No existe formulario público de autoregistro**» |

**Qué preguntar:**
- ¿Prefiere que la gente se registre sola y usted (o alguien) apruebe, o que alguien cree las cuentas directamente?
- ¿Quién haría de administrador?

---

# 3 · Datos nuevos registrados

Decisiones y datos que llegaron después de la última versión del documento del TT y que todavía **no están escritos en el LaTeX**.

| Dato | Detalle | Estado |
|---|---|---|
| **Identificador de usuario** | Será un identificador único: `idBoleta` | Decidido por el equipo · ver P-03 |
| **Identificador de rata** | Se quiere que exista, pero falta definir cuál | Pendiente · ver P-01 |
| **Dispositivo de grabación** | Cámara **web**, no celular. El documento dice «cámara de celular» y está mal | Confirmado · corregir en cap. 3 y 4 |
| **Iluminación** | ~2,500 lúmenes es el estándar del laboratorio | Confirmado |
| **Acervo histórico** | Los 80–100 videos antiguos **quedan fuera** del sistema; solo se usan para entrenar el modelo | Confirmado |
| **Unidad del desglose** | En **segundos** | Confirmado |
| **Reanálisis** | Un video **sí** se puede volver a analizar | Confirmado |
| **El «otro equipo»** | Trabaja con ansiolíticos y laberinto T elevado — otro paradigma, no compite con el FST | Confirmado |

---

# 4 · Ya respondido — no volver a preguntar

Para no repetir preguntas que el doctor ya contestó.

| Tema | Respuesta | Fuente |
|---|---|---|
| Roles de usuario | Un solo rol de investigador, sin permisos diferenciados entre ellos | Entrevista P1 |
| Acceso a resultados | Todos los que tengan cuenta pueden ver todos los experimentos | Entrevista P18 |
| Usuarios simultáneos | Una persona a la vez; 4 usuarios posibles en el mismo periodo | Entrevista P14 |
| Formato de video | Siempre MP4 | Entrevista P5 |
| Duración de sesiones | 20 min el Día 1, 5 min el Día 2, 24 h de diferencia | Entrevista P4 |
| Qué se analiza del Día 1 | Solo los primeros 5 min, y solo del grupo control | Entrevista PC |
| Conductas | Tres: nado activo, inmovilidad y escalamiento. El buceo cuenta como nado | Entrevista P7 |
| Episodio válido | La conducta debe mantenerse de 3 a 5 segundos | Entrevista P6 |
| Concordancia aceptable | 85 % o más contra el analista humano | Entrevista P8 |
| Variabilidad humana actual | 15–20 % entre analistas | Transcripción informal |
| Tiempo de análisis manual | ~30 min por rata; ~2 h por video de 4 ratas; por triplicado | Entrevista P12 · transcripción |
| Grupos experimentales | 6–8 ratas por grupo, mínimo 3 grupos, promedio 4 | Entrevista PA · P19 |
| El grupo control | Sin placebo ni fármaco, solo nado forzado | Entrevista PB |
| Retención de videos | 30 días es suficiente | Entrevista P17 |
| Disponibilidad | 24/7 sería lo ideal | Entrevista P16 |
| Infraestructura | Preferentemente en la nube | Entrevista P15 |
| Estructura del CSV | Cabecera de tiempo + una columna por conducta, en segundos | Entrevista P10 |
| Comparación estadística | Por grupo: media, desviación estándar y varianza; luego grupo contra grupo | Entrevista P11 |
| Entrenamiento del modelo | Con clips cortos de conducta inequívoca, no con los reportes completos | Entrevista PD |
| Nombre del laboratorio | Laboratorio de Bioquímica Estructural, Sección de Posgrado, ENMyH-IPN | Entrevista PE |

---

# 5 · Compromisos pendientes del laboratorio

Cosas que el Dr. Sandino se comprometió a entregar y que conviene recordar en la reunión.

| Entregable | Estado |
|---|---|
| Reportes / análisis manuales de los videos ya compartidos | Pendiente — «estoy localizando los archivos de Excel» |
| Guía o manual de cómo identificar las conductas | Pendiente — mencionado en la reunión |
| Coordinar reunión conjunta con el otro equipo y el Dr. Israel Salas | Pendiente |
