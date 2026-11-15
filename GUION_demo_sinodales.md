# Guion de demostración para sinodales: del login al reporte

Una sola persona, en vivo, con el sistema abierto desde la pantalla de inicio de sesión. Tono de venta: cada pantalla dice qué problema resuelve.
Las indicaciones en cursiva entre corchetes no se dicen: son lo que hay que hacer en pantalla.
Basado en el repositorio `ErickJester/fst-ai-system` (commit `d2295b0`, 8-nov-2026).

---

*[Pantalla: Iniciar sesión, sin tocar nada todavía]*

Buenos días, miembros del jurado. Lo que van a ver no es una maqueta ni una presentación de diapositivas: es el sistema funcionando. Quiero mostrarles el recorrido completo de una persona del laboratorio, desde que abre el navegador hasta que tiene en las manos el reporte de su experimento.

Para ubicarnos: en el Laboratorio de Bioquímica Estructural, analizar una prueba de nado forzado significa que alguien se sienta frente al video y anota, segundo a segundo, si el espécimen nada, escala o está inmóvil. Es un trabajo largo, cansado y, sobre todo, repetitivo. Este sistema hace esa primera pasada por la persona, y le deja a ella lo que sí requiere criterio: revisar y corregir.

Empiezo por el principio. Esta es la pantalla de inicio de sesión. Fíjense en el encabezado: dice a qué laboratorio pertenece y para qué sirve. El acceso es con correo y contraseña, y el sistema valida lo que se escribe antes de enviarlo: si el correo no tiene formato válido o falta la contraseña, lo dice al momento, sin hacer esperar al usuario.

*[Hacer clic en «Olvidé mi contraseña»]*

Algo que a cualquier laboratorio le pasa: alguien olvida su contraseña. Aquí no hace falta llamar a nadie. La persona escribe su correo y el sistema le manda un enlace de restablecimiento que dura sesenta minutos. Y por seguridad, el mensaje es el mismo exista o no el correo en el sistema, para que nadie pueda averiguar qué cuentas existen.

*[Volver a iniciar sesión]*

Voy a entrar con una cuenta nueva, de las que crea el administrador. Estas cuentas llegan con una contraseña temporal.

*[Iniciar sesión con la cuenta temporal]*

Y aquí ven la primera decisión de seguridad: el sistema no me deja pasar a ninguna otra pantalla hasta que cambie esa contraseña. No es una sugerencia, es obligatorio. Pide la temporal, la nueva con mínimo ocho caracteres, y que sea distinta de la temporal. Así, la contraseña que el administrador conoce solo sirve una vez.

*[Cambiar la contraseña y entrar]*

Ya estamos dentro. Esta es la lista de experimentos.

*[Pantalla: Experimentos]*

Aquí vive el trabajo del laboratorio. Cada fila es un experimento, con su estado: si no tiene videos, si está esperando el video del segundo día, si hay un análisis en curso, o si ya hay resultados. Hay búsqueda por nombre o tratamiento y paginación, para que la lista siga siendo manejable cuando haya cientos.

Arriba hay una campanita de notificaciones. El sistema avisa cuando un análisis termina o falla, y también avisa cuando un video está por borrarse. Eso último importa: los videos crudos se borran treinta días después del análisis, o antes si el disco pasa del noventa por ciento. El sistema se lo dice a la persona con anticipación, y deja claro que los resultados y los reportes se conservan siempre. Así el disco del laboratorio no se llena sin que nadie lo note.

*[Clic en «Nuevo experimento»]*

Creemos un experimento. Fíjense en lo poco que pide: un nombre, que es único en todo el sistema, una fecha de inicio y notas opcionales. Los grupos y los tratamientos no se piden aquí; se definen en el siguiente paso, cuando se sube el video. Esto es a propósito: el investigador no tiene que llenar un formulario largo antes de empezar.

*[Escribir un nombre, fecha y pulsar «Crear y cargar videos»]*

Ahora viene la parte que más cuidamos: cargar el video.

*[Pantalla: Cargar video por tanda]*

En el laboratorio las pruebas se hacen por tandas: varios espécimenes al mismo tiempo, cada uno en su cilindro. Entonces el sistema organiza el trabajo igual. Un video corresponde a una tanda de un solo grupo. Indico el grupo; si es nuevo, lo creo aquí mismo, con su tipo y su tratamiento, sustancia y dosis. Confirmo qué tanda es, y el sistema ya me propone la letra siguiente para no equivocarme. Indico cuántos espécimenes hay en la tanda, y suelto el archivo.

Acepta archivos mp4 y mov, y si el archivo es de otro tipo o pasa del límite de tamaño, lo rechaza de inmediato y explica por qué, antes de que la persona espere una subida de varios minutos. Hay barra de avance, y si me equivoco de archivo puedo cancelar la subida sin que nada quede a medias.

