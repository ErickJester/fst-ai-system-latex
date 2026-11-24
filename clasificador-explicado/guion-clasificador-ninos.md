# Guion del video: el clasificador explicado para niños

Voz: Microsoft Sabina (es-MX), velocidad lenta. Los tiempos son del MP4.

## 1. ¿Qué queremos que haga la computadora?  (0:00)

- **0:00** Hola. Hoy vamos a enseñarle a una computadora a mirar un video y decir qué está haciendo un espécimen, un animalito de laboratorio.
- **0:11** Lo ponemos en un cilindro con agua y lo grabamos. En cada segundo del video, hace una de tres cosas.
- **0:20** Puede nadar.
- **0:22** Puede quedarse quieto, flotando. A eso le decimos inmovilidad.
- **0:29** O puede trepar por la pared. A eso le decimos escalamiento.
- **0:35** Revisar horas de video, segundo por segundo, cansa mucho a una persona. Por eso queremos que la computadora lo haga y nos avise.

## 2. Aprender con ejemplos  (0:46)

- **0:47** ¿Cómo aprendiste lo que es una manzana y lo que es un plátano? Alguien te mostró muchos ejemplos y te dijo el nombre de cada uno.
- **0:57** Con muchos ejemplos aprendiste a reconocerlos tú solo. Ahora, cuando ves una fruta nueva, ya sabes cuál es.
- **1:07** A esto se le llama aprendizaje supervisado: aprender con ejemplos que ya traen su respuesta. A la respuesta la llamamos etiqueta.
- **1:17** Aquí, cada ejemplo es un clip de video de un segundo. Y la etiqueta la puso el equipo, a mano: nadó, estuvo quieto o trepó.
- **1:29** Así la computadora aprende con unos ocho mil segundos de ejemplos, todos con su etiqueta.

## 3. Lo que ve la computadora: un clip  (1:37)

- **1:37** Para decidir qué pasa en un segundo, la computadora no mira una sola foto. Mira un pedacito de video.
- **1:47** Toma 16 fotos de una ventana de 4 segundos, alrededor del segundo que quiere decidir.
- **1:54** ¿Por qué tantas? Porque en una sola foto no se sabe si el espécimen flota o nada despacio. Para saberlo, hay que ver cómo cambia.
- **2:06** Y la ventana avanza de un segundo en un segundo. Así, cada segundo tiene su propia decisión.

## 4. R(2+1)D-18: la red que mira el video  (2:15)

- **2:16** Ahora, ¿quién mira ese clip? Una red neuronal. Imagínala como una fila de detectores pequeños, puestos capa tras capa.
- **2:27** Los primeros detectan cosas simples, como bordes y manchas. Los siguientes juntan eso para reconocer partes del cuerpo, y después movimientos.
- **2:39** La nuestra se llama R(2+1)D-18. Suena complicado, pero son tres ideas.
- **2:50** Primera idea: el 2 + 1. Primero mira cada foto sola, para ver la forma: son 2 dimensiones. Después mira cómo cambia de una foto a otra, el tiempo: es 1 dimensión.
- **3:06** Segunda idea: el 18 es el número de capas que aprenden.
- **3:11** Tercera idea: viene preentrenada. Antes de conocer a nuestro espécimen, ya vio muchísimos videos de personas haciendo 400 actividades distintas. Esa colección se llama Kinetics.
- **3:27** Así ya sabe algo de movimiento, como quien ya sabe leer y solo aprende un idioma nuevo.
- **3:34** Al final, la red entrega 512 números. ¿Qué son? Eso es lo más importante, y lo vemos en la siguiente parte.

## 5. Las pistas: ¿qué son esos 512 números?  (3:46)

- **3:47** Piensa en la red como 512 inspectores. Cada inspector mira el clip, y cada uno está pendiente de un patrón distinto de forma y de movimiento.
- **3:59** Cada inspector contesta con un número: cuánto vio de lo suyo. Un número alto significa: lo vi mucho. Uno bajo: casi no lo vi.
- **4:11** Esos 512 números juntos son las pistas. Es como una ficha con 512 casillas, y cada casilla dice cuánto hay de un patrón en el clip.
- **4:23** Nadie les puso nombre a los inspectores. La red los descubrió sola, viendo primero los videos de Kinetics y después los nuestros. Por eso no sabemos decir qué mira cada uno.
- **4:38** Pero sirven: dos clips de nado dan fichas parecidas, y un clip de inmovilidad da una ficha distinta. Con eso la red puede decidir.

## 6. Las medidas: la libreta del detective  (4:49)

- **4:50** Pero la red de video no está sola. Hay una segunda fuente de pistas, que funciona muy distinto: las medidas.
- **5:00** Son 22 números que se calculan con reglas, como si midiéramos con una regla y un cronómetro.
- **5:08** Quince son rasgos del espécimen: cuánto se mueve su cuerpo, qué tan vertical está, y qué camino recorre.
- **5:17** Siete son reglas de observación: cuánto patalea con las patas de atrás y con las de adelante, y si se mueve la nariz justo arriba de la línea del agua. Un movimiento brusco de nariz apunta a trepar.
- **5:31** Las distancias se miden en largos de cuerpo, no en píxeles. Así, un video grabado más cerca o más lejos da números comparables.
- **5:42** Fíjate en la diferencia. Las pistas de la red las descubrió la red sola y no tienen nombre. Las medidas las diseñamos nosotros: cada una tiene nombre y mide solo el cuerpo del espécimen.

## 7. La fusión: juntar dos fuentes de pistas  (5:58)

