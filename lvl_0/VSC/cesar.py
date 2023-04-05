ALFABETO = list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ')

def cesar(caracter, clave):
    posicion = ALFABETO.index(caracter)
    nposicion = posicion + clave
    nposicion = nposicion % len(ALFABETO)
    return ALFABETO[nposicion]

def cifrar(mensaje, clave):
    resultado = ''
    for caracter in mensaje:
        nuevo_caracter = cesar(caracter, clave)
        resultado += nuevo_caracter
        #equivalente a lo anterior: resultado = resultado + nuevo_caracter
    return resultado


def creaEncriptador(clave):
    def encriptar(mensaje):
        res = ''
        for caracter in mensaje:
            nuevo_caracter = cesar(caracter, clave)
            res += nuevo_caracter
        return res

    return encriptar




