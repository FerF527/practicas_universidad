# d) Idem anterior para la sucesión an = n**3 − n**2.

terminos = int(input("Ingrese un número de términos "))
ciclo = 1
while ciclo <= terminos :
    print(ciclo**3-ciclo**2,end=" ")
    ciclo = ciclo + 1