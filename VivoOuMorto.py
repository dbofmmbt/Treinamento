# Resolução do problema "Vivo ou Morto", proposto no URI:
import pdb; pdb.set_trace()
nTeste = 1
qtdPessoas, qtdRodadas = map(int, input().split())
while(qtdPessoas != 0 and qtdRodadas != 0):
    jogadores = [0]
    jogadores += [1] * qtdPessoas
    ID = [0]
    ID += list(map(int,input().split()))
    print(ID)
    for i in range(qtdRodadas):
        rodada = list(map(int, input().split()))
        j = 2
        print(jogadores)
        if rodada[1] == 0:
            while j < rodada[0]+2:
                if rodada[j] != 0:
                    jogadores[ID[j-3]] = 0
                    ID.pop(j-3)
                else:
                    j += 1
        else:
            while j < rodada[0]+2:
                if rodada[j] != 1:
                    jogadores[ID[j-3]] = 0
                    ID.pop(j-3)
                else:
                    j += 1
    for i in range(qtdPessoas):
        if jogadores[ID[i]] == 1:
            vencedor = ID[i]

    # Resultado
    print("Teste", nTeste)
    print(vencedor)
    print()
    nTeste += 1
    qtdPessoas, qtdRodadas = map(int, input().split())
