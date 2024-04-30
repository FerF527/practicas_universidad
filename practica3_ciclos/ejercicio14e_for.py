# e) Idem anterior para la sucesión an = 1/n^2.

terminos = int(input("Ingrese un número de términos "))
for ciclo in range(1,terminos + 1) :
    print(1/ciclo**2,end=" ")