# b) Hacer un programa que pida al usuario dos números reales y muestre por pantalla
# el resultado de llamar a la función del primer inciso.
from ejercicio4a import *
num = float(input("Ingrese el primer número "))
num2 = float(input("Ingrese el segundo número "))
num3 = float(input("Ingrese el tercer número "))
resultado = promedio3num(num,num2,num3)
print("El promedio de",num,",",num2,"y",num3,"es",resultado)