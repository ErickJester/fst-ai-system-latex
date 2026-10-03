# Preguntas pendientes

> Una por punto. Al responder, se borra de aquí. Si la respuesta debe persistir, se deja
> el tiempo necesario y luego se mueve al `.md` que corresponda.

## Revisión segundo a segundo (decisiones D-34 y D-35)

Ya decidido y registrado: el análisis corre en segundo plano a su ritmo; solo al final el
usuario ve la pantalla de revisión segundo a segundo; las correcciones se guardan en una
tabla nueva por segundo.

1. **Quién corrige y cómo cuenta.** ¿Cualquier investigador puede corregir un análisis o
   solo quien lo creó (y el administrador)? ¿Los reportes usan las correcciones y marcan
   que fueron revisadas?
2. **Video para reproducir en el navegador.** Los `.mov` del iPhone suelen venir en un
   códec (HEVC) que Chrome y Firefox no reproducen. Para la pantalla de revisión hay que
   generar una copia en formato compatible (H.264) de los primeros 300 s. ¿La genera el
   worker al terminar el análisis? Es trabajo extra de procesamiento por video.

## Diferido: intervención humana cuando se pierde el tubo

Quedó fuera de esta versión porque no habrá vista en vivo. Si se retoma:

3. **¿Y si el usuario no está mirando cuando el sistema pierde el tubo?** ¿El análisis
   queda en pausa esperando, se le avisa con una notificación, y cuánto tiempo espera?
4. **¿Cómo decide el sistema que «el video se movió»?** Por ejemplo: el alineado de la
   cámara falla, o no se ve al espécimen durante N segundos. ¿Quién fija ese criterio?
5. **¿Se guarda el recuadro que dibuja el usuario?** Habría que guardar segundo, tubo y
   coordenadas: sería un cambio más al modelo de datos.
6. **¿Cambian las reglas de pausar y cancelar?** Hoy el investigador no puede pausar,
   cancelar ni reiniciar un análisis.
7. **¿Se permiten varios análisis en pantalla a la vez?** Hoy se procesan uno por uno en
   cola.
