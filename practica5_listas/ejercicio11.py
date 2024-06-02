# Escribir una función llamada maximoEntre que tome una lista de números y dos enteros a y b
# menores que la longitud de la lista y devuelva el índice del máximo elemento considerando solo
# los que están entre el índice a y el índice b.
def maximoEntre(lista,num1,num2) :
    num_mas_alto = 0
    indice_num_mas_alto = -1
    if num1 > num2 :
        maximo_indice = num1
        minimo_indice = num2
    else :
        maximo_indice = num2
        minimo_indice = num1
    for i in range(len(lista)) :
        if lista[i] > num_mas_alto and i >= minimo_indice and i<=maximo_indice :
            num_mas_alto = lista[i]
            indice_num_mas_alto = i
    return indice_num_mas_alto