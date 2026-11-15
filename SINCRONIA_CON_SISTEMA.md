# Sincronía del documento con el sistema

Protocolo acordado con orquestador_web (9-nov-2026). **Solo visualizar y registrar: nadie edita LaTeX ni el sistema todavía.**

- **Versión del sistema que refleja el documento:** el documento no cita ningún número de versión. Su última puesta al día completa del cap. 6 es el commit `23e774f` («documento listo capitulo 6», 1-nov-2026); el cap. 5 se tocó hasta el 2-nov. Referencia de orquestador_web: producción v1.0.0 = `15489f4` (21-oct); hoy v1.9.2 = `ba903f4`.
- **Fase 1 (orquestador_latex):** sección 1. **Fase 2 (orquestador_web):** confirmar cada ítem: lo tiene / lo tiene distinto / no lo tiene. **Fase 3:** secciones 2 y 3.

## 1. Inventario de lo que el documento afirma del sistema

Generado con búsqueda por patrones sobre `chapters/01-06`, `back/` y `front/`. Cada ítem: `archivo.tex:línea` y el texto (recortado). Es la base para que orquestador_web confirme ítem por ítem; no es una lista editada a mano.

## (a) API: endpoints, rutas, roles, errores, proxy y límites

### Rutas, endpoints y métodos

