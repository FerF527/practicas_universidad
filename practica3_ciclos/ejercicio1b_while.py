# b) Hacer un programa que permita al usuario elegir un número n y luego muestre los
# primeros n números naturales (1, 2, · · · , n).
n = int(input("Ingrese un número natural mayor a 0: "));
numero_inicial = 1;
print("Mostrando números desde 1 a",n);
while numero_inicial <= n :
    print(numero_inicial);
    numero_inicial = numero_inicial + 1;