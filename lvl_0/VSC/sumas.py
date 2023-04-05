def sumaTodos(n):
    resultado = 0
    for i in range(n + 1):
        resultado += i
    return resultado

def sumaTodosAlCuadrado(n):
    resultado = 0
    for i in range(n + 1):
        resultado += (i ** 2)
    return resultado

def sumatorio(n, funcion=None):
    resultado = 0
    for i in range(n + 1):
        if funcion == None:
            nuevo_i = i
        else:
            nuevo_i = funcion(i)
        resultado +=nuevo_i
    return resultado

