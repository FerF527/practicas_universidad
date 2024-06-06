def interseccion (lista1, lista2):
    lista_nueva=[]
    for i in lista1:
        if i in lista2:
            lista_nueva.append(i)
    return lista_nueva
lista1=[]
cantidad=int(input("Ingresar cuantos elementos quiere ingresar"))
intentos=1
while intentos<=cantidad:
    elementos=int(input("Ingresar los numeros que desea a la lista"))
    lista1.append(elementos)
    intentos+=1
print(lista1)
print("--------------------------")
lista2=[]
cantidad=int(input("Ingresar cuantos elementos quiere ingresar"))
intentos=1
while intentos<=cantidad:
    elementos=int(input("Ingresar los numeros que desea a la lista"))
    lista2.append(elementos)
    intentos+=1
print(lista2)

programa=interseccion(lista1,lista2)
print("la nueva lista es: ",programa)