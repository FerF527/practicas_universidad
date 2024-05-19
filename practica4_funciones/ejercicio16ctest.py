# c) transformar el código del ejercicio 25 de la práctica de ciclos y cadenas para que utilice la nueva función.

# ejercicio 25 a Escribir un programa que pida al usuario un número n y muestre una línea de n
# asteriscos. Ejemplo, para n = 8, el programa deberá mostrar:
# ********
from ejercicio16c import *
# prueba 25a con función asteriscos_en_linea()
num_asteriscos = int(input("Ingrese la cantidad de asteriscos a imprimir "))
resultado = asteriscos_en_linea(num_asteriscos)
print(resultado)

# 25 b) Escribir un programa que pida al usuario un número n y muestre n líneas de
# 1, 2, 3, ...n asteriscos respectivamente. Ejemplo, para n = 5, el programa deberá
# mostrar:
# *
# **
# ***
# ****
# *****

# prueba 25b con función asteriscos_con_saltos_de_linea()
print("\n")
num_saltos = int(input("Ingrese la cantidad de saltos a imprimir "))
resultado = asteriscos_con_saltos_de_linea(num_saltos)
print(resultado)

# 25 c) Escribir un programa que pida al usuario un número n y muestre n líneas de 2n − 1
# asteriscos respectivamente. Ejemplo, para n = 5, el programa deberá mostrar:
# *
# ***
# *****
# *******
# *********

# prueba 25c con función asteriscos_impares_con_saltos_de_linea()
print("\n")
num_saltos_impares = int(input("Ingrese la cantidad de saltos a imprimir "))
resultado = asteriscos_impares_con_saltos_de_linea(num_saltos_impares)
print(resultado)