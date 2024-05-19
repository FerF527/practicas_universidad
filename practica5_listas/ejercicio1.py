# Hacer un programa que guarde la siguiente lista en una variable: ["elefante", "jirafa",
# "mono"], luego pida el nombre de otro animal, lo agregue a la lista e imprima en pantalla el
# cuarto animal de la lista.
def agregarAnimal(animal) :
    animales = ["elefante", "jirafa", "mono"]
    animales.append(animal)
    return animales[len(animales)-1]