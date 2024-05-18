# b) Hacer una función que reciba tres enteros y retorne el mayor.
def mayor(num,num2,num3) :
    if num > num2 and num > num3 :
        return num
    if num2 > num and num2 > num3 :
        return num2
    return num3

# prueba
# print(mayor(2,1,3))