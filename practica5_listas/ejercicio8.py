# Hacer una función que tome una lista de números decimales y devuelva el promedio de los
# elementos

def promedioElementos(lista):
    suma = 0
    for numero in lista:
        suma += numero
    cantNumeros = len(lista)
    return suma / cantNumeros   