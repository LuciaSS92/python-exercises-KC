def sumatorioR(n):
    if n <= 0:
        return 0
    else:
        return n + sumatorioR(n - 1)
    
print(sumatorioR(10))
