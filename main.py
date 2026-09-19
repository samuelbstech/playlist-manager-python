playlist = []

while True:
    print("\n=== SISTEMA DE PLAYLIST MUSICAL ===")
    print("1. Adicionar música")
    print("2. Remover música")
    print("3. Listar playlist")
    print("4. Mostrar duração total")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n--- Adicionar Música ---")
        nome = input("Nome da música: ")
        artista = input("Nome do artista: ")
        duracao = float(input("Duração (em minutos, ex: 3.5): "))

        nova_musica = {
            "nome": nome,
            "artista": artista,
            "duracao": duracao
        }
        playlist.append(nova_musica)
        print("Música", nome, "adicionada com sucesso!")

    elif opcao == "2":
        print("\n--- Remover Música ---")
        if len(playlist) == 0:
            print("A playlist está vazia.")
        else:
            nome_remover = input("Digite o nome da música que deseja remover: ")

            encontrada = False
            for musica in playlist:
                if musica["nome"].lower() == nome_remover.lower():
                    playlist.remove(musica)
                    print("Música", musica["nome"], "removida com sucesso!")
                    encontrada = True
                    break

            if not encontrada:
                print("Erro: Música não encontrada na playlist.")

    elif opcao == "3":
        print("\n--- Playlist Atual ---")
        if len(playlist) == 0:
            print("A playlist está vazia.")
        else:
            posicao = 1
            for musica in playlist:
                print(f"{posicao}. {musica['nome']} - {musica['artista']} ({musica['duracao']} min)")
                posicao = posicao + 1

            print("\nTotal de músicas cadastradas:", len(playlist))

    elif opcao == "4":
        print("\n--- Duração Total ---")
        if len(playlist) == 0:
            print("A playlist está vazia. Duração: 0 minutos.")
        else:
            duracao_total = 0
            for musica in playlist:
                duracao_total = duracao_total + musica["duracao"]

            print("A duração total da playlist é de:", duracao_total, "minutos.")

    elif opcao == "5":
        print("\nSaindo do sistema. Obrigado por usar o aplicativo! ")
        break

    else:
        print("Opção inválida! Tente novamente.")
