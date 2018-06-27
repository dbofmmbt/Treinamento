""" Esse é o arquivo principal do trabalho de Banco de Dados
    em python, cujo tema escolhido foi 'Música'. """

from style import *
from data import *

# Inicialização do programa:
cabecalho()
opcao_menu = menu()

# Loop Principal:
while opcao_menu:  # Se == 0, programa se encerra.
    limparTela()
    try:
        if opcao_menu == 1:  # Criar Playlist:
            estilo.sublinhado("Criando Playlist")
            estilo.negrito("Digite o nome da Playlist: ")
            nome = input().strip()
        elif opcao_menu == 2:  # Salvar Playlist:
            print("\n\tOpção 2 escolhida!\n")

        elif opcao_menu == 3:  # Ler Playlist:
            print("\n\tOpção 3 escolhida!\n")

        elif opcao_menu == 4:  # Apagar Playlist:
            print("\n\tOpção 4 escolhida!\n")

        elif opcao_menu == 5:  # Listar Músicas de Playlist:
            print("\n\tOpção 5 escolhida!\n")

        elif opcao_menu == 6:  # Consultar Música:
            print("\n\tOpção 6 escolhida!\n")

        elif opcao_menu == 7:  # Inserir nova Música:
            print("\n\tOpção 7 escolhida!\n")

        elif opcao_menu == 8:  # Apagar uma Música:
            print("\n\tOpção 8 escolhida!\n")

        elif opcao_menu == 9:  # Listar algumas Músicas:
            print("\n\tOpção 9 escolhida!\n")
    except KeyboardInterrupt:
        break  # Encerra o programa.
    limparTela()
    cabecalho()
    opcao_menu = menu()

# Fim do programa:

print("\n{1}Encerrando o programa...{0}".format(estilo.normal, estilo.bold+estilo.red))
