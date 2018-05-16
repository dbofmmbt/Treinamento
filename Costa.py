#Resolução do problema "Costa", por busca em largura, do URI:

#Inicialização e aquisição dos dados da Matriz:
contador = 0
m, n = map(int, input().split())
matriz = [[0]*n for i in range(m)]
for i in range(m):
    temp = list(map(str, input()))
    for j in range(n):
        matriz[i][j] = temp[j]

#Processamento por Busca em Largura:
for i in range(m):
    for j in range(n):
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
                
                elif matriz[i][j] == '.':
                    contador += 1
                    matriz[i][j] = '1'
            except IndexError:
                contador += 1
                matriz[i][j] = '1'

print(contador)
