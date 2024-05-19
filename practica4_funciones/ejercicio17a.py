# Escribir una función (y probarla en un programa) para cada una de las siguientes descripciones:
# a) una función que se llame tieneRepetidas que tome una cadena como parámetro y
# devuelva True si esa cadena tiene alguna letra que aparece más de una vez y False
# en caso contrario.
def tieneRepetidas(cadena) :
    for letra in cadena :
        num_letras = cantLetras(cadena,letra)
        if num_letras >= 2 :
            return True
    return False
def cantLetras(cadena,letra) :
    cant_letras = 0
    for char in cadena :
        if char == letra :
            cant_letras += 1
    return cant_letras