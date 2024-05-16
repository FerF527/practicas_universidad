# Hacer un programa para cada inciso que pida al usuario un número decimal x y muestre por
# pantalla el resultado de evaluar las siguientes fórmulas:
# d)  √|x − 5|
def calcular_valor_absoluto (num) :
    diferencia = num - 5
    if diferencia < 0 :
        valor_absoluto = diferencia * - 1
        valor_absoluto = valor_absoluto**(1/2)
    else :
        valor_absoluto = diferencia**(1/2)
        return valor_absoluto
    return valor_absoluto
#programa principal
numero = int(input("Ingrese un número "))
valor_absoluto = calcular_valor_absoluto(numero)
print("El valor absoluto de",numero,"es",valor_absoluto)