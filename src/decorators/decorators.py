import time
import logging

#Configuración básica de logging: Definir formato de mensaje de registro (marca de tiempo - nivel de mensaje - mensaje)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#Decorador para medir tiempo de ejecución de una función
def dec_tiempo(func):
    def wrapper(*args,**kargs):
        inicio=time.time()
        resultado=func(*args,**kargs)
        fin=time.time()
        tiempo_ejecucion=fin-inicio
        logging.info(f"{func.__name__} executada en {tiempo_ejecucion:.4f} segundos")
        return resultado
    return wrapper

#Decorador para registrar el inicio y la finalización de la ejecución de una función
def dec_logging(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Ejecutando {func.__name__}")
        resultado = func(*args, **kwargs)
        logging.info(f"Completado {func.__name__}")
        return resultado
    return wrapper






