# Definir una función que tome un entero n y devuelva los primeros n primos.
def es_primo(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
        
def devolverprimos(n):
    primos=[1]
    for i in range(2,n):
        if es_primo(i):
            primos.append(i)
    return primos 
    

n=int(input("ingrese un numero"))
programa=devolverprimos(n)
print("los primero numeros primos de:",n," son:",programa)