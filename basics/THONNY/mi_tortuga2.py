import turtle

miTortuga = turtle.Turtle()

strLados = input("¿cuantos lados quieres? ")

lados = int(strLados)

if lados == 3:
    for _ in range(0,lados):
        miTortuga.forward(59)
        miTortuga.left(120)
        
elif lados == 4:
    for _ in range(0,lados):
        miTortuga.forward(59)
        miTortuga.left(90)
        
else:
    print("Solo se dibujar cuadrados y triangulos")