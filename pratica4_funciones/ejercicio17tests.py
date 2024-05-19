from ejercicio17a import *
from ejercicio17b import *
from ejercicio17c import *
from ejercicio17d import *

# test 17 a
print("Test función tieneRepetidas \n")
palabra = input("Ingrese un texto ")
hayRepetidas =  tieneRepetidas(palabra)
if hayRepetidas : 
    print(palabra,"tiene letras repetidas")
else :
    print(palabra,"no tiene letras repetidas")

# test 17 b
print()
print("Test función aparece \n")
palabra = input("Ingrese un texto ")
letra = input("Ingrese una letra ")
existeLetra =  aparece(palabra,letra)
if existeLetra : 
    print(letra,"aparece en la palabra",palabra)
else :
    print(letra,"no aparece en la palabra",palabra)

# test 17 c
print()
print("Test función dameRepetida \n")
palabra = input("Ingrese un texto ")
letraRepetida =  dameRepetida(palabra)
if letraRepetida == False  : 
    print(palabra,"no tiene letras repetidas")
else :
    print("La primera letra que se repite en",palabra,"es:",letraRepetida)

# test 17 b
print()
print("Test función quitarRepeticiones \n")
texto = input("Ingrese un texto ")
letra = input("Ingrese una letra ")
nuevo_texto =  quitarRepeticiones(texto,letra)
print(nuevo_texto)