# Hacer un programa que permita al usuario elegir un número positivo n y luego muestre en
# pantalla el producto (es decir, la multiplicación) de los numeros entre 1 y n.
n = int(input("Ingrese un número positivo: "));
producto = 1;
ciclos = 1;
if n > 0 :
    while ciclos <= n :
        producto = producto * ciclos;
        ciclos = ciclos + 1;
    print("El producto es:",producto);
else :
    print("Debe ingresar un número positivo, vuelva a ejecutar el programa por favor.");