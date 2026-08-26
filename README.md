# Prototipo de un sistema web de análisis conductual asistido por IA en un modelo de conducta depresiva en rata mediante nado forzado

**Trabajo Terminal No. 2026-B066** 

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
├── compilar.sh           # Script de compilación (pdflatex + biber, 3 pasadas)
├── CORRECCIONES.md       # Checklist de correcciones pendientes del documento
│
│   # ── Fuentes del documento LaTeX ──────────────────────────
├── front/                # Portada, resumen, glosario, abreviaturas
├── chapters/             # Capítulos 1–5
├── back/                 # Apéndices y trabajo futuro
├── bib/                  # Referencias bibliográficas (.bib)
├── figures/              # Imágenes que el documento incluye
│   ├── mermaid/          #   Diagramas exportados a PNG
│   └── mockups/          #   Capturas de los mockups de interfaz
├── logos/                # Logos institucionales (IPN, ESCOM)
│
│   # ── Material de trabajo (no entra a la compilación) ──────
├── diagramas/            # Fuentes de diagramas (.puml, .svg) y exportaciones
│   ├── puml/             #   Casos de uso por paquete
│   └── pdf/              #   Diagramas exportados a PDF
├── mockups/              # Mockups de interfaz en HTML
├── scripts/              # Generadores en Python (se ejecutan desde la raíz)
├── docs/                 # Documentos de trabajo en Word y PDFs generados
└── build/                # Salida de compilación (ignorada por git)
```

> Las presentaciones `.pptx` no se versionan en este repositorio. Pesaban cerca de
> 300 MB y se eliminaron también del historial, que pasó de 628 MB a 34 MB. Las
> versiones anteriores se conservan fuera del repositorio, en el respaldo local
> del equipo. El `.gitignore` impide que vuelvan a entrar.

### Ejecutar los scripts

Los scripts de `scripts/` resuelven sus rutas respecto a la raíz del repositorio,
así que se invocan desde la raíz:

```bash
python scripts/convert_mermaid.py
```

## 🚀 Instrucciones de Compilación

Este proyecto está configurado para compilarse utilizando **Visual Studio Code** con la extensión **LaTeX Workshop**.

### Requisitos Previos
* Tener instalada una distribución de TeX (**TeX Live** en Linux/WSL o **MiKTeX** en Windows).
* Tener instalado **biber** para la gestión de bibliografía.

### Pasos
1.  Abrir el archivo `main.tex` en VS Code.
2.  Abrir el panel de comandos de LaTeX (barra lateral izquierda).
3.  Ejecutar la receta: **Build LaTeX project**.
4.  El archivo PDF se generará automáticamente en la raíz como `main.pdf`.

> **Nota:** El archivo `.gitignore` está configurado para ignorar archivos auxiliares de compilación (`.aux`, `.log`, `.out`, etc.), manteniendo el repositorio limpio.

---

## 🔒 Confidencialidad

**PROYECTO ACADÉMICO EN DESARROLLO.**

La información contenida en este repositorio, incluyendo datos experimentales y diseño del sistema, es parte de una investigación en curso en el **Instituto Politécnico Nacional**.

*Última actualización: Febrero 2026*
