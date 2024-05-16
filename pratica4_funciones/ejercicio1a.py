# Hacer un programa para cada inciso que pida al usuario un número decimal x y muestre por
# pantalla el resultado de evaluar las siguientes fórmulas:
# a) √x
def raiz (num) :
    resultado = num**(1/2)
    return resultado
#programa principal
numero = int(input("Ingrese un número "))
raiz_numero = raiz(numero)
print("La raíz cuadrada de",numero,"es",raiz_numero)