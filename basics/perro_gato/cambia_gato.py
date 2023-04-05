perro = open("perro_perra.txt", "r")

lineas = perro.readlines()

nuevas_lineas = []
for linea in lineas:
    nueva_linea = linea.replace("perr", "gat")
    nuevas_lineas.append(nueva_linea)

    # equivalente y MEJORnuevas_lineas.append(linea.replace("perr", "gat"))

gato = open("gato.txt", "w")
gato.writelines(nuevas_lineas)
gato.close()