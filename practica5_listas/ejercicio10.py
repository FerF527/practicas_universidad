# Escribir una función llamada maximoIndice que tome una lista de números y devuelva el
# índice del máximo elemento.
def maximoindice(lista):
    if not lista:
        return None
    indice_mas_alto = -1
    for i in range(len(lista)):
        if lista[i] > lista[indice_mas_alto]:
            indice_mas_alto = i
    return indice_mas_alto