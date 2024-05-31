def sonFactores(numero,lista_enteros) :
    for num in lista_enteros :
        if numero % num != 0 :
            return False
    return True