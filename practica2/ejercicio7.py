# Escribir en papel un programa que pida al usuario dos números de punto flotante y muestre
# su promedio. Además, si el promedio es mayor que 7 el programa debe mostrar en pantalla
# "Aprobado" y si no, debe mostrar "Desaprobado". Después de hacerlo en papel, pasarlo a Python.
nota1 = float(input("Ingrese una nota "));
nota2 = float(input("Ingrese otra nota "));
promedio = (nota1 + nota2) / 2;
print("promedio",promedio);
if promedio > 7 :
    print("Aprobado");
else :
    print("Desaprobado");