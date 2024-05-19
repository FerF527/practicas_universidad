# Hacer una función que indique si un número es Poderoso: Número poderoso: es un número
# natural n que cumple que todos sus divisores primos al cuadrado también son divisores, es decir,
# si p es un divisor primo entonces p^2 también lo es. Por ejemplo, el número 36 es un número
# poderoso ya que los únicos primos que son divisores suyos son 2 y 3 y se cumple que 4 y 9
# también son divisores de 36.

# importamos la funcion para saber si un número es primo
from ejercicio8b import *

def num_poderoso(num) :
    es_poderoso = False
    for i in range(1,num) :
        if num%i == 0 and es_primo(i) :
            cuadrado = i**2
            if num%cuadrado == 0 and num!=cuadrado :
                es_poderoso = True
            else :
                es_poderoso = False
    return es_poderoso

# prueba
# numero = int(input("Ingrese un número entero "))
# es_poderoso = num_poderoso(numero)
# if es_poderoso :
#     print(numero,"es poderoso.")
# else :
#     print(numero,"no es poderoso.")