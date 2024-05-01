# Escribir un programa que solicite al usuario un número positivo y aproxime el valor del número
# e de la siguiente manera: (ejemplo para 7 términos)
# e = 1/0! + 1/1! + 1/2! + 1/3! + 1/4! + 1/5! + 1/6!
terminos = int(input("Ingresar un número de términos "))
total = 0
ciclo = 0
if terminos > 0 :
    while ciclo < terminos :
        multiplicacion = 1
        contador = 1
        while contador <= ciclo :
            multiplicacion = multiplicacion * contador
            contador = contador + 1
        total = total + 1/multiplicacion
        ciclo = ciclo + 1
    print(total,end=" ")
else :
    print("Debe ingresar un número de términos mayor a 0")