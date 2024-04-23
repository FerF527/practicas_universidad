# Hacer un programa que solicite dos cadenas, nombre y apellido y arme el legajo de estudiantes
# de la universidad de la siguiente manera:
# Los 3 primeros números del legajo coinciden con los primeros del dni luego "_", luego las 3
# primeras letras del apellido y por ultimo la primera y ultima del nombre.
# Por ejemplo:
# Javier Rodriguez 38946702
# Legajo: 389_rodjr

nombre = input("Ingresar nombre ")
apellido = input("Ingresar apellido ")
dni = input("Ingresar DNI ")
legajo = ""
# Parte 1, 3 primeros dígitos del DNI

# contador DNI
cont_dni = 1

for char in dni :
    if cont_dni < 4 :
        legajo = legajo + char
    cont_dni = cont_dni + 1

# verificación parte 1
print("P1",legajo)

# parte 2, agregar el guion bajo "_"
p2 = "_"
legajo = legajo + p2

# verifico parte 2
print("P2",legajo)

# parte 3, 3 primeras letras del apellido
cont_apellido = 1
for char in apellido :
    if 1<=cont_apellido<=3 :
        legajo = legajo + char
    cont_apellido = cont_apellido + 1

# verifico parte 4
print("P3",legajo)

#parte 4, primera y última letra del nombre
cont_nombre = 1
ultimo_char = len(nombre)
for char in nombre :
    if cont_nombre==1 or cont_nombre==ultimo_char :
        legajo = legajo + char
    cont_nombre = cont_nombre + 1
print("El legajo es:",legajo)