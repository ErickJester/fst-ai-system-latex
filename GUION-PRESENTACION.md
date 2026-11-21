### Diapositiva 1 — Portada

A: Imaginemos que por parte del IPN se desarrolla un antidepresivo tan efectivo como la fluoxetina, el más conocido del mercado. Pero para llegar a ese nivel, hay muchos pasos para tan siquiera llegar al consumo humano. Uno de los primeros son los modelos preclínicos.

V: Pero para dichos modelos preclínicos, se analiza por experimentos. Esto actualmente lo hace a mano el Laboratorio de Bioquímica Estructural de la ENMyH. Nuestro trabajo hace que esa etapa la haga un sistema y puedan avanzar más rápido y con un criterio consistente.

A: Buenas tardes a los sinodales, directores y presentes que nos acompañan. El día de hoy estaremos presentando el Trabajo Terminal II con número 2026-B066, que lleva por nombre *Prototipo de un sistema web de análisis conductual asistido por IA en un modelo de conducta depresiva en rata mediante nado forzado*. Mi nombre es Ángel Frausto Robles.

V: Mi nombre es Vanesa Rodríguez Verdín Sandoval. Nuestros directores son la Dra. Martha Rosa Cordero López y el Dr. Israel Salas Ramírez.

### Diapositiva 2 — Índice

V: Vamos a ver el contexto y los objetivos, la propuesta de solución, las herramientas utilizadas, el desarrollo del sistema, las pruebas realizadas, una demostración, el cumplimiento de los objetivos, las conclusiones y el trabajo futuro.

### Diapositiva 3 — Contexto

V: Vamos a empezar con el contexto, hablando sobre la prueba de nado forzado, por sus siglas en inglés FST (*Forced Swim Test*). Esta prueba, propuesta por Porsolt en 1977, es la más citada para evaluar antidepresivos antes de pasar a ensayos en humanos.

A: Adicionando: desde 1977 la prueba ha tenido modificaciones, y los protocolos varían de un laboratorio a otro. Además, analizar los videos sigue siendo trabajo manual. Por eso un criterio consistente y automático es lo que aporta nuestro trabajo.

V: Lo que se mide es qué hace cada espécimen: la inmovilidad refleja desesperanza conductual y se reduce con antidepresivos, y el nado activo y el escalamiento indican qué sistema neurotransmisor actúa.

### Diapositiva 4 — La prueba de nado forzado: qué se observa

V: Cada espécimen nada en un cilindro con agua del que no puede escapar, y observamos qué hace en cada segundo.

§[Abrir el video del Anexo A, con los cuatro especímenes a la vista]§

V: En el cilindro de la izquierda, el espécimen está en inmovilidad: flota y solo hace movimientos mínimos para mantener la cabeza fuera del agua.

V: Aquí otro está en nado activo: se mueve de forma horizontal, desplazándose por el cilindro.

V: Y aquí está en escalamiento: hace movimientos verticales enérgicos con las patas contra la pared del cilindro.

### Diapositiva 5 — Objetivo general

V: Nuestro objetivo general es diseñar, desarrollar y validar un prototipo de sistema web que automatice la clasificación de las conductas de los especímenes en la prueba de nado forzado, con visión por computadora y aprendizaje supervisado.

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

V: Para el aprendizaje supervisado, una red R(2+1)D-18 en PyTorch, fusionada con una rama de 22 medidas; y scikit-learn para las métricas de validación.

A: La plataforma web usa Spring Boot con Java 21 para la API, React con Vite para la interfaz y un worker en Python para el análisis. Los datos y la cola de análisis van en PostgreSQL, y todo se empaqueta con Docker Compose, un contenedor por servicio.

### Diapositiva 10 — Arquitectura de software por capas

V: El sistema se organiza en cuatro capas: presentación, lógica de negocio, procesamiento asíncrono y datos. La lógica de negocio valida los videos y encola el análisis.

A: El procesamiento analiza un video a la vez, y la capa de datos guarda todo en PostgreSQL y en dos volúmenes: uno con los videos y los reportes y otro, de solo lectura, con el modelo.

### Diapositiva 11 — Arquitectura en contenedores Docker

V: Esas capas se empaquetan en cuatro contenedores: web, API, worker y base de datos.

