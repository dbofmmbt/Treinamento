''' Resolução do Problema 'Transmissão de Energia', do Uri Online Judge: '''
E, L = map(int, input().split())
nTeste = 1

while E != 0 and L != 0:
    estacao = ['branco'] * (E+1)
    adj = []
    for i in range(E+1):
        adj.append([])
    ligacoes = []
    EstadoNormal = True

    # Recebendo linhas de transmissão:
    for i in range(L):
        linha = list(map(int, input().split()))
        ligacoes.append(linha)

    # Preenchendo adjacencias:
    for i in range(1, E+1):
        for j in range(L):
            if i == ligacoes[j][0]:
                adj[i].append(ligacoes[j][1])
            elif i == ligacoes[j][1]:
                adj[i].append(ligacoes[j][0])

    # Verificar se, a partir de uma estação qualquer,
    #é possível alcançar as outras.
    fila = [1]
    estacao[1] = 'cinza'
    while fila != []:
        for i in adj[fila[0]]:
            if estacao[i] == 'branco':
                estacao[i] = 'cinza'
                fila.append(i)
        estacao[fila[0]] = 'preto'
        fila.pop(0)

        # Se houver algum elemento diferente de preto, quer
        # dizer que não foi possível alcançar aquele elemento.

    for i in range(1, E+1):
        if estacao[i] != 'preto':
            EstadoNormal = False

    # Impressão do Resultado:
    print("Teste", nTeste)
    if EstadoNormal:
        print("normal\n")
    else:
        print("falha\n")
    nTeste = nTeste + 1
    E, L = map(int, input().split())
