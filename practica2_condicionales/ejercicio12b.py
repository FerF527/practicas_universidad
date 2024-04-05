# Ejercicio 12
# Un profesor clasifica las notas de sus alumnos de la siguiente manera:
# 1-3 Reprobado
# 4-6 Debe rendir examen final
# 7-10 Eximido
# b) Escribir un programa que pida 3 notas, calcule el promedio e indique la clasificación
# del mismo.
nota1 = int(input("Ingrese la primer nota "));
nota2 = int(input("Ingrese la segunda nota "));
nota3 = int(input("Ingrese la tercer nota "));
clasificacion = "Reprobado";
promedio = (nota1 + nota2 + nota3) / 3;
print("promedio",promedio);
if promedio >=4 and promedio < 7 :
    clasificacion = "Debe rendir examen final";

if promedio >= 7 :
    clasificacion = "Eximido";
print(clasificacion);