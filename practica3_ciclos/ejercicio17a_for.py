# El número 1/4 π se puede aproximar de la siguiente manera:
# 1/4 π = 1 - 1/3 + 1/5 -1/7 + 1/9 -1/11 + 1/13 - 1/15 ...
# a) Escribir un programa que le pregunte al usuario la cantidad de términos a sumar y
# que muestre la aproximación de π con esa cantidad de términos.

terminos = int(input("Ingresar un número de términos "))
suma = 0
for ciclo in range (1,terminos+1) :
    if ciclo % 2 == 0 :
        suma = suma - 1/(2*ciclo-1)
    else :
        suma = suma + 1/(2*ciclo-1)
print(suma,end=" ")