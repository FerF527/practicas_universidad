# a) Hacer un programa que permita al usuario elegir un número positivo n y luego
# muestre en pantalla las n primeras sumas parciales de la sucesión an = 2n. Es decir,
# 2 6 12 20...
terminos = int(input("Ingrese un número de términos "))
if terminos > 0 :
    suma = 0
    for ciclo in range(1,terminos + 1) :
        suma = suma + 2*ciclo
        print(suma,end=" ")
else :
    print("Debe ingresar un número de términos mayor a 0")