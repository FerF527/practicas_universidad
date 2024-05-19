# Hacer un programa que solicite al usuario un número entero positivo e indique cuál es el
# número primo mayor más cercano. Usar funciones. Por ejemplo, si el usuario ingresa 24, el
# programa devolverá 29 (29 es el número primo más cercano mayor que 24). Si el usuario ingresa
# 5 el programa devolverá 7.


# importamos la funcion para saber si un número es primo
from ejercicio8b import *

def primo_mayor(num) :
    for i in range(num+1,500000) :
        if es_primo(i) :
            return i
    return -1

# prueba
# numero = int(input("Ingrese un número entero "))
# numero_primo_mayor = primo_mayor(numero)
# if numero_primo_mayor != -1:
#     print(numero_primo_mayor,"es el número primo mas cercano de",numero)
# else :
#     print("no se encontro un primo cercano a",numero,"en el rango de",numero,"a 500000")