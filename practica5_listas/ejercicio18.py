# Define a function que tome un integer n y return los primeros n primos.
def is_cousin(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
        
def return_cousins(n):
    primos=[1]
    for i in range(2,n):
        if is_cousin(i):
            primos.append(i)
    return primos 
    

n=int(input("input a number"))
program=return_cousins(n)
print("los primeros numbers primos de:",n," son:",program)