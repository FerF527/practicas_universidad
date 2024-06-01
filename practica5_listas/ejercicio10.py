def maximoindice(lista):
    if not lista:
        return None
    indice_mas_alto = 0
    for i in range(len(lista)):
        if lista[i] > lista[indice_mas_alto]:
            indice_mas_alto = i
    return indice_mas_alto

lista = [13, 24, 65, 78, 6]
indice_mas_alto = maximoindice(lista)
print(f"El índice del número más alto en la lista es: {indice_mas_alto}")