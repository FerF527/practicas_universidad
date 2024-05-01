# El logaritmo natural de 2 (ln(2)) se puede aproximar de la siguiente manera:
# ln(2) = 1 − 1/2 + 1/3 − 1/4 + 1/5 . . .
# a) Escribir un programa que le pregunte al usuario la cantidad de términos a sumar y
# que muestre la aproximación de ln(2) con esa cantidad de términos.

terminos = int(input("Ingresar un número de términos "))
suma = 0
for ciclo in range (1,terminos+1) :
    if ciclo % 2 == 0 :
        suma = suma - 1/ciclo
    else :
        suma = suma + 1/ciclo
print(suma,end=" ")