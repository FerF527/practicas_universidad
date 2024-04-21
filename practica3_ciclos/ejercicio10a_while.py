# Hacer un programa que reciba un número n y muestre todas las potencias de 2
# menores a n. Por ejemplo, si el usuario ingresa 20, el programa mostrará: 1 2 4 8
# 16. Ayuda: pensar primero si sería más práctico utilizar la sentencia while o for.

numero_ingresado = int(input("Ingrese un número natural mayor a 0: "));
numero_inicial = 1;
while numero_inicial <= numero_ingresado :
    print(numero_inicial);
    numero_inicial = numero_inicial * 2;