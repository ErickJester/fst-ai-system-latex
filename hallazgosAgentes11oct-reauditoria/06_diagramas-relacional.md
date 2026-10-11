# 06 — Diagramas relacionales y de clases (reauditoría, HEAD 975ec4c)

## Alcance auditado
`diagramas/grafo_relacional_3_vigente.puml` (referencia), `esquema_fisico.puml`, `clases.puml`,
`diagram_design/clases_completo.md/.html/.png` y `diagram_design/generadores/gen_clases.py` (la ruta
real no es `generadores/` en la raíz), `esquema_conceptual.tex`, `back/apendice_D.tex`,
`chapters/05_diseno.tex` (§Diseño de la BD, Normalización, Diagrama de clases), `DISENO-BD.md` (cifras).
Imágenes abiertas: `diagramas/clases.png`, `diagram_design/clases_completo.png`, `figures/mermaid/esquema_fisico.png`.

### Conteos recontados del grafo vigente
- 15 relaciones; 63 atributos (7+5+5+4+3+6+6+3+3+1+3+4+1+5+7); 17 FK (EXPERIMENTO 1, GRUPO 1, TANDA 1, ESPECIMEN 1, VIDEO 1, ANALISIS 1, OBSERVACION 2, INTERVALO 1, PRESENTA 2, SEGUNDO 2, ADMINISTRADOR 1, REPORTE 1, NOTIFICACION 2) y 17 aristas.
- Coinciden: encabezado del grafo (`:16`), `esquema_fisico.puml:8,30,42,323`, cap. 5 (15 relaciones, `:489,593,620,647`), `DISENO-BD.md:282` («15 / 63 / 17; físico 64»), apéndice D (15 tablas; 64 columnas = 63 + `rutaDiagnostico`; 8 dominios, coincide con los 8 del físico), `clases_completo.md` (18 clases; 24 relaciones = 25 aristas del `.puml`/generador menos el enlace de clase asociativa).
- Tablas, columnas, FK y nombres de métodos de `clases.puml`/HTML/PNG de `clases_completo` coinciden con el grafo (FK omitidas por convención). `clases_completo.html` se regeneró en seco con `gen_clases.py` y es idéntico al archivo publicado.

| Severidad | Cantidad | Pregunta abierta |
|---|---|---|
| Alta | 0 | 0 |
| Media | 8 | 2 (DR-06, DR-08) |
| Baja | 8 | 1 (DR-16) |

## Media

### DR-01 — `diagramas/clases.png` (el que entra al cap. 5) es anterior a `clases.puml`
- Severidad: Media
- Ubicación: `diagramas/clases.png` (git 2026-10-06 11:23) vs `diagramas/clases.puml` (git 2026-10-08 12:56); incluida en `chapters/05_diseno.tex:2472`. `clases_completo.png` (8-oct) sí está al día.
- Cita: PNG: `clasificarConducta(especimen, frame) : String`, `ROI` con solo `-x -y -w -h`, `Observacion` sin métodos, sin asociación `Especimen—ROI`, `crea` sin «2..4». `.puml:91,96-104,123,182-183`: «clasificarConducta(especimen, roi, segundo)», `-numeroCilindro … -yAgua -yFondo`, «+calcularBloques()», «"2..4" ROI».
- Fuente que decide: `clases.puml` (vigente; `clases_completo.md:78-86` documenta los cambios del 8-oct).
- Destinatario: Erick
- Previo: DR-01
- Corrección sugerida: regenerar `clases.png` desde `clases.puml`.

### DR-02 — Multiplicidad `Intervalo 2..4 — Conducta` puesta en el extremo equivocado
- Severidad: Media
- Ubicación: `clases.puml:196`; `gen_clases.py:125`; `clases_completo.html/.png` (la etiqueta 2..4 queda junto a `Intervalo`); `clases.png` igual. Grafo `:248-249`: `INTERVALO "1" --o "2..4" PRESENTA`, `CONDUCTA "1" --o "0..*" PRESENTA`.
- Cita: «Intervalo "2..4" -- "0..*" Conducta : presenta». En UML la etiqueta junto a `Intervalo` es cuántos `Intervalo` hay por `Conducta` (2..4), cuando el grafo dice que cada intervalo tiene 2..4 conductas y cada conducta aparece en 0..* intervalos.
- Fuente que decide: grafo vigente (D-29, D-28).
- Destinatario: Erick
- Previo: DR-02
- Corrección sugerida: `Intervalo "0..*" -- "2..4" Conducta : presenta`; en el generador, `edge(..., PLAIN, '0..*', '2..4', '')`; regenerar HTML y PNG.

