# b) Hacer un programa que permita al usuario elegir un número n y luego muestre los
# primeros n números naturales (1, 2, · · · , n).
n = int(input("Ingrese un número natural mayor a 0: "));
for numero in range(1,n+1):
    print(numero);