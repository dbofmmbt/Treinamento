#Programa para a resolução do problema "Caçadores de Mitos":

nTestes = int(input())
listaX = []
listaY = []
contador, resposta, j = 0, 0, 0

'''
for i in range(nTestes):
	x,y = map(int, input().split())
	listaRaios.append(x)
	listaRaios.append(y)
while i < nTestes and (not fimdoprograma):
	while j < nTestes and (not fimdoprograma):
		if listaRaios[i] == listaRaios[j]:
			contador +=1
			if contador == 2:
				while k < nTestes and (not fimdoprograma):
					if listaRaios[i+1] == listaRaios[k]:
						resposta = 1
						fimdoprograma = 1
					k += 2
		j += 2
	contador = 0
	i += 1
print(resposta)'''

for i in range(nTestes):
	x,y = map(int, input().split())
	listaX.append(x)
	listaY.append(y)

for i in range(nTestes):
	for j in range(i,nTestes):
		if listaX[i] == listaX[j]:
			if listaY[i] == listaY[j]:
				contador += 1
				if contador == 2:
					resposta = 1
	contador = 0
print(resposta)