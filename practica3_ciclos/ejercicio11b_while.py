# b) Hacer un programa que permita al usuario elegir un número positivo n y luego
# muestre en pantalla todos los divisores pares de n.

numero_ingresado = int(input("Ingrese un número positivo: "));
divisor = 2;
if numero_ingresado > 0 :
    print("Mostrando divisores pares de",numero_ingresado);
    while divisor < numero_ingresado + 1 :
        if numero_ingresado % divisor == 0 and divisor % 2 == 0 :
            print(divisor,end=" ");
        divisor = divisor + 1;
else :
    print("Debe ingresar un número positivo, vuelva a ejecutar el programa por favor.");