### DR-03 — Cap. 5: «el esquema físico tiene las mismas columnas que el lógico»
- Severidad: Media
- Ubicación: `chapters/05_diseno.tex:595` (y `:647-649`, «el esquema físico no repite columnas») vs `esquema_fisico.puml:219` y `apendice_D.tex:182`; grafo `:164-172` sin `rutaDiagnostico`. Además `esquema_fisico.puml:30-31` cita al grafo como fuente de estructura con «63 atributos» mientras él mismo tiene 64.
- Cita: «El esquema físico tiene las mismas columnas que el lógico» vs «rutaDiagnostico : text (nulo salvo error)».
- Fuente que decide: D-23/D-42 y D-53 (6): `rutaDiagnostico` se mantiene; `DISENO-BD.md:282` ya dice «64 atributos (más rutaDiagnostico)». El hueco del grafo es el ya conocido; lo que contradice es la frase.
- Destinatario: Erick
- Previo: DR-06 (C5-05)
- Corrección sugerida: «…las mismas columnas que el lógico, más \texttt{ANALISIS.rutaDiagnostico}, que depende solo de la clave, así que también cumple FNBC». Cuando se decida, añadir `rutaDiagnostico` al grafo (64 atributos).

### DR-04 — Tabla de normalización omite `PRESENTA` entre las claves no subrogadas
- Severidad: Media
- Ubicación: `chapters/05_diseno.tex:620-623` vs `esquema_fisico.puml:259-260` / `apendice_D.tex:221-223` (PK compuesta `idIntervalo, conducta`); el propio texto lo dice en `:529-530`.
- Cita: «Clave subrogada autogenerada, salvo USUARIO/ADMINISTRADOR (idInstitucional), CONDUCTA (nombre) y SEGUNDO (clave compuesta…)».
- Fuente que decide: grafo vigente (`PRESENTA` con dos columnas subrayadas).
- Destinatario: Erick
- Previo: DR-08
- Corrección sugerida: añadir «y \texttt{PRESENTA} (clave compuesta \texttt{idIntervalo}, \texttt{conducta})».

### DR-05 — `clases_completo.md` dice que el documento no tiene `humano_ciego` ni `sin_revisar`
- Severidad: Media
- Ubicación: `diagram_design/clases_completo.md:91` vs `back/apendice_D.tex:65` y `esquema_fisico.puml:83-85`.
- Cita: «ni los valores de `origen` `humano_ciego` y `sin_revisar`, que el documento no tiene» vs «sin_revisar: el usuario lo etiquetó sin llegar a verlo… humano_ciego: etiquetado en el modo de revisión que oculta…». Además `chapters/05_diseno.tex:~432` lista solo cuatro orígenes («del sistema, confirmada, corregida o dudosa»): es el hueco conocido, pero el apéndice D sí los define.
- Fuente que decide: pregunta abierta por el hueco de dominio (ya conocido); lo verificable es que el `.md` afirma algo falso sobre el apéndice D.
- Destinatario: Erick
- Previo: DR-05
- Corrección sugerida: cambiar a «que el cap. 5 no menciona (el apéndice D sí los define)» o alinear los dos textos.

### DR-06 — Video de Día 1 contra cardinalidades «1 análisis» y «2..4 observaciones» (pregunta abierta)
- Severidad: Media
- Ubicación: grafo `:244-246`; `esquema_fisico.puml:339-342`; `esquema_conceptual.tex:147-153`; `apendice_D.tex:159,172,191`; `05_diseno.tex:356-358`.
- Cita: «VIDEO "1" --o "1" ANALISIS»; «Cada video tiene de 2 a 4 observaciones» vs D-54 (d): el Día 1 «solo confirma que ese video existe… no se analiza».
- Fuente que decide: pregunta abierta → equipo (D-54 deja (a) y (d) «sin aplicar» al modelo). Además, el cap. 5 dice «Día 1 y/o Día 2» y el apéndice «el Día 1 es opcional»: dos lecturas distintas de qué sesión es obligatoria.
- Destinatario: ambos
- Previo: DR-04
- Corrección sugerida: decidir si Día 1 no tiene `ANALISIS`/`OBSERVACION` (VIDEO–ANALISIS 0..1) y registrarlo como D-xx; no tocar diagramas antes.

