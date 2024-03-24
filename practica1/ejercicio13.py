# Suponga que una persona desea invertir su capital en un banco y quiere saber cuánto dinero tendrá en
# su cuenta si el banco incrementa el 6 % mensual(no acumulativo). Se le debe pedir al usuario el capital
# a invertir y la cantidad de meses. Por ejemplo, si invierte 500 mil pesos por 4 meses el banco debería
# devolverle 620 mil pesos.

capital = float(input("Ingrese el capital "));
cant_meses = int(input("Ingrese la cantidad de meses "));
porcentaje = 6;
interes = porcentaje * cant_meses * capital / 100;
total = interes + capital;
print("Ud. recibira $",total);