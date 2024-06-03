# Escribir una función llamada intercambiar que tome una lista de números s y dos enteros
# positivos a y b menores que la longitud de la lista y cambie el elemento ubicado en s[a] por el
# elemento ubicado en s[b]. Ojo, esta función no debe devolver una lista, sino modificar la que
# toma como parámetro.
def intercambiar(s,a,b) :
    aux = s[a]
    s[a] = s[b]
    s[b] = aux
#     return s
# s = [1,2,3,4,5]
# a = 0
# b = 4
# print(intercambiar(s,a,b))