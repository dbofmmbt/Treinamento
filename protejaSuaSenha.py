# Funções e declarações:
def resposta(teste, resposta):
    print("Teste", teste)
    for i in range(5):
        print(resposta[i], end=" ")
    print(resposta[5], "\n", sep="")
'''
def verificarSenha(listaLetra, posicao1, posicao2, letra):

    for i in range(len(listaLetra)):
        if lista[posicao1] == A[i]:
            if i % 2 == 0:
                if lista[i + 1] != lista[posicao2]:
                    mapaDigitoLetra[letra] = lista[posicao1]
            else:
                if lista[i - 1] != lista[posicao2]:
                    mapaDigitoLetra[letra] = lista[posicao1]

        elif lista[posicao2] == A[i]:
            if i % 2 == 0:
                if lista[i + 1] != lista[posicao1]:
                    mapaDigitoLetra[letra] = lista[posicao2]
            else:
                if lista[i - 1] != lista[posicao1]:
                    mapaDigitoLetra[letra] = lista[posicao2]
'''
def calcularDigito(digito):
    listaNumeros = []
    for i in range((len(senha)//6)):
        letra = senha[6 % digito * (i+1)]
        if letra == 'A':
            listaNumeros.append(A[(i * 2):(i * 2 + 1)])
        elif letra == 'B':
            listaNumeros.append(B[(i * 2):(i * 2 + 1)])
        elif letra == 'C':
            listaNumeros.append(C[(i * 2):(i * 2 + 1)])
        elif letra == 'D':
            listaNumeros.append(D[(i * 2):(i * 2 + 1)])
        else:
            listaNumeros.append(E[(i * 2):(i * 2 + 1)])


def descobreNumero(listaLetra, pos1, pos2):
    for i in range(len(listaLetra)):
        if lista[pos1] == listaLetra[i]:
            if i % 2 == 0:
                if lista[i + 1] != lista[pos2]:
                    mapaDigitoLetra['A'] = lista[0]
            else:
                if lista[i - 1] != lista[pos2]:
                    mapaDigitoLetra['A'] = lista[0]

        elif lista[pos2] == A[i]:
            if i % 2 == 0:
                if lista[i + 1] != lista[pos1]:
                    mapaDigitoLetra['A'] = lista[1]
            else:
                if lista[i - 1] != lista[pos1]:
                    mapaDigitoLetra['A'] = lista[1]


lista = []
senha = []
mapaDigitoLetra = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
A, B, C, D, E = [], [], [], [], []

# Início do programa "Proteja sua Senha!":
nLinhas = int(input())
while nLinhas != 0:
    for i in range(nLinhas):
        lista = input().split()

        A.append(lista[0:2])
        B.append(lista[2:4])
        C.append(lista[4:6])
        D.append(lista[6:8])
        E.append(lista[8:10])
        senha.append(lista[10:16])
    nLinhas = int(input())