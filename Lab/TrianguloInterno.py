''' Resolução do Problema 'Triângulo Interno', em preparação para a P2 de LAB:'''
S, N, M = map(int, input().split())

while (S+N+M):
    c1, c2, c3 = map(int, input().split())
    H = c1/(N+1)
    B = abs(c3-c2)/(M+1)
    resposta = int( (c1 * abs(c3-c2) * S)/( (N+1)*(M+1) ) )
    print(resposta)
    S, N, M = map(int, input().split())
