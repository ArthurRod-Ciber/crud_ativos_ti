#funcoes para organizar melhor o codigo

from enums import TipoAtivo, Severidade, Status
import json

ARQUIVO = "ativos.json"

# ==================== FUNÇÕES DE UTILIDADE ====================

#funcao para ler opcoes numericas
def ler_opcao(mensagem, minimo, maximo):
    while True:
        try:
            opcao = int(input(mensagem))
            if minimo <= opcao <= maximo:
                return opcao
            else:
                print(f"\nTente novamente! Digite um numero entre {minimo} e {maximo}")
        except ValueError:
            print("\nResposta invalida, tente novamente!\n")
            input("Pressione Enter para continuar")

#funcao para ler estritamente textos
def ler_textos(mensagem):
    while True:
        valor = input(mensagem)
        if valor.strip() != "":
            return valor
        print("\nCampo não pode ser vazio, tente novamente!\n")


# ==================== FUNÇÕES DE EXIBIÇÃO ====================

#funcao para exibir o menu principal
def exibir_menu():
    opcoes = [
        "Cadastrar ativo",
        "Buscar ativo",
        "Atualizar ativo",
        "Deletar ativo",
        "Gerenciar vulnerabilidades",
        "Sair\n"
    ]
    for i, opcao in enumerate(opcoes, start=1):
        print(f"[{i}] {opcao}")

#funcao para exibir o menu de atualizacao
def exibir_menu_atualizacao():
    opcoes = [
        "Nome",
        "Responsavel",
        "Setor",
        "Tipo",
        "Cancelar",
    ]
    print()
    for i, opcao in enumerate(opcoes, start=1):
        print(f"[{i}] {opcao}")

#funcao para exibir o menu de vulnerabilidades
def exibir_menu_vulnerabilidades():
    print("\n--- GERENCIAR VULNERABILIDADES ---")
    opcoes = [
        "Cadastrar Vulnerabilidade",
        "Listar Vulnerabilidades",
        "Voltar"
    ]
    for i, opcao in enumerate(opcoes, start=1):
        print(f"[{i}] {opcao}")

#funcao para exibir os tipos de ativos
def exibir_tipos():
    for tipo in TipoAtivo:
        print(f"[{tipo.value}] {tipo.name.replace('_', ' ')}")

#funcao para exibir as severidades
def exibir_severidades():
    for severidade in Severidade:
        print(f"[{severidade.value}] {severidade.name.replace('_', ' ')}")

#funcao para exibir os status
def exibir_status():
    for status in Status:
        print(f"[{status.value}] {status.name.replace('_', ' ')}")

#funcao para exibir os dados de um ativo
def exibir_ativo(ativo):
    print(f"\nID: {ativo['id']}")
    print(f"Nome: {ativo['nome']}")
    print(f"Responsavel: {ativo['responsavel']}")
    print(f"Setor: {ativo['setor']}")
    print(f"Tipo: {ativo['tipo'].replace('_', ' ')}")
    print()


# ==================== FUNÇÕES DE ARQUIVO ====================

