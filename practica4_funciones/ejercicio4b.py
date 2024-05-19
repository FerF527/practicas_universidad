# b) Hacer un programa que pida al usuario dos números reales y muestre por pantalla
# el resultado de llamar a la función del primer inciso.
from ejercicio4a import *
num = float(input("Ingrese el primer número "))
num2 = float(input("Ingrese el segundo número "))
resultado = promedio(num,num2)
print("El promedio de",num,"y",num2,"es",resultado)