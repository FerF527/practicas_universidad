# b) Ídem anterior pero deberá frenarse cuando el lado izquierdo pase a ser más grande
# que el derecho.

m = int(input("Ingresar un número "))
n = int(input("Ingresar un número mayor al anterior "))
if m < n :
    while m <= n+1 :
        print(m,n);
        m+=1
        n-=1
else :
    print("El primer número debe ser menor al segundo")