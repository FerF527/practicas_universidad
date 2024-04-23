# Hacer un programa que reciba un número m y determine el primer n para el cual la suma
# 1+2+...+n > m. Por ejemplo, si el usuario ingresa 11 se deberá retornar 5 ya que 1+2+3+4 =
# 10 < 11 y 1 + 2 + 3 + 4 + 5 = 15 > 11

m = int(input("Ingrese un número: "));
suma = 0;
n = 1;

while suma <= m :
    suma = suma + n;
    if suma <= m :
        n = n + 1;
print(n);