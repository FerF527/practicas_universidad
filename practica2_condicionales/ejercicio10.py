# Hacer en pseudocodigo y luego un programa que calcule el importe que se le facturará a un
# cliente por consumo de electricidad sabiendo que la compañía que se la provee cobra una tarifa
# fija de 480 pesos que incluye los primeros 200 KW consumidos y los KW excedentes se los cobra
# a 25,5 pesos el KW, además se agregan $78 de impuestos. Se leen los valores del medidor al
# comienzo y al fin del período.
tarifa_fija = 480;
impuestos = 78;
kw_iniciales = int(input("Ingrese los KW del inicio del período "));
kw_finales = int(input("Ingrese los KW del final del período "));
importe_total = tarifa_fija + impuestos;
kw_medidos = kw_finales - kw_iniciales;

if kw_medidos > 200 :
    kw_extra = kw_medidos - 200;
    importe_extra = kw_extra * 25.5;
    importe_total = importe_total + importe_extra;

print("El importe a pagar es de $",importe_total);