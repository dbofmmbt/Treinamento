''' Resolução do Problema 'Triângulo Interno', em preparação para a P2 de LAB:'''
import math
import random
S, N, M = map(int, input().split())
import pdb; pdb.set_trace()

while (S and N and M != 0):
    c1, c2, c3 = map(int, input().split())
    H = c1/N
    B = math.fabs(c3-c2)/M
    resposta = S * H * B
    print(resposta)
    S, N, M = map(int, input().split())

# TODO: A solução acima não funciona e não tenho mais ideias no momento.
