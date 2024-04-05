# Se desea escribir un programa que pida al usuario tres números y luego muestre el mayor de
# ellos. Escribir el programa en papel, realizar 3 pruebas de escritorio y luego pasarlo a Python y
# verificar los resultados.
a = int(input("Ingrese el primer número "));
b = int(input("Ingrese el segundo número "));
c = int(input("Ingrese el tercer número "));
mayor = c;
if a > b and a > c :
     mayor = a;
else :
     if b > a and  b > c :
          mayor = b;
print("El mayor es:",mayor);