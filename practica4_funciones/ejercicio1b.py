# Hacer un programa para cada inciso que pida al usuario un número decimal x y muestre por
# pantalla el resultado de evaluar las siguientes fórmulas:
# b) |x|

def calcular_valor_absoluto (num) :
    if num < 0 :
        valor_absoluto = num * - 1
    else :
        return num
    return valor_absoluto
#programa principal
numero = int(input("Ingrese un número "))
valor_absoluto = calcular_valor_absoluto(numero)
print("El valor absoluto de",numero,"es",valor_absoluto)