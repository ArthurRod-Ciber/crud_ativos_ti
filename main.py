from enums import TipoAtivo, Severidade,  Status
from funcoes import exibir_menu, ler_opcao, carregar_ativos, cadastrar, deletar, atualizar_ativo, buscar, gerenciar_vulnerabilidades

opcao = 0
ativos = carregar_ativos()

while opcao != 6:
    exibir_menu()
    opcao = ler_opcao("O que deseja realizar? ", 1, 6)

    if opcao == 1:
        cadastrar(ativos) #função para realizar o cadastro de um ativo, nela é gerado um id usando uma função que garante que o numero de identificação do ativo seja unico e exatamente o proximo numero na sequencia
    elif opcao == 2:
        buscar(ativos) #realiza a busca de ativos
    elif opcao == 3:
        atualizar_ativo(ativos) #abre a opção de atualizar cada um dos campos do ativo, já atualizando diretamente no .json
    elif opcao == 4:
        deletar(ativos) #funcao para fazer a remoção de um ativo diretamente no arquivo.json
    elif opcao == 5:
        gerenciar_vulnerabilidades(ativos) #funcao que abre o submenu para gerenciar vulnerabilidades e todas as funcoes sobre as vulnerabilidades, como cadastrar, listar etc
        


