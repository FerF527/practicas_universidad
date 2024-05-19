# Hacer una función (no pura) que reciba una palabra y la imprima recuadrada por asteriscos.
# Por ejemplo si la cadena fuera sobrevivir, la función debería imprimir
# **************
# * sobrevivir *
# **************
def recuadrar_texto(cadena) :
    cant_letras = len(cadena)
    for i in range(cant_letras + 4) :
        print("*",end="")
    print("\n*",cadena,"*")
    for i in range(cant_letras + 4) :
        print("*",end="")

#programa principal
palabra = input("Ingrese un texto ")
recuadrar_texto(palabra)