def fatorial(x, resposta = 1):
    if x != 1:
        resposta = resposta*x
        return fatorial(x-1, resposta)
    return resposta

nTeste = input()
while nTeste != '0':
    tamanho = len(nTeste)
    answer = fatorial(tamanho)
    print(answer)
    try:
        nTeste = input()
    except EOFError:
        nTeste = '0'
