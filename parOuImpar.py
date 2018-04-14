nome1 = "qualquer nome"
nome2 = "qualquer nome"
mao1 = 2
mao2 = 2
contador = 1

nTestes = int(input())
while(nTestes != 0):
	nome1 = input()
	nome2 = input()
	print("Teste", contador)
	for i in range(nTestes):
		mao1, mao2 = input().split()
		mao1, mao2 = int(mao1), int(mao2)
		if((mao1+mao2)%2==0):
			print(nome1)
		else:
			print(nome2)
	print()
	contador += 1
	nTestes = int(input())
