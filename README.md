# Proyecto Final Python
## Sistema de Análisis de Datos de Comercio Electrónico

Este proyecto realiza scraping de datos de productos de un sitio web. Los limpia y realiza un analisis de datos que posteriormente será guardado en un archivo CSV y Excel, respectivamente.

## Requisitos

- Python 3.7+
- pandas
- beautifulsoup4
- requests
- matplotlib
- time
- logging
- openpyxl
- fpdf2

## Instalacion

Para instalar las dependencias se creó el archivo "dependencias.txt" en el cual se encuentran todas las dependecias necesarias para una rápida instalación.
Su método de uso es utilizando PIP con el siguiente comando: 

````bash
pip install -r ./dependencias.txt
````

## Estructura del módulo

````bash
PROYECTOPYTHON
|-- data/
|    |- processed/
|        |__ informeEstadistico.xlsx  
|        |__ productosProcesados.csv  
|        |__ productosProcesados.pdf 
|    |- raw/
|        |__ productos.csv
|
|-- notebooks/
|    |__ analisisDatos.ipynb
|
|-- src/
|    |- analysis/
|        |__ __init__.py
|        |__ analysis.py
|    |- decorators/
|        |__ __init__.py
|        |__ decorators.py
|    |- scraping/
|        |__ __init__.py
|        |__ scraper.py
|
|__ dependencias.txt
|__ README.md
|__ requisitosProyecto.txt    
````
## Modo de Uso

Para el uso del Scrapping y posterior análisis de datos se pueden revisar los archivos "screper.py" y "analysis.py" respectivamente para una visualización detallada del código. También se pueden ejecutar de manera individual con las siguientes indicaciones:


## Ejecución del Scraper

Para ejecutar el scraper, ejecuta el siguiente comando en tu terminal:

````bash
python ./src/scraping/scraper.py
````

Esto va a generar un archivo CSV en la carpeta "raw" dentro de la carpeta "data" llamado "productos.csv" con los datos de los productos obtenidos del sitio web.

## Ejecución para el análisis de datos.

### Ejecución archivo "analysis.py"

Para ejecutar el script para análisis de datos, ejecuta el siguiente comando en tu terminal:

````bash
python -m src.analysis.analysis
````

Esto va a generar un archivo CSV y un archivo PDF en la carpeta "processed" dentro de la carpeta "data" llamados "productosProcesados.csv" y "productosProcesados.pdf", respectivamente. Estos archivos contienen los datos de los productos obtenidos del sitio web limpios y procesados. 
Adicionalmente se generará un archivo Excel en la carpeta "processed" dentro de la carpeta "data" llamado "informaEstadistico.xlsx" con los resultados de los cálculos estadísticos.

### Archivo de Jupyter Notebook

Respecto a análisis de datos, en la carpeta "notebooks" se encuentra el archivo "analisisDatos.ipynb" donde también encontrarás cálculos estadísticos básicos y avanzados representados gráficamente (Histograma, gráfico de barras, diagrama de pastel). Los mismos que se pueden ejecutar directamente con la interfaz de Jupiter Notebook.

#### Karen Nicole Tandazo Reyes
#### karen_tandazo22@hotmail.com