A: La API y el worker no se llaman entre sí: se comunican solo a través de la base de datos, que funciona como cola. Los videos y los reportes viven en un volumen compartido, el modelo en uno de solo lectura, y una cuenta de correo sirve para los avisos.

### Diapositiva 12 — Diagrama de flujo del sistema

A: Este es el flujo completo. El investigador sube el video y el backend lo valida y lo guarda; el del día 1 solo se guarda, y el del día 2 queda en cola. El worker toma el más antiguo, un video a la vez, y corre el pipeline: preprocesamiento, cilindros y clasificación.

V: Al terminar se guardan la conducta de cada segundo, los tiempos por minuto y una copia para revisión. El investigador revisa, los totales se recalculan, y puede descargar los reportes. Arriba, fuera del flujo por video, está el entrenamiento: el equipo revisa las conductas, entrena con los segundos etiquetados y evalúa el modelo.

A: Hay dos caminos alternos. Si el video no abre o no se encuentran los cilindros, el análisis termina en error y se genera un reporte de diagnóstico, y el worker sigue con el siguiente. Y si un espécimen no se ve tres segundos seguidos, el análisis queda en pausa: el usuario tiene 72 horas para ajustar el recuadro del cilindro y continuar, o cancelar. Si el worker se apaga a media tarea, el análisis vuelve a la cola.

### Diapositiva 13 — Desarrollo: clasificador de conducta

V: Para cada segundo, la red recibe un clip de 16 fotogramas del cilindro y 22 medidas: 15 rasgos y 7 reglas de observación. Usamos una ventana de 4 segundos centrada en cada segundo, que se desliza de uno en uno, lo que permite detectar conductas de unos 2 segundos.

A: La red da tres salidas: nado, inmovilidad y escalamiento. La cuarta, conducta activa, no sale de la red: una regla de 0.80 la asigna cuando nado más escalamiento suman al menos 0.80 y ninguna clase llega sola a ese umbral.

A: Las etiquetas son propias, hechas con el etiquetador del equipo y revisadas a mano. Entrenamos 15 épocas, con lotes de 16 clips, y validamos en 5 particiones agrupadas por video, para no inflar el resultado con segundos vecinos.

### Diapositiva 14 — Pruebas realizadas

V: Validamos el clasificador por video, en cinco particiones: los videos de prueba de cada partición no participan en el entrenamiento. Son 11 videos, 25 especímenes y 8,248 segundos etiquetados por el equipo.

A: El F1, que combina precisión y recall, fue de 0.732 para nado, 0.719 para inmovilidad y 0.663 para escalamiento, con un promedio de 0.705, y una exactitud de 71.6 % por segundo. Responder siempre «nado» acertaría 47.8 %.

V: Del sistema corrimos 77 pruebas automáticas contra PostgreSQL real, y las 77 pasan. En la prueba de carga con cuatro sesiones hubo 1,474 peticiones, ningún error y un percentil 95 de 0.041 segundos, contra el límite de 3.

A: Y en tiempos: a mano, un video toma unas 2 horas; con el sistema, un video de 5 minutos con cuatro especímenes se analizó en unos 9 minutos, sin que nadie interviniera.

### Diapositiva 15 — Demostración

V: Ahora les mostramos el sistema funcionando.

§[Pantalla 1: iniciar sesión]§

V: Al entrar, el usuario puede ver el aviso de privacidad y los términos y condiciones. Las cuentas las crea el administrador con una contraseña temporal, y en el primer acceso el sistema obliga a cambiarla.

§[Pantalla 2: crear experimento y subir video]§

V: Un experimento tiene grupos: control, referencia y tratamiento, y el nombre del grupo es libre. Cada grupo se divide en tandas de hasta cuatro especímenes. El video del día 1 solo se guarda; el análisis es del día 2. El control recibe placebo, para que todos los grupos tengan el mismo estrés de inyección.

§[Pantalla 3: seguir el progreso]§

A: El análisis corre en segundo plano, en cola: el primero que llega es el primero que se procesa. Mientras tanto se puede seguir usando el sistema, y la pantalla muestra el porcentaje y la etapa en la que va cada análisis.

§[Pantalla 4: notificaciones]§

A: Cuando un análisis termina, queda en pausa o se detiene por error, el sistema avisa en el panel de notificaciones de la barra superior y también por correo.

