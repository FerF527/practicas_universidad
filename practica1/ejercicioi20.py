# Escribir en Python un programa que pida al usuario que ingrese tres valores y los guarde en tres
# variables, x, y, y z. El programa deberá intercambiar circularmente los valores de x, y y z, es decir, x
# debe tomar el valor de y, y el de z y z el de x. Y luego mostrarlos en pantalla:
x = input("Ingrese el valor de x ");
y = input("Ingrese el valor de y ");
z = input("Ingrese el valor de z ");
print("x es",x,"y es",y,"z es",z);
aux = y;
y = z;
z = x;
x = aux;
print("El valor de x es:",x);
print("El valor de y es:",y);
print("El valor de z es:",z);