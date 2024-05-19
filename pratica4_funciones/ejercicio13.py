# Hacer una función que indique si un número es Libre de Cuadrados: Número libre de cuadrados:
# todo número natural que cumple que en su descomposición en factores primos no aparece ningún
# factor repetido. Por ejemplo, el número 30 es un número libre de cuadrados.

# importamos la funcion para saber si un número es primo
from ejercicio8b import *

def libre_de_cuadrados(num) :
    es_libre_de_cuadrados = True
    for i in range(1,num) :
        if num%i == 0 and es_primo(i) :
            cuadrado = i**2
            if num%cuadrado == 0 and num!=cuadrado :
                return False
    return es_libre_de_cuadrados

# prueba
# numero = int(input("Ingrese un número entero "))
# es_libre_de_cuadrados = libre_de_cuadrados(numero)
# if es_libre_de_cuadrados :
#     print(numero,"es libre de cuadrados.")
# else :
#     print(numero,"no es libre de cuadrados.")