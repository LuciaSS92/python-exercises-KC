import turtle

miTortuga = turtle.Turtle()

respuesta = input("Quieres un triángulo? ")

if respuesta == "S" or respuesta == "s":
    for _ in range(0,3):
        miTortuga.forward(59)
        miTortuga.left(120)
else:
    for _ in range(0,4):
        miTortuga.forward(59)
        miTortuga.left(90)
    
    

    