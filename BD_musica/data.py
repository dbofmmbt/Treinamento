""" Arquivo auxiliar para manipulação de arquivos e listas. """

def iniciarArquivos():
    """ Obtém os arquivos e armazena-os num mapa. """
    tabelas = open("Dados/tabelas.csv", 'r')
    lista = []
    mapa_arquivo = {}
    for linha in tabelas:
        lista.append(linha.strip())

    mapa_arquivo = dict([tabela, open("Dados/"+arquivo+'.csv', 'r+')]\
    for arquivo in lista)

    return mapa_arquivo

def adicionarPlaylist(mapa_arquivo, mapa_tabela, nome_playlist):
    """ Adiciona uma nova playlist nos mapas arquivo e tabela. """
    # Primeiro em arquivo:
    aux = open('Dados/'+nome_playlist+'.csv', 'r+')
    mapa_arquivo[nome_playlist] = aux

    # Em tabela:
    mapa_tabela[nome_playlist] = []
    return

def adicionarMusica(mapa_tabela, nome_playlist='All', musica):
    """ Escreve os Dados de uma lista 'Música' em uma Playlist do Mapa.
    padrão de 'Música': nome, banda, album, genero. """
    musica = [nome, banda, album, genero]
    posicao = 0
    for i in mapa_tabela[nome_playlist]:
        elemento_atual = i.split('\t')
        if nome > elemento_atual[1]:
            posicao += 1
            continue
        else:
            elemento_atual[0] += 1

    musica = '\t'.join(musica)
    mapa_tabela[nome_playlist].append(musica)
    return

def excluirPlaylist(mapa_arquivo, mapa_tabela, nome_playlist):
    """ Remove o arquivo e a tabela de uma Playlist. """
    mapa_arquivo.pop(nome_playlist)
    mapa_tabela.pop(nome_playlist)
    return

def obterMusica(mapa_tabela, numero_musica):



def salvarTabelas(mapa_tabela, mapa_arquivo):
    """ Registra os dados do Mapa nos arquivos respectivos. """

# Código de teste:
mapa = iniciarArquivos()
print(mapa)
mapa['oi'].write("olá")
mapa['oi'].seek(0, 0)
print(mapa['oi'].read())
