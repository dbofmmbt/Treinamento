def calcular(x, resposta = 0):
    if x > 0:
        resposta += 2**(x-1)
        return calcular(x-1, resposta)
    return resposta
n = int(input())
for i in range(n):
    num = int(input())
    print(calcular(num))
