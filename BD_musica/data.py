""" Arquivo auxiliar para manipulação de arquivos e listas. """

def iniciarTabelas():
    tabelas = open("Dados/tabelas.txt", 'r')
    lista = []
    for linha in tabelas:
        lista.append(linha.strip())

    return lista