Una cosa más que refleja cómo trabaja el laboratorio: la prueba tiene dos días. El video del Día 1 es la sesión de habituación; el sistema lo guarda para dejar constancia, pero no lo analiza. El análisis se hace con el video del Día 2. Y puedo preparar varias tandas en esta misma página con «Agregar otra tanda»; se suben en orden, una por una.

*[Subir el video del Día 2 y pulsar «Guardar y encolar análisis»]*

El video quedó almacenado y el análisis entró a la cola. Esto es lo que quiero que noten: no tengo que quedarme esperando. Puedo cerrar el navegador.

*[Pantalla: Análisis en curso]*

Esta pantalla muestra la cola. El sistema analiza un video a la vez, por orden de llegada, y se lo dice al usuario con claridad: está en espera de turno, o ya está en proceso. Cuando está en proceso, muestra las tres etapas. Primero, la preparación del video. Segundo, la localización de los cilindros. Tercero, la clasificación de la conducta de cada espécimen, segundo a segundo, entre nado, inmovilidad, escalamiento y conducta activa.

Quiero detenerme en un detalle que, para mí, es lo que distingue a este sistema de una caja negra. En la etapa de cilindros, el sistema genera una imagen de control: marca en amarillo la zona que midió de cada tubo, en azul la línea de agua y en verde el fondo. Es decir, el investigador puede ver con sus propios ojos qué encontró el sistema antes de confiar en lo que decidió. Si los tubos están mal ubicados, se nota aquí, no después de analizar un video completo.

*[Mostrar la imagen de control]*

Y si algo sale mal, el sistema no se calla. Si el video no se pudo abrir o no se encontraron los cilindros, el análisis termina en error y ofrece descargar un reporte de diagnóstico en PDF que dice en qué etapa se detuvo y por qué. La persona no se queda con un mensaje genérico de «falló»; sabe qué corregir.

*[Pantalla: Análisis en pausa]*

Hay un caso más delicado, que el sistema resuelve de una forma que me parece muy acertada. A veces, durante el video, un espécimen sale de su recuadro y el sistema deja de verlo. Un sistema descuidado inventaría una conducta. Este no: se pone en pausa y espera.

Aquí vemos la pantalla de pausa. El investigador tiene setenta y dos horas para responder. Puede ajustar el recuadro del cilindro y el análisis vuelve a la cola, por delante de los que llegaron después, y se retoma con el recuadro corregido aplicado desde el segundo donde se detuvo. O, si el video no sirve, puede cancelar. Y si pasan las setenta y dos horas sin respuesta, el sistema cierra el análisis por sí mismo, para no dejar trabajos colgados. Solo quien subió el video o un administrador puede tomar esta decisión, para que nadie más altere un análisis ajeno.

*[Ir a un análisis completado y abrir Resultados]*

Pasemos a lo que importa: los resultados.

*[Pantalla: Resultados]*

Aquí está el análisis terminado. Arriba, cuántos segundos se analizaron, cuántos espécimenes y cuándo. Para cada espécimen, el tiempo en cada conducta, en minutos y segundos, y una línea de tiempo por minuto para ver cómo evolucionó la conducta a lo largo de la prueba. Hay también bloques de cinco segundos para ver el detalle fino.

Si el experimento tiene varios grupos, hay una comparación entre grupos: es lo que el investigador necesita para contrastar, por ejemplo, un grupo control contra uno tratado con fluoxetina, el antidepresivo de referencia, sin armar una hoja de cálculo a mano.

Hay una decisión de honestidad que quiero resaltar. La cuarta conducta, la conducta activa, no la decide la red; la asigna una regla. Se usa cuando el espécimen claramente no estaba inmóvil, pero el sistema no pudo decidir entre nado y escalamiento. El sistema lo dice así, con esas palabras, en la leyenda. No esconde la duda: la muestra. Y los segundos donde no se pudo ver al espécimen aparecen como «no se ve», para que todo sume cien por ciento y el investigador sepa exactamente qué parte del video quedó sin clasificar.

Los resultados salen del sistema en tres formatos: un CSV con una fila por espécimen y por minuto, con la media, la desviación estándar y la varianza; el mismo contenido en un libro de Excel; y un reporte en PDF listo para entregar. Es decir, el dato llega a la herramienta estadística que el investigador ya usa.

*[Clic en «Revisar segundo a segundo»]*

Y ahora la pantalla que, para mí, justifica todo el diseño.

*[Pantalla: Revisión segundo a segundo]*

