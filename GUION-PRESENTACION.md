### Diapositiva 1 — Portada

A: Imaginemos que por parte del IPN se desarrolla un antidepresivo tan efectivo como la fluoxetina, el más conocido del mercado. Pero para llegar a ese nivel, hay muchos pasos para tan siquiera llegar al consumo humano. Uno de los primeros son los modelos preclínicos.

V: Pero para dichos modelos preclínicos, se analiza por experimentos. Esto actualmente lo hace a mano el Laboratorio de Bioquímica Estructural de la ENMyH. Nuestro trabajo hace que esa etapa la haga un sistema y puedan avanzar más rápido y con un criterio consistente.

A: Buenos días. Somos Ángel Frausto y Vanesa Rodríguez. Presentamos el Trabajo Terminal II, número 2026-B066: *Prototipo de un sistema web de análisis conductual asistido por IA en un modelo de conducta depresiva en rata mediante nado forzado*. Nuestros directores son la Dra. Martha Rosa Cordero López y el Dr. Israel Salas Ramírez.

### Diapositiva 2 — Índice

V: Vamos a ver el contexto y los objetivos, la propuesta de solución, las herramientas utilizadas, el desarrollo del sistema, las pruebas realizadas, una demostración, el cumplimiento de los objetivos, las conclusiones y el trabajo futuro.

### Diapositiva 3 — Contexto

V: La prueba de nado forzado, propuesta por Porsolt en 1977, es la más citada para evaluar antidepresivos antes de pasar a ensayos en humanos. Hay más de 8,000 artículos que la reportan desde el año 2000.

V: Lo que se mide es qué hace cada espécimen. La inmovilidad refleja desesperanza conductual y se reduce con antidepresivos. El nado activo y el escalamiento indican qué sistema neurotransmisor actúa.

V: Este trabajo lo hicimos con el Laboratorio de Bioquímica Estructural, Sección de Posgrado, de la ENMyH del IPN.

### Diapositiva 4 — La prueba de nado forzado: qué se observa

V: Cada espécimen nada en un cilindro con agua del que no puede escapar, y observamos qué hace en cada segundo.

§[Abrir el video del Anexo A, con los cuatro especímenes a la vista]§

V: En el cilindro de la izquierda, el espécimen está en inmovilidad: flota y solo hace movimientos mínimos para mantener la cabeza fuera del agua.

V: Aquí otro está en nado activo: se mueve de forma horizontal, desplazándose por el cilindro.

V: Y aquí está en escalamiento: hace movimientos verticales enérgicos con las patas contra la pared del cilindro.

### Diapositiva 5 — Objetivo general

V: Nuestro objetivo general es diseñar, desarrollar y validar un prototipo de sistema web que automatice la clasificación de las conductas de los especímenes en la prueba de nado forzado, con visión por computadora y aprendizaje supervisado.

V: Las conductas son nado activo, inmovilidad y escalamiento, y una cuarta, conducta activa, que se usa cuando el sistema no puede separar el nado del escalamiento.

### Diapositiva 6 — Objetivos específicos

V: Los tres primeros objetivos específicos son revisar los trabajos y herramientas existentes, documentar el protocolo del laboratorio y diseñar la arquitectura del sistema.

A: Los otros tres son implementar el módulo de análisis conductual con visión por computadora y un clasificador supervisado; evaluar el clasificador con precisión, recall y F1 por conducta sobre un conjunto de prueba independiente; y cuantificar la reducción de tiempo frente al proceso manual, dejando el clasificador modular.

### Diapositiva 7 — Planteamiento del problema

V: Hoy este análisis se hace a mano: unos 30 minutos por espécimen, y unas 2 horas por cada video de cuatro especímenes.

V: Eso trae cuatro problemas. Primero, el costo de tiempo: limita cuántos experimentos se procesan por periodo. Segundo, la variabilidad entre evaluadores: dos analistas registran tiempos distintos en las transiciones entre conductas. Tercero, no hay un registro centralizado: los resultados quedan dispersos en hojas de cálculo y notas. Y cuarto, el análisis temporal es limitado: el desglose minuto a minuto es inviable a mano.

### Diapositiva 8 — Propuesta de solución

A: Nuestra propuesta es sencilla: el investigador sube el video desde el navegador, el análisis arranca solo al terminar la carga, y se genera un reporte con los tiempos por conducta, espécimen, sesión y minuto.

V: Para eso hay dos partes. Una cadena de análisis de video, que identifica a cada espécimen en su cilindro y clasifica su conducta cada segundo. Y una plataforma web, para cargar los videos, seguir el análisis, ver los resultados, comparar entre grupos y descargar los reportes, con todo guardado en una base de datos.

### Diapositiva 9 — Herramientas utilizadas

A: Para la visión por computadora usamos OpenCV, que lee, alinea y preprocesa el video, y una sustracción de fondo por percentil para localizar al espécimen en cada cilindro.

