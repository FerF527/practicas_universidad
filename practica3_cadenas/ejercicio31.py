# Hacer un programa que genere una clave provisoria para la gestión online de clientes de una
# empresa. El programa le pedirá el apellido y generará una clave de 5 caracteres, tomará las
# primeras 4 consonantes de la palabra ingresada. Cuando las consonantes no alcancen a 4, las
# faltantes las reemplazará por "*". Ejemplos:
# clemente CLMN
# rivera RVR*
# oreo R***
# La clave se completará con 1 dígito generado aleatoriamente entre 0 y 9.
# Ejemplos: CLMN1 RVR*4 R***7
import random
apellido = input("Ingrese el apellido ")
clave = ""
cont_consonantes = 0
# primer parte encontrar las consonantes
for carac in apellido :
    if carac != "a" and carac != "e" and carac != "i" and carac != "o" and carac != "u" and cont_consonantes < 4:
        clave += carac
        cont_consonantes += 1
# completo con asteriscos la clave en caso de no tener 4 letras
for i in range (1,5-cont_consonantes):
    clave += "*"

#segunda parte
num_random = str(random.randrange(0,10))
clave += num_random

print("Su clave es",clave)