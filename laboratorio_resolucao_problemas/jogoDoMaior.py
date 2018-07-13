# Resolução do problema 'Jogo do Maior', do URI:

n = int(input())
while n != 0:
    jogadas = []
    A, B = 0, 0
    for i in range(n):
        x, y = map(int, input().split())
        jogadas.append(x)
        jogadas.append(y)
    for i in range(0, len(jogadas), 2):
        if jogadas[i] > jogadas[i+1]:
            A += 1
        elif jogadas[i] < jogadas[i+1]:
            B += 1
    print(A, B)
    n = int(input())