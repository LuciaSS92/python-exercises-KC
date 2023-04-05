import turtle

miTortuga = turtle.Turtle()

strLados = input("¿cuantos lados quieres? ")

lados = int(strLados)

for _ in range(0,lados):
    miTortuga.forward(59)
    miTortuga.left(360/lados)
