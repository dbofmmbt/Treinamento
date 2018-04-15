#Programa para a resolução do problema "Caçadores de Mitos":

nTestes = int(input())
listaX = [-1]
listaY = [-1]
fimdoprograma, contador, resposta, j = 0, 0, 0, 0

for j in range(nTestes):
	x,y = map(int, input().split())
	for i in range(len(listaX)):
		if listaX[i] == x and listaY[i] == y:
					resposta = 1
	listaX.append(x)
	listaY.append(y)

print(resposta)