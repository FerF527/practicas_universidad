#Escribir una función llamada maximo que tome una lista de números y devuelva el valor del
#máximo elemento
def maximo (lista):
    if not lista:
        return None
    numero_mayor = lista[0]
    for numero in lista:
        if numero>numero_mayor:
            numero_mayor = numero
    return numero_mayor