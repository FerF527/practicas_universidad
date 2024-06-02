##programa principal ejercicio 11
from ejercicio11 import maximoEntre
lista = [13, 24, 65, 6, 78]
ultimo_indice = len(lista) - 1
a = 1
b = 4
if a > ultimo_indice or b > ultimo_indice : 
    print("Los numeros a y b deben ser menores a la longitud de la lista")
else :
    indice_mas_alto = maximoEntre(lista,a,b)
    print(f"El índice del número más alto en la lista es: {indice_mas_alto}")