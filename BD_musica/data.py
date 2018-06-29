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

def adicionarMusica(mapa_tabela, musica, nome_playlist='All'):
    """ Escreve os Dados de uma lista 'Música' em uma Playlist do Mapa.
    padrão de 'Música': id, nome, banda, album, genero. """
    id = len(mapa_tabela['All'])
    musica[0] = str(id)
    if nome_playlist != 'All':
        mapa_tabela['All'].append(musica)
    mapa_tabela[nome_playlist].append(musica)
    return

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
            while(not indice):
                if id in mapa_tabela['All'][i]:
                    indice = i
                else:
                    i += 1

        musica = [] # '0' é a música, resto é playlist.
        musica.append(mapa_tabela['All'][indice])

        for playlist in mapa_tabela:
            if indice in playlist:
                musica.append(playlist)
    except:
        return False
    return musica


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
