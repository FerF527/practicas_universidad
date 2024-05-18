# b) Hacer una función que indique si un número es perfecto. Número perfecto: a es
# perfecto si la suma de sus divisores propios es igual a a
from ejercicio11a import *
def num_perfecto(num) :
    suma_divisores = divisores_propios(num)
    if suma_divisores == num :
        return True
    return False

# prueba
# numero = int(input("Ingrese un número entero "))
# es_perfecto = num_perfecto(numero)
# if es_perfecto :
#     print(numero,"es perfecto.")
# else :
#     print(numero,"no es perfecto.")