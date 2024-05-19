from ejercicio17a import *
from ejercicio17b import *
# test 17 a
palabra = input("Ingrese un texto ")
hayRepetidas =  tieneRepetidas(palabra)
if hayRepetidas : 
    print(palabra,"tiene letras repetidas")
else :
    print(palabra,"no tiene letras repetidas")

# test 17 b
print("\n")
palabra = input("Ingrese un texto ")
letra = input("Ingrese una letra ")
existeLetra =  aparece(palabra,letra)
if existeLetra : 
    print(letra,"aparece en la palabra",palabra)
else :
    print(letra,"no aparece en la palabra",palabra)