- `back\apendice_D.tex:18` verificación. Todas las llaves foráneas se declaran con ON DELETE NO ACTION
- `chapters\01_introduccion.tex:434` Cap.~5 Diseño: arquitectura, base de datos, API REST, casos de uso, UML y wireframes (bocetos de pantalla)
- `chapters\01_introduccion.tex:442` Entorno Spring Boot\,/\,PostgreSQL\,/\,Docker, esquema de la base de datos y API REST
- `chapters\01_introduccion.tex:534` ---el endpoint (punto de acceso de la API) que recibe el video y el pipeline que lo procesa--- se prueba de forma
- `chapters\03_marco_teorico.tex:325` \subsectionArquitectura cliente-servidor y API REST
- `chapters\03_marco_teorico.tex:329` REST, y la base de datos (PostgreSQL) persiste los datos. Esta separación permite que
- `chapters\03_marco_teorico.tex:332` La API REST usa semántica HTTP estándar: GET para consultar,
- `chapters\03_marco_teorico.tex:333` POST para crear, PUT/PATCH para actualizar y
- `chapters\03_marco_teorico.tex:334` DELETE para eliminar. Cada recurso tiene una URL fija y las respuestas
- `chapters\04_analisis.tex:114` (sesión de habituación, 20~min) y Día~2 (sesión post-tratamiento, 5~min), según el protocolo. Cada
- `chapters\04_analisis.tex:869` & Spring Web MVC para la API REST, Spring Security con OAuth2 Resource Server para firmar y validar los JWT,
- `chapters\05_diseno.tex:11` a través de la API REST, y cómo se ve la interfaz desde la perspectiva del investigador.
- `chapters\05_diseno.tex:62` Se comunica con el backend exclusivamente mediante la API REST usando JSON.
- `chapters\05_diseno.tex:66` \item Backend (Spring Boot): expone la API REST, gestiona la autenticación con
- `chapters\05_diseno.tex:644` \sectionDiseño de la API REST
- `chapters\05_diseno.tex:647` La API REST sigue las convenciones HTTP estándar \citegrinberg2018. Es una API de
- `chapters\05_diseno.tex:649` verbos HTTP se usan con su significado (GET consulta, POST crea,
- `chapters\05_diseno.tex:650` PATCH modifica solo los campos que se envían y DELETE elimina). No
- `chapters\05_diseno.tex:657` Todos los endpoints requieren JWT, salvo el inicio de sesión, la recuperación y el restablecimiento de contraseña, el estado de salud (\path/health), 
- `chapters\05_diseno.tex:664` La Tabla~\reftab:api describe los endpoints principales agrupados por recurso.
- `chapters\05_diseno.tex:667` \captionEndpoints principales de la API REST.
- `chapters\05_diseno.tex:681` POST & \path/auth/login & Inicia sesión; devuelve token JWT. & Público
- `chapters\05_diseno.tex:683` POST & \path/auth/logout & Cierra la sesión; el navegador descarta el token. & Autenti\-cado
- `chapters\05_diseno.tex:685` POST & \path/auth/recover & Envía enlace de recuperación por correo. & Público
- `chapters\05_diseno.tex:687` POST & \path/auth/reset & Establece la nueva contraseña con el enlace de restablecimiento (vigente 60 minutos). & Público
- `chapters\05_diseno.tex:689` PATCH & \path/auth/password & Cambia la contraseña del usuario autenticado. & Autenti\-cado
- `chapters\05_diseno.tex:692` PATCH & \path/users/me & Cambia los datos del perfil propio. & Autenti\-cado
- `chapters\05_diseno.tex:696` GET & \path/experiments & Lista todos los experimentos del laboratorio (ver RN-08). & Investiga\-dor
- `chapters\05_diseno.tex:698` POST & \path/experiments & Crea un experimento con sus metadatos. & Investiga\-dor
- `chapters\05_diseno.tex:700` GET & \path/experiments/id & Devuelve detalle y estado de un experimento. & Investiga\-dor
- `chapters\05_diseno.tex:704` POST & \path/experiments/id/groups/grupo/videos & Sube un video (Día~1 o Día~2) a una tanda del grupo indicado (se crea la tanda si no existe) y, si e
- `chapters\05_diseno.tex:706` GET & \path/experiments/id/status & Devuelve el progreso del análisis en porcentaje. & Investiga\-dor
- `chapters\05_diseno.tex:708` GET & \path/experiments/id/groups & Lista los grupos del experimento y sus tandas. & Investiga\-dor
- `chapters\05_diseno.tex:710` DELETE & \path/experiments/id & Elimina el experimento con sus grupos, videos, resultados, reportes y notificaciones. 409 si algún análisis está proce
- `chapters\05_diseno.tex:712` DELETE & \path/experiments/id/tandas/idTanda & Elimina una tanda con sus videos y resultados y deja libre su letra; si era la última del grupo, tambié
- `chapters\05_diseno.tex:714` POST & \path/experiments/id/analyses/idAnalisis/restart & Reinicia un análisis completado: borra el resultado y toda la revisión, y lo vuelve a encola
- `chapters\05_diseno.tex:716` GET & \path/experiments/id/analyses/idAnalisis/pause & Devuelve los datos de la pausa del análisis (RN-17). & Creador o Admin
- `chapters\05_diseno.tex:718` GET & \path/experiments/id/analyses/idAnalisis/pause/image & Devuelve la imagen fija del instante de la pausa. & Creador o Admin
- `chapters\05_diseno.tex:720` POST & \path/experiments/id/analyses/idAnalisis/pause/adjust & Guarda el ajuste del recuadro del cilindro en la pausa. & Creador o Admin
- `chapters\05_diseno.tex:722` POST & \path/experiments/id/analyses/idAnalisis/pause/continue & Reanuda el análisis tras el ajuste. & Creador o Admin
- `chapters\05_diseno.tex:724` POST & \path/experiments/id/analyses/idAnalisis/cancel & Cancela el análisis en pausa. & Creador o Admin
- `chapters\05_diseno.tex:728` GET & \path/experiments/id/results & Devuelve los resultados por espécimen y conducta, con los segundos «sin ver» como una clave más. & Investiga\-dor
- `chapters\05_diseno.tex:730` GET & \path/experiments/id/results/byminute & Devuelve el desglose temporal por minuto, con los segundos «sin ver» como una clave más. & Investiga\-do
- `chapters\05_diseno.tex:732` GET & \path/experiments/id/results/groups & Devuelve la comparación entre grupos con el Día~2: el promedio por espécimen de cada grupo (RF-21). & Inve
- `chapters\05_diseno.tex:734` GET & \path/experiments/id/results/blocks & Devuelve, por espécimen, los bloques de 5~s con su conducta, su matiz y sus segundos (RF-18, RN-15); solo 
- `chapters\05_diseno.tex:738` GET & \path/experiments/id/report/pdf & Descarga el reporte de resultados en PDF. & Investiga\-dor
- `chapters\05_diseno.tex:740` GET & \path/experiments/id/report/csv & Descarga los datos en CSV, del grupo completo o de una tanda. & Investiga\-dor
- `chapters\05_diseno.tex:742` GET & \path/experiments/id/report/xlsx & Descarga los datos en XLSX, del grupo completo o de una tanda. & Investiga\-dor
- `chapters\05_diseno.tex:745` GET & \path/experiments/id/analyses/idAnalisis/diagnostic & Descarga el reporte de diagnóstico de un análisis con error. & Autenti\-cado
- `chapters\05_diseno.tex:747` PUT & \path/experiments/id & Edita el nombre, la fecha y las notas del experimento. & Creador o Admin
- `chapters\05_diseno.tex:749` GET & \path/experiments/id/analyses/idAnalisis/control & Imagen de control con los cilindros que encontró el pipeline; la muestra la pantalla de un an
- `chapters\05_diseno.tex:753` GET & \path/experiments/id/analyses/idAnalisis/review & Devuelve los especímenes, las etiquetas de cada segundo y los recuadros de los cilindros de un
- `chapters\05_diseno.tex:755` POST & \path/experiments/id/analyses/idAnalisis/video-token & Emite un permiso temporal de 120 minutos para ver el video. & Creador o Admin
- `chapters\05_diseno.tex:757` GET & \path/experiments/id/analyses/idAnalisis/video?vt= & Entrega el video de la revisión por partes, con el permiso temporal, para poder adelantar y
- `chapters\05_diseno.tex:759` PUT & \path/experiments/id/analyses/idAnalisis/segundos & Guarda las correcciones por segundo y recalcula el nivel de clasificación del análisis. & Cr
- `chapters\05_diseno.tex:763` GET & \path/notifications & Lista las notificaciones del usuario, las más recientes primero. & Autenti\-cado
- `chapters\05_diseno.tex:765` GET & \path/notifications/unread-count & Devuelve cuántas notificaciones no leídas tiene el usuario. & Autenti\-cado
- `chapters\05_diseno.tex:767` PATCH & \path/notifications/id & Marca la notificación como leída o no leída. Si no es del usuario, responde 404. & Autenti\-cado
- `chapters\05_diseno.tex:770` GET & \path/admin/users & Lista todos los usuarios (filtrable por administrador/investigador y estado). & Admin
- `chapters\05_diseno.tex:772` POST & \path/admin/users & Crea una cuenta de usuario con contraseña temporal. & Admin
- `chapters\05_diseno.tex:774` PATCH & \path/admin/users/id & Edita nombre, apellidos o correo; da o quita el rol de Administrador; desactiva o reactiva la cuenta (reactivar no gene
- `chapters\05_diseno.tex:776` POST & \path/admin/users/id/reset-temporal & Genera una contraseña temporal nueva para la cuenta. & Admin
- `chapters\05_diseno.tex:778` GET & \path/admin/system & Devuelve métricas del sistema: disco y cola. & Admin
- `chapters\06_desarrollo.tex:38` La interfaz y la API se comunican solo por una API REST que intercambia datos en formato JSON. La
- `chapters\06_desarrollo.tex:57` api & Backend: API REST, autenticación, validación de archivos y creación de análisis en cola. & Solo interno, puerto 8000. Límite de memoria de 1.5 G
- `chapters\06_desarrollo.tex:61` web & nginx. Sirve la interfaz compilada y reenvía las peticiones /api/ al backend. & Es el único servicio con puerto publicado: PUERTO\_WEB, 8088 por
- `front\abreviaturas.tex:54` REST & Representational State Transfer [2pt]
- `front\glosario.tex:40` API REST
- `front\glosario.tex:42` arquitectónicas REST (Representational State Transfer). En el
- `front\glosario.tex:43` sistema propuesto, la API REST del backend (Spring Boot) expone los recursos (experimentos,
- ... 1 coincidencias más (ampliar al revisar).

### Autenticación, token y roles

- `back\apendice_D.tex:94` contrasenaHash & varchar(255) & No & & Contraseña cifrada con bcrypt y sal. La contraseña en claro nunca se guarda
- `chapters\01_introduccion.tex:445` Autenticación y control de acceso (JSON Web Token, JWT, y roles)
- `chapters\04_analisis.tex:56` & El sistema debe cerrar la sesión del usuario descartando el token (JSON Web Token, JWT) activo
- `chapters\04_analisis.tex:57` en el navegador; el servidor no mantiene una lista de tokens cancelados y el
- `chapters\04_analisis.tex:58` token tiene una vigencia larga y configurable. La opción de cierre de sesión
- `chapters\04_analisis.tex:401` usa tokens JWT con tiempo de expiración configurable. Todos los
- `chapters\04_analisis.tex:404` & Autenticación con JWT verificada en pruebas de integración. Acceso a datos
- `chapters\04_analisis.tex:411` & Hash con sal usando bcrypt. Política de contraseña temporal verificada
- `chapters\04_analisis.tex:869` & Spring Web MVC para la API REST, Spring Security con OAuth2 Resource Server para firmar y validar los JWT,
- `chapters\04_analisis.tex:1252` con sal (bcrypt). Las credenciales de los investigadores
- `chapters\04_analisis.tex:1255` almacenamiento cifrado y acceso autenticado con JSON Web Token (JWT).
- `chapters\05_diseno.tex:67` JWT, valida los archivos subidos, encola las tareas de análisis y devuelve
- `chapters\05_diseno.tex:410` bcrypt), nombre, apellidos, bandera activo (baja lógica,
- `chapters\05_diseno.tex:657` Todos los endpoints requieren JWT, salvo el inicio de sesión, la recuperación y el restablecimiento de contraseña, el estado de salud (\path/health), 
- `chapters\05_diseno.tex:658` JWT identifica al usuario, y su rol decide qué puede hacer, con un control de acceso
- `chapters\05_diseno.tex:681` POST & \path/auth/login & Inicia sesión; devuelve token JWT. & Público
- `chapters\05_diseno.tex:683` POST & \path/auth/logout & Cierra la sesión; el navegador descarta el token. & Autenti\-cado
- `chapters\05_diseno.tex:710` DELETE & \path/experiments/id & Elimina el experimento con sus grupos, videos, resultados, reportes y notificaciones. 409 si algún análisis está proce
- `chapters\05_diseno.tex:755` POST & \path/experiments/id/analyses/idAnalisis/video-token & Emite un permiso temporal de 120 minutos para ver el video. & Creador o Admin
- `chapters\05_diseno.tex:914` Postcondición & 2>\raggedright\arraybackslashp11.9cm|Sesión iniciada; JWT emitido y almacenado en el cliente; usuario redirigido a la lista de experim
- `chapters\05_diseno.tex:918` Resumen & 2>\raggedright\arraybackslashp11.9cm|El usuario introduce sus credenciales; el sistema las valida, emite un JWT y redirige a la lista de exp
- `chapters\05_diseno.tex:937` 5 & Sistema & Emite un token de sesión y responde con el rol y si la cuenta debe cambiar la contraseña; el rol no va dentro del token y se vuelve a le
- `chapters\05_diseno.tex:971` Precondición & 2>\raggedright\arraybackslashp11.9cm|Sesión activa con JWT válido.
- `chapters\05_diseno.tex:973` Postcondición & 2>\raggedright\arraybackslashp11.9cm|Token JWT descartado en el navegador; usuario redirigido a la pantalla de inicio de sesión.
- `chapters\05_diseno.tex:975` Descripción & 2>\raggedright\arraybackslashp11.9cm|Permite al usuario terminar su sesión descartando el token de autenticación activo.
- `chapters\05_diseno.tex:977` Resumen & 2>\raggedright\arraybackslashp11.9cm|El usuario selecciona la opción de cierre de sesión; el navegador descarta el JWT y redirige a la panta
- `chapters\05_diseno.tex:990` 2 & Sistema & Descarta el JWT activo en el navegador (el servidor no guarda tokens cancelados).
- `chapters\05_diseno.tex:1085` Precondición & 2>\raggedright\arraybackslashp11.9cm|Sesión activa (JWT válido).
- `chapters\05_diseno.tex:1087` Postcondición & 2>\raggedright\arraybackslashp11.9cm|Se confirma o rechaza que el usuario pertenece a ADMINISTRADOR; la acción de administración solic
- `chapters\05_diseno.tex:1091` Resumen & 2>\raggedright\arraybackslashp11.9cm|Al invocar cualquiera de las acciones de administración, el sistema consulta si el idInstitucional del 
- `chapters\05_diseno.tex:1117` 2 & El usuario no tiene registro en ADMINISTRADOR: el sistema rechaza la solicitud con error 403 (no autorizado), sin importar si la petición vino de 
- `chapters\05_diseno.tex:2362` de datos y devuelve un token JWT, el rol y si la cuenta debe cambiar la contraseña; las credenciales incorrectas producen el mensaje «Correo o contras
- `chapters\05_diseno.tex:2363` (Figura~\reffig:seq_logout) descarta el token en el navegador; el servidor no guarda tokens cancelados. El cambio de
- `chapters\06_desarrollo.tex:25` Backend & Java 21 con Spring Boot 4.1: Spring Web MVC, Spring Data JPA, Spring Security como servidor de recursos OAuth2 con JWT, y Spring Mail. Gener
- `chapters\06_desarrollo.tex:39` sesión del usuario va en un token JWT firmado con HS256 que el navegador guarda y envía en cada
- `chapters\06_desarrollo.tex:86` importantes son la llave de firma del token, la duración de la sesión, la conexión a la base, los datos
- `chapters\06_desarrollo.tex:98` \item Autenticación. Las contraseñas se guardan con BCrypt. El token JWT no guarda el rol:
- `chapters\06_desarrollo.tex:405` El token de sesión dura 168 horas (una semana) por defecto, y ese plazo es configurable. El servidor no guarda una
- `chapters\06_desarrollo.tex:406` lista de tokens cancelados ni una tabla de sesiones. «Cerrar sesión» borra el token en el navegador; por eso, al cerrar
- `chapters\06_desarrollo.tex:407` sesión no hay ninguna escritura en la base. Cuando el token vence, el sistema pide iniciar sesión de nuevo.
- `front\abreviaturas.tex:39` JWT & JSON Web Token [2pt]
- `front\glosario.tex:181` JWT
- `front\glosario.tex:182` & (JSON Web Token.) Estándar abierto para la transmisión
- `front\glosario.tex:184` El backend emite un JWT al iniciar sesión; el frontend lo adjunta en el

### Gateway, proxy, límites y tiempos

- `chapters\05_diseno.tex:40` contenedores Docker independientes: web (interfaz servida por nginx), api (backend) y db (base de datos). Un cuarto
- `chapters\06_desarrollo.tex:27` Interfaz & React 18.3 con React Router 7 y Axios 1.20, compilado con Vite 8 en Node 22. Pruebas con Vitest 5. Se sirve con nginx 1.27.
- `chapters\06_desarrollo.tex:57` api & Backend: API REST, autenticación, validación de archivos y creación de análisis en cola. & Solo interno, puerto 8000. Límite de memoria de 1.5 G
- `chapters\06_desarrollo.tex:59` worker & Toma los análisis en cola, los procesa, escribe resultados, avisa y ejecuta las tareas programadas. & Sin puerto. Límite de memoria de 5 GB.
- `chapters\06_desarrollo.tex:61` web & nginx. Sirve la interfaz compilada y reenvía las peticiones /api/ al backend. & Es el único servicio con puerto publicado: PUERTO\_WEB, 8088 por
- `chapters\06_desarrollo.tex:87` del servidor de correo, el límite de tamaño de video y los umbrales de disco.
- `chapters\06_desarrollo.tex:103` 2048 MB (MAX\_UPLOAD\_MB). La extensión se valida también en la interfaz antes de subir. El
- `chapters\06_desarrollo.tex:127` La interfaz es una aplicación de una sola página, compilada con Vite y servida por nginx. Tiene las
- `chapters\06_desarrollo.tex:163` \item Control de tiempo. Cada paso del pipeline tiene un límite de una hora, y la copia para revisión, de 30 minutos.
- `chapters\06_desarrollo.tex:309` (PAUSE\_TIMEOUT\_HOURS), el worker lo cancela y crea una notificación de cancelación. El
- `chapters\06_desarrollo.tex:382` tiempo de espera de 10 segundos. El backend envía los correos de recuperación de contraseña y de cuenta nueva.

## (b) Base de datos

### Motor, índices, dominios, restricciones y cifrado

- `back\apendice_D.tex:11` (Figura~\reffig:er), implementado en PostgreSQL. Para cada columna se indica su
- `back\apendice_D.tex:18` verificación. Todas las llaves foráneas se declaran con ON DELETE NO ACTION
- `back\apendice_D.tex:19` y ON UPDATE NO ACTION: la base rechaza borrar una fila que otra tabla
- `back\apendice_D.tex:29` \section*Dominios cerrados
- `back\apendice_D.tex:31` Nueve columnas toman sus valores de una lista fija, declarada como dominio
- `back\apendice_D.tex:32` (CREATE DOMAIN con una condición CHECK). La Tabla~\reftab:dominios
- `back\apendice_D.tex:38` \captionDominios cerrados del esquema físico.
- `back\apendice_D.tex:39` \labeltab:dominios
- `back\apendice_D.tex:41` Dominio & Tipo base & Valores
- `back\apendice_D.tex:45` Dominio & Tipo base & Valores
- `back\apendice_D.tex:92` correo & varchar(254) & No & UK & Correo con el que el usuario inicia sesión y al que llegan los avisos. Acepta cualquier dominio
- `back\apendice_D.tex:94` contrasenaHash & varchar(255) & No & & Contraseña cifrada con bcrypt y sal. La contraseña en claro nunca se guarda
- `back\apendice_D.tex:127` tipo & tipo\_grupo & No & Dominio & Control, referencia o tratamiento experimental
- `back\apendice_D.tex:158` sesion & sesion\_video & No & Dominio; UK (idTanda, sesion) & Día 1 o Día 2. Una tanda tiene como máximo un video por día, y el Día 1 es opcional; el 
- `back\apendice_D.tex:175` estado & estado\_analisis & No & Dominio & En cola, procesando, en pausa (el sistema no ve al espécimen y espera al usuario hasta 72 horas), completad
- `back\apendice_D.tex:177` etapa & etapa\_analisis & No & Dominio & Etapa del pipeline en curso o, si hubo error, la etapa donde se detuvo. Con ella se arma el mensaje de error.
- `back\apendice_D.tex:179` nivelClasif & nivel\_clasif\_analisis & No & Dominio & Preciso o agrupado. La interfaz lo usa para avisar en los resultados. Al encolar el análisis el
- `back\apendice_D.tex:201` conducta & tipo\_conducta & Sí & Dominio & Conducta vigente del segundo, que el usuario puede corregir en la revisión. Queda nula cuando el sistema no
- `back\apendice_D.tex:203` origen & origen\_segundo & No & Dominio & Quién puso la conducta vigente y cómo (Tabla~\reftab:dominios)
- `back\apendice_D.tex:212` formato & formato\_reporte & No & Dominio & CSV, XLSX o PDF
- `back\apendice_D.tex:227` tipo & tipo\_notificacion & No & Dominio & Análisis completado, error del pipeline, análisis en pausa o cancelado (RN-17), alerta de disco o video bor
- `chapters\01_introduccion.tex:442` Entorno Spring Boot\,/\,PostgreSQL\,/\,Docker, esquema de la base de datos y API REST
- `chapters\01_introduccion.tex:528` pipeline; PostgreSQL para la base de datos; React con Vite para el frontend; un etiquetador propio del equipo, que propone la conducta de cada
- `chapters\02_estado_arte.tex:241` Las redes residuales 3D extienden las convoluciones al dominio temporal: en lugar de
- `chapters\03_marco_teorico.tex:238` Este enfoque reduce los requerimientos de datos cuando el dominio de origen (ImageNet
- `chapters\03_marco_teorico.tex:329` REST, y la base de datos (PostgreSQL) persiste los datos. Esta separación permite que
- `chapters\03_marco_teorico.tex:357` \subsectionPersistencia de datos con PostgreSQL
- `chapters\03_marco_teorico.tex:359` PostgreSQL es un sistema de gestión de bases de datos relacionales de código abierto
- `chapters\04_analisis.tex:408` & Las contraseñas deben almacenarse cifradas con sal, nunca en texto plano.
- `chapters\04_analisis.tex:411` & Hash con sal usando bcrypt. Política de contraseña temporal verificada
- `chapters\04_analisis.tex:746` correo), con qué finalidad y cómo se protegen (contraseña con hash y sal).
- `chapters\04_analisis.tex:879` PostgreSQL
- `chapters\04_analisis.tex:1028` ImageNet \citemeng2024_dsaan, lo que da respaldo empírico a la viabilidad de esa
- `chapters\04_analisis.tex:1034` (Python, OpenCV, scikit-learn y PyTorch) de la plataforma web (Spring Boot, React, PostgreSQL) mediante una
- `chapters\04_analisis.tex:1153` Herramientas de desarrollo (Java, Spring Boot, Python, React, PostgreSQL, Docker, OpenCV,
- `chapters\04_analisis.tex:1251` institucional, nombre, apellidos y correo), con la contraseña guardada con hash
- `chapters\04_analisis.tex:1255` almacenamiento cifrado y acceso autenticado con JSON Web Token (JWT).
- `chapters\04_analisis.tex:1271` PostgreSQL License (PostgreSQL).
- `chapters\04_analisis.tex:1315` PyTorch, Spring Boot, React, PostgreSQL) tienen desarrollo activo y comunidades grandes.
- `chapters\05_diseno.tex:48` (PostgreSQL y sistema de archivos). El archivo del clasificador de conducta reside en una
- `chapters\05_diseno.tex:69` PostgreSQL.
- `chapters\05_diseno.tex:92` \item Base de datos (PostgreSQL): almacena usuarios, experimentos,
- `chapters\05_diseno.tex:365` entidades del dominio y las relaciones entre ellas, sin entrar en detalles de
- `chapters\05_diseno.tex:367` las tablas, columnas y tipos de datos concretos de PostgreSQL.
- `chapters\05_diseno.tex:377` conducta por espécimen, mientras que el video del Día~1 se guarda sin análisis (OBSERVACION, SEGUNDO y CONDUCTA). La figura muestra las entidades del 
- `chapters\05_diseno.tex:409` \item USUARIO: credenciales (correo, hash de contraseña con
- `chapters\05_diseno.tex:464` conceptual; en el relacional no es tabla sino el dominio cerrado
- `chapters\05_diseno.tex:465` tipo\_conducta de la columna SEGUNDO.conducta, porque son cuatro valores fijos y no tiene atributos propios. En el modelo físico, Conducta se implemen
- `chapters\05_diseno.tex:490` La base de datos usa PostgreSQL como gestor relacional. Los datos del sistema
- `chapters\05_diseno.tex:527` al día cada vez que el usuario corrige una etiqueta. El dominio tipo\_conducta
- `chapters\05_diseno.tex:528` tiene cuatro valores, por lo que una conducta adicional sería un cambio de dominio y no
- `chapters\05_diseno.tex:542` partes. El valor de conducta es uno de los cuatro del dominio cerrado
- `chapters\05_diseno.tex:620` (idObservacion, segundo); la conducta es un valor del dominio
- `chapters\05_diseno.tex:1368` Postcondición & 2>\raggedright\arraybackslashp11.9cm|Cuenta creada en la base de datos con contraseña temporal; investigador notificado por correo con
- `chapters\05_diseno.tex:1395` 7 & Sistema & Muestra la contraseña temporal una sola vez al Administrador, como respaldo por si el correo no llega.
- `chapters\05_diseno.tex:2665` las entidades principales del dominio y sus relaciones desde la perspectiva del
- `chapters\05_diseno.tex:2666` backend. Las clases centrales del dominio experimental son Usuario,
- `chapters\05_diseno.tex:2992` el sistema envía la contraseña temporal por correo en texto plano, después de confirmar la creación, y además se la muestra una sola vez al Administra
- `chapters\06_desarrollo.tex:29` Worker & Python 3.12 con PyTorch 2.14 y torchvision 0.29 (CPU), OpenCV 5.0 sin interfaz gráfica, NumPy 2.5, pandas 3.1, scikit-learn 1.9, psycopg2 2.9
- `chapters\06_desarrollo.tex:31` Base de datos & PostgreSQL 16.
- ... 5 coincidencias más (ampliar al revisar).

### Tablas y entidades en la prosa del cap. 5 (el detalle por columna está en `back/apendice_D.tex`)

- `chapters\05_diseno.tex:365` entidades del dominio y las relaciones entre ellas, sin entrar en detalles de
- `chapters\05_diseno.tex:369` La Figura~\reffig:der muestra el diagrama entidad-relación (DER) conceptual del
- `chapters\05_diseno.tex:370` sistema. Las entidades principales son USUARIO, EXPERIMENTO,
- `chapters\05_diseno.tex:377` conducta por espécimen, mientras que el video del Día~1 se guarda sin análisis (OBSERVACION, SEGUNDO y CONDUCTA). La figura muestra las entidades del 
- `chapters\05_diseno.tex:378` ADMINISTRADOR (un usuario con permisos adicionales) y las entidades
- `chapters\05_diseno.tex:385` \captionDiagrama entidad-relación conceptual del sistema [autoría propia].
- `chapters\05_diseno.tex:390` al modelo relacional: cada entidad se convierte en una tabla, cada relación se
- `chapters\05_diseno.tex:463` decide entre nado y escalamiento; ver RN-13). Es una entidad del esquema
- `chapters\05_diseno.tex:464` conceptual; en el relacional no es tabla sino el dominio cerrado
- `chapters\05_diseno.tex:516` conjuntos ni estructuras anidadas--- y que cada tabla tenga una clave primaria que
- `chapters\05_diseno.tex:578` clave candidata de la tabla \citeelmasri2015. Con el tratamiento dentro de
- `chapters\05_diseno.tex:1089` Descripción & 2>\raggedright\arraybackslashp11.9cm|Antes de ejecutar cualquier acción de administración (crear cuenta, desactivar cuenta, listar usuar
- `chapters\05_diseno.tex:1569` Resumen & 2>\raggedright\arraybackslashp11.9cm|Una vez almacenado el video, el sistema crea un registro en la tabla ANALISIS con estado «en cola», y e
- `chapters\05_diseno.tex:1582` 2 & Sistema & Crea un registro en la tabla ANALISIS con: identificador del video, estado «en cola» y marca de tiempo.
- `chapters\05_diseno.tex:1595` 2 & Error al escribir en la tabla ANALISIS (p.~ej.\ fallo de base de datos): el sistema informa al investigador del error y no deja el video en estado
- `chapters\05_diseno.tex:1692` 2 & Worker & Recupera la tarea de la cola de análisis mediante polling a la tabla ANALISIS.
- `chapters\05_diseno.tex:2665` las entidades principales del dominio y sus relaciones desde la perspectiva del

## (c) Pantallas, casos de uso y flujo

### Casos de uso (primera aparición de cada CU)

- `chapters\05_diseno.tex:2818` **CU-06** ); y carga del video de una tanda, donde se indica el grupo o tratamiento, la

### Pantallas y maquetas

- `chapters\05_diseno.tex:264` marca a mano en la pantalla de revisión.
- `chapters\05_diseno.tex:284` OBSERVACION del espécimen en ese video). Es la fuente de la pantalla
- `chapters\05_diseno.tex:288` en un formato que el navegador reproduce (H.264), para la pantalla de revisión.
- `chapters\05_diseno.tex:326` pantalla de revisión, siempre que su video siga en el servidor: el resultado anterior y la revisión se borran, y el análisis vuelve a
- `chapters\05_diseno.tex:749` GET & \path/experiments/id/analyses/idAnalisis/control & Imagen de control con los cilindros que encontró el pipeline; la muestra la pantalla de un an
- `chapters\05_diseno.tex:931` 2 & Sistema & Muestra la pantalla de inicio de sesión con campos de correo y contraseña.
- `chapters\05_diseno.tex:939` 6 & Sistema & Muestra la lista de experimentos, o la pantalla de cambio de contraseña si la cuenta lo exige.
- `chapters\05_diseno.tex:973` Postcondición & 2>\raggedright\arraybackslashp11.9cm|Token JWT descartado en el navegador; usuario redirigido a la pantalla de inicio de sesión.
- `chapters\05_diseno.tex:977` Resumen & 2>\raggedright\arraybackslashp11.9cm|El usuario selecciona la opción de cierre de sesión; el navegador descarta el JWT y redirige a la panta
- `chapters\05_diseno.tex:988` 1 & Inv. / Admin. & Selecciona «Cerrar sesión» en el menú de usuario, disponible desde cualquier pantalla.
- `chapters\05_diseno.tex:992` 3 & Sistema & Redirige al usuario a la pantalla de inicio de sesión.
- `chapters\05_diseno.tex:1041` 1 & Inv. / Admin. & Selecciona «Olvidé mi contraseña» en la pantalla de inicio de sesión.
- `chapters\05_diseno.tex:1144` Resumen & 2>\raggedright\arraybackslashp11.9cm|Al detectar la marca de «cambio obligatorio», el sistema redirige al usuario a la pantalla de cambio de
- `chapters\05_diseno.tex:1157` 2 & Sistema & Redirige al usuario a la pantalla de cambio de contraseña antes de acceder a la lista de experimentos.
- `chapters\05_diseno.tex:1256` Descripción & 2>\raggedright\arraybackslashp11.9cm|Permite al investigador actualizar su nombre, apellidos y correo electrónico desde la pantalla de p
- `chapters\05_diseno.tex:1269` 1 & Investigador & Accede a la pantalla de perfil desde el menú de usuario.
- `chapters\05_diseno.tex:1271` 2 & Sistema & Muestra los datos de la sesión y, en otro formulario de la misma pantalla, la opción de cambiar la contraseña.
- `chapters\05_diseno.tex:1456` 6 & Sistema & Redirige a la pantalla de carga de video del experimento.
- `chapters\05_diseno.tex:1490` Postcondición & 2>\raggedright\arraybackslashp11.9cm|Archivo almacenado en el volumen compartido; si el video es del Día~2, tarea de análisis encolada
- `chapters\05_diseno.tex:1521` 9 & Sistema & Muestra la confirmación del guardado y, si es el Día~2, redirige a la pantalla de progreso del análisis.
- `chapters\05_diseno.tex:1675` Postcondición & 2>\raggedright\arraybackslashp11.9cm|Pipeline ejecutado por el Worker; estado visible en pantalla del investigador; al completarse exi
- `chapters\05_diseno.tex:1679` Resumen & 2>\raggedright\arraybackslashp11.9cm|El Worker toma la tarea de la cola y ejecuta el pipeline completo. El frontend consulta periódicamente 
- `chapters\05_diseno.tex:1690` 1 & Investigador & Accede a la pantalla de progreso (o es redirigido automáticamente tras subir el video).
- `chapters\05_diseno.tex:1700` 6 & Sistema & Actualiza periódicamente la barra de porcentaje y la etapa activa en la pantalla del investigador.
- `chapters\05_diseno.tex:1704` 8 & Sistema & Notifica al investigador y habilita el acceso a la pantalla de resultados.
- `chapters\05_diseno.tex:1715` 4 & El Worker no puede abrir el video o no encuentra los cilindros (ver RN-11): detiene el pipeline, genera el reporte de diagnóstico PDF (ver CU-13) 
- `chapters\05_diseno.tex:1746` Resumen & 2>\raggedright\arraybackslashp11.9cm|El Worker genera y almacena el PDF de diagnóstico al detener el pipeline por error. El sistema pone dis
- `chapters\05_diseno.tex:1757` 1 & Sistema & Muestra en la pantalla de progreso la descripción del error: el video no se pudo abrir o no se encontraron los cilindros.
- `chapters\05_diseno.tex:1797` Postcondición & 2>\raggedright\arraybackslashp11.9cm|Tiempos por conducta y desglose por minuto visibles en pantalla; acceso a descarga habilitado.
- `chapters\05_diseno.tex:1812` 1 & Inv. / Admin. & Accede a la pantalla de resultados desde la lista de experimentos, el detalle del experimento, el detalle de un grupo, la pantalla
- `chapters\05_diseno.tex:1871` 1 & Inv. / Admin. & Selecciona el formato de descarga (CSV, XLSX o PDF) desde la pantalla de resultados; en CSV o XLSX, la tanda o el grupo completo q
- `chapters\05_diseno.tex:1922` 1 & Inv. / Admin. & Pide las estadísticas desde la pantalla de resultados de una tanda o del grupo completo (ver CU-14) o descarga un reporte en CSV o
- `chapters\05_diseno.tex:1960` Postcondición & 2>\raggedright\arraybackslashp11.9cm|Pantalla de revisión abierta con las etiquetas de cada segundo; si el usuario no corrige nada, la
- `chapters\05_diseno.tex:1964` Resumen & 2>\raggedright\arraybackslashp11.9cm|Cuando el análisis termina, el usuario abre una pantalla con el video y una línea de tiempo por espécim
- `chapters\05_diseno.tex:1975` 1 & Inv. / Admin. & Elige «Revisar segundo a segundo» desde la pantalla de progreso o la de resultados.
- `chapters\05_diseno.tex:1998` 2 & El usuario no es el creador del experimento ni Administrador: la pantalla se abre en solo lectura. Ve los segundos y sus etiquetas, sin el video, 
- `chapters\05_diseno.tex:2000` 4 & El usuario elige «Reiniciar el análisis»: el sistema avisa que se borrarán el resultado anterior y toda la revisión hecha, y que no se puede desha
- `chapters\05_diseno.tex:2019` Precondición & 2>\raggedright\arraybackslashp11.9cm|Pantalla de revisión abierta (CU-17); la conducta del sistema no coincide con lo que el usuario ob
- `chapters\05_diseno.tex:2131` Descripción & 2>\raggedright\arraybackslashp11.9cm|Pantalla principal del investigador. Muestra todos los experimentos del laboratorio con nombre, fec
- `chapters\05_diseno.tex:2150` 4 & Investigador & Selecciona un experimento para ver su detalle, progreso o resultados, o aplica filtros para acotar la lista. Si el estado es «proce
- `chapters\05_diseno.tex:2414` activa y permite actualizar nombre, apellidos y correo electrónico; la contraseña se cambia en otro formulario de la misma pantalla.
- `chapters\05_diseno.tex:2455` persiste la notificación y cómo el frontend la consulta al entrar a cada pantalla y cada 30 segundos (sin consultar con la pestaña oculta). Las notifi
- `chapters\05_diseno.tex:2703` La interfaz tiene catorce pantallas (inicio de sesión, restablecer contraseña, primer acceso, perfil, experimentos, nuevo experimento, experimento, gr
- `chapters\05_diseno.tex:2708` \subsectionPantalla de inicio de sesión
- `chapters\05_diseno.tex:2713` las credenciales, la pantalla comprueba que el correo tenga un formato válido.
- `chapters\05_diseno.tex:2730` \captionPantalla de inicio de sesión [autoría propia].
- `chapters\05_diseno.tex:2738` investigador puede consultar sus datos y cambiar su contraseña desde la pantalla de
- `chapters\05_diseno.tex:2847` \captionPantalla de carga de video por tanda [autoría propia].
- `chapters\05_diseno.tex:2867` \caption[]Pantalla de carga de video por tanda (continuación).
- `chapters\05_diseno.tex:2877` la pantalla habilita «Ver resultados» y «Revisar segundo a segundo». Debajo lista la
- `chapters\05_diseno.tex:2882` aparece una notificación y el usuario ve una imagen fija de ese instante, con tres botones en la pantalla de pausa («Ajustar y continuar», «El recuadr
- `chapters\05_diseno.tex:2883` análisis»); si no responde en 72~horas, el análisis se cancela (RN-17). En la pantalla de progreso, un análisis en pausa solo muestra el enlace «Ajust
- `chapters\05_diseno.tex:2885` Administrador (si no, el sistema responde «Solo quien subió el video o un Administrador puede reiniciar este análisis.»): la pantalla avisa antes que 
- `chapters\05_diseno.tex:2892` \caption[Pantalla de progreso del análisis [autoría propia].]Pantalla de progreso del análisis: un análisis en curso, uno completado con acceso a resu
- `chapters\05_diseno.tex:2899` \caption[Pantalla de pausa del análisis [autoría propia].]Pantalla de pausa: imagen fija del instante en que no se ve al espécimen, con el recuadro de
- `chapters\05_diseno.tex:2912` pantalla de bloques tiene tantas columnas como bloques tiene el espécimen más largo, y
- `chapters\05_diseno.tex:2914` Los fragmentos «no se ve» se marcan en pantalla y en el reporte de resultados.
- `chapters\05_diseno.tex:2940` \captionPantalla de resultados del experimento [autoría propia].
- `chapters\05_diseno.tex:2953` \caption[]Pantalla de resultados del experimento (continuación).
- `chapters\05_diseno.tex:2958` Se abre solo cuando el análisis está completado, desde la pantalla de progreso o
- ... 11 coincidencias más (ampliar al revisar).

## (d) RF, RN, RNF y decisiones D-xx

### Requerimientos funcionales

- `chapters\04_analisis.tex:49` **RF-01** Autenticación
- `chapters\04_analisis.tex:55` **RF-02** Autenticación
- `chapters\04_analisis.tex:62` **RF-03** Autenticación
- `chapters\04_analisis.tex:67` **RF-04** Autenticación
- `chapters\04_analisis.tex:80` **RF-05** Gestión de usuarios
- `chapters\04_analisis.tex:93` **RF-06** Gestión de usuarios
- `chapters\04_analisis.tex:99` **RF-07** Gestión de usuarios
- `chapters\04_analisis.tex:106` **RF-08** Carga de video
- `chapters\04_analisis.tex:112` **RF-09** Carga de video
- `chapters\04_analisis.tex:126` **RF-10** Carga de video
- `chapters\04_analisis.tex:133` **RF-11** Carga de video
- `chapters\04_analisis.tex:141` **RF-12** Carga de video
- `chapters\04_analisis.tex:149` **RF-13** Análisis conductual
- `chapters\04_analisis.tex:159` **RF-14** Análisis conductual
- `chapters\04_analisis.tex:165` **RF-15** Análisis conductual
- `chapters\04_analisis.tex:173` **RF-16** Análisis conductual
- `chapters\04_analisis.tex:180` **RF-17** Análisis conductual
- `chapters\04_analisis.tex:190` **RF-18** Análisis conductual
- `chapters\04_analisis.tex:207` **RF-19** Resultados
- `chapters\04_analisis.tex:214` **RF-20** Resultados
- `chapters\04_analisis.tex:219` **RF-21** Resultados
- `chapters\04_analisis.tex:225` **RF-22** Resultados
- `chapters\04_analisis.tex:244` **RF-23** Lista de experimentos
- `chapters\04_analisis.tex:254` **RF-24** Lista de experimentos
- `chapters\04_analisis.tex:265` **RF-25** Lista de experimentos
- `chapters\04_analisis.tex:272` **RF-26** Lista de experimentos
- `chapters\04_analisis.tex:277` **RF-27** Lista de experimentos
- `chapters\04_analisis.tex:285` **RF-28** Administración
- `chapters\04_analisis.tex:292` **RF-29** Administración
- `chapters\04_analisis.tex:299` **RF-30** Administración
- `chapters\04_analisis.tex:304` **RF-31** Resultados
- `chapters\04_analisis.tex:315` **RF-32** Resultados
- `chapters\04_analisis.tex:333` **RF-33** Notificaciones

### Requerimientos no funcionales

- `chapters\04_analisis.tex:373` **RNF-01** Rendimiento
- `chapters\04_analisis.tex:380` **RNF-02** Calidad del análisis
- `chapters\04_analisis.tex:393` **RNF-03** Disponibilidad
- `chapters\04_analisis.tex:399` **RNF-04** Seguridad
- `chapters\04_analisis.tex:407` **RNF-05** Seguridad
- `chapters\04_analisis.tex:414` **RNF-06** Usabilidad
- `chapters\04_analisis.tex:423` **RNF-07** Compatibilidad
- `chapters\04_analisis.tex:429` **RNF-08** Almacenamiento
- `chapters\04_analisis.tex:437` **RNF-09** Almacenamiento
- `chapters\04_analisis.tex:447` **RNF-10** Portabilidad
- `chapters\04_analisis.tex:453` **RNF-11** Escalabilidad
- `chapters\04_analisis.tex:461` **RNF-12** Mantenibilidad
- `chapters\04_analisis.tex:468` **RNF-13** Concurrencia
- `chapters\04_analisis.tex:479` **RNF-14** Repetibilidad

### Reglas de negocio

- `chapters\04_analisis.tex:185` **RN-07** ). Cada análisis tiene un nivel de clasificación: «agrupado» si queda algún
- `chapters\04_analisis.tex:520` **RN-13** . Por eso se mide también en una segunda evaluación, inmovilidad contra
- `chapters\04_analisis.tex:540` **RN-15** ).
- `chapters\04_analisis.tex:584` **RN-01** Las credenciales incorrectas muestran un mensaje de error genérico que no
- `chapters\04_analisis.tex:588` **RN-02** Un video pertenece a exactamente una tanda (y, a través de ella, a un
- `chapters\04_analisis.tex:593` **RN-03** Una tanda tiene como máximo dos videos: uno del Día~1 (20~min) y uno del
- `chapters\04_analisis.tex:599` **RN-04** El análisis lo inicia el sistema automáticamente al terminar la carga. El
- `chapters\04_analisis.tex:611` **RN-05** Los videos se borran automáticamente 30~días después de que el análisis
- `chapters\04_analisis.tex:619` **RN-06** Los resultados y reportes (PDF, CSV y XLSX) se conservan indefinidamente aunque
- `chapters\04_analisis.tex:630` **RN-08** Todos los investigadores con cuenta activa pueden consultar los experimentos
- `chapters\04_analisis.tex:636` **RN-09** Borrar un experimento es permanente e irreversible: se eliminan el video,
- `chapters\04_analisis.tex:644` **RN-10** La interfaz rechaza cualquier archivo que no sea .mp4 o
- `chapters\04_analisis.tex:651` **RN-11** Si el video no se puede abrir o el pipeline no encuentra los cilindros, se
- `chapters\04_analisis.tex:659` **RN-12** La comparación entre grupos usa solo los videos del Día~2. Los
- `chapters\04_analisis.tex:682` **RN-14** Solo se puede revisar un análisis completado, y solo lo corrigen el
- `chapters\04_analisis.tex:721` **RN-16** Siempre debe existir al menos un Administrador activo: el sistema rechaza
- `chapters\04_analisis.tex:727` **RN-17** Si en un segundo no se ve al espécimen, ese segundo se registra como «no se ve».
- `chapters\04_analisis.tex:742` **RN-18** La pantalla de inicio de sesión ofrece el aviso de privacidad y los términos y

### Menciones de D-xx en el texto (no debería haber)

- `chapters\01_introduccion.tex:210` R(2+1)D-18 combinada con rasgos medidos del espécimen) cuyo atributo objetivo
- `chapters\02_estado_arte.tex:249` El sistema usa la R(2+1)D-18 \citetran2018, una ResNet-18 para video que
- `chapters\03_marco_teorico.tex:261` de 18 capas, ResNet-18, porque es la base de la red del clasificador, la R(2+1)D-18
- `chapters\03_marco_teorico.tex:264` \subsectionRed R(2+1)D-18
- `chapters\03_marco_teorico.tex:266` La R(2+1)D-18 \citetran2018 es una ResNet-18 para video. Conserva sus 18 capas y sus
- `chapters\03_marco_teorico.tex:277` que se unen antes de la capa de salida. La rama de video es la R(2+1)D-18, que procesa
- `chapters\04_analisis.tex:816` R(2+1)D-18 \citetran2018
- `chapters\04_analisis.tex:828` neuronales. Su biblioteca torchvision incluye la R(2+1)D-18 preentrenada.
- `chapters\05_diseno.tex:238` espacio-temporal R(2+1)D-18 \citetran2018, preentrenada con Kinetics-400 (videos de acciones
- `chapters\06_desarrollo.tex:253` La red es de fusión. Una rama es un backbone R(2+1)D-18 preentrenado con Kinetics-400, que analiza el
- `front\glosario.tex:68` conductas es una CNN espacio-temporal (R(2+1)D-18) fusionada con una rama de
- `front\glosario.tex:163` la R(2+1)D-18. [5pt]
- `front\glosario.tex:256` profundas sin degradación del gradiente. La R(2+1)D-18, base del
- `front\glosario.tex:304` entrenar el clasificador de conductas con menos fotogramas etiquetados. En el sistema, la R(2+1)D-18 parte de pesos preentrenados en Kinetics-400 (vid

## (e) Reportes, correos y notificaciones

### Reportes y formatos

- `chapters\04_analisis.tex:162` genera un reporte de diagnóstico.
- `chapters\04_analisis.tex:175` según la etapa en que se detuvo, y un botón para descargar el reporte de
- `chapters\04_analisis.tex:176` diagnóstico en PDF. El investigador no puede reiniciar el análisis desde esta
- `chapters\04_analisis.tex:202` reporte de resultados.
- `chapters\04_analisis.tex:226` & El investigador debe poder descargar los datos de resultados en formato CSV
- `chapters\04_analisis.tex:227` y XLSX desde la pantalla de resultados. El archivo debe
- `chapters\04_analisis.tex:237` separado y en PDF, el reporte de resultados (los tiempos por espécimen y
- `chapters\04_analisis.tex:239` reporte de diagnóstico (ver RN-11).
- `chapters\04_analisis.tex:258` para descargar reportes antes del borrado, conforme al atributo
- `chapters\04_analisis.tex:273` & Los resultados y reportes deben conservarse indefinidamente, aunque el video
- `chapters\04_analisis.tex:311` el reporte descargable (CSV/XLSX), para la misma vista que se descarga, junto
- `chapters\04_analisis.tex:416` experimento, subir un video, esperar el análisis y descargar el reporte
- `chapters\04_analisis.tex:431` termina exitosamente. Los resultados y reportes se conservan
- `chapters\04_analisis.tex:544` como plazo suficiente para descargar reportes antes del borrado automático
- `chapters\04_analisis.tex:619` RN-06 & Los resultados y reportes (PDF, CSV y XLSX) se conservan indefinidamente aunque
- `chapters\04_analisis.tex:637` los resultados y los reportes. Antes de ejecutarlo, el sistema muestra un diálogo de confirmación
- `chapters\04_analisis.tex:652` detiene y el sistema genera automáticamente un reporte de diagnóstico
- `chapters\04_analisis.tex:673` mezclar las cuatro conductas, y los reportes muestran la conducta activa
- `chapters\04_analisis.tex:686` calculan desde las etiquetas, y los reportes guardados del experimento se
- `chapters\04_analisis.tex:687` borran y se generan de nuevo cuando alguien los pide. La caché de reportes se invalida al corregir segundos, al
- `chapters\04_analisis.tex:706` ve» se marcan en pantalla y en el reporte de resultados. Los bloques y los
- `chapters\04_analisis.tex:844` corregidas en formato CSV, compatible con Python.
- `chapters\04_analisis.tex:870` Spring Data JPA y JdbcTemplate para el acceso a datos, Spring Mail para el correo, iText y Apache POI para los reportes.
- `chapters\04_analisis.tex:871` & Integra en un solo framework la API, la seguridad, el acceso a datos, el correo y los reportes del prototipo.
- `chapters\04_analisis.tex:925` cilindros, se genera el reporte de diagnóstico (ver RN-11).
- `chapters\04_analisis.tex:1055` asignar grupos y descargar el reporte deben ser las únicas acciones necesarias.
- `chapters\04_analisis.tex:1071` el laboratorio ya usa para sus análisis estadísticos: CSV y XLSX para datos tabulares
- `chapters\04_analisis.tex:1072` y PDF para el reporte de resultados y el reporte de diagnóstico.
- `chapters\04_analisis.tex:1090` \item El reporte generado debe incluir, al menos, la duración acumulada por conducta
- `chapters\04_analisis.tex:1094` CSV y XLSX y el reporte PDF añaden la quinta columna «Sin ver» (los segundos sin conducta),
- `chapters\04_analisis.tex:1099` reporte de diagnóstico en lugar de entregar un resultado silencioso
- `chapters\05_diseno.tex:93` sesiones de video, resultados por espécimen y conducta, y reportes generados.
- `chapters\05_diseno.tex:143` El preprocesamiento solo verifica que existan el archivo de video, los especímenes y el modelo, y lee el ancho, el alto y la duración del video, sin a
- `chapters\05_diseno.tex:147` su reporte de diagnóstico.
- `chapters\05_diseno.tex:196` reporte de diagnóstico (ver RN-11).
- `chapters\05_diseno.tex:274` Cuando el sistema registra un segundo como conducta activa, los reportes
- `chapters\05_diseno.tex:319` error y se genera el reporte de diagnóstico; si las tres
- `chapters\05_diseno.tex:328` reencola los que quedaron en procesando y los empieza de nuevo, y cancela los en pausa que ya no tengan su archivo de pausa. Si el pipeline falla por 
- `chapters\05_diseno.tex:358` reporte de diagnóstico (ver RN-11); no se entregan resultados parciales.
- `chapters\05_diseno.tex:379` REPORTE y NOTIFICACION, derivadas del experimento, aparecen en el esquema
- `chapters\05_diseno.tex:449` cuando falla, la ruta al reporte de diagnóstico (ver RN-11).
- `chapters\05_diseno.tex:456` Resultados, reportes y notificaciones.
- `chapters\05_diseno.tex:473` \item REPORTE: referencia a los archivos PDF, CSV y XLSX
- `chapters\05_diseno.tex:510` REPORTE y NOTIFICACION. Las subsecciones siguientes explican
- `chapters\05_diseno.tex:710` DELETE & \path/experiments/id & Elimina el experimento con sus grupos, videos, resultados, reportes y notificaciones. 409 si algún análisis está proce
- `chapters\05_diseno.tex:738` GET & \path/experiments/id/report/pdf & Descarga el reporte de resultados en PDF. & Investiga\-dor
- `chapters\05_diseno.tex:740` GET & \path/experiments/id/report/csv & Descarga los datos en CSV, del grupo completo o de una tanda. & Investiga\-dor
- `chapters\05_diseno.tex:742` GET & \path/experiments/id/report/xlsx & Descarga los datos en XLSX, del grupo completo o de una tanda. & Investiga\-dor
- `chapters\05_diseno.tex:745` GET & \path/experiments/id/analyses/idAnalisis/diagnostic & Descarga el reporte de diagnóstico de un análisis con error. & Autenti\-cado
- `chapters\05_diseno.tex:842` del análisis por etapas y descargar el reporte de diagnóstico cuando el análisis termina
- `chapters\05_diseno.tex:853` \subsectionPaquete 4: Resultados y reportes
- `chapters\05_diseno.tex:857` estadísticas por grupo o por tanda (media, desviación estándar y varianza), descarga de reportes en PDF, CSV y XLSX y, cuando el análisis termina, rev
- `chapters\05_diseno.tex:863` \captionCasos de uso — Paquete 4: Resultados y reportes [autoría propia].
- `chapters\05_diseno.tex:1671` Referencias & 2>\raggedright\arraybackslashp11.9cm|RF-13, RF-14, RF-15, RF-16. Reglas: RN-04, RN-17. Extiende: CU-07 (Subir video). Extendido por: CU-
- `chapters\05_diseno.tex:1675` Postcondición & 2>\raggedright\arraybackslashp11.9cm|Pipeline ejecutado por el Worker; estado visible en pantalla del investigador; al completarse exi
- `chapters\05_diseno.tex:1679` Resumen & 2>\raggedright\arraybackslashp11.9cm|El Worker toma la tarea de la cola y ejecuta el pipeline completo. El frontend consulta periódicamente 
- `chapters\05_diseno.tex:1715` 4 & El Worker no puede abrir el video o no encuentra los cilindros (ver RN-11): detiene el pipeline, genera el reporte de diagnóstico PDF (ver CU-13) 
- `chapters\05_diseno.tex:1727` \noindentDescargar reporte de diagnóstico
- `chapters\05_diseno.tex:1732` Caso de Uso & Descargar reporte de diagnóstico & Identificador: CU-13
- `chapters\05_diseno.tex:1734` Actores & 2>\raggedright\arraybackslashp11.9cm|Investigador / Worker \textsf<<system>> (genera el PDF)
- ... 67 coincidencias más (ampliar al revisar).

### Correo y notificaciones

- `chapters\05_diseno.tex:379` REPORTE y NOTIFICACION, derivadas del experimento, aparecen en el esquema
- `chapters\05_diseno.tex:409` \item USUARIO: credenciales (correo, hash de contraseña con
- `chapters\05_diseno.tex:456` Resultados, reportes y notificaciones.
- `chapters\05_diseno.tex:477` \item NOTIFICACION: avisos al investigador sobre eventos del
- `chapters\05_diseno.tex:510` REPORTE y NOTIFICACION. Las subsecciones siguientes explican
- `chapters\05_diseno.tex:567` Un segundo caso es USUARIO. El correo identifica al usuario en la
- `chapters\05_diseno.tex:571` del correo. El correo se declara como clave alterna (UNIQUE), no como
- `chapters\05_diseno.tex:573` EXPERIMENTO y NOTIFICACION.
- `chapters\05_diseno.tex:630` Los atributos dependen de la clave primaria, no del correo &
- `chapters\05_diseno.tex:632` idInstitucional como primaria; correo declarado como clave alterna
- `chapters\05_diseno.tex:685` POST & \path/auth/recover & Envía enlace de recuperación por correo. & Público
- `chapters\05_diseno.tex:710` DELETE & \path/experiments/id & Elimina el experimento con sus grupos, videos, resultados, reportes y notificaciones. 409 si algún análisis está proce
- `chapters\05_diseno.tex:763` GET & \path/notifications & Lista las notificaciones del usuario, las más recientes primero. & Autenti\-cado
- `chapters\05_diseno.tex:765` GET & \path/notifications/unread-count & Devuelve cuántas notificaciones no leídas tiene el usuario. & Autenti\-cado
- `chapters\05_diseno.tex:767` PATCH & \path/notifications/id & Marca la notificación como leída o no leída. Si no es del usuario, responde 404. & Autenti\-cado
- `chapters\05_diseno.tex:774` PATCH & \path/admin/users/id & Edita nombre, apellidos o correo; da o quita el rol de Administrador; desactiva o reactiva la cuenta (reactivar no gene
- `chapters\05_diseno.tex:811` Agrupa los flujos de acceso al sistema: inicio de sesión con correo y contraseña,
- `chapters\05_diseno.tex:867` \subsectionPaquete 5: Lista de experimentos, notificaciones y administración
- `chapters\05_diseno.tex:877` \captionCasos de uso — Paquete 5: Lista de experimentos, notificaciones y administración [autoría propia].
- `chapters\05_diseno.tex:916` Descripción & 2>\raggedright\arraybackslashp11.9cm|Permite al usuario autenticarse en el sistema mediante correo electrónico y contraseña.
- `chapters\05_diseno.tex:918` Resumen & 2>\raggedright\arraybackslashp11.9cm|El usuario introduce sus credenciales; el sistema las valida, emite un JWT y redirige a la lista de exp
- `chapters\05_diseno.tex:931` 2 & Sistema & Muestra la pantalla de inicio de sesión con campos de correo y contraseña.
- `chapters\05_diseno.tex:933` 3 & Inv. / Admin. & Introduce su correo electrónico y contraseña.
- `chapters\05_diseno.tex:950` 4 & Credenciales incorrectas o cuenta inactiva: el sistema muestra el mensaje «Correo o contraseña incorrectos», sin indicar cuál campo falló (ver RN-
- `chapters\05_diseno.tex:1024` Precondición & 2>\raggedright\arraybackslashp11.9cm|El usuario tiene una cuenta activa con correo electrónico registrado.
- `chapters\05_diseno.tex:1026` Postcondición & 2>\raggedright\arraybackslashp11.9cm|Enlace de restablecimiento enviado al correo; nueva contraseña establecida; el usuario vuelve a i
- `chapters\05_diseno.tex:1028` Descripción & 2>\raggedright\arraybackslashp11.9cm|Permite al usuario restablecer su contraseña mediante un enlace temporal enviado a su correo regist
- `chapters\05_diseno.tex:1030` Resumen & 2>\raggedright\arraybackslashp11.9cm|El usuario solicita el restablecimiento; el sistema envía un enlace de validez limitada al correo del u
- `chapters\05_diseno.tex:1043` 2 & Sistema & Solicita el correo electrónico registrado.
- `chapters\05_diseno.tex:1045` 3 & Inv. / Admin. & Introduce su correo electrónico.
- `chapters\05_diseno.tex:1047` 4 & Sistema & Envía un enlace de restablecimiento, válido 60 minutos, al correo indicado.
- `chapters\05_diseno.tex:1062` 3 & El correo no está registrado: el sistema responde con el mismo mensaje que si existiera, para no exponer información sobre cuentas registradas.
- `chapters\05_diseno.tex:1256` Descripción & 2>\raggedright\arraybackslashp11.9cm|Permite al investigador actualizar su nombre, apellidos y correo electrónico desde la pantalla de p
- `chapters\05_diseno.tex:1275` 4 & Sistema & Valida que el correo tenga un formato válido y que no esté en uso por otra cuenta.
- `chapters\05_diseno.tex:1288` 4 & El correo nuevo ya está registrado en otra cuenta: el sistema informa el conflicto y no aplica el cambio.
- `chapters\05_diseno.tex:1315` Resumen & 2>\raggedright\arraybackslashp11.9cm|El Administrador accede a la lista de usuarios y ejecuta la acción deseada: alta con contraseña tempora
- `chapters\05_diseno.tex:1328` 2 & Sistema & Muestra la lista de usuarios con nombre, correo, si es administrador o investigador, y estado.
- `chapters\05_diseno.tex:1330` 3 & Administrador & Selecciona la acción: (a) crear una cuenta nueva (ver CU-21); (b) editar nombre, apellidos o correo; (c) dar o quitar el rol de Ad
- `chapters\05_diseno.tex:1343` 4a & Intento de desactivar la última cuenta de Administrador activa, o de quitarle el rol: el sistema rechaza la acción y muestra advertencia de que d
- `chapters\05_diseno.tex:1345` 4b & Al crear una cuenta nueva, el identificador institucional o el correo ya están registrados (ver CU-21): el sistema informa el conflicto y no crea
- `chapters\05_diseno.tex:1368` Postcondición & 2>\raggedright\arraybackslashp11.9cm|Cuenta creada en la base de datos con contraseña temporal; investigador notificado por correo con
- `chapters\05_diseno.tex:1372` Resumen & 2>\raggedright\arraybackslashp11.9cm|El Administrador introduce los datos del nuevo usuario (identificador institucional, nombre, apellidos 
- `chapters\05_diseno.tex:1385` 2 & Sistema & Muestra el formulario de alta con campos: identificador institucional, nombre, apellidos y correo electrónico.
- `chapters\05_diseno.tex:1389` 4 & Sistema & Valida por separado el identificador institucional y el correo; si alguno ya existe, muestra su propio mensaje.
- `chapters\05_diseno.tex:1393` 6 & Sistema & Después de confirmar la creación, envía al investigador un correo con su correo y la contraseña temporal en texto plano.
- `chapters\05_diseno.tex:1395` 7 & Sistema & Muestra la contraseña temporal una sola vez al Administrador, como respaldo por si el correo no llega.
- `chapters\05_diseno.tex:1406` 4 & El identificador institucional ya registrado y el correo ya registrado tienen cada uno un mensaje distinto («Ya existe una cuenta con ese identifi
- `chapters\05_diseno.tex:1408` 6 & El envío del correo falla: la cuenta queda creada, la interfaz no avisa del fallo y la contraseña temporal se muestra una sola vez en el paso 7.
- `chapters\05_diseno.tex:1812` 1 & Inv. / Admin. & Accede a la pantalla de resultados desde la lista de experimentos, el detalle del experimento, el detalle de un grupo, la pantalla
- `chapters\05_diseno.tex:2061` \subsubsection*Paquete 5: Lista de experimentos, notificaciones y administración
- ... 42 coincidencias más (ampliar al revisar).

## (f) Worker, modelo y pipeline

### Worker, modelo y pipeline

- `chapters\04_analisis.tex:182` activo, inmovilidad o escalamiento \citearmario2021. Cuando ninguna clase alcanza el umbral de 0.80, pero la suma de nado y escalamiento sí lo alcanza
- `chapters\04_analisis.tex:355` operaciones interactivas cortas (navegación, filtros, consultas) el umbral estándar es
- `chapters\04_analisis.tex:383` aceptable un F1 $\geq 85$\,\% por conducta. Este umbral corresponde a la
- `chapters\04_analisis.tex:386` justificación de umbrales en la sección~\refsec:umbrales).
- `chapters\04_analisis.tex:387` & F1 $\geq 85$\,\% por conducta (primera evaluación, por clase de la red
- `chapters\04_analisis.tex:434` & Tarea programada (cron job) diaria, a cargo del worker. Aviso visible en la lista de experimentos
- `chapters\04_analisis.tex:441` & Umbral de alerta: 80\,\%. Umbral de limpieza automática: 90\,\%.
- `chapters\04_analisis.tex:442` Los valores 80/90\,\% son umbrales estándar de gestión de capacidad
- `chapters\04_analisis.tex:473` levantamiento (véase la justificación de umbrales en la
- `chapters\04_analisis.tex:474` sección~\refsec:umbrales).
- `chapters\04_analisis.tex:483` (véase la justificación de umbrales en la sección~\refsec:umbrales).
- `chapters\04_analisis.tex:491` \subsectionJustificación de umbrales y valores numéricos
- `chapters\04_analisis.tex:492` \labelsec:umbrales
- `chapters\04_analisis.tex:500` \item F1 mínimo por conducta: $\geq 85$\,\%.
- `chapters\04_analisis.tex:509` ubica en ese rango y que es consistente con los umbrales reportados en
- `chapters\04_analisis.tex:511` El F1 se calcula contra las etiquetas del conjunto de prueba propio, hechas
- `chapters\04_analisis.tex:513` El F1 por conducta se evalúa sobre el conjunto de prueba propio, con
- `chapters\04_analisis.tex:514` validación agrupada por video. El umbral se exige a las tres clases que da la red
- `chapters\04_analisis.tex:553` \item Umbral de alerta de disco: 80\,\% / limpieza: 90\,\%.
- `chapters\04_analisis.tex:554` Umbrales estándar de gestión de capacidad en sistemas de almacenamiento
- `chapters\04_analisis.tex:668` segundo con un umbral de confianza de 0.80 en tres pasos. Primero, si la
- `chapters\04_analisis.tex:689` creador, y cuando el worker termina o falla un análisis.
- `chapters\04_analisis.tex:719` sección~\refsec:umbrales.
- `chapters\04_analisis.tex:788` Sustracción de fondo por percentil \citepiccardi2004
- `chapters\04_analisis.tex:789` & El fondo se estima como el percentil 10 de cada píxel a lo largo del video,
- `chapters\04_analisis.tex:791` un percentil bajo lo borra del fondo.
- `chapters\04_analisis.tex:816` R(2+1)D-18 \citetran2018
- `chapters\04_analisis.tex:818` \citehe2016: una ResNet-18 para video. Recibe clips de 16 fotogramas y se
- `chapters\04_analisis.tex:819` preentrena con Kinetics-400 (videos de acciones humanas) para aplicar
- `chapters\04_analisis.tex:824` (ver RN-13). Se evalúa con F1 por clase.
- `chapters\04_analisis.tex:828` neuronales. Su biblioteca torchvision incluye la R(2+1)D-18 preentrenada.
- `chapters\04_analisis.tex:838` clasificación (F1, precisión y recall por conducta) y la validación
- `chapters\04_analisis.tex:884` & Empaqueta todos los servicios (backend, frontend, base de datos, worker) en
- `chapters\04_analisis.tex:929` con el F1 objetivo.
- `chapters\04_analisis.tex:950` uso de GPU. El umbral aceptable de tiempo lo fija el laboratorio
- `chapters\04_analisis.tex:1086` cómputo y su umbral aceptable lo fija el laboratorio;
- `chapters\05_diseno.tex:26` La decisión de diseño más importante fue separar el worker (proceso de segundo
- `chapters\05_diseno.tex:29` de 5 minutos se procesa. El pipeline procesa el video completo; para cada espécimen se conservan y revisan únicamente los últimos 300~s. El worker res
- `chapters\05_diseno.tex:41` contenedor ---worker--- ejecuta el pipeline de análisis de forma asíncrona, sin
- `chapters\05_diseno.tex:49` carpeta del equipo que el worker monta en solo lectura al arrancar el contenedor.
- `chapters\05_diseno.tex:71` \item Worker (Python): proceso independiente que consume tareas de la
- `chapters\05_diseno.tex:84` registro con estado «en cola». El worker obtiene las tareas mediante
- `chapters\05_diseno.tex:99` separación entre worker
- `chapters\05_diseno.tex:101` al servidor web atendiendo peticiones mientras el worker procesa un video a la vez.
- `chapters\05_diseno.tex:165` como el percentil 10 de cada píxel a lo largo del video, tomando
- `chapters\05_diseno.tex:167` oscura, un percentil bajo lo borra. La mediana, que es la opción habitual
- `chapters\05_diseno.tex:193` escala lo hace pegado a la pared exterior. Las columnas de los cilindros salen del mapa de ocupación, y las líneas de agua y de fondo, de los bordes h
- `chapters\05_diseno.tex:194` el aparato engañan a un umbral. La geometría se deduce sin medidas en píxeles escritas a mano; las proporciones respecto al ancho del cilindro son con
- `chapters\05_diseno.tex:238` espacio-temporal R(2+1)D-18 \citetran2018, preentrenada con Kinetics-400 (videos de acciones
- `chapters\05_diseno.tex:240` fotogramas del cilindro de cada espécimen y lo fusiona con una rama de medidas: los
- `chapters\05_diseno.tex:244` cada segundo con una regla de tres pasos y un umbral de 0.80. Primero, si la mayor de las
- `chapters\05_diseno.tex:252` toma el clip y las medidas de una ventana de 4~s alrededor de él (desde 1.5~s antes
- `chapters\05_diseno.tex:253` hasta 2.5~s después) y aplica la red. La ventana avanza un segundo a la vez,
- `chapters\05_diseno.tex:255` 2~s, que una decisión por bloques de 5~s esconde. Una ventana más corta vería
- `chapters\05_diseno.tex:259` sec.~\refsec:umbrales). Al agrupar los segundos de cada bloque de 5~s y tomar la
- `chapters\05_diseno.tex:271` \paragraphEstado de la red. La red de fusión está integrada en el worker; su desempeño
- `chapters\05_diseno.tex:272` se evalúa con precisión, recall y F1 por clase, con validación agrupada por video (ver OE-5 y RNF-02).
- `chapters\05_diseno.tex:286` \item Copia del video para revisión: el worker genera, al
- `chapters\05_diseno.tex:315` Al encolarse, el análisis inicia en en cola; cuando el Worker lo toma,
- `chapters\05_diseno.tex:321` en pausa (registrada en la etapa de cilindros), el Worker lo suelta para atender el siguiente de la cola y el
- `chapters\05_diseno.tex:327` en cola, al final de la cola (RN-04). Si el Worker se apaga a media análisis, al arrancar
- `chapters\05_diseno.tex:328` reencola los que quedaron en procesando y los empieza de nuevo, y cancela los en pausa que ya no tengan su archivo de pausa. Si el pipeline falla por 
- `chapters\05_diseno.tex:796` las capacidades del Investigador y además puede crear, modificar y desactivar cuentas. El Worker, que ejecuta el análisis, aparece en los diagramas co
- `chapters\05_diseno.tex:843` en error (ver RN-11). El pipeline lo ejecuta el Worker de forma autónoma;
- `chapters\05_diseno.tex:1565` Postcondición & 2>\raggedright\arraybackslashp11.9cm|Registro de análisis creado en estado «en cola»; Worker disponible para procesarlo en la siguient
- `chapters\05_diseno.tex:1569` Resumen & 2>\raggedright\arraybackslashp11.9cm|Una vez almacenado el video, el sistema crea un registro en la tabla ANALISIS con estado «en cola», y e
- `chapters\05_diseno.tex:1667` Actores & 2>\raggedright\arraybackslashp11.9cm|Investigador (solo observa) / Worker \textsf<<system>> (ejecuta el pipeline)
- `chapters\05_diseno.tex:1673` Precondición & 2>\raggedright\arraybackslashp11.9cm|Tarea de análisis encolada; Worker disponible para procesar; sesión activa del investigador.
- `chapters\05_diseno.tex:1675` Postcondición & 2>\raggedright\arraybackslashp11.9cm|Pipeline ejecutado por el Worker; estado visible en pantalla del investigador; al completarse exi
- `chapters\05_diseno.tex:1677` Descripción & 2>\raggedright\arraybackslashp11.9cm|El Worker ejecuta el pipeline de análisis conductual de forma autónoma en tres etapas secuenciales.
- `chapters\05_diseno.tex:1679` Resumen & 2>\raggedright\arraybackslashp11.9cm|El Worker toma la tarea de la cola y ejecuta el pipeline completo. El frontend consulta periódicamente 
- `chapters\05_diseno.tex:1692` 2 & Worker & Recupera la tarea de la cola de análisis mediante polling a la tabla ANALISIS.
- `chapters\05_diseno.tex:1694` 3 & Worker & Verifica el archivo, los especímenes y el modelo, y lee el ancho, el alto y la duración.
- `chapters\05_diseno.tex:1696` 4 & Worker & Alinea la cámara, construye el modelo de fondo, localiza los cilindros y la línea de agua y mide al espécimen en cada cilindro.
- `chapters\05_diseno.tex:1698` 5 & Worker & Ejecuta la 3.ª etapa: clasificación de conductas (nado activo, inmovilidad, escalamiento y conducta activa).
- `chapters\05_diseno.tex:1702` 7 & Worker & Registra los resultados en la base de datos al completar el pipeline y genera la copia del video recortada en H.264 para la revisión (ver
- `chapters\05_diseno.tex:1715` 4 & El Worker no puede abrir el video o no encuentra los cilindros (ver RN-11): detiene el pipeline, genera el reporte de diagnóstico PDF (ver CU-13) 
- `chapters\05_diseno.tex:1717` 5 & Hay tres segundos seguidos sin ver al espécimen: el Worker guarda una imagen fija tomada a la mitad de esos tres segundos, deja el análisis «en pa
- `chapters\05_diseno.tex:1734` Actores & 2>\raggedright\arraybackslashp11.9cm|Investigador / Worker \textsf<<system>> (genera el PDF)
- `chapters\05_diseno.tex:1740` Precondición & 2>\raggedright\arraybackslashp11.9cm|Pipeline detenido por error (no se pudo abrir el video o no se encontraron los cilindros, ver RN-1
- `chapters\05_diseno.tex:1744` Descripción & 2>\raggedright\arraybackslashp11.9cm|El Worker genera automáticamente un PDF de diagnóstico cuando el pipeline falla porque no puede abr
- `chapters\05_diseno.tex:1746` Resumen & 2>\raggedright\arraybackslashp11.9cm|El Worker genera y almacena el PDF de diagnóstico al detener el pipeline por error. El sistema pone dis
- `chapters\05_diseno.tex:1763` 4 & Sistema & Sirve el archivo PDF generado por el worker al navegador del investigador.
- `chapters\05_diseno.tex:1873` 2 & Sistema & Genera o recupera el archivo de la vista pedida. El reporte guardado se regenera cuando un evento lo invalida (corregir segundos, reinic
- `chapters\05_diseno.tex:1979` 3 & Sistema & Muestra, si el usuario puede corregir, la copia del video en formato H.264 que generó el worker al terminar el análisis, la línea de tie
- `chapters\05_diseno.tex:2294` Actores & 2>\raggedright\arraybackslashp11.9cm|Worker \textsf<<system>>
- `chapters\05_diseno.tex:2304` Descripción & 2>\raggedright\arraybackslashp11.9cm|El Worker ejecuta diariamente, de forma automática, una tarea programada que elimina los archivos d
- `chapters\05_diseno.tex:2306` Resumen & 2>\raggedright\arraybackslashp11.9cm|El Worker identifica los videos que expiran en 7 días o menos y emite avisos en la lista de experimento
- `chapters\05_diseno.tex:2317` 1 & Worker & Ejecuta la tarea programada de expiración (cron diario).
- `chapters\05_diseno.tex:2319` 2 & Worker & Consulta la base de datos para identificar videos con análisis exitoso hace $\geq 23$ días y $< 30$ días.
- ... 49 coincidencias más (ampliar al revisar).

## (g) Despliegue

### Hostinger, contenedores, .env, versionado, respaldos

- `back\apendice_C.tex:219` \section*Sección 7. Datos, retención y volumen
- `chapters\01_introduccion.tex:118` \item Costo de tiempo: el volumen de anotación manual limita cuántos
- `chapters\01_introduccion.tex:256` se instala con Docker en un equipo de cómputo del laboratorio, sin infraestructura
- `chapters\01_introduccion.tex:442` Entorno Spring Boot\,/\,PostgreSQL\,/\,Docker, esquema de la base de datos y API REST
- `chapters\01_introduccion.tex:463` Empaquetado con Docker Compose, manuales y material de defensa
- `chapters\01_introduccion.tex:530` para control de versiones y Docker para empaquetar el sistema.
- `chapters\02_estado_arte.tex:57` si fueran un volumen tridimensional--- en lugar de cuadros individuales. Eso le permite
- `chapters\02_estado_arte.tex:242` filtrar sobre una imagen 2D, filtran sobre un volumen de $T$ cuadros consecutivos.
- `chapters\03_marco_teorico.tex:348` \subsectionContenedorización con Docker
- `chapters\03_marco_teorico.tex:350` Docker permite empaquetar una aplicación con todas sus dependencias en una imagen
- `chapters\03_marco_teorico.tex:351` reproducible \citemerkel2014. Docker Compose orquesta múltiples contenedores
- `chapters\03_marco_teorico.tex:355` hardware, software u operación a otro. Docker empaqueta el sistema con todas sus dependencias, de modo que se ejecuta de la misma forma en cualquier e
- `chapters\04_analisis.tex:448` & El sistema debe poder empaquetarse con Docker Compose para ejecutarse igual
- `chapters\04_analisis.tex:449` en cualquier equipo con Docker, sin dependencias adicionales en el sistema
- `chapters\04_analisis.tex:557` se ajustan según el volumen real de videos generados (ver RNF-09).
- `chapters\04_analisis.tex:830` Compatible con Docker para el empaquetado.
- `chapters\04_analisis.tex:883` Docker + Docker Compose \citemerkel2014
- `chapters\04_analisis.tex:885` contenedores y los levanta con un solo comando.
- `chapters\04_analisis.tex:887` \citeiso25010. El laboratorio no instala nada más allá de Docker.
- `chapters\04_analisis.tex:1015` especializada: cualquier equipo con Docker instalado puede correr el prototipo, lo que
- `chapters\04_analisis.tex:1028` ImageNet \citemeng2024_dsaan, lo que da respaldo empírico a la viabilidad de esa
- `chapters\04_analisis.tex:1038` Docker empaqueta el sistema con todas sus dependencias, de modo que se ejecuta de la misma forma en cualquier equipo que tenga Docker \citemerkel2014.
- `chapters\04_analisis.tex:1153` Herramientas de desarrollo (Java, Spring Boot, Python, React, PostgreSQL, Docker, OpenCV,
- `chapters\04_analisis.tex:1196` computadora y Docker)
- `chapters\04_analisis.tex:1270` PSF (Python), Apache~2.0 (Spring Boot, Docker y OpenCV), BSD-3-Clause (scikit-learn y PyTorch), MIT (React) y
- `chapters\04_analisis.tex:1312` básico de Python y Docker. La documentación técnica de este documento y el
- `chapters\05_diseno.tex:40` contenedores Docker independientes: web (interfaz servida por nginx), api (backend) y db (base de datos). Un cuarto
- `chapters\05_diseno.tex:41` contenedor ---worker--- ejecuta el pipeline de análisis de forma asíncrona, sin
- `chapters\05_diseno.tex:45` contenedor y cómo se comunican entre sí. Se distinguen cuatro grupos: la capa de
- `chapters\05_diseno.tex:49` carpeta del equipo que el worker monta en solo lectura al arrancar el contenedor.
- `chapters\05_diseno.tex:89` un contenedor y una dependencia más; con el volumen del laboratorio, de
- `chapters\05_diseno.tex:98` La separación en contenedores empaqueta cada servicio con sus dependencias. La
- `chapters\05_diseno.tex:1368` Postcondición & 2>\raggedright\arraybackslashp11.9cm|Cuenta creada en la base de datos con contraseña temporal; investigador notificado por correo con
- `chapters\05_diseno.tex:1395` 7 & Sistema & Muestra la contraseña temporal una sola vez al Administrador, como respaldo por si el correo no llega.
- `chapters\05_diseno.tex:1490` Postcondición & 2>\raggedright\arraybackslashp11.9cm|Archivo almacenado en el volumen compartido; si el video es del Día~2, tarea de análisis encolada
- `chapters\05_diseno.tex:1563` Precondición & 2>\raggedright\arraybackslashp11.9cm|Video validado en formato .mp4 o .mov, reproducible y en horizontal; almacenado en el volumen comp
- `chapters\05_diseno.tex:1580` 1 & Sistema & Confirma que el video ha sido almacenado exitosamente en el volumen compartido.
- `chapters\05_diseno.tex:2323` 4 & Worker & Al cumplirse los 30 días, elimina el archivo de video del volumen de almacenamiento.
- `chapters\05_diseno.tex:2325` 5 & Worker & Elimina el archivo físico del volumen de almacenamiento; la fila de VIDEO permanece en la base de datos (no puede eliminarse mientras ANA
- `chapters\05_diseno.tex:2992` el sistema envía la contraseña temporal por correo en texto plano, después de confirmar la creación, y además se la muestra una sola vez al Administra
- `chapters\06_desarrollo.tex:4` las tecnologías, la arquitectura en contenedores, cada uno de los servicios (backend,
- `chapters\06_desarrollo.tex:15` contenedores, de modo que el laboratorio no necesita instalar más que Docker.
- `chapters\06_desarrollo.tex:29` Worker & Python 3.12 con PyTorch 2.14 y torchvision 0.29 (CPU), OpenCV 5.0 sin interfaz gráfica, NumPy 2.5, pandas 3.1, scikit-learn 1.9, psycopg2 2.9
- `chapters\06_desarrollo.tex:33` Empaquetado & Docker Compose. El sistema se arranca con portable\textbackslash iniciar.bat, que fija la versión y ejecuta docker compose up.
- `chapters\06_desarrollo.tex:42` \sectionArquitectura en contenedores
- `chapters\06_desarrollo.tex:44` El sistema se compone de cuatro servicios que se levantan juntos. La Tabla~\reftab:contenedores
- `chapters\06_desarrollo.tex:50` \labeltab:contenedores
- `chapters\06_desarrollo.tex:55` db & Base de datos PostgreSQL. El esquema se crea la primera vez, con el volumen vacío. & Solo interno, puerto 5432.
- `chapters\06_desarrollo.tex:67` y por el volumen compartido. La cola de análisis es una tabla de la base: no hay Redis ni un sistema
- `chapters\06_desarrollo.tex:70` El volumen videos\_reportes se monta en /data/archivos tanto en backend como
- `chapters\06_desarrollo.tex:73` base guarda son relativas a la raíz de este volumen. El modelo entrenado no va dentro de la imagen: el
- `chapters\06_desarrollo.tex:85` Los parámetros de funcionamiento salen de un archivo .env, nunca del código. Los más
- `chapters\06_desarrollo.tex:90` docker compose up; el primer Administrador se crea con los datos ADMIN\_* del archivo .env.
- `chapters\06_desarrollo.tex:106` \item Guardado de videos. El video se guarda en el volumen con el nombre del identificador del
- `chapters\06_desarrollo.tex:174` Los resultados se escriben solo en la base y en el volumen. Cada notificación que el worker crea se
- `chapters\06_desarrollo.tex:178` madrugada (WORKER\_DAILY\_HOUR, por defecto las 3 a. m.). Son seis: el respaldo diario de la base con
- `chapters\06_desarrollo.tex:179` pg\_dump, en una carpeta del equipo fuera de los volúmenes de Docker; el borrado de los videos vencidos; la
- `chapters\06_desarrollo.tex:210` abrir en el volumen (si no está, el análisis termina en error) y lo lee con ffprobe; si el archivo está dañado o
- `chapters\06_desarrollo.tex:362` Los reportes se guardan en una carpeta por experimento dentro del volumen, y la tabla de reportes guarda la ruta y la
- `chapters\06_desarrollo.tex:417` reportes, el respaldo, los tiempos y la vigilancia del disco. Además, se hizo una prueba de carga con cuatro sesiones simultáneas (consultas y revisió
- `front\glosario.tex:107` Docker
- `front\glosario.tex:108` & Plataforma de contenedorización que empaqueta una aplicación junto con todas
- `front\glosario.tex:110` despliega como cuatro contenedores orquestados: web (interfaz), api
- `front\glosario.tex:309` tareas y ejecuta el pipeline de análisis completo. Al correr en un contenedor
- `front\glosario.tex:310` Docker separado, permite que el backend siga respondiendo peticiones HTTP

## (h) Pruebas y cifras

### Pruebas y cantidades

- `chapters\04_analisis.tex:391` prueba propio.
- `chapters\04_analisis.tex:404` & Autenticación con JWT verificada en pruebas de integración. Acceso a datos
- `chapters\04_analisis.tex:412` en prueba funcional.
- `chapters\04_analisis.tex:419` & Prueba con al menos un usuario real del laboratorio, con los videos
- `chapters\04_analisis.tex:426` & Pruebas en los tres navegadores en sus versiones actuales al cierre de
- `chapters\04_analisis.tex:455` pueda reconfigurarse para paradigmas conductuales distintos a la prueba de nado forzado (forced swim test, FST) sin
- `chapters\04_analisis.tex:511` El F1 se calcula contra las etiquetas del conjunto de prueba propio, hechas
- `chapters\04_analisis.tex:513` El F1 por conducta se evalúa sobre el conjunto de prueba propio, con
- `chapters\04_analisis.tex:710` tal como la describen Craft et~al.\ \citecraft2010 para la prueba de nado
- `chapters\04_analisis.tex:942` & Se etiqueta el conjunto de prueba propio con el etiquetador del equipo y
- `chapters\04_analisis.tex:957` y se ejecuta una prueba de integración de extremo a extremo antes de agregar
- `chapters\04_analisis.tex:1018` \subsubsectionSimulación, modelado y pruebas
- `chapters\04_analisis.tex:1023` cilindros simultáneos. Esa prueba reduce el riesgo técnico de la etapa de localización
- `chapters\04_analisis.tex:1106` Estos cuatro criterios se comprueban con los videos del laboratorio y las métricas de clasificación de RNF-02.
- `chapters\06_desarrollo.tex:6` el correo y las cuentas, y las pruebas automatizadas. Las reglas de negocio que cada parte cumple
- `chapters\06_desarrollo.tex:27` Interfaz & React 18.3 con React Router 7 y Axios 1.20, compilado con Vite 8 en Node 22. Pruebas con Vitest 5. Se sirve con nginx 1.27.
- `chapters\06_desarrollo.tex:198` Preprocesamiento & Comprueba que el archivo se pueda abrir y lee sus dimensiones y su duración. Comprueba que los especímenes y el modelo estén dispon
- `chapters\06_desarrollo.tex:209` Esta etapa solo comprueba el archivo y no modifica el video. El worker verifica que el video se pueda
- `chapters\06_desarrollo.tex:211` no es un video, el análisis termina en error; un video con duración cero ya se rechaza al subirlo. Después comprueba que
- `chapters\06_desarrollo.tex:221` \item Alineación. Toma un cuadro de referencia en la mitad del video (si no alcanza, prueba otros
- `chapters\06_desarrollo.tex:222` puntos) y lo compara con los demás cuadros mediante puntos característicos ORB, con prueba de razón de 0.75 y un
- `chapters\06_desarrollo.tex:412` \sectionPruebas automatizadas
- `chapters\06_desarrollo.tex:414` El sistema tiene pruebas en sus tres partes. El backend tiene 162 pruebas JUnit repartidas en 16 clases; las de
- `chapters\06_desarrollo.tex:415` integración corren contra una base PostgreSQL de prueba. La interfaz tiene 202 pruebas con Vitest, jsdom y Testing
- `chapters\06_desarrollo.tex:416` Library. El worker tiene 71 pruebas con unittest, que cubren los correos, el diagnóstico, la pausa, los
- `chapters\06_desarrollo.tex:417` reportes, el respaldo, los tiempos y la vigilancia del disco. Además, se hizo una prueba de carga con cuatro sesiones simultáneas (consultas y revisió

## (i) Números y textos concretos citados del sistema

### Cifras (segundos, MB, horas, días, puertos, porcentajes)

- `chapters\04_analisis.tex:64` restablecimiento al correo registrado; el enlace dura 60~minutos.
- `chapters\04_analisis.tex:117` 300~segundos del video de Día~2 (si dura menos, lo analiza completo; el resto
- `chapters\04_analisis.tex:170` o pasen 72~horas (ver RN-17).
- `chapters\04_analisis.tex:193` unos 2~segundos) que el análisis manual por bloques de 5~segundos no
- `chapters\04_analisis.tex:195` 5~segundos, los resultados también se muestran en bloques de 5~segundos,
- `chapters\04_analisis.tex:256` 7~días de ser eliminado automáticamente, indicando el nombre del experimento
- `chapters\04_analisis.tex:257` y la fecha de vencimiento exacta. El período de 7~días da tiempo suficiente
- `chapters\04_analisis.tex:266` & El sistema debe borrar automáticamente los archivos de video 30~días después
- `chapters\04_analisis.tex:340` los 30 días por falta de espacio (ver RN-05). Los
- `chapters\04_analisis.tex:342` el envío falla, el aviso permanece en el panel de notificaciones. «Cancelado» se notifica solo cuando el análisis se cancela por plazo. Las notificaci
- `chapters\04_analisis.tex:356` de 1 a 3 segundos; para operaciones de procesamiento intensivo (análisis de video) el
- `chapters\04_analisis.tex:430` & Los videos se borran automáticamente 30~días después de que el análisis
- `chapters\04_analisis.tex:433` de 7~días de ser borrado.
- `chapters\04_analisis.tex:530` \item Sin duración mínima de episodio; bloques de 5~segundos como referencia.
- `chapters\04_analisis.tex:533` a 5~segundos. El sistema no adopta ese mínimo: asigna una conducta a cada
- `chapters\04_analisis.tex:534` segundo y detecta conductas breves de unos 2~segundos, que es justo lo que el
- `chapters\04_analisis.tex:536` referencia: los resultados también se agrupan en bloques de 5~segundos, con la
- `chapters\04_analisis.tex:542` \item Período de retención de videos: 30~días.
- `chapters\04_analisis.tex:611` RN-05 & Los videos se borran automáticamente 30~días después de que el análisis
- `chapters\04_analisis.tex:613` menos 7~días de anticipación. Excepción: si el disco supera el 90\,\%, se
- `chapters\04_analisis.tex:615` los 30~días y se notifica al investigador de cada experimento afectado
- `chapters\04_analisis.tex:697` RN-15 & Los resultados también se agrupan en bloques de 5~segundos, la unidad de la
- `chapters\04_analisis.tex:717` cada 5~segundos y no la predominante del periodo. El empate en el primer lugar
- `chapters\04_analisis.tex:734` Si no hay respuesta en 72~horas, el análisis se cancela. Mientras el análisis espera, el sistema atiende el
- `chapters\04_analisis.tex:749` a segundo, y que los videos se borran 30~días después de un análisis exitoso (RN-05).
- `chapters\04_analisis.tex:978` de retención de 30~días.
- `chapters\04_analisis.tex:1011` dispone de GPU, Google Colab ofrece hasta 12~horas de GPU por sesión de forma gratuita,
- `chapters\04_analisis.tex:1112` el recurso humano: dos integrantes que destinan aproximadamente 500~horas cada uno
- `chapters\04_analisis.tex:1147` & \$0 --- el nivel gratuito ofrece hasta 12~horas de GPU por sesión.
- `chapters\04_analisis.tex:1293` cualquier lugar. La política de borrar videos a los 30~días evita que el disco crezca
- `chapters\05_diseno.tex:29` de 5 minutos se procesa. El pipeline procesa el video completo; para cada espécimen se conservan y revisan únicamente los últimos 300~s. El worker res
- `chapters\05_diseno.tex:78` las tareas programadas: el borrado de los videos a los 30~días, el aviso de
- `chapters\05_diseno.tex:119` El pipeline recibe un video del FST, analiza el video completo, conserva los resultados de sus últimos 300 segundos y produce
- `chapters\05_diseno.tex:299` Además, los resultados se muestran en bloques de 5~segundos, la unidad de la técnica de
- `chapters\05_diseno.tex:323` vuelve a en cola, por delante de los que llegaron después; al retomarse, el análisis se procesa desde el principio y el recuadro corregido rige desde 
- `chapters\05_diseno.tex:687` POST & \path/auth/reset & Establece la nueva contraseña con el enlace de restablecimiento (vigente 60 minutos). & Público
- `chapters\05_diseno.tex:755` POST & \path/experiments/id/analyses/idAnalisis/video-token & Emite un permiso temporal de 120 minutos para ver el video. & Creador o Admin
- `chapters\05_diseno.tex:1047` 4 & Sistema & Envía un enlace de restablecimiento, válido 60 minutos, al correo indicado.
- `chapters\05_diseno.tex:1064` 5 & El enlace ya expiró (pasaron más de 60 minutos): el sistema informa que el enlace no es válido y solicita reiniciar el proceso desde el paso 1.
- `chapters\05_diseno.tex:1140` Postcondición & 2>\raggedright\arraybackslashp11.9cm|Contraseña actualizada en la base de datos; marca de «cambio obligatorio» eliminada; acceso habil
- `chapters\05_diseno.tex:1719` 5 & El usuario pulsa «Cancelar análisis» durante la pausa (el sistema pide confirmar con «¿Cancelar el análisis? No se puede reanudar: habrá que subir
- `chapters\05_diseno.tex:2131` Descripción & 2>\raggedright\arraybackslashp11.9cm|Pantalla principal del investigador. Muestra todos los experimentos del laboratorio con nombre, fec
- `chapters\05_diseno.tex:2148` 3 & Sistema & Verifica si algún video expira en 7 días o menos y muestra aviso con nombre del experimento y fecha exacta de eliminación (ver RF-24).
- `chapters\05_diseno.tex:2300` Precondición & 2>\raggedright\arraybackslashp11.9cm|Análisis del video completado exitosamente; han transcurrido 30 días desde la fecha de análisis ex
- `chapters\05_diseno.tex:2304` Descripción & 2>\raggedright\arraybackslashp11.9cm|El Worker ejecuta diariamente, de forma automática, una tarea programada que elimina los archivos d
- `chapters\05_diseno.tex:2306` Resumen & 2>\raggedright\arraybackslashp11.9cm|El Worker identifica los videos que expiran en 7 días o menos y emite avisos en la lista de experimento
- `chapters\05_diseno.tex:2323` 4 & Worker & Al cumplirse los 30 días, elimina el archivo de video del volumen de almacenamiento.
- `chapters\05_diseno.tex:2336` 4 & El uso de disco supera el 90\,\%: el sistema borra primero los videos más antiguos aunque no hayan cumplido 30 días y notifica al investigador de 
- `chapters\05_diseno.tex:2455` persiste la notificación y cómo el frontend la consulta al entrar a cada pantalla y cada 30 segundos (sin consultar con la pestaña oculta). Las notifi
- `chapters\05_diseno.tex:2764` cuando un video está a menos de 7~días de ser eliminado automáticamente (RF-24).
- `chapters\05_diseno.tex:2883` análisis»); si no responde en 72~horas, el análisis se cancela (RN-17). En la pantalla de progreso, un análisis en pausa solo muestra el enlace «Ajust
- `chapters\05_diseno.tex:2899` \caption[Pantalla de pausa del análisis [autoría propia].]Pantalla de pausa: imagen fija del instante en que no se ve al espécimen, con el recuadro de
- `chapters\06_desarrollo.tex:55` db & Base de datos PostgreSQL. El esquema se crea la primera vez, con el volumen vacío. & Solo interno, puerto 5432.
- `chapters\06_desarrollo.tex:57` api & Backend: API REST, autenticación, validación de archivos y creación de análisis en cola. & Solo interno, puerto 8000. Límite de memoria de 1.5 G
- `chapters\06_desarrollo.tex:59` worker & Toma los análisis en cola, los procesa, escribe resultados, avisa y ejecuta las tareas programadas. & Sin puerto. Límite de memoria de 5 GB.
- `chapters\06_desarrollo.tex:103` 2048 MB (MAX\_UPLOAD\_MB). La extensión se valida también en la interfaz antes de subir. El
- `chapters\06_desarrollo.tex:154` El worker es un proceso de Python independiente del servidor web. Consulta la base cada 5 segundos
- `chapters\06_desarrollo.tex:163` \item Control de tiempo. Cada paso del pipeline tiene un límite de una hora, y la copia para revisión, de 30 minutos.
- `chapters\06_desarrollo.tex:248` la red recibe un clip de 16 cuadros a 4 cuadros por segundo, es decir, una ventana de 4 segundos que va de un segundo
- `chapters\06_desarrollo.tex:284` esos 300 segundos. Antes de guardarlos, el worker los renumera de 1 a 300 para que coincidan con el video
- `chapters\06_desarrollo.tex:308` \item Si el usuario cancela, el análisis pasa a cancelado sin notificación. Si pasan 72 horas sin respuesta
- `chapters\06_desarrollo.tex:311` puede ocurrir un poco después de las 72 horas.
- `chapters\06_desarrollo.tex:334` cuatro conductas más los sin ver suman 60 segundos y el 100\,\% del minuto.
- `chapters\06_desarrollo.tex:382` tiempo de espera de 10 segundos. El backend envía los correos de recuperación de contraseña y de cuenta nueva.
- `chapters\06_desarrollo.tex:405` El token de sesión dura 168 horas (una semana) por defecto, y ese plazo es configurable. El servidor no guarda una
- `chapters\06_desarrollo.tex:409` La recuperación de contraseña usa un enlace que vence a los 60 minutos y lleva su vencimiento firmado dentro, así que no

### Ítems ya identificados por orquestador_web / orquestador_latex
- **RN-18** (aviso de privacidad y su aceptación): está en `chapters/04_analisis.tex` como cambio **sin commit** (tabla de reglas, tras RN-17); el sistema no lo tiene. Además esa fila termina con una sola barra invertida en vez de dos.
- **«Almacenamiento cifrado»**: el documento lo afirma; el sistema solo guarda la contraseña con hash. Ubicación: `chapters/04_analisis.tex:1255` («almacenamiento cifrado y acceso autenticado con JWT»); RNF de contraseñas con sal en `chapters/04_analisis.tex:408` (ese sí coincide con bcrypt).
- **«Gráficas de barras»**: mención que orquestador_web dice retirada; el sistema tiene hoy seis gráficas. Búsqueda de «barras» en `chapters/01-06`: sin coincidencias, o sea que ya no está en el .tex; falta ver qué dice el documento de las gráficas de resultados (buscar `gráfica`).
- **Apéndice D (diccionario)**: falta el CHECK `video.duracion > 0`, los 5 índices (el quinto es `ix_notificacion_experim`) y los 11 valores por defecto (confirmado por orquestador_web el 9-nov).

## 2. Por agregar (el sistema lo tiene y el documento no)

Fase 3 (9-nov). Lista de orquestador_web: `D:\proyectos\fst\FALTA_EN_DOCUMENTO.md`. **Solo se propone ubicación; no se editó nada.** Las líneas son del árbol de trabajo actual. «Confirmación» la llena orquestador_web.

Referencias de estructura. **Cap. 5:** §Diseño de la API REST `05_diseno.tex:644`, tabla de endpoints `:681-778` (cierra en `:780`); §Casos de uso `:784`, especificación `:882`; §Diseño de la interfaz web `:2700` (Resultados `:2903`, Revisión `:2956`). **Cap. 6:** §Entorno `06_desarrollo.tex:9`, §Backend `:92`, §Interfaz `:125`, §Worker `:152`, §Progreso, resultados y reportes `:317`, §Pruebas `:412`. **Apéndice D:** `back/apendice_D.tex`, dominios `:29`, columnas por tabla `:69-235`.

### 2A. Nuevo desde producción (posterior a `15489f4`)

| ID | Posición propuesta | Tabla / CU / RF nuevo | Confirmación |
|---|---|---|---|
| N-01 `GET /results/charts` | `05_diseno.tex`, tabla de endpoints, fila nueva tras `:734` (`/results/blocks`) | no | pendiente |
| N-02 `GET /results/seconds` | misma tabla, fila nueva tras N-01 (`:734`) | no | pendiente |
| N-03 `GET /report/excel` | misma tabla, junto a pdf/csv/xlsx: fila nueva tras `:742` (`/report/xlsx`) | no | pendiente |
| N-04 `GET /dev/modelo-actual` | misma tabla: grupo nuevo «Modo desarrollador» tras `:778` (`/admin/system`), con aviso de que responde 404 sin el modo; además cap. 6 §Backend (`06_desarrollo.tex:92-124`) | no (grupo de filas) | pendiente |
| N-05 Pantalla de resumen de resultados del experimento | `05_diseno.tex:2903` (§Resultados del experimento), párrafo nuevo antes de «Cuatro pestañas» (`:2905`); apoyo en CU-14 (`:1787`) y RF-19 a RF-22 (`04_analisis.tex:207-225`); posible maqueta nueva | probable: RF o ampliación de RF-19; CU-14 se amplía (no CU nuevo) | pendiente |
| N-06 Galería de seis gráficas | **Solo ubicar; decide el usuario.** Cabrían en: `05_diseno.tex:2903-2930` (§Resultados, con maqueta), RF-22 (`04_analisis.tex:225`) / CU-14 (`:1787`), y `06_desarrollo.tex:328` (§Resultados). Recordar que Sandino no las pidió | si entran: RF nuevo en la familia «Resultados» (`04_analisis.tex:207-230`) | pendiente |
| N-07 Vista «Segundo a segundo» | `05_diseno.tex:2905-2906` (lista de pestañas, ver C-06); `04_analisis.tex:190` (RF-18, bloques de 5 s) o RF nuevo tras RF-22 (`:225`); `06_desarrollo.tex:328` | probable: RF nuevo o ampliar RF-18 | pendiente |
| N-08 Hoja «Segundo a segundo» del Excel | `04_analisis.tex:225` (RF-22, descarga de datos); CU-15 (`05_diseno.tex:1846`); `05_diseno.tex:2923` («descarga en PDF, CSV y XLSX»); `06_desarrollo.tex:354` (§Reportes y caché) | no (se amplía RF-22/CU-15) | pendiente |
| N-09 Cinco pestañas y selector de grupo y tanda | `05_diseno.tex:2905-2906` (corregir; es C-06) | no | pendiente |
| N-10 «Agregar otra tanda» en carga de video | `05_diseno.tex:2815` (§Creación de experimento y carga de video); CU-07 (`:1480`); RF-08 a RF-10 (`04_analisis.tex:106-126`) | no (se amplía CU-07) | pendiente |
| N-11 Aviso de lo primero que falta al guardar | `05_diseno.tex:2815-2870`, una frase en la pantalla de carga (detalle menor) | no | pendiente |
| N-12 Versión del sistema abajo a la derecha | `05_diseno.tex:2700-2707` (introducción de §Diseño de la interfaz web, elementos globales); `06_desarrollo.tex:125` (§Interfaz) | no | pendiente |
| N-13 Modo desarrollador (franja roja, modelo en reportes, modelo en carga) | `06_desarrollo.tex:85-90` (configuración por `.env`) y `:92` (§Backend), con una frase en `:125` (§Interfaz) y en `:354` (§Reportes); en el cap. 5 solo si se agregan sus endpoints (N-04, B-02) | no | pendiente |
| N-14 Revisión con tema claro | **No aplica:** el documento no menciona el tema oscuro (verificado en `05_diseno.tex:2956`, §Revisión) | no | pendiente |
| N-15 Cifras de pruebas actuales | `06_desarrollo.tex:414-416` (es C-10) | no | pendiente |

### 2B. Ya estaba en producción y el documento nunca lo tuvo

| ID | Posición propuesta | Confirmación |
|---|---|---|
| B-01 `GET /health` | `05_diseno.tex`, tabla de endpoints: fila nueva antes de `/auth/login` (`:681`) o grupo «Sistema» tras `:778` | pendiente |
| B-02 `GET /dev/salida-modelo` | misma tabla, grupo «Modo desarrollador» (con N-04) | pendiente |
| B-03 CHECK `video.duracion > 0` | `back/apendice_D.tex:164` (columna `duracion`, celda «Restricción») | pendiente |
| B-04 Once valores por defecto | `back/apendice_D.tex:69-235`: o columna nueva «Por defecto» en la tabla de columnas (encabezados `:74` y `:79`) o frase en la «Descripción» de cada columna; ver nota abajo | pendiente |
| B-05 Cinco índices | `back/apendice_D.tex`, sección y tabla nuevas tras `:235` (fin de «Columnas por tabla»), nombre real `ix_notificacion_experim`; o antes de `:69` | pendiente |
| B-06 Dos migraciones | `back/apendice_D.tex:8-27` (nota en la introducción) o `06_desarrollo.tex:42-91` (§Arquitectura en contenedores, inicialización de la base). La columna `nombreOriginal` ya está en `apendice_D.tex:162`; falta solo decir que llegó por migración, y el documento no afirma `uq_reporte_formato` (el apéndice solo da UK a `ruta`, `:214`) | pendiente |

Nota B-04: si se añade la columna «Por defecto», la tabla (`longtable` de 5 columnas, `apendice_D.tex:72`) pasa a 6 y hay que reajustar anchos. La alternativa sin tocar columnas es una sola tabla corta de valores por defecto, después de los índices.

Observación 3 de orquestador_web, comprobada: el apéndice D **ya** lista los CHECK de `tanda.ordinal` (CK ≥ 1), `tanda.nCilindros` (2 a 4), `especimen.numeroCilindro` (1 a 4) y `segundo.segundo` (1 a 300), además de `analisis.rutaDiagnostico` (solo con estado error, `:183`). Lo único que falta es `video.duracion > 0` (B-03).

## 3. Por corregir o retirar (el documento lo afirma y el sistema no lo tiene o lo tiene distinto)

Sin proponer redacción en C-02 a C-05 (decisión del usuario): solo ubicación.

| ID | `archivo.tex:línea` | Dónde más aparece / efecto | Acción |
|---|---|---|---|
| C-01 Subir video lo hace «Investigador» | `05_diseno.tex:704` | CU-07 (`:1480`) y RN relacionadas: revisar que digan «creador» | corregir celda de rol a «Creador» (el texto de `:2883` ya dice «quien subió los videos») |
| C-02 RN-03: 20 min y 5 min | `04_analisis.tex:593` | repetido en `05_diseno.tex` (pantalla de carga, `:2815-2870`) y CU-07 (`:1480`) si cita las duraciones | **decisión del usuario**: ubicar solamente |
| C-03 RN-17: cancelar no crea notificación | `04_analisis.tex:727` | `05_diseno.tex:2883` (cancelación a las 72 h) y CU de pausa (`:1671`, RN-17) | **decisión del usuario**: ubicar solamente |
| C-04 RN-18: aviso de privacidad y términos | `04_analisis.tex:742` (**cambio sin commit**: no está en HEAD) | si se conserva: RF-01/RF-05 (`:80`), `05_diseno.tex:2708-2760` (inicio de sesión y primer acceso), factibilidad legal (`04_analisis.tex`, §Factibilidad legal); la fila tiene además un `\` suelto | **decisión del usuario**: ubicar solamente |
| C-05 «Almacenamiento cifrado» | `04_analisis.tex:1255` | RNF de contraseñas con sal, `04_analisis.tex:408` (este sí coincide con bcrypt) | **decisión del usuario**: ubicar solamente |
| C-06 Cuatro pestañas | `05_diseno.tex:2905-2906` | `06_desarrollo.tex:328` (§Resultados); RF-18, RF-20 (`04_analisis.tex:190`, `:214`) | corregir a cinco pestañas con sus nombres reales |
| C-07 Botón «Guardar» | `05_diseno.tex:2966-2967` | CU-18 (`:2011`) y secuencia `:2492` | corregir a «Guardar correcciones» |
| C-08 Columnas de la lista (RF-23) | `04_analisis.tex:244` | `05_diseno.tex:2760` (§Lista de experimentos) y maqueta de la lista | corregir lista de columnas |
| C-09 Pausa solo muestra el enlace | `05_diseno.tex:2883` | `05_diseno.tex:2870` (§Progreso del análisis); maqueta de progreso | agregar el tiempo restante para responder |
| C-10 Pruebas 162 / 202 / 71 | `06_desarrollo.tex:414-416` | (= N-15) | actualizar a 206 (122 con base), 331 y 93 |
| C-11 Simulador `worker_fake` | `06_desarrollo.tex:418` | — | retirar la frase |
| C-12 Umbrales de disco del `.env` | `06_desarrollo.tex:85-87` | `06_desarrollo.tex:152-184` (§Worker, vigilancia del disco) | corregir: variables con valor por omisión en `worker/comun.py`, no en `.env.example` |
| C-13 Tratamiento no vacío | `back/apendice_D.tex:129` (la descripción dice «no puede quedar vacía») | cap. 5 §Diseño de la base de datos (`05_diseno.tex:361-486`) si lo repite | corregir: es NOT NULL sin CHECK |
| C-14 «duraciones y segundos usan numeric» | `back/apendice_D.tex:24-26` (la frase dice «las duraciones y los segundos usan numeric»); la prueba en contra está en `:199` (`segundo` es `smallint`), que es la línea que vio orquestador_web, no la frase | `duracion` sí es `numeric(8,2)` (`:164`) | corregir el párrafo introductorio (`:24-26`) |
| C-15 «Gráficas de barras» | no aparece en ningún `.tex` (verificado) | ver N-06 | sin ubicación; **decisión del usuario** |

## 4. Sin poder confirmar (lista de orquestador_web, ubicación en el documento)

RN-06, RN-09, RN-11 y RN-17 (reinicio): `04_analisis.tex:584-742`. RF-09: `04_analisis.tex:112`. RF-17: `04_analisis.tex:180`. RF-18: `04_analisis.tex:190`. RF-33: `04_analisis.tex:333`. RNF-02 (F1 ≥ 85 %): `04_analisis.tex:380`. RNF-12 (PEP 8): `04_analisis.tex:461`.

## 5. Confirmación de orquestador_web (9-nov)

Confirmó todas las posiciones (están en la sección 6 de su `FALTA_EN_DOCUMENTO.md`). Ajustes acordados: `/health` va en un grupo «Sistema» tras `05_diseno.tex:778`, antes del grupo «Modo desarrollador»; N-05 amplía RF-19 (sin RF nuevo); **N-07 sí pide RF nuevo tras RF-22** (`04_analisis.tex:225`); N-08 amplía RF-22 y CU-15; N-10 amplía CU-07; B-04 y B-05 van juntos en una sola sección «Índices y valores por defecto» tras `apendice_D.tex:235`, como tabla corta aparte (no columna nueva); C-11 se retira. N-06 y C-02 a C-05 siguen como decisión del usuario. **Nadie edita hasta que el usuario decida; cuando lo haga, orquestador_latex ejecuta y orquestador_web revisa línea por línea.**

## 6. RN-18: construido en el sistema (9-nov)

Decisión del usuario: opción C (se construye en el sistema) y **la aceptación no se guarda en la base de datos**. orquestador_web lo construyó y probó (frontend 344/344, backend 219 con PostgreSQL); está sin commit en su árbol y será v1.10.0 cuando el usuario pida el commit (él la confirma). Nada de esto se ha editado todavía en el LaTeX.

**Lo que hace el sistema:**
- Rutas públicas `/aviso-privacidad` («Aviso de privacidad») y `/terminos` («Términos y condiciones de uso»), con o sin sesión. Dos enlaces con esos nombres bajo el formulario de inicio de sesión.
- Primer acceso: casilla obligatoria «He leído y acepto el Aviso de privacidad y los Términos y condiciones de uso», con los dos enlaces en pestaña nueva. Sin marcarla: «Debes aceptar el aviso de privacidad y los términos para continuar.» y no envía.
- No se guarda ningún dato: sin columna nueva; esquema físico, apéndice D y diagramas no cambian. El cuerpo de `PATCH /auth/password` lleva `aceptaTerminos` (booleano), obligatorio solo con contraseña temporal pendiente; sin él, 400.
- Se pide cada vez que la cuenta pasa por contraseña temporal (alta o contraseña temporal nueva del Administrador), no una sola vez. Las cuentas que ya habían cambiado su contraseña no lo aceptaron.
- Textos: borrador, con la nota «Este texto se ajustará a la redacción oficial de la institución cuando se revise.»

**Posiciones propuestas en el documento (sin editar hasta que el usuario lo pida):**

| Qué | Posición | Cambio |
|---|---|---|
| RN-18, justificación | `chapters/04_analisis.tex:750` | «deja constancia» ya no es cierto (no se guarda); cambiar la frase |
| RN-18, texto | `chapters/04_analisis.tex:742-749` | coincide con lo construido; agregar que se pide en cada paso por contraseña temporal |
| Tabla de endpoints | `chapters/05_diseno.tex:689` (`PATCH /auth/password`) | el cuerpo lleva `aceptaTerminos`; obligatorio con contraseña temporal |
| Pantalla de inicio de sesión | `chapters/05_diseno.tex:2724` | los dos enlaces bajo el formulario |
| Pantalla de primer acceso | `chapters/05_diseno.tex:2750` | casilla obligatoria y su mensaje |
| CU-04 (primer acceso) | `chapters/05_diseno.tex:1146` | paso y flujo alterno de aceptar el aviso |
| CU-02 (iniciar sesión) | `chapters/05_diseno.tex:920` | enlaces al aviso y a los términos (opcional) |
| RF-01 / RF-05 | `chapters/04_analisis.tex:80` | citadas por RN-18; revisar que no contradigan |
| Factibilidad legal | `chapters/04_analisis.tex:1246-1255` | referencia cruzada a RN-18; ver también la decisión de «almacenamiento cifrado» |
| Modelo de datos, apéndice D, clases, esquema | — | **sin cambios** |
