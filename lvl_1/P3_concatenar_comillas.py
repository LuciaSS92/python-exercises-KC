#Construir un programa que pida una cita y un autor 
# y devuelva una única cadena con la cita entre comillas y el autor.

cita = input("Introduzca una cita: ")
autor = input ("Introduzca nombre del autor: ")

output = '\'' + cita + '\', ' + autor

print(output)