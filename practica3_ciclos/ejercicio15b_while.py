# b)Hacer un programa que permita al usuario elegir un número positivo n y luego
# muestre en pantalla las n primeras sumas parciales de la sucesión an = n^2.
terminos = int(input("Ingrese un número de términos "))
if terminos > 0 :
    suma = 0
    ciclo = 1
    while ciclo <= terminos :
        suma = suma + ciclo**2
        #suma += + ciclo**2
        ciclo +=1
        print(suma,end=" ")
else :
    print("Debe ingresar un número de términos mayor a 0")