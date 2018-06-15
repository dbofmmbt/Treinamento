J, R = map(int, input().split())

pontos = [[0] * J for i in range(R)]

entrada = list(map(int, input().split()))

for i in range(R):
    for j in range(J):
        pontos[i][j] += entrada[(J*i)+j]

jogadores = [0 for i in range(J)]

for i in range(J):
    for j in range(R):
        jogadores[i] += pontos[j][i]

vencedor = 0
maiorPontuacao = jogadores[0]
for i in range(J):
    if jogadores[i] >= maiorPontuacao:
        vencedor = i
        maiorPontuacao = jogadores[i]

print(vencedor+1)
