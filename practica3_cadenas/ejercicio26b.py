# b) Hacer una programa que, dada una palabra, la escriba pegada a la derecha de la
# pantalla.

palabra = input("Ingrese un texto ")
largo = len(palabra)

#espacios iniciales 
for i in range(0,80 - largo) :
    print(end=" ")
print(palabra)