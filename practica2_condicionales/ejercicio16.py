# Un año es bisiesto si es múltiplo de 4. Pero no siempre, las excepciones son los años múltiplos
# de 100 que no son múltiplos de 400 (1900 no es bisiesto pero 2000, sí). Escribir en papel un
# programa que diga si un año ingresado por el usuario es bisiesto, realizar varias pruebas de
# escritorio, luego pasarlo a Python y verificar los resutlados.
anio = int(input("Ingrese el año "));
bisiesto = False;
if anio % 4 == 0 :
    bisiesto = True;

if anio % 100 == 0 :
    if anio % 400 == 0 :
        bisiesto = True
    else :
        bisiesto = False;
if bisiesto :
    print(anio,"es bisiesto");
else :
    print(anio,"no es bisiesto");    