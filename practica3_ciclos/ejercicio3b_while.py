# b) Hacer un programa que permita al usuario elegir un número n y luego muestre los
# 5 números naturales que le siguen a n (n + 1, n + 2, · · · , n + 5).
n = int(input("Ingrese un número natural "));
print("Mostrando los siguientes 5 números naturales");
n = n + 1;
fin_ciclo = n + 5;
while n < fin_ciclo :
    print(n);
    n = n + 1;