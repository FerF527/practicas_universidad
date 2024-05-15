# Hacer un programa que dada una palabra y una letra, imprima la cantidad de apariciones de
# esa letra.

palabra = input("Ingrese un texto ")
letra = input("Ingrese la letra a buscar ")
apariciones = 0

for carac in palabra :
    if carac == letra :
        apariciones += 1
print("La letra",letra,"aparece",apariciones,"veces")