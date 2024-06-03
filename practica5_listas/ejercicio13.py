# Escribir una función llamada frecuencia que tome una lista de enteros s y otro entero n como
# parametros y devuelva la cantidad de veces que aparece n en s.
def frecuencia(s,n) :
    cant_veces = 0
    for i in range(len(s)) :
        if s[i] == n :
            cant_veces += 1
    return cant_veces
s = [1,2,5,4,5]
n = 5
print(frecuencia(s,n))