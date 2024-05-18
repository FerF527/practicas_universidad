# b) Escribir una función que tome un parámetro de tipo entero y devuelva el valor True
# si se la llama con un número primo y False en caso contrario.
from ejercicio8a import *
def es_primo(num) : 
    num_divisores = cant_divisores(num)
    if num_divisores == 2 :
        return True
    else :
        return False
    
# prueba
# print(es_primo(10))