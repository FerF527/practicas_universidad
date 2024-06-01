# Hacer una función que tome una lista de números decimales y devuelva el promedio de los
# elementos

def promedioElementos(lista):
    suma = 0
    for numero in lista:
        suma += numero
    cantNumeros = len(lista)
    return suma / cantNumeros

lista=[6.5,7.0,6.0]
programa=promedioElementos(lista)
print(f"el promedio de los terminos en la lista es de: {programa}")


        
    
        
        