V: Para el aprendizaje supervisado, una red R(2+1)D-18 en PyTorch, fusionada con una rama de 22 medidas; un modelo de scikit-learn sobre los rasgos, y un etiquetador propio del equipo.

A: La plataforma web usa Spring Boot con Java 21 para la API, React con Vite para la interfaz y un worker en Python para el análisis. Los datos y la cola de análisis van en PostgreSQL, y todo se empaqueta con Docker Compose, un contenedor por servicio.

### Diapositiva 10 — Arquitectura de software por capas

V: El sistema se organiza en cuatro capas. La de presentación es la interfaz en React. La de lógica de negocio es la API en Spring Boot, que valida los videos y encola el análisis.

A: La de procesamiento asíncrono es el worker en Python, que analiza un video a la vez. Y la capa de datos es PostgreSQL, más un volumen con los videos y los reportes y otro, de solo lectura, con el modelo.

### Diapositiva 11 — Arquitectura en contenedores Docker

V: Esas capas se empaquetan en cuatro contenedores: la web con nginx y React, la API en Spring Boot, el worker en Python con PyTorch, y PostgreSQL.

A: La API y el worker no se llaman entre sí: se comunican solo a través de la base de datos, que funciona como cola. Los videos y los reportes viven en un volumen compartido, el modelo en uno de solo lectura, y una cuenta de correo sirve para los avisos.

### Diapositiva 12 — Diagrama de flujo del sistema

A: Este es el flujo completo. El investigador sube el video, y el backend valida el formato y lo guarda. El video del día 1 solo se guarda; el del día 2 queda en cola. El worker toma el más antiguo, un video a la vez, y corre el pipeline: preprocesamiento, cilindros y clasificación.

V: Si todo sale bien, se guardan la conducta de cada segundo, los tiempos por minuto y una copia para revisión. El investigador revisa cada segundo, los totales se recalculan, y puede reiniciar el análisis o descargar los reportes en PDF, CSV o XLSX. Si algo falla, el análisis queda en error y se genera un diagnóstico, y el worker sigue con el siguiente.

V: Arriba, fuera del flujo por video, está el entrenamiento: el equipo revisa las conductas, entrena con los segundos etiquetados y evalúa el modelo.

### Diapositiva 13 — Diagrama de flujo del pipeline de análisis

A: El pipeline tiene tres etapas. Primero, el preprocesamiento: comprueba que el video se abra y lee su ancho, alto y duración. Después, la localización de los cilindros: alinea la cámara, construye el fondo, ubica la línea de agua y el suelo, separa los cilindros y mide al espécimen en cada uno.

V: Al final, la clasificación: mide 15 rasgos y 7 reglas de observación, arma un clip de 4 segundos alrededor de cada segundo, la red da tres salidas y una regla con umbral de 0.80 asigna la conducta.

V: Si el video no abre o no se encuentran los cilindros, el análisis termina en error y genera un reporte de diagnóstico. Si un espécimen no se ve tres segundos seguidos, el análisis queda en pausa, y el usuario tiene 72 horas para ajustar el recuadro del cilindro y continuar.

### Diapositiva 14 — Estados de un análisis

A: Un análisis entra en cola cuando se valida el video. Cuando el worker lo toma pasa a procesando, con sus etapas de preprocesamiento, cilindros y clasificación, y al terminar queda completado.

V: Si no se puede abrir el video o no se hallan los cilindros, pasa a error. Si no se ve al espécimen durante tres segundos seguidos, queda en pausa: el usuario ajusta o confirma el recuadro y vuelve a la cola, o cancela, o pasan 72 horas y se cancela.

A: Si el worker se apaga a media tarea, el análisis vuelve a la cola, y un análisis completado se puede reiniciar.

### Diapositiva 15 — Desarrollo: clasificador de conducta

V: Para cada segundo, la red recibe un clip de 16 fotogramas del cilindro y 22 medidas: 15 rasgos y 7 reglas de observación. Usamos una ventana de 4 segundos centrada en cada segundo, lo que permite detectar conductas de unos 2 segundos.

A: Adicionando: la red es una fusión de R(2+1)D-18 con una rama de medidas, y da tres salidas: nado, inmovilidad y escalamiento. La cuarta, conducta activa, no sale de la red: se asigna por una regla de 0.80, cuando nado más escalamiento suman al menos 0.80 y ninguna clase llega sola a ese umbral.

A: Las etiquetas son propias, hechas con el etiquetador del equipo y revisadas a mano. Entrenamos 15 épocas, con lotes de 16 clips, y validamos en 5 particiones agrupadas por video, para no inflar el resultado con segundos vecinos.

### Diapositiva 16 — Desarrollo: plataforma web

V: El backend está en Java 21 con Spring Boot: es una API REST con 12 entidades, sesión con JWT y roles, y genera el reporte en PDF. El frontend está en React con Vite: son 8 pantallas, desde el inicio de sesión hasta la administración, además de la revisión segundo a segundo.

