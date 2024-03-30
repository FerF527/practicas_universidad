segundos = int(input("Ingrese los segundos "));
aux = segundos;
dias = segundos // 86400;
segundos = segundos % 86400;
horas = segundos // 3600;
segundos = segundos % 3600;
minutos = segundos // 60;
segundos = segundos % 60;

print(aux,"segundos son:",dias,"días",horas,"horas",minutos,"minutos",segundos,"segundos");