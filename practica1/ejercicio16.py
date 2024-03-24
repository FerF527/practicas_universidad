# Escribir un programa en Python que pida al usuario una cantidad de segundos y muestre cuantos
# minutos son, así como también cuantas horas y cuantos días.
segundos_ingresados = int(input("Ingrese los segundos "));
segundos_a_minutos = segundos_ingresados / 60;
segundos_a_horas = segundos_ingresados / 3600;
segundos_a_dias = segundos_ingresados / 86400;
print(segundos_ingresados,"segundos son",segundos_a_minutos,"minutos");
print(segundos_ingresados,"segundos son",segundos_a_horas,"horas");
print(segundos_ingresados,"segundos son",segundos_a_dias,"dias");