# Hacer un programa que permita al usuario elegir dos números positivos c y n y luego
# muestre en pantalla los últimos c divisores de n
n = int(input("Ingrese un número positivo: "));
c = int(input("Ingrese la cantidad de divisores a mostrar: "));
divisores_mostrados = 1;

if n > 0 and c > 0 :
    print("Mostrando los últimos",c,"divisores de",n);
    for ciclo in range(n,0,-1) :
        if n % ciclo == 0 and divisores_mostrados <= c :
            print(ciclo,end=" ");
            divisores_mostrados = divisores_mostrados + 1;
else :
    print("El número y el número de divisores deben ser mayores a 0, vuelva a intentar");