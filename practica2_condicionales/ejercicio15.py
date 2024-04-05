# Escribir un programa que pida al usuario tres enteros y los guarde en tres variables a, b y c.
# El programa deberá luego hacer que en la variable a quede el menor de los valores recibidos, en
# b el intermedio y en c el mayor (es decir, ordenará los valores).
a = int(input("Ingrese el primer valor "));
b = int(input("Ingrese el segundo valor "));
c = int(input("Ingrese el terce valor "));
if a > b and a > c :
    aux = c;
    c = a;
    a = aux;
if a > b and a < c:
    aux = b;
    b = a;
    a = aux;
if b > a and b > c :
    aux = c;
    c = b;
    b = aux;
if b < a and b < c:
    aux = b;
    b = a;
    a = aux;
print("Orden de menor a mayor;",a,b,c);