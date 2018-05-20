#Resolução do problema "Costa", por busca em largura, do URI:

#Inicialização e aquisição dos dados da Matriz:
contador = 0
m, n = map(int, input().split())
matriz = [['.']*(n+2) for i in range(m+2)]
for i in range(1, m+1):
    temp = list(map(str, input()))
    for j in range(1, n+1):
        matriz[i][j] = temp[j-1]

#Processamento por Busca em Largura:
for i in range(m+2):
    for j in range(n+2):
        if matriz[i][j] == '#':
            try:
                if matriz[i-1][j] == '.':
                    contador += 1
                    matriz[i][j] = '1'

                elif matriz[i+1][j] == '.':
                    contador += 1
                    matriz[i][j] = '1'

                elif matriz[i][j-1] == '.':
                    contador += 1
                    matriz[i][j] = '1'

                elif matriz[i][j+1] == '.':
                    contador += 1
                    matriz[i][j] = '1'
            except IndexError:
                contador += 1
                matriz[i][j] = '1'

print(contador)
