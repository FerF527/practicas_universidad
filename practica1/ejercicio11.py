# Escribir un programa en Python que pida al usuario que ingrese un valor y luego imprima en la
# pantalla:
# ******************************
# * El resultado es: <valor>
# ******************************
# donde en vez de <valor> debe mostrarse el valor que el usuario ingresó por teclado.

valor_ingresado = input("Ingrese un valor: ");
print("******************************");
print("* El resultado es: " + valor_ingresado);
print("******************************");

# con un solo print
print("******************************\n* El resultado es: "+ valor_ingresado + "\n******************************");