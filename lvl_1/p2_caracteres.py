#Pedir cadena de caracteres y devolver su numero
#Devuelve cadena original, y usa funcion especifica de Python

str = input("Introduzca caracteres ")

print("La cadena ", str, " tiene ", len(str), " caracteres")
    #print("La cadena '{}' tiene {} caracteres".format(str, len(str)))


#Sin funcion especifica de Python

str = input("Introduzca caracteres ")
contador = 0

while str != "":
    str = str[1:]
    contador += 1

print("La cadena ", str, " tiene ", contador, " caracteres")
    #print("La cadena '{}' tiene {} caracteres".format(str, contador))


#!!!!!!!!!!!! NO FUNCIONA !!!!!!!
#Si no se introduce nada, vuelva a preguntar
str = input("Introduzca caracteres ")

def vacio(str):
    while str == "":
        print("Debe introducir texto")
        str = input("Introduzca caracteres ")
    return str

print("La cadena ", str, " tiene ", len(str), " caracteres")


