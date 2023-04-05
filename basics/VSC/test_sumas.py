from sumas import sumaTodos, sumaTodosAlCuadrado, sumatorio

print(sumaTodos(100), sumatorio(100)) # 5050 5050

def cuadrado(x):
    return x ** 2

print(sumaTodosAlCuadrado(3), sumatorio(3, cuadrado), sumatorio(3, lambda x: x*x)) # 14 14 14

print(sumatorio(15, lambda x: 2 * x + 1)) #256