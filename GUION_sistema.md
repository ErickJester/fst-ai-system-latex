# Guion hablado: presentación del sistema (una persona)

Duración: 15 minutos a 170 palabras por minuto. Diapositivas 8 a 12 de `TT2_presentacion_estructura.pptx`.
Solo lo que está en cursiva entre corchetes no se dice: son las indicaciones de cambio de lámina.

---

*[Diapositiva 8]*

Buenos días. Voy a presentar el sistema que construimos para este trabajo terminal: un sitio web que recibe el video de una prueba de nado forzado y entrega, segundo a segundo, la conducta que tuvo cada espécimen. Quiero que al final de esta presentación queden claras cuatro cosas. Primero, cómo está armado el sistema por dentro. Segundo, cómo analiza un video desde que se sube hasta que se obtiene una conducta por segundo. Tercero, cómo decide esa conducta el clasificador. Y cuarto, cómo se ve todo esto cuando lo usa un investigador. Empiezo por la arquitectura.

El sistema se compone de cuatro partes, y cada una corre en su propio contenedor Docker. Eso significa que cada parte se puede arrancar, detener o reemplazar sin tocar a las demás.

La primera parte es el frontend, la que ve el investigador. Está hecho con React y Vite, y corre dentro del navegador. Su única función es mostrar pantallas y recoger lo que el usuario hace. No analiza videos ni toma decisiones de negocio, y solo habla con la API.

La segunda parte es el backend, escrito en Java 21 con Spring Boot. Es el cerebro administrativo del sistema. Expone una API REST que intercambia datos en formato JSON, maneja la sesión de cada usuario mediante tokens JWT y controla quién puede hacer qué según su rol. También es quien recibe el video cuando se sube y quien coloca el análisis en una cola, para que se ejecute cuando le toque.

La tercera parte es la base de datos y el almacenamiento de archivos. La base es PostgreSQL 16 y guarda las cuentas de usuario, los experimentos, los resultados y la propia cola de análisis. Los videos y el modelo entrenado no van dentro de la base, sino en un volumen de archivos compartido.

La cuarta parte es el worker, el trabajador que hace el análisis pesado. Está escrito en Python 3.12 y usa OpenCV para procesar video y PyTorch para ejecutar la red neuronal. Toma un video de la cola, lo analiza de principio a fin y guarda el resultado. Procesa un video a la vez, y además ejecuta las tareas diarias de limpieza.

Para que se entienda por qué se separó así, piensen en lo que pasa en el laboratorio. Una persona sube un video y quiere seguir trabajando; otra persona, al mismo tiempo, quiere consultar los resultados de la semana pasada; y el administrador quiere crear una cuenta nueva. Si todo estuviera en un solo programa, el análisis, que es la parte que más recursos consume, haría lento todo lo demás. Al dividirlo, cada parte se ocupa de una sola cosa y se puede mejorar sin romper las otras. Además, la separación nos permite dar seguridad por capas: el navegador nunca toca los archivos ni la base de datos de forma directa, todo pasa primero por la API, que revisa quién eres y qué puedes hacer.

Ahora, hay una decisión de diseño que quiero resaltar. El backend y el worker no se llaman entre sí. No existe una conexión directa entre ellos. Se comunican a través de la base de datos y del volumen compartido: el backend escribe en la cola que hay un análisis pendiente, y el worker, cuando está libre, lo encuentra ahí. Esto tiene una ventaja práctica. Un análisis puede tardar varios minutos, pero como el sitio no está esperando al worker, sigue respondiendo con normalidad. El usuario puede cerrar la pestaña, volver más tarde y encontrar su análisis en el estado en que haya quedado.

*[Diapositiva 9]*

Veamos ahora qué hace el worker con un video. El análisis ocurre en tres etapas, siempre en el mismo orden. Primero el preprocesamiento, luego la localización de los cilindros y al final la clasificación. De ahí sale el resultado del sistema: una conducta por cada segundo del video y por cada cilindro.

La primera etapa es el preprocesamiento, y su trabajo es asegurarse de que el análisis pueda empezar. Comprueba que el video realmente se abra, usando una herramienta llamada ffprobe, que lee la información del archivo sin reproducirlo. Corrige la rotación, porque muchos videos grabados con cámara web o con otros dispositivos traen una orientación guardada que, si no se corrige, deja la imagen de lado. Y confirma que el modelo entrenado esté disponible, porque no tendría sentido procesar minutos de video para descubrir al final que no hay con qué clasificarlo.

La segunda etapa es la localización de los cilindros, y es la parte de visión por computadora del sistema. Primero alinea los cuadros del video. Aunque la cámara esté fija, siempre hay pequeños movimientos o vibraciones, y para compensarlos usamos una técnica llamada ORB, que encuentra puntos característicos en la imagen, junto con RANSAC, que descarta los puntos que no coinciden y calcula la alineación más confiable.

