def dondeAparece (lista,blanco):
    for i in range (len(lista)):
        if lista [i] == blanco:
            return i
    return -1

lista=[10,20,30,40,50,60,70,80]
entero=int(input("ingrese un entero"))
indice=dondeAparece(lista,entero)
print(indice)