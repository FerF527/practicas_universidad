# Un vendedor recibe un sueldo base de $42000 más un 10 % extra del total de sus ventas, el vendedor
# desea saber cuánto dinero obtendrá en total en el mes si ha logrado realizar 3 ventas este mes. Tenga en
# cuenta el sueldo básico y la comisión por las ventas. Hacer un programa que solicite el monto de cada una
# de las ventas del mes e indique cuál será el sueldo final del vendedor. Por ejemplo, si realizó una venta
# de $12000, otra de $6000 y una tercera de $22000 su sueldo será de $46000

sueldo_base = 42000;
venta1 = float(input("Ingresenel el valor de la primera venta "));
venta2 = float(input("Ingresenel el valor de la segunda venta "));
venta3 = float(input("Ingresenel el valor de la tercera venta "));
total_ventas = venta1 + venta2 + venta3;
plus = (10 * total_ventas) / 100;
sueldo_a_cobrar = sueldo_base + plus;
print("El sueldo a cobrar es de $",sueldo_a_cobrar);