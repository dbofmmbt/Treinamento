#Programa para a resolução do problemas Trilhas:
nTrilhas = int(input())
listaMedidas = []
melhorTrilha, direitaSubida, esquerdaSubida, desnivel, nMedidas = 0,0,0,0,0
menorDesnivel = 1010

#Para cada trilha a ser mostrada:
for i in range(nTrilhas):
	#Armazene a entrada em uma lista e anote o primeiro
	#valor, que é o numero de medições daquela trilha.
	listaMedidas = list(map(int, input().split()))
	nMedidas = listaMedidas[0]
	
	#Para cada uma das medições, calcule o desnivel e
	#realize as atribuições necessárias com base nisso.
	#OBS: se o valor é positivo, quer dizer que há um 
	#desnivel para a direita. Se é negativo, o desnivel
	#desejado encontra-se no sentido contrário, esquerda.
	for j in range(1, nMedidas):
		desnivel = listaMedidas[j+1]-listaMedidas[j]
		#Certamente tem um problema bizarro aqui embaixo
		'''
		if desnivel>0:
			direitaSubida += desnivel
			esquerdaDescida += desnivel
		else:
			esquerdaSubida -= desnivel
			DireitaDescida -= desnivel
		
	if direitaSubida == 0:
		if direitaDescida < menorDesnivel:
			menorDesnivel = direitaDescida
			melhorTrilha = i+1
	elif esquerdaSubida == 0:
		if esquerdaDescida < menorDesnivel:
			menorDesnivel = esquerdaDescida
			melhorTrilha = i+1
	esquerda, direita = 0, 0
		'''

		if desnivel > 0:
			direitaSubida += desnivel
		else:
			esquerdaSubida -= desnivel
	if direitaSubida < menorDesnivel:
		menorDesnivel = direitaSubida
		melhorTrilha = i+1
	if esquerdaSubida < menorDesnivel:
		menorDesnivel = esquerdaSubida
		melhorTrilha = i+1
	direitaSubida = 0
	esquerdaSubida = 0
print(melhorTrilha)
