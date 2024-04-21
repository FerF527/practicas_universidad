# a) Hacer un programa que permita al usuario elegir un número positivo n y luego
# muestre en pantalla todos los divisores de n.
numero_ingresado = int(input("Ingrese un número positivo: "));
inicio = 1;
if numero_ingresado > 0 :
    print("Mostrando divisores de",numero_ingresado);
    print("divisores:",end=" ");
    for inicio in range(1,numero_ingresado + 1) :
        if numero_ingresado % inicio == 0 :
            print(inicio,end=" ");
else :
    print("Debe ingresar un número positivo, vuelva a ejecutar el programa por favor.");