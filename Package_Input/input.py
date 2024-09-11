from .validate import *

def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int|None:
    """Funcion para validar si el dato es un numero entero.

    Args:
        mensaje (str): Mensaje a mostrar para que el usuario ingrese el dato.
        mensaje_error (str): Mensaje en caso de que haya un error en el programa.
        minimo (int): Minimo de numero ingresado.
        maximo (int): Maximo de numero ingresado.
        reintentos (int): Cantidad de reintentos de ingreso.
    

    Returns:
        int|None: Si el dato se valida devuelve un entero, en caso contratio no devuelva nada.
    """
    while reintentos > 0:
        dato_ingresado = input(mensaje)
        if validate_number(dato_ingresado):
            dato_ingresado = int(dato_ingresado)
            if dato_ingresado > minimo and dato_ingresado < maximo:
                return dato_ingresado
                break
        print(mensaje_error)
        reintentos -= 1
    

def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos: int) -> float|None:
    """Funcion para validar si el dato ingresado es un numero flotante.

    Args:
        mensaje (str): Mensaje a mostrar para que el usuario ingrese el dato.
        mensaje_error (str): Mensaje en caso de que haya un error en el programa.
        minimo (int): Minimo de numero ingresado.
        maximo (int): Maximo de numero ingresado.
        reintentos (int): Cantidad de reintentos de ingreso.

    Returns:
        float|None: Si el dato se valida devuelve el numero flotante, en caso contrario no devuelve nada.
    """
    while reintentos > 0:
        dato_ingresado = input(mensaje)
        if validate_number(dato_ingresado):
            dato_ingresado = float(dato_ingresado)
            if dato_ingresado > minimo and dato_ingresado < maximo:
                return dato_ingresado
                break
        print(mensaje_error)
        reintentos -= 1

def get_string(mensaje: str, longitud: int) -> str|None:
    """Funcion para validar si el dato ingresado tiene cierta longitud.

    Args:
        mensaje (str): Mensaje a mostrar para que el usuario ingrese el dato.
        longitud (int): Longitud requerida para la validacion.

    Returns:
        str|None: Si el dato se valida devuelve el string, en caso contrario no devuelve nada.
    """
    dato_ingresado = input(mensaje)
    if validate_lenght(dato_ingresado, longitud):
        return dato_ingresado