# Proyecto de Análisis de Datos

Este proyecto contiene scripts de Python para análisis de datos y ejercicios de programación, incluyendo análisis estadístico de datos CSV y el clásico problema FizzBuzz.

## 📋 Descripción

El proyecto incluye:

- **`analisis.py`**: Script para analizar datos CSV, calcular estadísticas descriptivas (media, mediana, desviación estándar) y generar gráficas de dispersión.
- **`prueba2`**: Implementación del problema FizzBuzz que recorre números del 1 al 50.
- **`datos.csv`**: Archivo CSV de ejemplo con dos columnas de datos numéricos.

## 🚀 Instalación

### Requisitos previos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Pasos de instalación

1. **Clonar el repositorio** (si es necesario):
   ```bash
   git clone https://github.com/natalia2006-cpu/Matasangres.git
   cd Matasangres
   ```

2. **Crear un entorno virtual** (recomendado):
   ```bash
   python -m venv venv
   ```

3. **Activar el entorno virtual**:
   
   **En Windows (PowerShell):**
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
   
   **En Windows (CMD):**
   ```cmd
   venv\Scripts\activate.bat
   ```
   
   **En Linux/Mac:**
   ```bash
   source venv/bin/activate
   ```

4. **Instalar las dependencias**:
   ```bash
   pip install pandas matplotlib
   ```

## 📖 Uso

### Análisis de datos CSV

Para ejecutar el script de análisis de datos:

```bash
python analisis.py
```

El script:
- Lee el archivo `datos.csv`
- Calcula estadísticas descriptivas (media, mediana, desviación estándar) para cada columna
- Genera una gráfica de dispersión (`scatter_plot.png`) comparando las dos columnas
- Muestra los resultados en la consola

**Ejemplo de salida:**
```
==================================================
ESTADÍSTICAS DESCRIPTIVAS
==================================================

Columna: col1
  Media: 57.50
  Mediana: 57.50
  Desviación estándar: 29.58

Columna: col2
  Media: 72.50
  Mediana: 72.50
  Desviación estándar: 29.58
```

### Ejecutar FizzBuzz

Para ejecutar el programa FizzBuzz:

```bash
python prueba2
```

El programa recorre números del 1 al 50 e imprime:
- "Fizz" si el número es múltiplo de 3
- "Buzz" si el número es múltiplo de 5
- "FizzBuzz" si el número es múltiplo de ambos (3 y 5)
- El número en caso contrario

## 📁 Estructura del proyecto

```
contador_palabras/
│
├── analisis.py          # Script principal de análisis de datos
├── datos.csv            # Archivo CSV de ejemplo
├── prueba2              # Programa FizzBuzz
├── README.md            # Este archivo
├── .gitignore           # Archivos ignorados por Git
└── venv/                # Entorno virtual (no se incluye en el repo)
```

## 📦 Dependencias

- **pandas**: Para manipulación y análisis de datos
- **matplotlib**: Para generar gráficas y visualizaciones

## 🔧 Personalización

### Usar tus propios datos

1. Crea un archivo CSV con dos columnas numéricas
2. Modifica `analisis.py` para cambiar el nombre del archivo CSV:
   ```python
   df = pd.read_csv('tu_archivo.csv')
   ```
3. Ajusta los nombres de las columnas si es necesario:
   ```python
   plt.scatter(df['tu_columna1'], df['tu_columna2'], ...)
   ```

## 📝 Notas

- El archivo `.gitignore` está configurado para excluir el entorno virtual, archivos compilados de Python y gráficas generadas.
- Las gráficas se guardan automáticamente como `scatter_plot.png` en el directorio del proyecto.

## 👤 Autor

Natalia

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso educativo y personal.

