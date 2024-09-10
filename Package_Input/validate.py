def validate_number(valor: int|float) -> bool:
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
    validacion = False
    if len(dato) == longitud:
        validacion = True
    return validacion