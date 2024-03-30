# La empresa que administra los cajeros automáticos lo contrata para que programen la entrega de
# billetes, el usuario ingresa la cantidad de dinero que desea y usted debe indicar cuantos billetes de cada
# denominación se debe entregar. Es importante entregar siempre la menor cantidad de billetes. Ayuda:
# El operador % da el resto de la división a/b, y el operador // da la parte entera del cociente de a/b.

dinero = int(input("Ingrese el monto a retirar "));
aux = dinero;
billetes_de_1000 = dinero // 1000;
dinero = dinero % 1000;
billetes_de_500 = dinero // 500;
dinero = dinero % 500;
billetes_de_200 = dinero // 200;
dinero = dinero % 200;
billetes_de_100 = dinero // 100;

print("Para retirar $",aux,"se entregaran",billetes_de_1000,"billetes de 1000",billetes_de_500,"de 500",billetes_de_200,"de 200 y",billetes_de_100,"de 100");