# Escribe un programa que pida los coficientes de una ecuación de primer grado (ax + b = 0)
# y escriba la solución. Recuerda que una ecuación de primer grado puede no tener solución, tener
# una solución única, o que todos los números reales sean solución.
a = float(input("Ingrese el coeficiente 'a': "));
b = float(input("Ingrese el coeficiente 'b': "));

if a != 0:
    x = -b / a
    print("La solución de la ecuación es",x);
   
else:
    if a == 0 and  b != 0:
        print("La ecuación no tiene solución"); 
        
    else:
        print("La ecuación tiene como solucion todos los números reales.");