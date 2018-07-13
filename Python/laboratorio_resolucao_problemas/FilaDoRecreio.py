# Resolução do Problema "Fila do Recreio", do URI online Judge:

nTestes = int(input())

for i in range(nTestes):
    trocados = 0
    nAlunos = int(input())
    fila = list(map(int, input().split()))
    baguncada = fila.copy()
    fila.sort(reverse=1) # Se for necessário implementar, usaria Selection Sort.
    for j in range(nAlunos):
        if fila[j] != baguncada[j]:
            trocados += 1
    print(nAlunos - trocados)
