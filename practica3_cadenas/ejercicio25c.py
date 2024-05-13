# c) Escribir un programa que pida al usuario un número n y muestre n líneas de 2n − 1
# asteriscos respectivamente. Ejemplo, para n = 5, el programa deberá mostrar:
# *
# ***
# *****
# *******
# *********

n = int(input("Ingrese un número mayor a 0 "))

ciclo = 1
if n > 0 :
    while ciclo <= n :
        for i in range(0,ciclo *2 - 1) :
            print("*",end="")
        ciclo += 1
        print("\n")
else :
    print("debe ingresar un número mayor a 0")