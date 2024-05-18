# d) Hacer una función (no pura) que reciba un entero e imprima sus factores primos.
# Por ejemplo para a = 20 la función debe mostrar 2 y 5.
# Nota: Los números primos son aquellos cuyos únicos divisores positivos son ellos
# mismos y el 1.
from ejercicio8b  import *
def factores_primos(num) :
    num_primo = False 
    for i in range(1,num + 1) :
        if num%i==0 :
            num_primo = es_primo(i)
            if(num_primo) : 
                print(i,"es factor de",num,"y es un número primo")
    
# prueba
factores_primos(8)