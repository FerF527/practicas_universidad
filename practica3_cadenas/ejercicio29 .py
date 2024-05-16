# Escribir un programa que pida al usuario una cadena e indique si esta posee un diptongo (dos
# vocales unidas).
palabra = input("Ingrese un texto ")
letras_diptongo = 0
diptongo = False
for carac in palabra :
    if carac == "a" or carac == "e" or carac == "i" or carac == "o" or carac == "u" :
        letras_diptongo += 1
    else :
        letras_diptongo = 0
    if letras_diptongo == 2 :
        diptongo = True
if(diptongo) :
    print("La palabra",palabra,"posee un diptongo")
else :
    print("La palabra",palabra,"no posee un diptongo")