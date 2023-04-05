#Pide la entrada del ancho y profundo de la habitación en metros. 
# Devuelve la superficie en metros cuadrados y en yardas cuadradas

metro_yarda = 0.9361

ancho = float(input("Introduzca ancho habitacon en metro: "))
profundo = float(input("Introduzca profundo habitacion en metros: "))

s_metros = ancho * profundo
s_yardas = s_metros / metro_yarda ** 2

print("La superifice en metros cuadrados: ", s_metros, "\nLa superficie en yardas cuadradas: ", s_yardas)