### DR-07 — El texto del DER cita entidades que la figura conceptual no dibuja
- Severidad: Media
- Ubicación: `chapters/05_diseno.tex:349-363` (figura `fig:der`) vs `diagramas/esquema_conceptual.tex:18` («11 entidades»; no existen `Reporte`, `Notificación`, `Administrador`).
- Cita: «Las entidades REPORTE y NOTIFICACION se derivan también del experimento» / «Un usuario puede además ser ADMINISTRADOR» vs figura con 11 entidades sin ellas.
- Fuente que decide: grafo vigente (15 relaciones); el texto describe 15 y la figura 11.
- Destinatario: Erick
- Previo: nuevo
- Corrección sugerida: o añadir las tres al `.tex` (ya incluye todo lo demás) o decir en el texto que la figura muestra solo las entidades del dominio experimental y que el resto aparece en el esquema físico.

### DR-08 — `INTERVALO–PRESENTA (2..4)` frente a «una fila por cada una de las cuatro conductas, incluso con 0» (pregunta abierta)
- Severidad: Media
- Ubicación: grafo `:248`; `esquema_fisico.puml:264-267,345`; `apendice_D.tex:225`; `esquema_conceptual.tex:162-163` vs `DISENO-BD.md:340` («en la práctica una fila por cada conducta»).
- Cita: «"2..4" PRESENTA» vs «Hay una fila por conducta aunque valga 0».
- Fuente que decide: pregunta abierta → equipo: si siempre son 4 filas la cardinalidad exacta es (4,4); si puede haber 2 a 4 (sin filas de cero) la nota del físico y el apéndice sobran.
- Destinatario: ambos
- Previo: nuevo
- Corrección sugerida: decidir y alinear nota/cardinalidad.

## Baja

### DR-09 — Fila 3FN de `USUARIO` mal rotulada
- Severidad: Baja
- Ubicación: `05_diseno.tex:640-642` y `:552-559`.
- Cita: «Clave sustituta en lugar de dato de negocio como clave primaria» para `USUARIO`, cuya PK es `idInstitucional` (boleta/número de empleado, dato de negocio, no sustituta; el correo es la alterna).
- Fuente que decide: grafo (`idInstitucional` PK, `correo [AK]`).
- Destinatario: Erick
- Previo: DR-09
- Corrección sugerida: rotular «Atributos dependen de la clave, no del correo (alterna)».

### DR-10 — Notas de la figura del esquema físico con SQL y siglas D-xx
- Severidad: Baja
- Ubicación: `esquema_fisico.puml:145-152,192-197,221-234,279-296` (visibles en `figures/mermaid/esquema_fisico.png`, `05_diseno.tex:380`).
- Cita: «D-24 (15-sep): idVideo UNIQUE…», «PRIMARY KEY», «DELETE», «estado='error'», «Aplicado aqui por primera vez a peticion del usuario (15-sep)».
- Fuente que decide: CLAUDE.md «Reglas de diagramas» (sin SQL ni código; nada de historial de sesión).
- Destinatario: Erick
- Previo: DR-10
- Corrección sugerida: quitar las notas de la versión que entra al documento o reescribirlas en lenguaje natural sin D-xx ni fechas.

### DR-11 — Encabezado del grafo cuenta mal el bloque «dominio experimental»
- Severidad: Baja
- Ubicación: `grafo_relacional_3_vigente.puml:8-9,107` vs `:110-209` (12 clases + `ADMINISTRADOR`).
- Cita: «Las 11 relaciones del esquema logico definitivo mas las dos…» (suman 14, no 15; falta `SEGUNDO` desde D-35).
- Destinatario: Erick
- Previo: DR-11
- Corrección sugerida: «12 relaciones del dominio experimental, más las dos de soporte y ADMINISTRADOR».

### DR-12 — `EXPERIMENTO–NOTIFICACION`: grafo y físico dibujan «1», clases «0..1»
- Severidad: Baja
- Ubicación: grafo `:255`, físico `:333` vs `clases.puml:200`; `NOTIFICACION.idExperimento (nulo)` en grafo `:228`.
- Cita: «EXPERIMENTO "1" --o "0..*" NOTIFICACION» (el extremo Experimento debería ser 0..1 por el nulo).
- Fuente que decide: el propio grafo (columna nula).
- Destinatario: Erick
- Previo: DR-03
- Corrección sugerida: `EXPERIMENTO "0..1" --o "0..*" NOTIFICACION` en grafo y físico.

