''' Resolução do Problema 'Bolsa de Valores', do URI online judge:'''
import pdb; pdb.set_trace()
def sublistaMaxima(sublista):
    #Inicializa as variaveis usadas:
    maiorNessePonto = maiorDeTodos = sublista[0]
    indice1 = indice2 = 0
    sublistaNova = False
    # Para cada elemento a partir do segundo:
    for i in range(1, len(sublista)):
        # Pega o maior valor entre a posicao atual e a sublista, contando a posicao atual.
        maiorNessePonto = max(sublista[i], maiorNessePonto + sublista[i])
        # Verifica se inclui o proximo elemento ou não.
        if maiorNessePonto > maiorDeTodos:
            indice2 = i
            if sublistaNova:
                indice1 = i
        else:
            sublistaNova = False
        maiorDeTodos = max(maiorDeTodos, maiorNessePonto)
    return maiorDeTodos, indice1, indice2

N, C = map(int, input().split())
cotacoes = list(map(int, input().split()))

sublista = [[0] for i in range(N)]

# Criando a sublista contígua para obtenção da Soma Máxima:
sublista[0] = 0
for i in range(1, N):
    sublista[i] = cotacoes[i] - cotacoes[i-1]
x = []
resposta = 0
while sublista:
    x = (sublistaMaxima(sublista))
    if x[0] > C:
        resposta += x[0] - C
    indice1 = x[1]
    indice2 = x[2]
    for i in range(x[1], x[2]+1):
        sublista.pop(x[1])
print(resposta)
