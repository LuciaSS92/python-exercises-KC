"""
Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. 
Definir los métodos para inicializar sus atributos, imprimirlos(Nombre y Nota) y mostrar un mensaje con el resultado 
de la nota y si ha aprobado o no --> Menos que 5 no aprueba
"""

class Alumno:
    def __init__(self, nombre, nota):
            self.nombre = nombre
            self.nota = nota 

    def Info(self): 
        print('Alumno/a: {} - Nota: {}'.format(self.nombre,self.nota))
        #print(f"{self.nombre} ha sacado un {self.nota}")
        
    def Aprobar(self):
        if self.nota <= 5:
            print("No aprobado")
        else:
            print("Aprobado")


alumno1 = Alumno("Ale", 7)
alumno2 = Alumno("JJ", 3)

alumno1.Info()
alumno1.Aprobar()
alumno2.Info()
alumno2.Aprobar()
