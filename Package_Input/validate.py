def validate_number(valor: int|float) -> bool:
    """Funcion para validar si es un numero.

    Args:
        valor (int | float): Dato a verificar

    Returns:
        bool: Si el dato se verifica el programa devuelve True, en caso contrario devuelve False.
    """
    validacion = False
    try:
        valor = float(valor)
        validacion = True
    except:
        try:
            valor = int(valor)
            validacion = True
        except:
            pass
    return validacion

def validate_lenght(dato: str, longitud: int) -> bool:
    """Funcion para validar si es un numero.
    
    Args:
        valor (int | float): Dato a verificar
    
    Returns:
    bool: Si el dato se verifica el programa devuelve True, en caso contrario devuelve False.
    """
    validacion = False
    if len(dato) == longitud:
        validacion = True
    return validacion