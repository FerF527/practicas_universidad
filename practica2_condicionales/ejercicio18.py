# Una función cuadrática se escribe como ax2+bx+c. La misma puede tener una, dos o ninguna
# raíz. Escribir un programa que pida al usuario los datos de la misma, es decir, a, b y c, y muestre
# todas sus raíces, o el mensaje "No tiene raíces" cuando corresponda. Recordar que las raíces están
# dadas por la fórmula (−b ± √b**2 − 4ac) / 2a

print("Ingrese los coeficientes de la función cuadrática:")
a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

# Calculamos el discriminante
discriminante = b**2 - 4*a*c

# Verificamos el número de raíces
if discriminante > 0:
    # Dos raíces reales distintas
    raiz1 = (-b + discriminante ** 0.5) / (2*a)
    raiz2 = (-b - discriminante ** 0.5) / (2*a)
    print("La función cuadrática tiene dos raíces reales distintas:")
    print("Raíz 1:", raiz1)
    print("Raíz 2:", raiz2)
elif discriminante == 0:
    # Una raíz real doble
    raiz = -b / (2*a)
    print("La función cuadrática tiene una raíz real doble:")
    print("Raíz:", raiz)
else:
    # No tiene raíces reales
    print("La función cuadrática no tiene raíces reales.")