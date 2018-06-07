''' Resolução do problema "Tarzan", proposto pelo professor Rodrigo Monteiro\
    através do Uri Online Judge, para a aula de laboratório:'''

#   Definição de funções:
def distancia(A, B):
    'Esta função recebe dois pares ordenados e retorna a distancia entre eles.'
    dist  = ((A[0] - B[0])**2 + (A[1] - B[1])**2)**(1/2)
    return dist

#   Inicialização:
n, alcance = map(int, input().split())
arvores = [[None, None] for i in range(n)]
arvores_alcancadas = [False for i in range(n)]
resposta = 'S' # Na dúvida, olhe a "Verificação dos resultados".

#   Recebimento dos Dados:
for i in range(n):
    x, y = map(int, input().split())
    arvores[i][0] = x
    arvores[i][1] = y

#   A busca a ser implementada será em profundidade, utilizando-se de uma pilha.
primeiro = 0
pilha = [primeiro]
arvores_alcancadas[primeiro] = True

#   Implementação da busca:
while pilha != []:
    atual = pilha.pop()
    for i in range (n):
        if distancia(arvores[atual], arvores[i]) <= alcance and not arvores_alcancadas[i]:
            pilha.append(i)
            arvores_alcancadas[i] = True

#   Verificação dos resultados:
for i in arvores_alcancadas:
    if not i:
        resposta = 'N'

#   Exibição da resultado:
print(resposta)

#   Fim do Programa.
