from ejercicio2 import mostrarEnUnaLinea
BANDERA = True
lista_enteros = []
while BANDERA :
    numero = input("Ingrese un número entero ")
    lista_enteros.append(numero)
    seguir = input("Si desea seguir ingresando valores, presione 's'; de lo contrario, presione 'n'. s/n ")
    if seguir == "n" :
        BANDERA = False
numeros_a_mostrar = mostrarEnUnaLinea(lista_enteros)
print(numeros_a_mostrar)