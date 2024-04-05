# Escribir un programa que pida al usuario dos enteros y los guarde en dos variables. Si el
# primero de los valores fuera menor que el segundo, el programa deberá además intercambiar los
# valores de las variables y mostrarlos de mayor a menor.
numero1 = int(input("Ingrese el primer número "));
numero2 = int(input("Ingrese el segundo número "));
if numero1 < numero2 :
    mayor = numero2;
    numero2 = numero1;
    numero1 = mayor;
print("Orden de mayor a menor",numero1,"",numero2);