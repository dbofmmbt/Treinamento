""" Esse é o arquivo principal do trabalho de Banco de Dados
    em python, cujo tema escolhido foi 'Música'. """

from time import sleep
from style import *
from data import *

# Inicialização do programa:
cabecalho()
opcao_menu = menu()
mapa_arquivo = iniciarArquivos()
mapa_playlist = iniciarTabelas(mapa_arquivo)

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

            adicionarPlaylist(mapa_arquivo, mapa_playlist, nome)
            resultado_opcao = estilo.bold+estilo.green\
            +'1 - Playlist adicionada com Sucesso!\n'+estilo.normal

        elif opcao_menu == 2:  # Salvar Playlist:
            estilo.sublinhado('Salvando Playlist')
            estilo.negrito('Escolha a Playlist a ser Salva:\n')

            playlists = []
            for chave in mapa_playlist:
                playlists.append(chave)

            numeracao = listarElementos(playlists)
            numero_playlist = setaInput(int)
            while not (0 <= numero_playlist < numeracao):
                limparTela()
                estilo.sublinhado('Salvando Playlist')
                estilo.negrito('Escolha um Número Válido!\n')
                listarElementos(playlists)
                numero_playlist = setaInput(int)

            nome_playlist = playlists[numero_playlist]
            salvarPlaylist(mapa_arquivo, mapa_playlist, nome_playlist)
            resultado_opcao = estilo.bold+estilo.green\
            +'2 - Playlist Armazenada com Sucesso!\n'+estilo.normal


        elif opcao_menu == 3:  # Ler Playlist:
            print("\n\tOpção 3 escolhida!\n")

        elif opcao_menu == 4:  # Apagar Playlist:
            print("\n\tOpção 4 escolhida!\n")

        elif opcao_menu == 5:  # Listar Músicas de Playlist:
            print("\n\tOpção 5 escolhida!\n")

        elif opcao_menu == 6:  # Consultar Música:
            print("\n\tOpção 6 escolhida!\n")
            estilo.sublinhado('Consultando Música:')
            estilo.negrito('Digite o Nome ou o ID da Música Desejada:\n')
            resposta = setaInput(str)
            if resposta.isnumeric():
                musica = consultarMusica(mapa_playlist, id=resposta)
            else:
                musica = consultarMusica(mapa_playlist, nome=resposta)
            if musica:
                estilo.negrito('Dados da Música solicitada:\n')
                exibirMusica(musica[0], id=True)
                estilo.negrito('Está Contida nas seguintes Playlists:\n')
                for playlist in musica[1:]:
                    print('\t'+playlist, end=';\n')
            else:
                resultado_opcao = 'A música identificada por \"'\
                +estilo.bold+resposta+estilo.normal+\
                '\" não foi encontrada!\n'

        elif opcao_menu == 7:  # Inserir nova Música:
            estilo.sublinhado('Inserindo nova Música')
            confirmado = False
            while not confirmado:
                musica = ['id', 'nome', 'banda,', 'album', 'genero']
                # Recebendo Dados:
                estilo.negrito('Digite o nome da Música:')
                musica[1] = setaInput(str)
                estilo.negrito('\nDigite a banda da Música:')
                musica[2] = setaInput(str)
                estilo.negrito('\nDigite o album da Música:')
                musica[3] = setaInput(str)
                estilo.negrito('\nDigite o gênero da Música:')
                musica[4] = setaInput(str)

                # Confirmação; Dados:
                limparTela()
                estilo.sublinhado('Inserindo nova Música')
                estilo.negrito('\nConfirma os Dados?[S/N]:\n')
                exibirMusica(musica, id=False)
                resposta = setaInput(str)

                # Confirmando a própria confirmação:
                if resposta == 'S' or resposta == 's'\
                or resposta == 'Y' or resposta == 'y' or resposta == '':
                    confirmado = True
                    limparTela()
                elif resposta == 'N' or resposta == 'n':
                    limparTela()
                    estilo.sublinhado('Inserindo nova Música')
                    print('\nPreencha novamente!\n')
                else:
                    limparTela()
                    estilo.sublinhado('Inserindo nova Música')
                    print('\nResposta Inválida, repita o processo!\n')

            adicionarMusica(mapa_playlist, musica)
            resultado_opcao = estilo.bold+estilo.green\
            +'7 - Música Adicionada com Sucesso!\n'+estilo.normal

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
