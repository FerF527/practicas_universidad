# c) Hacer una función que determine si un número ingresado por el usuario es un número
# abundante. Número abundante: todo número natural que cumple que la suma de sus
# divisores propios es mayor que el propio número. Por ejemplo, 12 es abundante ya
# que sus divisores son 1, 2, 3, 4 y 6 y se cumple que 1+2+3+4+6=16, que es mayor
# al propio 12.
from ejercicio11a import *
def num_abundante(num) :
    suma_divisores = divisores_propios(num)
    if suma_divisores > num :
        return True
    return False

# prueba
# numero = int(input("Ingrese un número entero "))
# es_abundante = num_abundante(numero)
# if es_abundante :
#     print(numero,"es abundante.")
# else :
#     print(numero,"no es abundante.")