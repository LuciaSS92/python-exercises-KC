def nota_numerica(letra):
    """
    Pide un valor por la pantalla y lo devuelve en numerico decimal. Da error si la nota no es correcta
    """
    letras = ['A+', 'A', 'A-', 'B+', 'B', 'B-','C+', 'C', 'C-', 'D+', 'D', 'F']
    notas = [4, 4, 3.7, 3.3, 3, 2.7, 2.3, 2, 1.7, 1.3, 1, 0]
    
    puntero = 0
    letra = letra.upper()
    
    while letras[puntero] != letra:
        puntero += 1
        
    return notas[puntero]

def pedir_nota_correcta():
    """
    Pide una nota en forma de letra y si es incorrecta vuelve a pedirla.
    Devuelve el valor del numero decimal
    """
    valor = ""
    while valor == "":
        #EQUIVALE A nota = input("Nota: ").upper()
        nota = input("Nota: ")
        nota = nota.upper()
        
        try:
            valor = nota_numerica(nota)
        except IndexError:
            print("Nota", nota, "incorrecta. Vuelva a introducir")
            valor = ""
            
    return valor

def pedir_numero():
    """
    Pide un valor por la pantalla. Si no es entero, vuelve a pedirlo.
    Devuelve el numero entero introducido
    """
    valor = ""
    while valor == "":
        try:
            valor = int(input("Número de asignaturas: "))
        except ValueError:
            valor = ""
            print("Debe ser un numero entero. Vuelva a introducirlo")
        
    return valor