#funcao para carregar os ativos do json
def carregar_ativos():
    try:
        with open(ARQUIVO, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

#funcao para salvar os ativos no json
def salvar_ativos(ativos):
    with open(ARQUIVO, "w") as arquivo:
        json.dump(ativos, arquivo, indent=4)


# ==================== FUNÇÕES DE ATIVOS ====================

#funcao para gerar um id automaticamente
def gerar_id(ativos):
    if len(ativos) == 0:
        return 1
    return max(ativo["id"] for ativo in ativos) + 1

#funcao para cadastrar um ativo
def cadastrar(ativos):
    print("\n--- CADASTRAR ATIVO ---")
    id = gerar_id(ativos)
    nome = ler_textos("Digite o nome do ativo: ")
    responsavel = ler_textos("Digite o responsavel pelo ativo: ")
    setor = ler_textos("Qual setor do ativo? ")
    exibir_tipos()
    tipo_opcao = ler_opcao("Digite o tipo de ativo: ", 1, 8)
    tipo = TipoAtivo(tipo_opcao)

    ativo = {
        "id": id,
        "nome": nome,
        "responsavel": responsavel,
        "setor": setor,
        "tipo": tipo.name,
        "vulnerabilidades": []
    }
    ativos.append(ativo)
    salvar_ativos(ativos)
    print(f"\nAtivo cadastrado com sucesso! ID gerado: {id}")

#funcao para listar todos os ativos
def listar_ativos(ativos):
    print("\n--- LISTA DE ATIVOS ---")
    if len(ativos) == 0:
        print("Nenhum ativo encontrado.")
        return
    for ativo in ativos:
        exibir_ativo(ativo)

#funcao para buscar ativos
def buscar(ativos):
    print("\n--- BUSCAR ATIVO ---")
    metodo = ler_opcao("\nComo deseja buscar?\n[1] ID\n[2] NOME\n", 1, 2)

    if metodo == 1:
        id_busca = ler_opcao("Digite o ID do ativo: ", 1, 9999)
        for ativo in ativos:
            if ativo["id"] == id_busca:
                exibir_ativo(ativo)
                return
        print("\nAtivo não encontrado.")

    elif metodo == 2:
        nome_busca = ler_textos("Digite o nome do ativo: ")
        encontrado = False
        for ativo in ativos:
            if ativo["nome"].lower() == nome_busca.lower():
                exibir_ativo(ativo)
                encontrado = True
        if not encontrado:
            print("\nAtivo não encontrado.")

#funcao para atualizar um ativo
def atualizar_ativo(ativos):
    print("\n--- ATUALIZAR ATIVO ---")
    id_att = ler_opcao("Digite o ID do ativo que você deseja atualizar: ", 1, 9999)

    for ativo in ativos:
        if ativo["id"] == id_att:
            exibir_ativo(ativo)
            break
    else:
        print("\nID não encontrado.")
        return

    exibir_menu_atualizacao()
    opcao = ler_opcao("Digite o que deseja atualizar: ", 1, 5)

    if opcao == 1:
        ativo["nome"] = ler_textos("Digite o novo nome: ")
    elif opcao == 2:
        ativo["responsavel"] = ler_textos("Digite o novo responsavel: ")
    elif opcao == 3:
        ativo["setor"] = ler_textos("Qual o novo setor do ativo? ")
    elif opcao == 4:
        exibir_tipos()
        tipo_opcao = ler_opcao("Digite o novo tipo: ", 1, 8)
        ativo["tipo"] = TipoAtivo(tipo_opcao).name
    elif opcao == 5:
        print("\nOperação cancelada.")
        return

    salvar_ativos(ativos)
    print("\nAtivo atualizado com sucesso!")

#funcao para deletar um ativo
def deletar(ativos):
    print("\n--- DELETAR ATIVO ---")
    id_deletar = ler_opcao("Digite o ID do ativo que deseja deletar: ", 1, 9999)

    for ativo in ativos:
        if ativo["id"] == id_deletar:
            exibir_ativo(ativo)
            confirmacao = ler_opcao("Tem certeza?\n[1] SIM\n[2] NAO\n", 1, 2)
            if confirmacao == 1:
                ativos.remove(ativo)
                salvar_ativos(ativos)
                print("\nAtivo deletado com sucesso!")
            else:
                print("\nOperação cancelada.")
            return
    print("\nAtivo não encontrado.")


# ==================== FUNÇÕES DE VULNERABILIDADES ====================

#funcao para cadastrar uma vulnerabilidade
def cadastrar_vulnerabilidade(ativos):
    print("\n--- CADASTRAR VULNERABILIDADE ---")
    id_ativo = ler_opcao("Digite o ID do ativo que deseja cadastrar a vulnerabilidade: ", 1, 9999)

    for ativo in ativos:
        if ativo["id"] == id_ativo:
            descricao = ler_textos("Digite a descrição da vulnerabilidade: ")
            categoria = ler_textos("Digite a categoria da vulnerabilidade: ")
            exibir_severidades()
            severidade_opcao = ler_opcao("Digite a severidade: ", 1, 4)
            severidade = Severidade(severidade_opcao)
            exibir_status()
            status_opcao = ler_opcao("Digite o status: ", 1, 4)
            status = Status(status_opcao)

            vulnerabilidade = {
                "descricao": descricao,
                "categoria": categoria,
                "severidade": severidade.name,
                "status": status.name,
            }
            ativo["vulnerabilidades"].append(vulnerabilidade)
            salvar_ativos(ativos)
            print("\nVulnerabilidade cadastrada com sucesso!")
            return
    print("\nAtivo não encontrado.")

#funcao para listar vulnerabilidades de um ativo
def listar_vulnerabilidades(ativos):
    print("\n--- VULNERABILIDADES ---")
    id_ativo = ler_opcao("Digite o ID do ativo: ", 1, 9999)

    for ativo in ativos:
        if ativo["id"] == id_ativo:
            if len(ativo["vulnerabilidades"]) == 0:
                print("\nEste ativo não possui vulnerabilidades registradas.")
                return
            for vulnerabilidade in ativo["vulnerabilidades"]:
                print(f"\nDescrição: {vulnerabilidade['descricao']}")
                print(f"Categoria: {vulnerabilidade['categoria']}")
                print(f"Severidade: {vulnerabilidade['severidade']}")
                print(f"Status: {vulnerabilidade['status']}")
                print("-" * 30)
            return
    print("\nAtivo não encontrado.")

#funcao para gerenciar vulnerabilidades
def gerenciar_vulnerabilidades(ativos):
    opcao_vul = 0
    while opcao_vul != 3:
        exibir_menu_vulnerabilidades()
        opcao_vul = ler_opcao("Digite a opção que deseja realizar: ", 1, 3)
        if opcao_vul == 1:
            cadastrar_vulnerabilidade(ativos)
        elif opcao_vul == 2:
            listar_vulnerabilidades(ativos)