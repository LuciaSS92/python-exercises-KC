#Quien eres
nombre = input("Cómo te llamas? ")
print("Hola", nombre)

#Toma de datos
edad = input("¿Cuántos años tienes? ")
edad = int(edad)
anyo_actual = input("¿En qué año estamos? ")
anyo_actual = int(anyo_actual)
has_cumplido = input("¿Has cumplido años ya (S/N)? ")

#Calculo del año
if has_cumplido == "S":
    anyo_nacimiento = anyo_actual - edad
else:
    anyo_nacimiento = anyo_actual - edad
    anyo_nacimiento = anyo_nacimiento - 1
    
#Presentación resultado
print(nombre, "naciste en", anyo_nacimiento)