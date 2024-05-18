# a) Hacer una función que sume los divisores propios de un número.
def divisores_propios(num) :
    suma_divisores = 0
    for i in range(1,num) :
        if num % i == 0 :
            suma_divisores += i
    return suma_divisores

# prueba
# print(divisores_propios(4))