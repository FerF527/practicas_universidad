# c) Hacer un programa que permita al usuario elegir un número n y un número c, y
# luego muestre los c números naturales que le siguen a n (n + 1, n + 2, · · · , n + c).

n = int(input("Ingrese el número natural n "));
c = int(input("Ingrese el número natural c "));

print("Mostrando números desde",n+1,"hasta",n+c);
c = n + c + 1;
n = n + 1;
while n < c :
    print(n);
    n = n + 1; 