V: El panel se actualiza al entrar a cada pantalla y cada 30 segundos, indica cuántas notificaciones no se han leído, y permite marcar una como leída o como no leída, o todas como leídas. Si el correo falla, el aviso se queda en el panel.

§[Pantalla 5: ver resultados]§

A: Aquí vemos los resultados por espécimen, por minuto y por grupo: media, desviación estándar y varianza, en tablas.

V: Debajo hay una galería de seis gráficas, con un selector para elegir la conducta. La primera muestra el promedio de cada grupo con su desviación estándar y cada espécimen como un punto; se puede ver en barras y en segundos, en minutos y segundos, o como porcentaje del tiempo. Las otras son la curva por minuto, las barras por minuto, el reparto de la duración, la variabilidad entre especímenes y el mapa por minuto.

A: Cada gráfica tiene su tabla de números y se puede descargar como imagen. Además, el resumen del experimento compara la conducta que elijamos de cada grupo contra el grupo de referencia, que por omisión es el control, con promedios, diferencias y una frase en palabras. No hace pruebas estadísticas.

§[Pantalla 6: revisar segundo a segundo]§

A: Esta es la revisión segundo a segundo, y solo se puede revisar un análisis completado. Se reproduce la copia del video, junto con una línea de tiempo por espécimen: cada cuadro es un segundo.

V: Cada segundo queda marcado con su origen: de la máquina, confirmado, corregido o dudoso. Si el sistema se equivocó, el investigador corrige la conducta y guarda; los totales por minuto y el nivel del análisis se recalculan, y el segundo conserva que fue revisado. Si hace falta, también puede reiniciar el análisis.

§[Pantalla 7: descargar reporte]§

V: El reporte se descarga en PDF, CSV o XLSX. Los reportes se conservan, y el video se borra automáticamente a los 30 días.

§[Pantalla 8: administración]§

V: Por último, el panel de administración, que solo ve el administrador. Lista las cuentas con su correo, su rol, su estado y el número de experimentos, y se puede filtrar por rol y por estado.

A: Desde ahí crea cuentas nuevas: el sistema genera una contraseña temporal, que se muestra una sola vez y se envía por correo. También puede cambiar el estado o el rol de una cuenta, o generar otra contraseña temporal. El sistema nunca borra cuentas.

V: El panel muestra además el estado del sistema: el uso del disco y el espacio disponible, el tamaño de la cola, los análisis activos y el tiempo estimado para vaciarla, y avisa cuando el disco pasa del 80 %. El administrador también puede ver y gestionar los experimentos de todos los investigadores.

### Diapositiva 16 — Se cumplió el objetivo general y los seis específicos

V: Con esto se cumplió el objetivo general y los seis específicos.

A: La arquitectura la vimos en las capas y los contenedores, y la evaluación y la reducción de tiempo, en las pruebas.

### Diapositiva 17 — Conclusiones

A: Tenemos cuatro conclusiones. Primera: un prototipo completo, que va del video a los reportes, con análisis en segundo plano y revisión segundo a segundo. Segunda: un pipeline que alinea, localiza los cilindros y clasifica, y que si falla entrega un reporte de diagnóstico. Tercera: un clasificador validado con precisión, recall y F1 por conducta sobre un conjunto de prueba independiente. Y cuarta: el alcance y los límites: solo nado forzado, con videos de un laboratorio y una calidad mínima, y como la red no es 100 % exacta, el usuario revisa y corrige.

A: El prototipo cumple el objetivo general: apoya al laboratorio, no diagnostica ni sustituye al investigador. Su valor está en el criterio consistente y el registro centralizado.

### Diapositiva 18 — Trabajo futuro

V: Como trabajo futuro proponemos entrenar el clasificador con otros protocolos, como el laberinto en cruz elevado o el campo abierto; ofrecer más resultados al laboratorio, como latencias, comparación estadística entre grupos y curvas de dosis-respuesta; hacer análisis en tiempo real con una cámara conectada; y mejorar el sistema, analizando también el día 1, permitiendo reentrenar desde la plataforma y ganando robustez ante reflejos y pelaje claro.

### Diapositivas 19, 20 y 21 — Referencias, gracias y preguntas

V: Muchas gracias. Agradecemos a nuestros directores, a los sinodales y al Dr. Sandino, nuestro usuario final, que nos dio la oportunidad de desarrollar un sistema con requerimientos reales. Quedamos atentos a sus preguntas.
