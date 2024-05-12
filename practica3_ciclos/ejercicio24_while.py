# ¿Para qué números enteros distintos de cero es cierto que A + B + C = A x B x C ? (lo
# curioso es que sólo hay una solución)
BANDERA = True
contador = 1
A = 1
B = 2
C = 3

while BANDERA == True and contador <= 100 :
    if A + B + C == A * B * C :
        BANDERA = False
        print("A =",A,"B =",B,"y C =",C,"son soluciones")
    contador += 1
    A += 1
    B += 1
    C += 1