# a) Hacer un programa que permita al usuario elegir un número positivo n y luego
# muestre en pantalla las n primeras sumas parciales de la sucesión an = n^3 − n^2.
terminos = int(input("Ingrese un número de términos "))
if terminos > 0 :
    suma = 0
    for ciclo in range(1,terminos + 1) :
        suma = suma + ciclo**3 - ciclo**2
        print(suma,end=" ")
else :
    print("Debe ingresar un número de términos mayor a 0")