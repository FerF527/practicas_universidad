# c) transformar el código del ejercicio 25 de la práctica de ciclos y cadenas para que utilice la nueva función.

# ejercicio 25 a Escribir un programa que pida al usuario un número n y muestre una línea de n
# asteriscos. Ejemplo, para n = 8, el programa deberá mostrar:
# ********

def asteriscos_en_linea(cant_astericos) :
    contador = 0
    resultado = ""
    while contador < cant_astericos :
        resultado += "*"
        contador += 1
    return resultado

# 25 b) Escribir un programa que pida al usuario un número n y muestre n líneas de
# 1, 2, 3, ...n asteriscos respectivamente. Ejemplo, para n = 5, el programa deberá
# mostrar:
# *
# **
# ***
# ****
# *****
def asteriscos_con_saltos_de_linea(cant_saltos) :
    resultado = ""
    for cont in range(1,cant_saltos + 1) :
        resultado += cont * "*" + "\n"
    return resultado

# c) Escribir un programa que pida al usuario un número n y muestre n líneas de 2n − 1
# asteriscos respectivamente. Ejemplo, para n = 5, el programa deberá mostrar:
# *
# ***
# *****
# *******
# *********
def asteriscos_impares_con_saltos_de_linea(cant_saltos) :
    resultado = ""
    for cont in range(1,cant_saltos + 1) :
        resultado += (cont * 2 - 1) * "*" + "\n"
    return resultado