# Guion de la defensa — TT 2026-B066

V: Vanesa · A: Ángel · §Lo que va en rojo son indicaciones de pantalla, no se dicen.§

### Diapositiva 1 — Portada

V: Buenos días. Somos Vanesa Rodríguez y Ángel Frausto. Presentamos el Trabajo Terminal II, número 2026-B066: *Prototipo de un sistema web de análisis conductual asistido por IA en un modelo de conducta depresiva en rata mediante nado forzado*. Nuestros directores son el Dr. Israel Salas Ramírez y la Dra. Martha Rosa Cordero López.

### Diapositiva 2 — Índice

V: Vamos a ver el contexto, los objetivos, qué cambió respecto al TT1 y por qué, el sistema, una demostración, el cumplimiento de los objetivos, las conclusiones y el trabajo futuro.

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

### Diapositiva 5 — Planteamiento del problema

V: Hoy este análisis se hace a mano: unos 30 minutos por espécimen, y unas 2 horas por cada video de cuatro especímenes.

V: Eso trae cuatro problemas. Primero, el costo de tiempo: limita cuántos experimentos se procesan por periodo. Segundo, la variabilidad entre evaluadores: dos analistas registran tiempos distintos en las transiciones entre conductas. Tercero, no hay un registro centralizado: los resultados quedan dispersos en hojas de cálculo y notas. Y cuarto, el análisis temporal es limitado: el desglose minuto a minuto es inviable a mano.

### Diapositiva 6 — Objetivo general

V: Nuestro objetivo general es diseñar, desarrollar y validar un prototipo de sistema web que automatice la detección y clasificación de las conductas de los especímenes en la prueba de nado forzado, con visión por computadora y aprendizaje supervisado.

V: Las conductas son nado activo, inmovilidad y escalamiento, y una cuarta, conducta activa, que se usa cuando el sistema no puede separar el nado del escalamiento.

### Diapositiva 7 — Objetivos específicos

V: Los tres primeros objetivos específicos se cubrieron en el TT1: revisar los trabajos y herramientas existentes, documentar el protocolo del laboratorio y diseñar la arquitectura conforme a la norma ISO/IEC/IEEE 12207.

A: Adicionando: los tres de este TT2 son implementar el módulo de análisis conductual con visión por computadora y un clasificador supervisado; evaluar el clasificador con precisión, recall y F1 por conducta sobre un conjunto de prueba independiente; y cuantificar la reducción de tiempo frente al proceso manual, dejando el clasificador modular.

### Diapositiva 8 — Qué cambió respecto al TT1

A: Respecto al TT1 casi todo se replanteó. La metodología y los objetivos no cambiaron; lo que cambió es cómo los cumplimos.

A: En la arquitectura pasamos de un backend en Flask con un pipeline de cinco módulos, con YOLOv8, ByteTrack y ResNet, a un backend en Spring Boot con Java 21 y un pipeline de tres etapas. Cambió porque el sistema detecta por sustracción de fondo, un espécimen por cilindro, así que ya no necesita seguimiento.

A: Los casos de uso pasaron de 24 a 25, y ahora están organizados por actor, con un flujo de tres etapas y una cola de análisis.

A: La base de datos la rehicimos con el método conceptual, lógico y físico; quedó en 12 tablas, normalizadas hasta la forma normal de Boyce-Codd. En el TT1 no habíamos entendido bien la prueba: asumimos que se comparaba el día 1 contra el día 2, y en realidad se comparan los grupos.

A: Los requisitos pasaron de 31 funcionales, 13 no funcionales y 13 reglas de negocio, a 33 funcionales, 14 no funcionales y 18 reglas de negocio.

A: La matriz de riesgos sigue con ocho riesgos; reescribimos el R-01, el R-02 y el R-03 al cambiar el pipeline y el clasificador.

A: Y el costo bajó de 56,500 a 53,655 pesos, porque el entrenamiento usa el nivel gratuito de Google Colab; a cambio se suma un mes de servidor para el desarrollo, de 455 pesos.

A: Cada uno de estos cambios lo vemos ahora en los diagramas.

### Diapositiva 9 — Modelo de datos: antes y después

A: A la izquierda está el modelo del TT1, con tablas por sujeto, animal, trabajo y región de interés. A la derecha, el del TT2: parte del experimento, que se divide en grupos, que son control, referencia y tratamiento. Cada grupo se divide en tandas de hasta cuatro especímenes, porque un video solo muestra cuatro cilindros. Son 12 tablas normalizadas.

### Diapositiva 10 — Arquitectura: antes y después

