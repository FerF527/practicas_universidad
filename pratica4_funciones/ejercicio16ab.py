# a) escribir una función que tome como parámetros una cadena y una letra, y retorne
# la cantidad de veces que aparece esa letra en esa cadena.
def encontrar_letra(palabra,letra) :
    cant_letras = 0
    for char in palabra :
        if char == letra :
            cant_letras += 1
    return cant_letras

# prueba
palabra = input("Ingrese un texto ")
letra = input("Ingrese la letra a encontrar ")
cant_letras_encontradas = encontrar_letra(palabra,letra)
print("La letra",letra,"aparece",cant_letras_encontradas,"veces en la palabra",palabra)