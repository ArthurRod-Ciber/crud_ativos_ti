from enums import TipoAtivo, Severidade,  Status

opcao = 0

while opcao != 6:
    print("\n=== MENU ===" \
    "\n[1] cadastrar ativo" \
    "\n[2] buscar ativo" \
    "\n[3] atualizar ativo" \
    "\n[4] deletar ativo" \
    "\n[5] gerenciar vulnerabilidades" \
    "\n[6] sair\n")

    try:
        opcao = int(input("O que deseja realizar? "))
    except ValueError:
        print("\nResposta invalida, tente novamente!\n")
        input("Pressione Enter para continuar")

    if opcao == 1:
        id = int(input("Digite o ID do ativo: "))
        nome = input("Digite o nome do ativo: ")
        responsavel = input("Digite o nome do responsavel pelo ativo: ")
        setor = input("Qual o setor ou localização do ativo: ")
            

            