# Hacer una programa que, dada una palabra, la escriba recuadrada por asteriscos. Por ejemplo,
# si la palabra es "Ganaste", el programa debería escribir:
# ***********
# * Ganaste *
# ***********

palabra = input("Ingrese un texto ")
largo = len(palabra)

for i in range(0,largo + 4) :
    print("*",end="")
print("\n* " + palabra + " *")
for i in range(0,largo + 4) :
    print("*",end="")