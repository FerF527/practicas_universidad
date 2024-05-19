# b) una función que se llame aparece que tome dos parámetros, una letra y una cadena,
# y devuelva True si la letra aparece en la cadena y False en caso contrario.
def aparece(cadena,letra) :
    for char in cadena :
        if char == letra :
            return True
    return False