# c) De no haberlo hecho en el punto anterior, escribir de nuevo la función gritar utilizando solo la función exclamar.
from ejercicio6a import *
def gritar2(unaCadena) :
    nueva_cadena = exclamar(unaCadena)
    nueva_cadena = "¡¡" + nueva_cadena + "!!"
    return nueva_cadena