# Escribir un programa en Python que pida al usuario una cantidad de segundos y muestre en pantalla
# la cantidad de días, minutos y segundos que representa. Por ejemplo, si el usuario ingresa 86461 segundos
# el programa debe mostrar por pantalla: 1 día 0 horas 1 minuto 1 segundo.

segundos = int(input("Ingrese los segundos "));
aux = segundos;
dias = segundos // 86400;
segundos = segundos % 86400;
horas = segundos // 3600;
segundos = segundos % 3600;
minutos = segundos // 60;
segundos = segundos % 60;

print(aux,"segundos son:",dias,"días",horas,"horas",minutos,"minutos",segundos,"segundos");