# Pasar los ejercicios 2, 3, 4 y 5 hechos en papel a programas en Python y probarlos.

# Ejercicio 4

# Escribir una expresión matemática que dado un número natural evalúe al siguiente número más
# grande. Por ejemplo, dado el número 1 el resultado de evaluar la expresión es 2, dado 37 el resultado
# es 38.

numero_ingresado = input("Ingrese un número natural ");
numero_ingresado = int(numero_ingresado);
if numero_ingresado <= 0 : 
    print("El número debe ser mayor a 0");
else:
    numero_siguiente = numero_ingresado + 1;
    print("Resultado: ",numero_siguiente);