Ningún sistema automático acierta el cien por ciento, y un laboratorio no puede publicar sobre resultados que no puede verificar. Por eso el sistema no entrega una respuesta final: entrega una propuesta revisable. Cada segundo ya viene con la conducta que decidió el sistema. El investigador ve el video, y si lo que ve no coincide con lo que dice el sistema, pulsa la conducta correcta con una sola tecla. Puede moverse entre espécimenes, hay una línea de tiempo con una lupa de cuarenta segundos para saltar a cualquier momento, y se puede trabajar con el teclado, sin tomar el ratón.

Dos reglas que protegen la calidad de la revisión. Primera: solo cuenta como visto lo que se reprodujo a velocidad doble o más lenta, y solo lo visto se guarda. Nadie puede corregir a ciegas. Segunda: si el investigador cierra la ventana, su borrador queda en el navegador, y no pierde el trabajo.

*[Corregir un segundo y pulsar «Guardar correcciones»]*

Al guardar, los totales, el desglose por minuto y los reportes se regeneran con los datos corregidos. Los resultados siempre reflejan lo que el investigador validó, y quedan marcados como «con revisión humana». Eso es lo que da confianza al usar estos datos en un artículo o en una tesis.

Y si el investigador cree que el análisis salió mal desde el principio, puede reiniciarlo desde cero; el sistema le advierte que perderá toda la revisión, y lo pide confirmar, porque esa acción no se puede deshacer.

*[Abrir «Perfil» desde el menú de usuario]*

Cada persona tiene su perfil: sus datos, su identificador institucional, que es de solo lectura, y el cambio de contraseña cuando quiera.

*[Cerrar sesión y entrar como administrador; abrir Administración]*

Ahora cambio de rol. El administrador tiene una sección que el investigador no ve.

*[Pantalla: Administración]*

Aquí se crean las cuentas. El administrador captura nombre, apellidos, correo e identificador institucional, que es numérico, una boleta o un número de empleado. La cuenta nace como investigador, y el sistema genera la contraseña temporal que el administrador entrega a la persona, y que ya vimos que se cambia en el primer ingreso. Si alguien pierde su contraseña temporal, el administrador genera otra y la anterior deja de servir. Se pueden editar y desactivar cuentas, y el sistema protege una regla básica: siempre debe existir al menos un administrador activo, para que nadie deje el sistema sin quien lo gobierne.

También ve la cola de trabajos de todo el laboratorio, los experimentos de todos los investigadores, que puede gestionar o eliminar, y cuántos videos crudos están por borrarse en los próximos siete días. Es el panel con el que una sola persona puede mantener el sistema al día.

*[Volver al inicio; cerrar con las manos libres, sin pantalla específica]*

Para cerrar, quiero hablarles de dónde vive todo esto, porque es parte de lo que ofrecemos. El sistema se instala en una computadora del laboratorio con Windows y Docker, desde un paquete que ya trae todo construido. No necesita internet para instalarse ni para usarse, así que los videos y los datos de los experimentos nunca salen del laboratorio. Las demás computadoras de la red entran por su dirección desde el navegador, sin instalar nada. Y el análisis usa el mismo modelo y el mismo procedimiento con los que el laboratorio ya trabaja, de modo que los resultados del sistema son los mismos que obtendría el equipo analizando por su cuenta.

Resumo lo que vieron. Una persona del laboratorio entra de forma segura, crea un experimento con tres datos, sube el video de cada tanda, y se va. El sistema analiza en cola, avisa cuando termina, y si algo falla explica qué. Los resultados llegan con sus dudas a la vista, el investigador los revisa y los corrige segundo a segundo, y descarga el reporte en el formato que necesita. Un administrador mantiene las cuentas y el espacio.

Todo el trabajo repetitivo lo hace el sistema; todas las decisiones que importan siguen siendo de la persona. Muchas gracias. Quedo atento a sus preguntas.

---

## Antes de presentar

- **Entren una vez con todo el recorrido.** El guion asume que existe un video de Día 2 ya analizado y una cuenta temporal sin estrenar.
- **Análisis en vivo:** en CPU tarda unos 5 a 10 minutos por video, y solo analiza los últimos 300 s del Día 2. Dejen listo uno terminado y muestren el de la cola solo hasta ver el progreso.
- **Modo demo:** en ese modo no se ve el video en la revisión ni en la pausa. Si presentan con datos de ejemplo, no digan «ven el video» en esos dos pasos.
- **Para el cierre:** «sin internet» y «mismo modelo que el laboratorio» salen de `portable/LEEME.md` y `pipeline/README.md`. Confirmen que así van a presentarlo.
- **No hay aviso de privacidad ni términos** en el login, así que el guion no los menciona.
- **No hay cifras de F1 ni de exactitud** en el repositorio; el guion no las cita.
