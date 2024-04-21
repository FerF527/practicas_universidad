# c) Hacer un programa que permita al usuario elegir un número positivo n y luego
# muestre en pantalla la cantidad de divisores de n.

numero_ingresado = int(input("Ingrese un número positivo: "));
cant_divisores = 0;
if numero_ingresado > 0 :
    for pos_div in range(1,numero_ingresado + 1) :
        if numero_ingresado % pos_div == 0 :
            cant_divisores = cant_divisores + 1;
    print(numero_ingresado,"tiene",cant_divisores,"divisores");
else :
    print("Debe ingresar un número positivo, vuelva a ejecutar el programa por favor.");