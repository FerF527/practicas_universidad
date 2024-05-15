# a) Sabiendo que la pantalla de la consola tiene 80 caracteres de ancho, hacer un programa que, 
# dada una palabra, la escriba en el centro de la pantalla.
palabra = input("Ingrese un texto ")
largo = len(palabra)

#primera línea de espacios
for i in range(0,40 - largo//2) :
    print(end=" ")
print(palabra,end="")
#segunda línea de espacios
for i in range(0,40 - largo//2) :
    print(end=" ")