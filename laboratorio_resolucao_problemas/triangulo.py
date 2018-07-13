# Resolução do problema "Triângulo", do URI:
#import pdb; pdb.set_trace()

def verifica(x, y, z):
    if x + y > z and x + z > y and z + y > x:
        return 'S'
    return 'N'

resposta = 'N'
A, B, C, D = map(int, input().split())

if verifica(A, B, C) == 'S':
    resposta = 'S'
if verifica(A, B, D) == 'S':
    resposta = 'S'
if verifica(A, C, D) == 'S':
    resposta = 'S'
if verifica(B, C, D) == 'S':
    resposta = 'S'
print(resposta)
