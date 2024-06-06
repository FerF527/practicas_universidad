# Definir una función llamada union que tome dos listas sin repetidos y devuelva una nueva lista
# que contenga los elementos de ambas listas. Ojo, la lista de retorno debe no tener repetidos.
def union (lista1,lista2):
    nueva_lista=[]
    for i in lista1:
        if i not in lista2:
            nueva_lista.append(i)
    for i in lista2:
        if i not in lista1:
            nueva_lista.append(i)
    return nueva_lista
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
print("--------------------------")
programa=union(lista1,lista2)
print("La nueva lista es: ",programa)