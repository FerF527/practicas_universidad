# Escribir un programa que pida al usuario una cadena y una letra y reemplace las apariciones
# de dicha letra por asteriscos. Por ejemplo, si el usuario ingresa:
# "programador"
# "r"
# el programa debe devolver "p ∗ og ∗ amado∗"

palabra = input("Ingrese un texto ")
letra = input("Ingrese la letra a reemplazar ")
nueva_palabra = ""
for carac in palabra :
    if carac == letra :
        nueva_palabra += "*"
    else :
        nueva_palabra += carac

print("Palabra modificada =",nueva_palabra)