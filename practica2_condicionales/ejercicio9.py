# Se tiene la siguiente lista con DNIs de personas.
# 30612453
# 23763290
# 21448503
# 34582048
# 15364857
# Dado otro número de DNI cualquiera, se desea construir un programa que determine si es alguno
# de los existentes en el listado. Escribir el programa en papel y luego pasarlo a Python.
dni = int(input("Ingrese un número de DNI "));
mensaje = "Esta en la lista";
if dni == 30612453 :
    print(dni,mensaje);
else :
    if dni == 23763290 :
        print(dni,mensaje);
    else :
        if dni == 21448503 :
            print(dni,mensaje);
        else :
            if dni == 34582048 :
                print(dni,mensaje);
            else :
                if dni == 15364857 :
                    print(dni,mensaje);
                else :
                    print("No esta en la lista");