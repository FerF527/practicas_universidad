# Definir una función llamada mostrarEnUnaLinea que tome una lista de enteros y muestre
# todos sus elementos en una linea separados por espacios.
def mostrarEnUnaLinea(listaEnteros) :
    cadena_elementos = ""
    for elemento in listaEnteros :
        cadena_elementos += elemento + " "
    return cadena_elementos