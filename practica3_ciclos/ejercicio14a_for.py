# a) Hacer un programa que permita al usuario elegir un número positivo n y luego
# muestre en pantalla los n primeros términos de la sucesión an = 2n. Es decir 2, 4,
# 6...
terminos = int(input("Ingrese un número de términos "))
for ciclo in range(1,terminos + 1) :
    print(ciclo*2,end=" ")