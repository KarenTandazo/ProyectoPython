import pandas as pd
import os
from ..decorators.decorators import dec_logging, dec_tiempo

@dec_logging
@dec_tiempo
def cargar_data(archivo_entrada):
    """
    Carga los datos de los productos desde un archivo CSV o Excel.

    Args:
        archivo_entrada (str): Ruta del archivo de entrada donde se encuentran los datos (CSV o Excel).

    Returns:
        DataFrame: DataFrame de pandas con los datos cargados.

    Raises:
        ValueError: Si el archivo de entrada no tiene un formato soportado (CSV o Excel).
    """
    if archivo_entrada.endswith(".csv"):
        df = pd.read_csv(archivo_entrada)
    elif archivo_entrada.endswith(".xlsx"):
        df = pd.read_excel(archivo_entrada)
    else:
        raise ValueError("Formato de archivo no soportado")
    print("El archivo fue leído exitosamente")
    return df

@dec_logging
@dec_tiempo
def limpiar_datos(df):
    """
    Limpia los datos de los productos.

    Args:
        df (DataFrame): DataFrame de pandas con los datos a limpiar.

    Returns:
        DataFrame: DataFrame con los datos limpios.
    """
    df["Marca"] = df["Marca"].str.replace(r"Marca", "", regex=False)
    df["Precio"] = df["Precio"].replace(r"[\$,.]", "", regex=True).astype(float)/100
    print("Data limpiada correctamente")
    return df

@dec_logging
@dec_tiempo
def guardar_data_limpia(df, archivo_salida):
    """
    Guarda los datos limpios en un archivo CSV o Excel.

    Args:
        df (DataFrame): DataFrame de pandas con los datos limpios a guardar.
        archivo_salida (str): Ruta del archivo de salida donde se guardarán los datos (CSV o Excel).

    Raises:
        ValueError: Si el archivo de salida no tiene un formato soportado (CSV o Excel).
    """
    if archivo_salida.endswith(".csv"):
        df.to_csv(archivo_salida, index=False)
    elif archivo_salida.endswith(".xlsx"):
        df.to_excel(archivo_salida, index=False)
    else:
        raise ValueError("Formato de archivo no soportado")
    print(f"Nueva data guardada exitosamente en {archivo_salida}")

@dec_logging
@dec_tiempo
def calcular_estadisticas(df):
    """
    Calcula estadísticas básicas de los productos

    Args:
        df (DataFrame): DataFrame de pandas con los datos limpios a analizar.

    Returns:
        estadistica_basica (DataFrame): DataFrame con estadísticas básicas.
        highest_products (DataFrame): DataFrame con los productos con precios más altos.
        smallest_products (DataFrame): DataFrame con los productos con precios más bajos.
        conteo_marcas (DataFrame): DataFrame con la cantidad de productos por marca.
    """
    estadistica_basica = df.describe().map(lambda x: f'{x:.4f}')
    highest_products = df.nlargest(10, "Precio")
    smallest_products = df.nsmallest(10, 'Precio')
    conteo_marcas = df['Marca'].value_counts().head(10)

    estadistica_basica.columns = ["Estadísticas Básicas"]
    highest_products.columns = ["Marca", "Producto", "Precio"]
    smallest_products.columns = ["Marca", "Producto", "Precio"]
    conteo_marcas.columns = ["Marca", "Cantidad"]

    return estadistica_basica, highest_products, smallest_products, conteo_marcas

@dec_logging
@dec_tiempo
def guardar_estadisticas(estadistica_basica, highest_products, smallest_products, conteo_marcas, informe_salida):
    """
    Guarda los cálculos estadísticos en un archivo Excel.

    Args:
        estadistica_basica (DataFrame): DataFrame con estadísticas básicas.
        highest_products (DataFrame): DataFrame con los productos con precios más altos.
        smallest_products (DataFrame): DataFrame con los productos con precios más bajos.
        conteo_marcas (DataFrame): DataFrame con la cantidad de productos por marca.
        informe_salida (str): Ruta del archivo de salida donde se guardarán los datos estadísticos (Excel)
    """
    nombres_pestanas = ['Estadísticas Básicas', 'Productos más caros', 'Productos más baratos', 'Marcas más ofertadas']

    with pd.ExcelWriter(informe_salida) as writer:
        for nombre, datos in zip(nombres_pestanas, [estadistica_basica, highest_products, smallest_products, conteo_marcas]):
            if nombre in ['Productos más caros', 'Productos más baratos']:
                datos.to_excel(writer, sheet_name=nombre, index=False)
            else:
                datos.to_excel(writer, sheet_name=nombre, index=True)
    print("Estadísticas guardadas en:", informe_salida)

if __name__ == "__main__":
    archivo_entrada="./data/raw/productos.csv"
    archivo_salida="./data/processed/productosProcesados.csv"
    informe_salida="./data/processed/informeEstadistico.xlsx"

df=cargar_data(archivo_entrada)
datos_limpios=limpiar_datos(df)
os.makedirs("./data/processed", exist_ok=True)
guardar_data_limpia(datos_limpios, archivo_salida)
estadistica_basica, highest_products, smallest_products, conteo_marcas = calcular_estadisticas(datos_limpios)
guardar_estadisticas(estadistica_basica, highest_products, smallest_products, conteo_marcas, informe_salida)