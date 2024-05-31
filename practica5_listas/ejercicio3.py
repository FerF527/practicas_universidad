# Definir una función llamada divisores que tome un entero y devuelva la lista de divisores de
# ese entero.
def divisores(numero) :
    div_encontrados = []
    for i in range(1,numero + 1) :
        if numero % i == 0 :
            div_encontrados.append(i)
    return div_encontrados