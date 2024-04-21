# b) Hacer un programa que reciba un número n (n > 0) y muestre las n primeras
# potencias de 2. Por ejemplo, si el usuario ingresa 6, el programa mostrará: 1 2 4 8
# 16 32.
numero_ingresado = int(input("Ingrese un número mayor a 0: "));
inicio = 1;
potencias = 1;
if numero_ingresado > 0 :
    print("Mostrando las primeras",numero_ingresado,"potencias de 2");
    for inicio in range(1,numero_ingresado + 1) :
        print(potencias);
        potencias = potencias*2;
else :
    print("Debe ingresar un número natural mayor a 0, reinicie el programa por favor.");