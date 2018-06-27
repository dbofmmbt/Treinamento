""" Arquivo auxiliar para manipulação de arquivos e listas. """

def iniciarTabelas():
    """ Obtém as tabelas e armazena-as num mapa. """
    tabelas = open("Dados/tabelas.csv", 'r')
    lista = []
    mapa_tabelas = {}
    for linha in tabelas:
        lista.append(linha.strip())

    mapa_tabelas = dict([tabela, open("Dados/"+tabela+'.csv', 'r+')]\
    for tabela in lista)

    return mapa_tabelas

def adicionarTabela(mapa, nome_tabela):
    """ Adiciona uma nova tabela ao Mapa. """
    aux = open('Dados/'+nome_tabela+'.csv', 'r+')
    mapa[nome_tabela] = aux
    return

# Código de teste:
mapa = iniciarTabelas()
print(mapa)
mapa['oi'].write("olá")
mapa['oi'].seek(0, 0)
print(mapa['oi'].read())
