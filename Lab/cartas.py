def crescente(carta):
    for i in range(4):
        if carta[i] > carta[i+1]:
            return False
    return True
def decrescente(carta):
    for i in range(4):
        if carta[i] < carta[i+1]:
            return False
    return True

lista = list(map(int, input().split()))

if crescente(lista):
    print("C")
elif decrescente(lista):
    print("D")
else:
    print("N")
