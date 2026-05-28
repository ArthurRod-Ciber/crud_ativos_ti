from enums import TipoAtivo, Severidade,  Status
from funcoes import exibir_menu, ler_opcao, ler_textos, exibir_tipos, exibir_ativo

opcao = 0

while opcao != 6:
    exibir_menu()

    opcao = ler_opcao("O que deseja realizar? ", 1, 6)

    if opcao == 1:
        id = ler_opcao("Digite o ID do ativo: ", 1, 9999)
        nome = ler_textos("Digite o nome do ativo: ")
        responsavel = ler_textos("Digite o nome do responsavel pelo ativo: ")
        setor = ler_textos("Qual o setor ou localização do ativo: ")

        exibir_tipos()
        
        tipo_opcao = ler_opcao("Digite o tipo de ativo: ", 1, 8,)
        tipo = TipoAtivo(tipo_opcao)

        with open("ativos.txt", "a") as arquivo:
            arquivo.write(f"{id} | {nome} | {responsavel} | {setor} | {tipo.name}\n")

    elif opcao == 2:
        metodo = ler_opcao("\nComo deseja buscar?\n [1] ID\n [2] NOME\n", 1, 2)
        if metodo == 1:
            id_busca = ler_opcao("Digite o ID do ativo que pretende buscar: ", 1, 9999)
            encontrado = False

            with open("ativos.txt", "r") as arquivo:
                for linha in arquivo:
                    campos = linha.strip().split("|")
                    if int(campos[0].strip()) == id_busca:
                        encontrado = True
                        print("ID encontrado!")
                        exibir_ativo(campos)
            if not encontrado:
                print("\nAtivo não encontrado")

        elif metodo == 2:
            nome_busca = ler_textos("Qual o nome do ativo que você procura?")
            encontrado2 = False

            with open("ativos.txt", "r") as arquivo:
                for linha in arquivo:
                    campos = linha.strip().split("|")
                    if campos[1].strip() == nome_busca:
                        encontrado2 = True
                        print("Nome encontrado!")
                        exibir_ativo(campos)
            if not encontrado2:
                print("\nAtivo nao encontrado")
    
    elif opcao == 3:
        