A: Antes teníamos Flask y un pipeline de cinco módulos. Ahora son cuatro contenedores Docker: la web con nginx y React, la API en Spring Boot, el worker en Python con PyTorch, y PostgreSQL. La API y el worker no se llaman entre sí: se comunican solo a través de la base de datos, que funciona como cola.

### Diapositiva 11 — Pipeline de análisis: antes y después

A: Ahora el pipeline tiene tres etapas. Primero, el preprocesamiento: comprueba que el video se abra, corrige la rotación y confirma que el modelo esté disponible. Después, localiza los cilindros. Y al final, clasifica la conducta.

A: Si el video no abre o no se encuentran los cilindros, el análisis termina en error y genera un reporte de diagnóstico. Si un espécimen no se ve tres segundos seguidos, el análisis queda en pausa, y el usuario tiene 72 horas para ajustar el recuadro del cilindro y continuar.

### Diapositiva 12 — Desarrollo: clasificador de conducta

V: Para cada segundo, la red recibe un clip de 16 fotogramas del cilindro y 22 medidas: 15 rasgos y 7 reglas de observación. Usamos una ventana de 4 segundos centrada en cada segundo, lo que permite detectar conductas de unos 2 segundos.

A: Adicionando: la red es una fusión de R(2+1)D-18 con una rama de medidas, y da tres salidas: nado, inmovilidad y escalamiento. La cuarta, conducta activa, no sale de la red: se asigna por una regla de 0.80, cuando nado más escalamiento suman al menos 0.80 y ninguna clase llega sola a ese umbral.

A: Las etiquetas son propias, hechas con el etiquetador del equipo y revisadas a mano. Entrenamos 15 épocas, con lotes de 16 clips, y validamos en 5 particiones agrupadas por video, para no inflar el resultado con segundos vecinos.

### Diapositiva 13 — Desarrollo: plataforma web

V: El backend está en Java 21 con Spring Boot: es una API REST con 12 entidades, sesión con JWT y roles, y genera el reporte en PDF. El frontend está en React con Vite: son 8 pantallas, desde el inicio de sesión hasta la administración, además de la revisión segundo a segundo.

A: Adicionando: el worker, en Python, toma un video a la vez de la cola en PostgreSQL, hace la pausa si no ve al espécimen y corre las tareas diarias. Todo va empaquetado con Docker Compose, un contenedor por servicio, con volúmenes para los videos y el modelo.

### Diapositiva 14 — Demostración

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

### Diapositiva 15 — Pruebas realizadas

§[Texto pendiente de escribir]§

### Diapositiva 16 — Se cumplió el objetivo general y los seis específicos

V: Con esto se cumplió el objetivo general y los seis específicos: revisamos las herramientas existentes, documentamos el protocolo del laboratorio, diseñamos la arquitectura conforme a la norma ISO/IEC/IEEE 12207, implementamos el análisis conductual y el clasificador, evaluamos el clasificador con precisión, recall y F1, y cuantificamos la reducción de tiempo dejando el clasificador modular.

### Diapositiva 17 — Conclusiones

A: Tenemos cuatro conclusiones. Primera: un prototipo completo, que va del video a los reportes en PDF, CSV y XLSX, con experimentos, grupos y tandas, análisis en segundo plano y revisión segundo a segundo. Segunda: un pipeline de tres etapas, que alinea, localiza los cilindros y clasifica, y que si falla entrega un reporte de diagnóstico. Tercera: un clasificador validado con precisión, recall y F1 por conducta sobre un conjunto de prueba independiente. Y cuarta: el alcance y los límites: solo nado forzado, con videos de un laboratorio y una calidad mínima, y como la red no es 100 % exacta, el usuario revisa y corrige.

A: El prototipo cumple el objetivo general: apoya al laboratorio, no diagnostica ni sustituye al investigador.

### Diapositiva 18 — Trabajo futuro

V: Como trabajo futuro proponemos entrenar el clasificador con otros protocolos, como el laberinto en cruz elevado o el campo abierto; ofrecer más resultados al laboratorio, como latencias, comparación estadística entre grupos y curvas de dosis-respuesta; hacer análisis en tiempo real con una cámara conectada; y mejorar el sistema, analizando también el día 1, permitiendo reentrenar desde la plataforma y ganando robustez ante reflejos y pelaje claro.

### Diapositivas 19, 20 y 21 — Referencias, gracias y preguntas

V: Muchas gracias. Agradecemos a nuestros directores, a los sinodales y al Dr. Sandino, nuestro usuario final, que nos dio la oportunidad de desarrollar un sistema con requerimientos reales. Quedamos atentos a sus preguntas.
