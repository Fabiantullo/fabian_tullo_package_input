from .validate import *

# def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int|None:
#     while reintentos > 0:
#         dato_ingresado = input(mensaje)
#         try:
#             dato_ingresado = int(dato_ingresado)
#             if dato_ingresado > minimo and dato_ingresado < maximo:
#                 return dato_ingresado
#                 break
#             else:
#                 print(mensaje_error)
#         except: 
#             print(mensaje_error)
#         reintentos -= 1

def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int|None:
    while reintentos > 0:
        dato_ingresado = input(mensaje)
        if validate_number(dato_ingresado):
            dato_ingresado = int(dato_ingresado)
            if dato_ingresado > minimo and dato_ingresado < maximo:
                return dato_ingresado
                break
            else:
                print(mensaje_error)
        else:
            print(mensaje_error)
        reintentos -= 1
    

def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos: int) -> float|None:
    while reintentos > 0:
        dato_ingresado = input(mensaje)
        if validate_number(dato_ingresado):
            dato_ingresado = float(dato_ingresado)
            if dato_ingresado > minimo and dato_ingresado < maximo:
                return dato_ingresado
                break
            else:
                print(mensaje_error)
        else: 
            print(mensaje_error)
        reintentos -= 1

def get_string(mensaje: str, longitud: int) -> str|None:
    dato_ingresado = input(mensaje)
    if validate_lenght(dato_ingresado, longitud):
        return dato_ingresado