Después construye una imagen del fondo. Lo hace calculando el percentil diez de cada píxel a lo largo del video. En palabras sencillas: como el espécimen se mueve y el fondo no, el valor que un píxel casi siempre tiene es el del fondo. Con esa imagen del fondo ya limpia, el sistema compara cada cuadro contra ella, y lo que cambia es el espécimen. Así localiza los cilindros y, dentro de cada uno, mide quince rasgos del espécimen, por ejemplo su posición y qué tanto se mueve.

Aquí hay algo importante. En esta prueba hay un espécimen por cilindro y el fondo es fijo. Por eso el sistema detecta por sustracción de fondo y no necesita seguir al animal de un cuadro al siguiente. Ese era un paso que necesitábamos en la versión anterior del trabajo, y aquí ya no hace falta.

Vale la pena decir por qué elegimos este camino. El enfoque más común para estos problemas es detectar al animal con una red neuronal y seguirlo cuadro por cuadro. Funciona, pero necesita muchos ejemplos etiquetados de posiciones y es más pesado de ejecutar. En nuestra prueba el escenario es controlado: cámara fija, cilindros que no se mueven y un solo espécimen en cada uno. Aprovechar esa regularidad nos permite usar una técnica más simple, más rápida y más fácil de explicar, y reservar la red neuronal para lo que de verdad lo necesita, que es decidir la conducta.

La tercera etapa es la clasificación. Para cada cilindro y para cada segundo, la red decide cuál fue la conducta, mirando una ventana de cuatro segundos alrededor de ese momento. En un momento explico cómo lo hace.

Quiero detenerme en lo que pasa cuando algo sale mal, porque un sistema que solo funciona cuando todo sale bien no es útil en un laboratorio. Hay dos casos que manejamos de forma explícita. El primero: si el video no abre o si no se encuentran los cilindros, el análisis termina en error y genera un reporte de diagnóstico, para que el usuario sepa qué ocurrió y pueda corregirlo. El segundo: si un espécimen no se ve durante tres segundos seguidos dentro de su cilindro, el análisis no inventa una conducta. Se pone en pausa y espera la decisión del usuario, hasta por setenta y dos horas. Si el usuario decide no continuar, puede cancelar el análisis.

*[Diapositiva 10]*

Llegamos al clasificador, que es la parte donde el sistema decide qué conducta hubo en cada segundo. Usamos aprendizaje supervisado: es decir, la red aprende a partir de ejemplos que ya tienen la respuesta correcta.

La red recibe dos tipos de información al mismo tiempo. La primera es un clip de dieciséis fotogramas del cilindro. Esa parte la procesa una red llamada R(2+1)D-18, que está diseñada para video porque no mira cada imagen por separado, sino que analiza cómo cambia a lo largo del tiempo, y la conducta es justamente eso, movimiento a través del tiempo.

La segunda información es un conjunto de veintidós medidas. Son los quince rasgos que el worker midió en la etapa anterior, más siete reglas de observación. Estas medidas entran por una rama aparte de la red y después se fusionan con lo que sacó la parte de video. La idea es que la red tenga dos fuentes: lo que ve en las imágenes y lo que miden los números.

Antes de seguir, recordemos qué significa cada conducta en la prueba de nado forzado. El espécimen se coloca en un cilindro con agua del que no puede escapar, y se observa qué hace. Hay nado cuando se desplaza activamente por el cilindro. Hay escalamiento cuando hace movimientos vigorosos contra las paredes, tratando de salir. Y hay inmovilidad cuando deja de luchar y solo realiza los movimientos mínimos necesarios para mantenerse a flote. Los investigadores comparan cuánto tiempo pasa en cada conducta, por ejemplo, entre un grupo que recibió fluoxetina, el antidepresivo de referencia, y uno que no. Por eso es tan valioso contar los segundos de cada una con precisión.

Con eso, la red da tres salidas: nado, inmovilidad y escalamiento. Pero el sistema reporta cuatro conductas. La cuarta es la conducta activa, y no sale de la red. Se asigna con una regla: cuando la suma de nado y escalamiento llega al menos a cero punto ochenta, y ninguna de las dos alcanza por sí sola ese umbral. Es el caso en que el espécimen claramente está activo, pero la red duda entre nado y escalamiento.

Cada decisión se toma por segundo, con una ventana de cuatro segundos que se desliza de uno en uno. Por eso cada segundo tiene su propia decisión.

Quiero explicar también de dónde salen los datos y cómo se midió que el modelo funciona. Los datos de entrenamiento son propios. Las etiquetas, es decir, la conducta correcta de cada segundo, las generamos con un etiquetador que construimos dentro del equipo, y después las revisamos a mano. Entrenamos durante quince épocas, con lotes de dieciséis clips.

Para validar, usamos cinco particiones, y las agrupamos por video. Esto es importante: si un mismo video aparece parte en entrenamiento y parte en validación, los segundos vecinos se parecen muchísimo entre sí, y el modelo parecería mejor de lo que realmente es. Al separar por video completo, la evaluación es más honesta, porque el modelo se prueba con videos que nunca vio.

