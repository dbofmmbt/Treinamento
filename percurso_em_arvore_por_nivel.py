''' Resolução do problema de Árvore Binária em Vetor, do Uri Online Judge: '''

# Entrada e inicialização de valores:
N_TESTES = int(input())
# Processamento do Problema:
for i in range(N_TESTES):
    # Para cada caso de Teste a ser Efetuado:
    QTD_NODES = int(input())
    ARVORE = [None] * (QTD_NODES*QTD_NODES)
    ELEMENTOS = list(map(int, input().split()))
    ARVORE[1] = ELEMENTOS[0]

    for j in ELEMENTOS:
        POS_CERTA = False
        K = 1
        while not POS_CERTA:
            try:
                if j == ARVORE[K]:
                    POS_CERTA = True
                elif j < ARVORE[K]:
                    K = 2*K
                else:
                    K = 2*K + 1
            except TypeError:
                ARVORE[K] = j
                POS_CERTA = True

    print("Case:", i+1)
    print(ARVORE[1], end='')
    for j in range(2, len(ARVORE)):
        if ARVORE[j] is not None:
            print(' ', ARVORE[j], sep='', end='')
    
    print()
    print()
