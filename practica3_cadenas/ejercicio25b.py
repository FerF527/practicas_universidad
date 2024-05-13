# b) Escribir un programa que pida al usuario un número n y muestre n líneas de
# 1, 2, 3, ...n asteriscos respectivamente. Ejemplo, para n = 5, el programa deberá
# mostrar:
# *
# **
# ***
# ****
# *****

n = int(input("Ingrese un número mayor a 0 "))

ciclo = 1
if n > 0 :
    while ciclo <= n :
        for i in range(1,ciclo + 1) :
            print("*",end="")
        ciclo += 1
        print("\n")
else :
    print("debe ingresar un número mayor a 0")