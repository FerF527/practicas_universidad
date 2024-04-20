# c) Hacer un programa que permita al usuario elegir un número n y un número c, y
# luego muestre los c números naturales que le siguen a n (n + 1, n + 2, · · · , n + c).

n = int(input("Ingrese el número natural n "));
c = int(input("Ingrese el número natural c "));

print("Numeros desde",n+1,"hasta",n+c);
for numero in range(n +1,n+c+1):
    print(numero);