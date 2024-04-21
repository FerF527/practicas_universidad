# c) Hacer un programa que permita al usuario elegir un número n, un m y un p y
# luego muestre todos los naturales entre m y n, pero salteando de a p números. Por
# ejemplo, si el usuario ingresara un n igual a 2 y un m igual a 14, y un p igual a 4,
# el programa deberá mostrar 2, 6, 10, 14.
n = int(input("Ingrese el número inicial "));
m = int(input("Ingrese el número final "));
p = int(input("Ingrese el número de saltos "));

print("Números entre",n,"y",m,"en saltos de",p);
while n <= m :
    print(n);
    n = n + p;