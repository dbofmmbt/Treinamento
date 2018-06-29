""" Esse é o arquivo principal do trabalho de Banco de Dados
    em python, cujo tema escolhido foi 'Música'. """

from time import sleep
from style import *
from data import *

# Inicialização do programa:
cabecalho()
opcao_menu = menu()
mapa_arquivo = iniciarArquivos()

# Loop Principal:
while opcao_menu:  # Se == 0, programa se encerra.
    limparTela()
    resultado_opcao = 0
    try:
        if opcao_menu == 1:  # Criar Playlist:
            estilo.sublinhado("Criando Playlist")
            estilo.negrito("Digite o nome da Playlist: ")
            nome = setaInput(str)

            # Testando se já existe tal playlist:
            while nome in mapa_arquivo:
                limparTela()
                estilo.sublinhado("Criando Playlist")
                estilo.negrito('Nome já utilizado! Digite outro: ')
                nome = setaInput(str)

            #adicionarTabela(mapa_arquivo, nome)
            resultado_opcao = "{1}1 - Playlist adicionada com Sucesso!{0}\n"\
            .format(estilo.normal, estilo.green+estilo.bold)

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
    if resultado_opcao:  # Se há algo != 0, imprima.
        print(resultado_opcao)
        sleep(1.5)
    opcao_menu = menu()

# Fim do programa:
frase_final = "\n{1}Encerrando o programa... ;){0}"\
.format(estilo.normal, estilo.bold+estilo.red)

for letra in frase_final:
    print(letra, flush=True, end='')
    sleep(0.03)
print()
