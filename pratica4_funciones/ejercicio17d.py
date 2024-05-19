# d) una función que se llame quitarRepeticiones que tome dos parámetros, una
# cadena y una letra, y devuelva otra cadena igual a la anterior pero sin las
# repeticiones de esa letra. Por ejemplo, un programa que llame a la función
# así: quitarRepeticiones("mate cocido", "c"), deberá retornar la cadena "mate coido".

def quitarRepeticiones(cadena,letra) :
    nuevo_texto = ""
    posicion_letra = 0
    for char in cadena :
        num_letras = encontrarLetraDuplicada(cadena,char)
        if num_letras >= 2 and char == letra :  
            posicion_letra += 1
            if posicion_letra >= 2 :
                nuevo_texto += ""
            else :
                nuevo_texto += char
        else :
            nuevo_texto += char
    return nuevo_texto

def encontrarLetraDuplicada(cadena,letra) :
    cant_letras = 0
    for char in cadena :
        if char == letra :
            cant_letras += 1
    return cant_letras