A: Adicionando: el worker, en Python, toma un video a la vez de la cola en PostgreSQL, hace la pausa si no ve al espécimen y corre las tareas diarias. Todo va empaquetado con Docker Compose, un contenedor por servicio, con volúmenes para los videos y el modelo.

### Diapositiva 17 — Pruebas realizadas

V: Validamos el clasificador por video, en cinco particiones: los videos de prueba de cada partición no participan en el entrenamiento. Son 11 videos, 25 especímenes y 8,248 segundos etiquetados por el equipo.

A: El F1 por conducta fue de 0.732 para nado, 0.719 para inmovilidad y 0.663 para escalamiento, con un promedio de 0.705, y una exactitud de 71.6 % por segundo. Responder siempre «nado» acertaría 47.8 %.

V: Del sistema corrimos 77 pruebas automáticas contra PostgreSQL real, y las 77 pasan. En la prueba de carga con cuatro sesiones hubo 1,474 peticiones, ningún error y un percentil 95 de 0.041 segundos, contra el límite de 3.

A: Y en tiempos: anotar a mano toma 30 minutos por espécimen y unas 2 horas por video. Con el sistema, un video de 5 minutos con cuatro especímenes se analizó en unos 9 minutos, sin que nadie interviniera.

### Diapositiva 18 — Demostración

V: Ahora les mostramos el sistema funcionando.

§[Pantalla 1: iniciar sesión]§

V: Al entrar, el usuario puede ver el aviso de privacidad y los términos y condiciones. Las cuentas las crea el administrador con una contraseña temporal, y en el primer acceso el sistema obliga a cambiarla.

§[Pantalla 2: crear experimento y subir video]§

V: Un experimento tiene grupos: control, referencia y tratamiento, y el nombre del grupo es libre. Cada grupo se divide en tandas de hasta cuatro especímenes. El video del día 1 solo se guarda; el análisis es del día 2. El control recibe placebo, para que todos los grupos tengan el mismo estrés de inyección.

§[Pantalla 3: seguir el progreso]§

A: El análisis corre en segundo plano, en cola: el primero que llega es el primero que se procesa. Mientras tanto se puede seguir usando el sistema.

§[Pantalla 4: ver resultados]§

A: Aquí vemos los resultados por espécimen, por minuto y por grupo: media, desviación estándar y varianza, con gráficas por conducta.

§[Pantalla 5: revisar segundo a segundo]§

A: Cada cuadro es un segundo. Si el sistema se equivocó, el investigador corrige la etiqueta y guarda; los totales por minuto se recalculan.

§[Pantalla 6: descargar reporte]§

V: El reporte se descarga en PDF, CSV o XLSX. Los reportes se conservan, y el video se borra automáticamente a los 30 días.

### Diapositiva 19 — Se cumplió el objetivo general y los seis específicos

V: Con esto se cumplió el objetivo general y los seis específicos: revisamos las herramientas existentes, documentamos el protocolo del laboratorio, diseñamos la arquitectura del sistema, implementamos el análisis conductual y el clasificador, evaluamos el clasificador con precisión, recall y F1, y cuantificamos la reducción de tiempo dejando el clasificador modular.

### Diapositiva 20 — Conclusiones

A: Tenemos cuatro conclusiones. Primera: un prototipo completo, que va del video a los reportes en PDF, CSV y XLSX, con experimentos, grupos y tandas, análisis en segundo plano y revisión segundo a segundo. Segunda: un pipeline de tres etapas, que alinea, localiza los cilindros y clasifica, y que si falla entrega un reporte de diagnóstico. Tercera: un clasificador validado con precisión, recall y F1 por conducta sobre un conjunto de prueba independiente. Y cuarta: el alcance y los límites: solo nado forzado, con videos de un laboratorio y una calidad mínima, y como la red no es 100 % exacta, el usuario revisa y corrige.

A: El prototipo cumple el objetivo general: apoya al laboratorio, no diagnostica ni sustituye al investigador.

### Diapositiva 21 — Trabajo futuro

V: Como trabajo futuro proponemos entrenar el clasificador con otros protocolos, como el laberinto en cruz elevado o el campo abierto; ofrecer más resultados al laboratorio, como latencias, comparación estadística entre grupos y curvas de dosis-respuesta; hacer análisis en tiempo real con una cámara conectada; y mejorar el sistema, analizando también el día 1, permitiendo reentrenar desde la plataforma y ganando robustez ante reflejos y pelaje claro.

### Diapositivas 22, 23 y 24 — Referencias, gracias y preguntas

V: Muchas gracias. Agradecemos a nuestros directores, a los sinodales y al Dr. Sandino, nuestro usuario final, que nos dio la oportunidad de desarrollar un sistema con requerimientos reales. Quedamos atentos a sus preguntas.
