""" Arquivo auxiliar para manipulação de arquivos e listas. """

import os
def iniciarArquivos():
    """ Obtém os arquivos e armazena-os num mapa. """
    tabelas = open("Dados/tabelas.csv", 'r+')
    lista = []
    mapa_arquivo = {}
    for linha in tabelas:
        lista.append(linha.strip())

    mapa_arquivo = {}
    for arquivo in lista:
        caminho = 'Dados/'+arquivo+'.csv'
        if os.path.exists(caminho):
            mapa_arquivo[arquivo] = open(caminho, 'r+')
        else:
            mapa_arquivo[arquivo] = open(caminho, 'w')

    return mapa_arquivo

def iniciarTabelas(mapa_arquivo):
    """ Inicializa as tabelas do Mapa fornecido. """
    mapa_tabela = {}
    for tabela in mapa_arquivo:
        mapa_tabela[tabela] = []
        for registro in mapa_arquivo[tabela]:
            registro = registro.split('\t')
            mapa_tabela[tabela].append(registro)
    return mapa_tabela

def calcularIndice(mapa_tabela, playlist='All'):
    """ Calcula o Índice P/ novo elemento. Função Auxiliar."""
    maiorIndice = 0
    for elemento in mapa_tabela['All']:
        indice_atual = int(elemento[0])
        if indice_atual > maiorIndice:
            maiorIndice = indice_atual
    return maiorIndice+1



def adicionarPlaylist(mapa_arquivo, mapa_tabela, nome_playlist):
    """ Adiciona uma nova playlist nos mapas arquivo e tabela. """
    # Primeiro em arquivo:
    aux = open('Dados/'+nome_playlist+'.csv', 'w')
    mapa_arquivo[nome_playlist] = aux

    # Em tabela:
    mapa_tabela[nome_playlist] = []
    return

def salvarPlaylist(mapa_arquivo, mapa_tabela, playlist):

    arquivo = mapa_arquivo[playlist]
    for registro in mapa_tabela[playlist]:
        registro = '\t'.join(registro)
        arquivo.write(registro+'\n')
    return

def adicionarMusica(mapa_tabela, musica,\
primeira_vez = True, nome_playlist='All'):
    """ Escreve os Dados de uma lista 'Música' em uma Playlist do Mapa.
    padrão de 'Música': id, nome, banda, album, genero. """
    musica[0] = str(musica[0])
    if primeira_vez and nome_playlist != 'All':
        mapa_tabela['All'].append(musica)
    mapa_tabela[nome_playlist].append(musica)
    return

def excluirMusica(mapa_tabela, musica, lista_playlists):
    """ Exclui a Música das playlists listadas. """
    nome = musica[1]
    
    try:
        for playlist in lista_playlists:
            indice = -1
            i = 0
            while(indice == -1):
                if nome in mapa_tabela[playlist][i]:
                    indice = i
                else:
                    i += 1
            del mapa_tabela[playlist][indice]
            
    except:
        return False
    return True

def consultarMusica(mapa_tabela, nome='', id=''):
    """ Retorna uma lista em que '0' é a música e o restante são
    as playlists que contêm tal música. Falso se não há música. """
    try:
        indice = -1
        i = 0
        if nome:
            while(indice == -1):
                if nome in mapa_tabela['All'][i]:
                    indice = i
                else:
                    i += 1
        else:
            while(indice == -1):
                if id in mapa_tabela['All'][i]:
                    indice = i
                else:
                    i += 1
        musica = [] # '0' é a música, resto é playlist.
        musica.append(mapa_tabela['All'][indice])
        indice = str(indice+1)

        for playlist in mapa_tabela:
            for registro in mapa_tabela[playlist]:
                if indice in registro:
                    musica.append(playlist)
    except:
        return False
    return musica

def ChavesEmLista(mapa):
    """ Recebe um mapa e retorna uma lista com as chaves. """
    lista = []
    for chave in mapa:
        lista.append(chave)
    return lista

def excluirPlaylist(mapa_arquivo, mapa_tabela, nome_playlist):
    """ Remove o arquivo e a tabela de uma Playlist. """
    mapa_arquivo.pop(nome_playlist)
    mapa_tabela.pop(nome_playlist)
    return

def salvarTabelas(mapa_tabela, mapa_arquivo):
    """ Registra os dados do Mapa nos arquivos respectivos. """
    pass

# Código de teste:
mapa = iniciarArquivos()
print(mapa)
mapa['oi'].write("olá")
mapa['oi'].seek(0, 0)
print(mapa['oi'].read())
