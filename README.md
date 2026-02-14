Aquí tienes el archivo `README.md` completo y formateado profesionalmente con la información de tu protocolo.

Copia y pega todo el siguiente bloque de código en tu archivo `README.md`:

```markdown
# Prototipo de un sistema web de análisis conductual asistido por IA en un modelo de conducta depresiva en rata mediante nado forzado

[cite_start]**Trabajo Terminal No. 2026-B066** [cite: 2]

Este repositorio contiene el código fuente en **LaTeX** correspondiente a la documentación, protocolo y reportes de avance del Trabajo Terminal desarrollado en la Escuela Superior de Cómputo (ESCOM - IPN).

## 📄 Resumen del Proyecto

La depresión es un problema de salud pública estudiado experimentalmente mediante la prueba de nado forzado (Forced Swim Test, FST). Este proyecto propone un **sistema web asistido por inteligencia artificial (IA)** que analiza grabaciones de FST para clasificar automáticamente conductas como:
* 🏊 **Nado activo**
* 🛑 **Inmovilidad**
* ⬆️ **Intentos de escape**

[cite_start]El sistema generará métricas por individuo y sesión, comparando los resultados automáticos con anotaciones expertas para validar la reducción de tiempo en el análisis y la precisión del modelo[cite: 5, 6, 7].

## 👥 Equipo de Trabajo

### [cite_start]Alumnos [cite: 3]
* **Frausto Robles Ángel Ali**
* **Rodríguez Verdín Sandoval Vanesa**

### [cite_start]Directores [cite: 3, 4]
* **Dr. Israel Salas Ramírez**
* **Dra. Martha Rosa Cordero López**

---

## 🛠️ Tecnologías del Sistema Propuesto

[cite_start]Aunque este repositorio contiene la documentación escrita, el sistema descrito utiliza el siguiente stack tecnológico[cite: 77, 78, 79, 80, 82]:

* **Backend:** Python (Flask).
* **Inteligencia Artificial:** OpenCV, TensorFlow y Scikit-learn (Visión por computadora y clasificación).
* **Frontend:** React.js (HTML/CSS/JS).
* **Base de Datos:** PostgreSQL.
* **Infraestructura:** Docker (Contenedores).
* [cite_start]**Metodología:** Scrum[cite: 71].

---

## 📂 Estructura del Repositorio

El proyecto de documentación está organizado de la siguiente manera para facilitar la compilación modular en LaTeX:

```text
/
├── main.tex              # Archivo maestro que estructura todo el documento
├── preamble.tex          # Configuración de paquetes, márgenes y bibliografía
├── front/                # Portada, Resumen, Abstract, Agradecimientos
├── chapters/             # Capítulos (Introducción, Estado del Arte, Metodología, etc.)
├── back/                 # Apéndices y Trabajos Futuros
├── bib/                  # Archivo de referencias bibliográficas (.bib)
├── figures/              # Imágenes, diagramas y gráficos del documento
└── tables/               # Tablas complejas (opcional)

```

## 🚀 Instrucciones de Compilación

Este proyecto está configurado para compilarse utilizando **Visual Studio Code** con la extensión **LaTeX Workshop**.

### Requisitos Previos

1. Tener instalado una distribución de TeX (TeX Live en Linux/WSL o MiKTeX en Windows).
2. Tener instalado `biber` para la gestión de bibliografía.

### Pasos

1. Abrir el archivo `main.tex` en VS Code.
2. Abrir el panel de comandos de LaTeX (barra lateral izquierda).
3. Ejecutar la receta: **Build LaTeX project**.
4. El archivo PDF se generará automáticamente en la raíz como `main.pdf`.

> **Nota:** El archivo `.gitignore` está configurado para ignorar archivos auxiliares de compilación (`.aux`, `.log`, `.out`, etc.), manteniendo el repositorio limpio.

---

## 🔒 Confidencialidad

**PROYECTO ACADÉMICO EN DESARROLLO**.
La información contenida en este repositorio, incluyendo datos experimentales y diseño del sistema, es parte de una investigación en curso en el Instituto Politécnico Nacional.

*Última actualización: Febrero 2026*

```

```
