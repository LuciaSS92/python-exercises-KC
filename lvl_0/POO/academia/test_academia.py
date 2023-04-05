from academia import Alumno, Asignatura, Profesor

roberto = Alumno('Roberto', 'Rodriguez')
susana = Alumno('Susana', 'Martin')

print(roberto.nombre, roberto.apellidos, roberto)  # Roberto Rodriguez
print(susana.nombre, susana.apellidos, susana)  # Susana Martin

print(roberto.correo_e, roberto.movil)

ingles = Asignatura("Ingles", 'A2')
ingles.precio_h = 7.5
aleman = Asignatura("Aleman", 'A2')
aleman.precio_h = 8
chino = Asignatura("Chino", 'A1')
chino.precio_h = 10

print(ingles)  # Asignatura: Ingles - A2 - (7.50/mes)

roberto.alta_asignatura(ingles)
roberto.alta_asignatura(chino)

# Asignatura: Ingles - A2 (30.00 €/mes), Asignatura: Chino - A1 (40.00 €/mes)
print(roberto.asignaturas)
print(susana.asignaturas)


donJose = Profesor("Jose", "martin Fusta", 'OW', "j@gmail.com")
print(donJose)

print(donJose.sueldo())  # 200

donJose.alta_asignatura(ingles)

print(donJose.asignaturas)
print(donJose.sueldo())
