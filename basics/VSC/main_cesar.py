from cesar import cesar, cifrar, creaEncriptador

print(cesar('A', 1)) # 'B'

print(cesar('C', 3)) # 'F'

print(cesar('Z', 1)) # 'A'

print(cifrar('ZAR', 1)) #ABS

print(cifrar('ABS', -1)) #ZAR

_encrypt = creaEncriptador(5)
_desencrypt = creaEncriptador (-5)

print(_encrypt('HOLA'), cifrar('HOLA', 5))
print(_desencrypt('MTPF'), cifrar('MTPF', -5))
