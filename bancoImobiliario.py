valorInicial, nOperacoes = map(int, input().split())

money = {'D': valorInicial, 'E': valorInicial, 'F': valorInicial}
transacao = []

for i in range(nOperacoes):
	transacao = input().split()
	if len(transacao) == 3:
		transacao[2] = int(transacao[2])
	else:
		transacao[3] = int(transacao[3])
	
	if transacao[0] == 'C':
		money[transacao[1]] -= transacao[2]
	elif transacao[0] == 'V':
		money[transacao[1]] += transacao[2]
	else:
		money[transacao[1]] += transacao[3]
		money[transacao[2]] -= transacao[3]
print(money['D'], money['E'], money['F'])
