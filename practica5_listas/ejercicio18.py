# Define a function that takes an integer n and return the first cousins numbers "n"
def is_cousin(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
        
def return_cousins(n):
    cousins=[1]
    for i in range(2,n):
        if is_cousin(i):
            cousins.append(i)
    return cousins 
    

n=int(input("input a number"))
cousin_list=return_cousins(n)
print("the first cousins numbers of:",n," are:",cousin_list) 