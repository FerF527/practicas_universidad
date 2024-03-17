# Pasar los ejercicios 2, 3, 4 y 5 hechos en papel a programas en Python y probarlos.

# Ejercicio 2
# Dar expresiones de código tal cual como las escribiría en python para calcular las siguientes expresiones matemáticas.
# c) (x+(y/z)) / (x-(y/z))

print("Ejercicio c: ");
valor_x = input("Ingrese el valor x: ");
valor_y = input("Ingrese el valor y: ");
valor_z = input("Ingrese el valor z: ");
x = float(valor_x);
y = float(valor_y);
z = float(valor_z);
resultado = (x+(y/z)) / (x-(y/z));
print("El resultado es: ",resultado);