*[Diapositiva 11]*

Resumo cómo quedó la plataforma completa, para ubicar cada tecnología en su lugar.

El backend, en Java 21 y Spring Boot 4.1, ofrece la API REST con doce entidades JPA, que son la forma en que el código representa las tablas de la base de datos. Maneja la sesión con JWT y distingue roles, de modo que un investigador y un administrador ven y pueden hacer cosas distintas. Y genera el reporte final en PDF.

El worker, en Python 3.12 con PyTorch, toma los videos de la cola en PostgreSQL, uno a la vez, y se detiene a esperar si no ve al espécimen durante tres segundos. También ejecuta las tareas diarias de limpieza, entre ellas el borrado de los videos que ya cumplieron su plazo.

El frontend, en React 18 con Vite, tiene ocho pantallas que van del inicio de sesión hasta la administración. Incluye la revisión segundo a segundo, que es donde el investigador valida lo que el sistema decidió.

Quiero subrayar tres decisiones que atraviesan toda la plataforma. La primera, que el investigador siempre tiene la última palabra: lo que el sistema decide se puede revisar y corregir. La segunda, que el sistema no se queda con los videos para siempre: se borran treinta días después de un análisis exitoso, y para eso existen las tareas diarias. Y la tercera, que las contraseñas no se guardan tal cual, sino con un hash y una sal, de modo que ni siquiera quien administre la base puede leerlas.

Y todo se apoya en PostgreSQL 16 y se empaqueta con Docker Compose. La base tiene doce tablas en el modelo relacional, los videos y el modelo entrenado viven en volúmenes, y cada servicio tiene su propio contenedor. Con un solo comando se levanta el sistema completo.

*[Diapositiva 12]*

Ahora paso a usarlo. La demostración sigue el camino completo de un investigador, en seis pasos.

Primer paso: iniciar sesión. Entro con mi cuenta de investigador, con mi identificador y mi contraseña. Lo que se ve a partir de aquí depende de mi rol: un investigador trabaja con sus propios experimentos, y un administrador tiene además la pantalla de administración.

Segundo paso: crear un experimento y subir el video. Creo el experimento, le doy un nombre, y subo el video de la prueba. El sistema recibe el archivo y lo registra. En este momento todavía no analiza nada: lo que hace es colocar el análisis en la cola.

Tercer paso: seguir el progreso. Aquí veo en qué etapa va el análisis: si está esperando su turno, si está en el preprocesamiento, localizando los cilindros o clasificando. Si el análisis llegara a pausarse porque un espécimen dejó de verse, esta pantalla me lo indicaría y me permitiría decidir si sigo o cancelo.

Cuarto paso: ver los resultados. Cuando el análisis termina, el sistema me muestra la conducta de cada espécimen a lo largo de toda la prueba. Puedo ver de un vistazo cuánto tiempo estuvo en cada conducta y cómo se distribuyó.

Quinto paso: la revisión segundo a segundo. Este es, para mí, el paso más importante. El sistema es una herramienta de apoyo para el investigador, no un reemplazo. Aquí puedo recorrer el video segundo por segundo, comparar lo que el sistema decidió con lo que yo veo, y corregir cualquier segundo donde no esté de acuerdo.

Sexto paso: descargar el reporte. Con la revisión hecha, genero el reporte en PDF con los resultados del experimento y lo descargo.

Antes de cerrar, quiero que veamos esta demostración desde la perspectiva de lo que ahorra. Sin el sistema, revisar un video de prueba significa que una persona lo vea completo, anotando a mano, segundo por segundo, qué hace el espécimen. Eso lleva tiempo, cansa, y dos personas pueden anotar cosas distintas. Con el sistema, el trabajo de la persona cambia: en lugar de anotar todo desde cero, parte de una propuesta ya hecha y se concentra en revisar los segundos dudosos. El criterio sigue siendo suyo, pero el trabajo repetitivo lo hace el sistema.

Con esto el flujo queda completo. Partimos de un video, y terminamos con una conducta por cada segundo, revisada por el investigador y reunida en un reporte.

Para cerrar, repaso lo que vimos. Primero, la arquitectura: cuatro partes independientes, cada una en su contenedor, que se comunican por la API, la base de datos y un volumen compartido. Segundo, el análisis del video: tres etapas, preprocesamiento, localización de los cilindros por sustracción de fondo y clasificación, con un manejo claro de los errores y de las pausas. Tercero, el clasificador: una red que combina el video con veintidós medidas, decide una conducta por segundo y se validó agrupando por video para no inflar el resultado. Y cuarto, la plataforma: un flujo completo que va del inicio de sesión al reporte, con el investigador siempre al mando de la revisión.

Con esto concluyo la presentación del sistema. Muchas gracias por su atención.
