#Incorpora el año actual al programa. 
# Crea un programa que cuente cuantos años faltan para tu jubilación 
# y que te diga el año en que te jubilarás. 

import datetime

now = datetime.datetime.now()
year = now.year


age = int(input("¿Cuantos años tienes? "))
end = int(input("¿A qué edad te jubilarás? "))


left = end - age
when = year + left

print("Te quedan ", left, " años para jubilarte")
print("Estamos en ", year , " te jubilarás en ", when)

#print("Te quedan {} años para jubilarte".format(faltan))
#print("Estamos en {}, te jubilarás en {}".format(año, cuando))

