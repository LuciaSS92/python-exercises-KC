#Hacer un programa que pida el nombre y te salude por tu nombre
## Mantener entrada, salida y concatenación separados

n = input("¿Como te llamas? ")

output = "Hola, " + n + ".¿Como estas?"

print(output)


#Reto1: sin variables

print("Hola, " + input("¿Como te llamas? ") + ". ¿Como estas?")


#Reto2: diferentes saludos a diferentes personas

n = input("¿Como te llamas? ")

if n == "Mon":
    print("Hola, " + n + ".¿Como estas?")
elif n == "Lu":
    print("Que pasaaaa, coleguita")
elif n == "Isa":
    print("Hola, mi amor. ¿Como estas?")
else:
   print("Holi, " + n + ".¿Como estas?")


#Reto2 TOP
import random
saludos = ("Hola, ", "Buenos días, ", "¿Que pasa?, ", "¿Como estás?, ")

n = input("¿Como te llamas? ")

nSaludos = random.randint(0,3)

print(saludos[nSaludos], n)
