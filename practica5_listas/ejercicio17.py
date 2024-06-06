# Definir una función llamada mcd que tome dos enteros positivos y devuelva el máximo común
# divisor usando funciones de los ejercicios anteriores.

def mcd (a,b):
    while b!=0:
        residuo=a%b
        a=b
        b=residuo
    return a
a=int(input("ingrese un número"))
b=int(input("ingrese un segundo número"))

print("el máximo común divisor es:",mcd(a,b))