# Ejercicio 12
# Un profesor clasifica las notas de sus alumnos de la siguiente manera:
# 1-3 Reprobado
# 4-6 Debe rendir examen final
# 7-10 Eximido
# a) Escribir un programa que indique la clasificación de una nota.
nota = int(input("Ingrese la nota "));
clasificacion = "Reprobado";
if nota >=4 and nota <= 6 :
    clasificacion = "Debe rendir examen final";

if nota >= 7 :
    clasificacion = "Eximido";
print(clasificacion);