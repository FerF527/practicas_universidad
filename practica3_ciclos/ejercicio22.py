# Hacer un programa que simule el juego de la quiniela. El usuario debe elegir un número del
# 0 al 99 y un monto a apostar, si acierta el número gana 70 veces lo apostado. (El número de la
# suerte debe ser elegido al azar)
import random

azar = random.randrange(1,100)
print(azar)
num = int(input("Ingresar un número del 0 al 99 "))
monto = float(input("Ingrese el monto a apostar "))
if num >= 0 and num <= 99 and monto > 0 :
    if(num == azar) :
        monto = monto * 70
        print("Ganaste un total de",monto,"pesos")
    else :
        print("Lo siento, no acertaste el número. Intenta de nuevo")    
else :
    print("El número debe estar entre 0 y 99 incluidos y el monto debe ser mayor a 0 pesos.")