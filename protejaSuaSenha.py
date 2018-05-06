# Funções e declarações:

def resposta(teste, resposta):
    print("Teste", teste)
    for i in range(5):
        print(resposta[i], end=" ")
    print(resposta[5],"\n")

def descobreNumero(dig):
    
    for i in dig:
        Achou =  True
        for j in range(0, len(dig), 2):
            if i != dig[j] and i != dig[j+1]:
                Achou = False
        if Achou:
            return i
        
def listarDigito(dig, numero):
    if senha[numero] == 'A':
        dig.append(A[0])
        dig.append(A[1])
    elif senha[numero] == 'B':
        dig.append(B[0])
        dig.append(B[1])
    elif senha[numero] == 'C':
        dig.append(C[0])
        dig.append(C[1])
    elif senha[numero] == 'D':
        dig.append(D[0])
        dig.append(D[1])
    else:
        dig.append(E[0])
        dig.append(E[1])

lista = []

resultado = []
nTeste = 1
# Início do programa "Proteja sua Senha!":
nLinhas = int(input())
while nLinhas != 0:
    dig1, dig2, dig3, dig4, dig5, dig6 = [], [], [], [], [], []   
    for i in range(nLinhas):
        A = B = C = D = E = []    
        senha = []
        lista = input().split()
        numeros = lista[0:10]
        A = lista[0:2]
        B = lista[2:4]
        C = lista[4:6]
        D = lista[6:8]
        E = lista[8:10]
        for j in range(10, 16):
            senha.append(lista[j])

        listarDigito(dig1, 0)
        listarDigito(dig2, 1)
        listarDigito(dig3, 2)
        listarDigito(dig4, 3)
        listarDigito(dig5, 4)
        listarDigito(dig6, 5)

    resultado.append(descobreNumero(dig1))
    resultado.append(descobreNumero(dig2))
    resultado.append(descobreNumero(dig3))
    resultado.append(descobreNumero(dig4))
    resultado.append(descobreNumero(dig5))
    resultado.append(descobreNumero(dig6))
    
    resposta(nTeste, resultado)
    resultado = []
    nTeste += 1
    nLinhas = int(input())
