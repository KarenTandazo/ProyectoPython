import requests
from bs4 import BeautifulSoup
import pandas as pd

url='https://www.tia.com.ec/tecnologia/celulares-tablets-y-complementos/celulares'

def fetch_page(url):
    """
    Solicitar a un URL el contenido de una página.

    Args:
        url (str): La URL de la página web a solicitar.

    Returns:
        str: El contenido de la página web.

    Raises:
        Exception: Si la solicitud HTTP falla (código de estado diferente de 200), se levanta una excepción con un mensaje de error.
    """
    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Failed to fecth page: {url}")
   
def scrape(url):
    """
    Recupera el contenido de la página y lo convierte en un objeto BeautifulSoup.

    Args:
        url (str): La URL de la página web de la que se quiere extraer el contenido.

    Returns:
        BeautifulSoup: Un objeto BeautifulSoup con el contenido HTML de la página.
    """
    contenido=fetch_page(url)
    soup = BeautifulSoup(contenido, 'html.parser')
    return soup
   
def obtener_productos(url):
    """
    Obtiene la información de los productos de la página.

    Args:
        url (str): La URL de la página web de la que se quiere extraer el contenido.

    Returns:
        list: Una lista con los datos de los productos en diccionarios. Cada diccionarios tiene las claves "Marca", "Producto" y "Precio".
    """
    soup=scrape(url)
    productos=[]

    items=soup.select(".product-item")
    for item in items:
        nombre_item=item.select_one('.product-item-link')
        precio_item=item.select_one(".price-wrapper .price")
        marca_item = item.select_one(".product-item-brand strong")

        if nombre_item and precio_item:
            nombre=nombre_item.get_text(strip=True)
            precio=precio_item.get_text(strip=True)
            marca=marca_item.get_text(strip=True)
            productos.append({"Marca": marca,"Producto": nombre , "Precio": precio})
        else:
            continue
    return productos

def datos_paginacion(pag_url):
    """
    Obtiene la información de los productos de todas las páginas de la paginación que tiene el sitio web.

    Args:
        pag_url (str): La URL base del sitio web con paginación del que se quiere extraer el contenido.

    Returns:
        list: Una lista con los datos de los productos en diccionarios. Cada diccionarios tiene las claves "Marca", "Producto" y "Precio".
    """
    productos=[]
    page=1
    while True:
        url=f"{pag_url}?p={page}"
        nuevos_productos=obtener_productos(url)
        if not nuevos_productos:
            break
        productos.extend(nuevos_productos)
        page += 1
    print("Sitio web srapeado correctamente")
    return productos

def guardar_csv(datos, archivo="./data/raw/productos.csv"):
    """
    Guarda los datos en un archivo CSV.

    Args:
        datos (list): Una lista de diccionarios con la información de los productos.
        archivo (str): El nombre y la ruta del archivo CSV donde se guardarán los datos.

    Returns:
        DataFrame: Un DataFrame de pandas con los datos guardados.
    """
    df=pd.DataFrame(datos)
    df.to_csv(archivo, index=False, encoding="utf-8")
    print(f"Data guardada exitosamente en {archivo}")

productos = datos_paginacion(url)
guardar_csv(productos)
