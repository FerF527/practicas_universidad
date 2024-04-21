# Hacer un programa que permita al usuario elegir un número m y un n y luego
# muestre todos los naturales entre m y n, pero salteando de a 3. Por ejemplo, si el
# usuario ingresara un n igual a 2 y un m igual a 14, el programa deberá mostrar
# 2, 5, 8, 11, 14.
n = int(input("Ingrese el número natural n "));
m = int(input("Ingrese el número natural m "));

print("Mostrando números entre",n,"y",m,"en saltos de 3");
m = m + 1;
while n < m :
    print(n);
    n = n +3;