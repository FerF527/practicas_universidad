# Definir una funcion que tome una lista y devuelva True si tiene al menos un elemento repetido,
# y False en caso contrario
def chequeoRepetido(lista):
    newlist=[]
    for elemento in lista:
        if elemento not in newlist:
            newlist.append(elemento)
        else:
            return True
    return False