# b) Hacer un programa que permita al usuario elegir un número n y luego muestre los
# 5 números naturales que le siguen a n (n + 1, n + 2, · · · , n + 5).
n = int(input("Ingrese el número natural "));
print("Mostrando los siguientes 5 números");
for numero in range(n+1,n+6):
    print(numero);