# Un ciudadano argentino está exento de votar en estos casos:
# Tiene más de 70 años
# Tiene entre 18 y 70 años pero se encuentra a más de 500 km del centro de votación.
# Suponiendo que las variables edad y distancia representan la edad y la distancia del ciudadano, escribir la expresión lógica que representa esta situación.

edad = int(input("Ingrese la edad "));
distancia = int(input("Ingrese la distancia "));

if edad < 18 or edad > 70 or distancia > 500 :
    print("esta exento de votar");
else :
    print("debe votar");