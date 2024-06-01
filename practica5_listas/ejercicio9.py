def maximo (lista):
    if not lista:
        return None
    numero_mayor= lista[0]
    for numero in lista:
        if numero>numero_mayor:
            numero_mayor = numero
    return numero_mayor
        

##programa principal
lista=[1,2,3,4]
programa=maximo(lista)
print(f"el número mayor de la lista es:{programa}")
