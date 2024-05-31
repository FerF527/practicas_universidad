from ejercicio3 import *
numero = int(input("Ingrese un número entero mayor a 0 "))
if numero > 0 :
    divisores_encontrados = divisores(numero)
    print("Estos son los divisores de",numero,":",divisores_encontrados)
else :
    print("No se ingresó un numero mayor a 0, vuelva a intentar")