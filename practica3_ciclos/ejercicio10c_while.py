# c) Hacer un programa que reciba un número n (n > 0) y muestre las n primeras
# potencias de n. Por ejemplo, si el usuario ingresa 4, el programa mostrará: 1 4 27
# 256. Es decir, 1**1 2**2 3**3 4**4.

numero_ingresado = int(input("Ingrese un número natural mayor a 0: "));
potencias = 1;
contador_ciclos = 1;
if numero_ingresado > 0 :
    while contador_ciclos <= numero_ingresado :
        print(potencias);
        contador_ciclos = contador_ciclos + 1;
        potencias = contador_ciclos**contador_ciclos;
else :
    print("Debe ingresar un número natural mayor a 0, reinicie el programa por favor.");