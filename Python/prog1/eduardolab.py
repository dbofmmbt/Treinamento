import pickle

def selectionSort(lista):
    listaOrdenada = []
    while lista:
        menor = lista[0]
        indice = 0
        for i in range(len(lista)):
            if menor > lista[i]:
                menor  = lista[i]
                indice = i
        lista.pop(indice)
        listaOrdenada.append(menor)
    return listaOrdenada

# Todos os elementos terão pelo menos dois campos em comum (0, 1): Nome e Categoria.
categorias = ('Linguagem de Programação', 'Ferramenta CASE', 'Técnica Computacional',\
              'Biblioteca', 'Framework', 'Hardware')
qtdCampos = {categorias[0]: 2, categorias[1]: 3, categorias[2]: 4,\
             categorias[3]: 3, categorias[4]: 3, categorias[5]: 3}

# Inicialização do Banco de Dados na memória:
try:
    arqBD = open('BD.txt', 'rb')
    listaBD = []
    i = 0
    x = pickle.load(arqBD)
    while True:
        listaBD.append([])
        listaBD[i].append(x)
        if listaBD[i][0] == categorias[0]:

        elif listaBD[i][0] == categorias[1]:

        elif listaBD[i][0] == categorias[2]:

        elif listaBD[i][0] == categorias[3]:

        elif listaBD[i][0] == categorias[4]:

        elif listaBD[i][0] == categorias[5]:

        elif listaBD[i][0] == categorias[6]:


except EOFError:
    BD.close()
pickle.dump('Ois', open('BD.txt', 'wb'))
pickle.dump('Oid', open('BD.txt', 'ab'))
pickle.dump('Oiw', open('BD.txt', 'ab'))
BD = open('BD.txt', 'rb')
x = pickle.load(BD)
y = pickle.load(BD)
z = pickle.load(BD)
print(x, y, z)



''''# Carregando a lista na memória:
listaBD = []
try:
    while True:
        listaBD.append([])
        i = 0
        x = BancoDeDados.readline()
        while x != '\n':
            listaBD[i].append(x)
            x = BancoDeDados.readline()
        i = i + 1

except EOFError:
    BancoDeDados.close()'''

