# Definir una función llamada dondeAparece que tome una lista de enteros y un entero llamado
# blanco como parámetros, y devuelva el primer índice donde blanco aparece en el arreglo, si lo
# hace, y -1 en caso contrario.
def dondeAparece (lista,blanco):
    for i in range (len(lista)):
        if lista [i] == blanco:
            return i
    return -1