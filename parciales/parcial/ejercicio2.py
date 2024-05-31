def paresEnLaInterseccion(lista1, lista2):
    interseccion = []

    for i in lista1:
        if i in lista2:
            interseccion.append(i)
   ## print(interseccion)
    contador = 0
    for i in interseccion:
        if i % 2 == 0:
            contador += 1
    return contador
lista1 = [24, 125, 32, 10, 56, 100, 90, 17]
lista2 = [199, 254, 17, 24, 32, 5, 12, 56, 145]
resultado = paresEnLaInterseccion(lista1, lista2)
print(resultado)  