# Laboratorio 2: La raíz que se esconde

**Autor:** Benjamín Barros  
**Carrera:** Ingeniería Civil Informática, Universidad Católica del Maule (UCM)  
**Asignatura:** Computación Numérica

---

Este repositorio contiene la implementación y comparación de seis métodos iterativos para encontrar raíces de ecuaciones:

* Bisección
* Falsa posición
* Punto fijo
* Secante
* Newton-Raphson
* Newton mejorado

## Entorno de trabajo

El proyecto está desarrollado en **Python** utilizando las librerías `numpy` y `matplotlib`.

### Configuración del entorno virtual

Para instalar las dependencias y preparar el entorno virtual, ejecuta los siguientes comandos según tu sistema operativo:

#### Windows

```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Ejecución del proyecto

Desde la carpeta raíz del repositorio, ejecuta los métodos y genera los archivos CSV:

```bash
python src/scripts/experimentos.py
```

Para generar los gráficos:

```bash
python src/scripts/graficos.py
```

---

## Estructura del proyecto

* **`src/scripts/`**: Código fuente: `funciones.py`, `metodos.py`, `experimentos.py` y `graficos.py`.
* **`src/data/`**: Archivos CSV generados con las curvas, los resultados, el historial de iteraciones y el análisis de sensibilidad.
* **`src/assets/`**: Gráficos exportados.
* **`informe.md`**: Respuestas a las preguntas del laboratorio y conclusión del análisis numérico.
