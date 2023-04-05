#Crear un programa que pida nombre, verbo, adverbio y adjetivo y con ellos construya una historia. 
#Utilizar una plantilla con los huecos donde colocar el nombre, el verbo, el adverbio y el adjetivo. 

n = input("Introduzca un nombre: ")
v = input("Introduzca un verbo: ")
adv = input("Introduzca un adverbio: ")
adj = input("Introduzca un adjetivo: ")

print("Mi ", n , " puede ", v , adv , " como si estuviera ", adj , " los domingos por la mañana")


#SOLUCION

plantilla = "Mi 0 1 debe 2 3"

n = input("Introduzca un nombre: ")
v = input("Introduzca un verbo: ")
adv = input("Introduzca un adverbio: ")
adj = input("Introduzca un adjetivo: ")

x = 0
frase = ""

while x < len(plantilla):
    cosa = plantilla[x]

    if cosa == "0":
        frase = frase + n
    elif cosa == "1":
        frase = frase + adj
    elif cosa == "2":
        frase = frase + v
    elif cosa == "3":
        frase = frase + adv
    else:
        frase = frase + cosa

    x = x + 1

print(frase)
