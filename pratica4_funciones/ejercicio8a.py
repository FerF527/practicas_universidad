# a) Escribir una función que tome un parámetro de tipo entero y devuelva la cantidad
# de divisores positivos de ese número.
def cant_divisores(num) : 
    cant_divisores = 0
    for i in range(1,num + 1) :
        if num%i==0 :
            cant_divisores += 1
    return cant_divisores