### DR-13 — Comentario del físico: CONDUCTA con «tres valores en modo completo, dos en modo degradado»
- Severidad: Baja
- Ubicación: `esquema_fisico.puml:91-94` vs `:265-266` (cuatro conductas) y D-29/RN-13.
- Cita: «tres valores en modo completo, dos en modo degradado / D-17».
- Fuente que decide: D-29 (cuatro conductas); D-17 ya reinterpretado por D-41.
- Destinatario: Erick
- Previo: nuevo
- Corrección sugerida: «cuatro conductas; el catálogo puede crecer».

### DR-14 — Apéndice D: `SEGUNDO.segundo` descrito como «segundo del video»
- Severidad: Baja
- Ubicación: `apendice_D.tex:212` vs CK 1..300 (`esquema_fisico.puml:277`) y D-54.
- Cita: «Segundo del video. Solo se analizan los últimos 300 segundos».
- Fuente que decide: D-54: el worker renumera de 1 a 300 las últimas filas; no es el segundo del video original.
- Destinatario: Erick
- Previo: nuevo
- Corrección sugerida: «Posición del segundo dentro de la ventana analizada (1 a 300), tras recortar los últimos 300 s».

### DR-15 — `DISENO-BD.md` conserva cifras viejas fuera del bloque «Cifras vigentes»
- Severidad: Baja
- Ubicación: `DISENO-BD.md:194,239,355-358,365` («16 relaciones», «41 restricciones») y `:224` («Análisis (1,N)»), `:258` («los otros 26 atributos») vs `:282` (15/63/17/64) y D-03 (1,1).
- Cita: «Resultado: 16 relaciones en BCNF» vs «Cifras vigentes (6-oct): 15 relaciones».
- Fuente que decide: grafo vigente (recontado).
- Destinatario: Vanesa/Erick (doc interno)
- Previo: nuevo (parcialmente MD-x de la carpeta anterior)
- Corrección sugerida: banner de «cifras anteriores» en esas secciones o actualizarlas.

### DR-16 — Conceptual dibuja `Grupo agrupa Espécimen (2,N)` que el modelo relacional no tiene (pregunta abierta)
- Severidad: Baja
- Ubicación: `esquema_conceptual.tex:67,114-119`; grafo sin arista GRUPO–ESPECIMEN (D-55 retiró `idGrupo` de `ESPECIMEN`); cap. 5 `:352-360` describe la jerarquía solo vía tanda.
- Cita: «(2,N): un grupo puede tener una sola tanda con 2 especimenes».
- Fuente que decide: pregunta abierta → equipo: ¿se conserva como interrelación derivada en el conceptual o se quita?
- Destinatario: Erick
- Previo: nuevo
- Corrección sugerida: quitar `agrupa` o rotularla como derivada.

## Cobertura y límites
- Leído completo: los 6 archivos de diagramas, `apendice_D.tex`, cap. 5 en las secciones citadas, `gen_clases.py`; `DISENO-BD.md` por `grep` y lecturas parciales. No usé `git log` de los `.puml` salvo fechas.
- Residuos viejos (`numeroRata`, `ultimoAcceso`, `propuesta`, `idConfig`, `hashModelo`, `confianza` como columna, «clase» como atributo) en textos visibles: ninguno en los archivos de mi área (solo en comentarios `'` históricos). `clases_completo.md` menciona `confianza` para decir que no se agregó.
- Fuera de lo pedido pero verificado de pasada: `arquitectura_software.puml:36` («16 relaciones», comentario) y `relacional.puml`/`er.png` (modelo viejo sin marca de obsoleto) siguen como en la auditoría previa (DR-12, DR-13 previos); no se rehicieron.
- No verificado: el PDF `esquema_conceptual.pdf` como imagen (solo su `.tex`); `figures/mermaid/clases.png` (copia más vieja; no la usa el cap. 5 porque `\includegraphics{diagramas/clases}` apunta a `diagramas/`).
- D-57 a D-60 y el despliegue no se tratan aquí.