- **5:59** Ya tenemos dos listas de pistas: las 512 de la red de video y las 22 medidas.
- **6:06** ¿Por qué usar las dos? Porque ven cosas distintas. La red de video mira todo el clip y descubre patrones que a nosotros no se nos ocurrirían, pero puede fijarse en cosas que no son el espécimen, como el fondo o la luz.
- **6:23** Las medidas se calculan solo sobre el cuerpo del espécimen y miden justo lo que un experto observa, como el pataleo y la nariz. Pero son pocas, y no lo ven todo.
- **6:36** Por eso se fusionan: se juntan las dos listas para decidir con las dos a la vez.
- **6:43** Primero se limpian las medidas: si falta una, se rellena con un valor típico, y todas se ponen en la misma escala, para que ninguna pese más solo por tener números más grandes.
- **6:57** Luego una red pequeña mezcla las 22 medidas y las convierte en 64 pistas nuevas. Cada una puede combinar varias medidas, por ejemplo: patalea fuerte y de golpe.
- **7:11** Ahora se pegan las dos listas: 512 más 64 son 576 pistas, una sola ficha.
- **7:21** Mientras entrena, se apagan algunas pistas al azar, a propósito. Se llama dropout, y evita que la red dependa de una sola pista.
- **7:33** La capa final es como un jurado. Cada pista tiene un peso: cuánto empuja hacia nado, hacia quieto o hacia trepa. El jurado suma los empujes y da un puntaje a cada opción.
- **7:47** Esos pesos son las perillas que se ajustan al entrenar. Así la red aprende cuánto confiar en cada pista, tanto en las del video como en las de las medidas.
- **7:59** Un ejemplo inventado: el video duda entre nado y quieto. Pero las medidas dicen que el pataleo es suave y que la nariz no se movió. Al juntar todo, el jurado se inclina por quieto.
- **8:14** Eso es la fusión: dos fuentes distintas de pistas, y una sola decisión.

## 8. Cómo aprende: el ciclo de entrenamiento  (8:21)

- **8:22** Al empezar, la red no sabe nada. Tiene millones de perillas, llamadas pesos, puestas en cualquier posición.
- **8:32** Entrenar es girar esas perillas poco a poco. Se hace con un ciclo de cuatro pasos.
- **8:39** Uno: la red recibe un lote de 16 clips, cada uno con sus medidas.
- **8:46** Dos: adivina. Para cada clip da sus tres probabilidades.
- **8:53** Tres: compara con la etiqueta, que es la respuesta del equipo. La diferencia es el error, que en el código se llama pérdida.
- **9:03** Cuatro: hacia atrás, calcula qué perillas tuvieron la culpa y mueve cada una un poquito para equivocarse menos.
- **9:12** Y se repite con el siguiente lote, una y otra vez.

## 9. Las épocas: repasar muchas veces  (9:18)

- **9:19** Cuando la red ya vio todos los clips de entrenamiento una vez, se completó una época. Es como leer el libro entero una vez.
- **9:29** Una lectura no basta. Nuestra red hace 15 épocas: repasa los mismos ejemplos 15 veces, y cada vez se equivoca un poco menos.
- **9:41** En esta gráfica, que es una ilustración, abajo están las épocas y arriba el error. Empieza alto y baja con cada repaso.
- **9:51** Y mira la respuesta para un mismo clip que de verdad es de nado: en la primera época duda, y en la última está mucho más segura.
- **10:01** Entre una época y otra los clips cambian un poco: más brillo, más oscuros, volteados o movidos. Así la red no se aprende de memoria un video.
- **10:13** También cambia el tamaño del paso: empieza chico, crece, y al final vuelve a ser muy chico para afinar.
- **10:22** Y las piezas nuevas aprenden diez veces más rápido que la red preentrenada, porque ellas empiezan de cero.
- **10:30** Además, como hay más segundos de nado que de escalamiento, se da un poco más de peso a los ejemplos raros, para que no se olviden.

## 10. El examen justo: probar con videos nuevos  (10:41)

- **10:42** ¿Cómo sabemos si aprendió bien? Con un examen. Pero debe ser un examen justo: no vale preguntar lo mismo que ya se vio en clase.
- **10:53** Tenemos 11 videos. Se hacen 5 grupos: la red se entrena con los demás y se examina con videos que nunca vio. Se repite 5 veces, cambiando los videos del examen.
- **11:08** ¿Por qué por video y no por segundo? Porque los segundos vecinos se parecen casi igual: comparten el 75 por ciento del clip. Sería como repetir la misma pregunta con otra letra.
- **11:23** Resultado: la red acierta en 7 de cada 10 segundos, el 71.6 por ciento. Contestar siempre nado acertaría 48 de cada 100.
- **11:36** No es perfecto: se confunde sobre todo entre nado e inmovilidad. Nuestra meta era sacar 85 en F1, una calificación que mezcla aciertos y errores. Vamos en 70, y todavía falta mejorar.

## 11. La decisión final de cada segundo  (11:54)

- **11:55** Falta un último paso: decidir la conducta de cada segundo. La red da tres probabilidades.
- **12:04** Regla uno: si una llega a 80 por ciento, gana. Es como pedir que alguien esté bastante seguro antes de contestar.
- **12:14** Regla dos: si ninguna llega, pero nado y escalamiento juntos suman 80, el sistema dice: está activo, pero no sé si nadó o trepó. Eso es conducta activa.
- **12:28** Regla tres: si tampoco, gana la más probable.

## 12. Todo junto  (12:34)

- **12:35** Resumamos. Un clip de 16 fotos entra a la red R(2+1)D-18, que entrega 512 pistas. Las 22 medidas entregan 64. Se fusionan en 576, y la capa final da tres probabilidades.
- **12:57** Para aprender, la red adivina, mide su error y mueve las perillas, lote tras lote, durante 15 épocas.
- **13:06** Se examina con videos que nunca vio, y acierta 7 de cada 10 segundos. Gracias por mirar.

Duración total: 13:16
