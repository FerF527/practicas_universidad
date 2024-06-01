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
        

<<<<<<< HEAD
##programa principal
lista=[1,2,3,4]
programa=maximo(lista)
print(f"el número mayor de la lista es:{programa}")
=======
>>>>>>> d08914ed9b5f444255a8215c52a220483696b591

