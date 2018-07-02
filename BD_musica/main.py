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
            resultado_opcao = '1 - Playlist adicionada com Sucesso!\n'

        elif opcao_menu == 2:  # Salvar Playlist:
            estilo.sublinhado('Salvando Playlist')
            estilo.negrito('Escolha a Playlist a ser Salva:\n')

            playlists = ChavesEmLista(mapa_playlist)

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
            resultado_opcao = '2 - Playlist Armazenada com Sucesso!\n'

        elif opcao_menu == 3:  # Ler Playlist:
            estilo.sublinhado('Lendo Playlists')

            mapa_auxiliar = iniciarArquivos()
            lista_auxiliar = ChavesEmLista(mapa_auxiliar)
            lista_playlists = ChavesEmLista(mapa_playlist)
            lista_exibir = []
            for playlist in lista_auxiliar:
                if playlist not in lista_playlists:
                    mapa_playlist[playlist] = mapa_auxiliar[playlist]
                lista_exibir.append(playlist)

            estilo.negrito('As seguintes Playlists foram encontradas:\n')
            listarElementos(lista_exibir, ordem=False)
            print('\nPressione Enter para continuar.\n')
            setaInput(str)
            resultado_opcao = '3 - Playlists Lidas com Sucesso!\n'

        elif opcao_menu == 4:  # Apagar Playlist:
            print("\n\tOpção 4 escolhida!\n")

        elif opcao_menu == 5:  # Listar Músicas de Playlist:
            estilo.sublinhado('Listando Músicas de Playlist')
            estilo.negrito('Selecione a Playlist Desejada:\n')
            lista_playlists = ChavesEmLista(mapa_playlist)
            listarElementos(lista_playlists)
            playlist_escolhida = setaInput(int)
            playlist_escolhida = lista_playlists[playlist_escolhida]
            playlist_escolhida = mapa_playlist[playlist_escolhida].copy()
            limparTela()
            estilo.sublinhado('Listando Músicas de Playlist')
            estilo.negrito('Músicas da Playlist Selecionada:\n')
            for i in range(len(playlist_escolhida)):
                playlist_escolhida[i] = '; '.join(playlist_escolhida[i])
            print(estilo.bold+estilo.blue\
            +'Colunas: ID; NOME; BANDA; ALBUM; GENERO\n'+estilo.normal)
            listarElementos(playlist_escolhida, ordem=False)
            print('\nPressione {1}Enter{0} para retornar ao Menu.\n'\
            .format(estilo.normal, estilo.italic))
            setaInput(str)

        elif opcao_menu == 6:  # Consultar Música:
            estilo.sublinhado('Consultando Música:')
            estilo.negrito('Digite o Nome ou o ID da Música Desejada:\n')
            resposta = setaInput(str)
            if resposta.isnumeric():
                musica = consultarMusica(mapa_playlist, id=resposta)
            else:
                musica = consultarMusica(mapa_playlist, nome=resposta)
            if musica:
                estilo.negrito('\nDados da Música solicitada:\n')
                exibirMusica(musica[0], id=True)

                estilo.negrito('Está Contida nas seguintes Playlists:\n')
                i = 1
                listarElementos(musica[1:], 1)
                print()
                del i
                estilo.negrito('Escolha uma Opção:\n')
                print('N - Remove a Música da Playlist de número N;\n')
                print('0 - Adiciona esta Música a alguma Playlist;\n')
                print('-1 - Remove a Música do Banco de Dados.\n')
                print('Qualquer valor não Númerico para voltar ao Menu.\n')
                opcao_escolhida = setaInput(str)
                if opcao_escolhida.isnumeric():
                    opcao_escolhida = int(opcao_escolhida)

                lista_playlists = ChavesEmLista(mapa_playlist)
                if opcao_escolhida == 0:
                    limparTela()
                    estilo.sublinhado('Consultando Música:')
                    estilo.negrito('Escolha a Playlist:\n')
                    listarElementos(lista_playlists)
                    print()
                    numero_playlist = setaInput(int)
                    playlist = lista_playlists[numero_playlist]
                    adicionarMusica(mapa_playlist, musica[0], False, playlist)
                    resultado_opcao = '6 - Música Adicionada à Playlist \
com Sucesso!\n'
                elif opcao_escolhida == -1:
                    excluirMusica(mapa_playlist, musica[0], musica[1:])
                    resultado_opcao = '6 - Música Removida do BD com Sucesso!\n'
                elif opcao_escolhida.isnumeric():
                    playlist_removida = [lista_playlists[opcao_escolhida-1]]
                    excluirMusica(mapa_playlist, musica[0], playlist_removida)
                    resultado_opcao = '6 - Música Removida de Playlist \
com Sucesso!\n'
                else:
                    pass
            else:
                resultado_opcao = '{0}{3}A música identificada por {2}"{1}"{0} \
{3}não foi encontrada!{0}\n'.format(estilo.normal, resposta, estilo.bold, estilo.red)

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
            
            musica[0] = calcularIndice(mapa_playlist)
            adicionarMusica(mapa_playlist, musica)
            resultado_opcao = '7 - Música Adicionada com Sucesso!\n'

        elif opcao_menu == 8:  # Listar algumas Músicas:
            print("\n\tOpção 8 escolhida!\n")

    except KeyboardInterrupt:
        break  # Encerra o programa.
    limparTela()
    cabecalho()
    if resultado_opcao:  # Se há algo != 0, imprima.
        resultado_opcao = logAtividade(resultado_opcao)  # Aplicando Style.
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
