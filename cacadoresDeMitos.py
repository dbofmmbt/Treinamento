#Programa para a resolução do problema "Caçadores de Mitos":
resposta = 0
matriz = [[False] * 510 for i in range(510)]
total = int(input())
for i in range(total):
	x, y = map(int, input().split())
	if matriz[x][y]:
		resposta = 1
		break
	else:
		matriz[x][y] = True
print(resposta)
