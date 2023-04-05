from funciones import *

dialogo = [
    ('Hola', gritando),
    ('Por favor, no chilles, me duele la cabeza', None),
    ('Perdona, quieres una aspirina?', voz_baja)
]

for frase, modo in dialogo:
    if modo == None:
        print(frase)
    else:
        print(modo(frase))