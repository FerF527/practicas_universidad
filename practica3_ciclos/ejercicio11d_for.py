# Hacer un programa que permita al usuario elegir un número positivo n y luego
# muestre en pantalla la suma de los divisores de n.
numero_ingresado = int(input("Ingrese un número positivo: "));
suma = 0;
if numero_ingresado > 0 :
    for ciclo in range(1,numero_ingresado + 1) :
        if numero_ingresado % ciclo == 0 :
            suma = suma + ciclo;
    print("La suma de los divisores de",numero_ingresado,"es",suma);
else :
    print("Debe ingresar un número positivo, vuelva a ejecutar el programa por favor.");