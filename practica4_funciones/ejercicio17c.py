# c) una función que se llame dameRepetida que tome una cadena como parámetro y
# retorne la primer letra que aparece repetida en la cadena
def dameRepetida(cadena) :
    for letra in cadena :
        num_letras = letraDuplicada(cadena,letra)
        if num_letras >= 2 :
            return letra
    return False

def letraDuplicada(cadena,letra) :
    cant_letras = 0
    for char in cadena :
        if char == letra :
            cant_letras += 1
    return cant_letras