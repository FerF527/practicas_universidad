# Definir una función llamada laMasCorta que tome dos listas y devuelva la que tenga menos
# elementos. Si tienen igual cantidad, deberá devolver la primera.
def laMasCorta(lista1,lista2) :
    cant_elementos_lista1 = len(lista1)
    cant_elementos_lista2 = len(lista2)
    lista_mas_corta = lista1
    if(cant_elementos_lista2 < cant_elementos_lista1) :
        lista_mas_corta = lista2
    return lista_mas_corta