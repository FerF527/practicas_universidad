# Una empresa telefónica desea un programa para calcular el importe de sus clientes. Sabiendo que el
# costo por comunicación es de $12 y por cada segundo se cobra $1, 5 hacer dicho programa. Se deben
# ingresar la cantidad de llamadas realizadas y el tiempo total de comunicación, el programa debe devolver
# el precio a cobrar. Por ejemplo, si realizó 10 llamadas con un total de 4000 segundos el importe a pagar
# sería de $6120


costo_comunicacion = 12;
costo_segundo = 1.5;
cantidad_llamadas = int(input("Ingrese la cantidad de llamadas realizadas "));
tiempo_llamadas = int(input("Ingrese la duración total de las llamadas "));
importe_cliente = (costo_comunicacion * cantidad_llamadas) + (costo_segundo * tiempo_llamadas);
print("El importe a pagar es $",importe_cliente);
