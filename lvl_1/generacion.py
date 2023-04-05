anyo = int(input("Introduzca año de nacimiento "))

#Calculo de la generacion
if (anyo >= 1920 and anyo <= 1940):
    print("Pertenece Generacion Silenciosa")
elif (anyo >= 1946 and anyo <= 1964):
    print("Pertenece Baby Boomer")
elif (anyo >= 1965 and anyo <= 1979):
    print("Pertenece Generacion X")
elif (anyo >= 1980 and anyo <= 2000):
    print("Pertenece Generacion Y")
elif (anyo >= 2001 and anyo <= 2010):
    print("Pertenece Generacion Z")
else:
    print("La generacion no tiene nombre")