# b) Hacer un programa que permita al usuario elegir un número m y un n y luego
# muestre todos los naturales entre m y n (m, m + 1, m + 2, · · · , n − 1, n). ¿Qué pasa si n es menor que m?

# si n es menor a m no se ejecuta muestra ningún numero porque paso el rango del final del ciclo.
m = int(input("Ingrese el número natural m "));
n = int(input("Ingrese el número natural n "));

print("Números entre",m,"y",n);
m = m+1;
while m < n :
    print(m);
    m = m + 1;