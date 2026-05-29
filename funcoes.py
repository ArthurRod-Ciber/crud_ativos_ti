#funcoes para organizar melhor o codigo

from enums import TipoAtivo
import json

#funcao para exibir o menu

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

#funcao para ler a opcao

def ler_opcao(mensagem, minimo, maximo):
    while True:
        try:
            opcao = int(input(mensagem))
            if minimo <= opcao <= maximo:
                return opcao
            else:
                print(f"\nTente novamente! digite um numero entre {minimo} {maximo}")
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


#funcao para cadastrar ativos

def cadastrar(ativos):
    print("\n--- CADASTRAR ATIVO ---")
    id = gerar_id(ativos) #gera um id automaticamente 
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
        "tipo": tipo.name
    }
    ativos.append(ativo)
    salvar_ativos(ativos)
    print(f"\nAtivo cadastrado com sucedo! ID gerado: {id}")


#funcao para gerar um id

def gerar_id(ativos):
    if len(ativos) == 0: #conta quantos ativos tem na lista, se for 0 o arquivo esta vazio portanto o id começara em 1
        return 1
    return max(ativo["id" for ativo in ativos]) +1    #percorre cada ativo da lista, pega o valor do campo id de cada um, encontra o maior id dentre todos, soma um ao maior id encontrado


#exibir submenu do tipo de ativos

def exibir_tipos():
    for tipo in TipoAtivo:
        print(f"[{tipo.value}] {tipo.name.replace("_", " ")}")


#funcao para exibir o ativo

def exibir_ativo(ativo):
    print(f"\nID: {ativo['id']}")
    print(f"Nome: {ativo['nome']}")
    print(f"Responsavel: {ativo['responsavel']}")
    print(f"Setor: {ativo['setor']}")
    print(f"Tipo: {ativo['tipo']}")
    print() 

#funcao para listar ativos


def listar_ativos(ativos):
    print(f"\n--- LISTA DE ATIVOS ---")
    if len(ativos) == 0: #verifica se a lista ta vazia
        print("Nenhum ativo encontrado")
        return #encerra tudo se nao tiver nada pra mostrar 
    for ativo in ativos: #percorre cada ativo da lista
        exibir_ativo(ativo) #chama uma funcao ja existente para exibir dos dados


#funcao para carregar os ativos no json
ARQUIVO = "ativos.json"

def carregar_ativos():
    try:
        with open(ARQUIVO, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

#funcao para salvar os ativos:

def salvar_ativos(ativos):
    with open(ARQUIVO, "w") as arquivo:
        json.dump(ativos, arquivo, indent=4)


#funcao para buscar os ativos no json

def busca(ativos):
    print("\n--- BUSCAR ATIVO ---")
    metodo = ler_opcao("\ncomo deseja buscar?\n[1]ID\n[2]NOME\n", 1, 2)
    if metodo == 1:
        id_busca = ler_opcao("Digite o ID do ativo: ", 1, 9999)
        for ativo in ativos:
            if ativo["id"] == id_busca:
                exibir_ativo(ativo)
                return #encerra na hora assim que encontrar
        print("\nAtivo nao encontrado")

    elif metodo == 2:
        nome_busca = ler_textos("Digite o nome do ativo: ")
        encontrado = False
        for ativo in ativos:
            if ativo["nome"].lower == nome_busca.loer():
                exibir_ativo(ativo)
                encontrado = True
        if not encontrado:
            print(f"\nAtivo não encontrado")

#funcao para deletar ativos

def deletar(ativos):
    print("\n--- DELETAR ATIVO ---")
    id_deletar = ler_opcao("Digite o ID do ativo que deseja deletar: ", 1, 9999)

    for ativo in ativos:
        if ativo["id"] == id_deletar: #busca o ativo pelo id
            exibir_ativo(ativo) #mostra ativo antes de deletar
            confirmacao = ler_opcao("Tem certeza?\n[1]SIM\n[2]NAO\n", 1, 2)
            if confirmacao == 1:
                ativos.remove(ativos)
                salvar_ativos(ativos) #salva no json
                print("\nAtivo deletado!!")
            else:
                print("\nOperação cancelada")
            return
    print("\nAtivo nao encontrado")


#funcao para exibir manu das atualizações

def exibir_menu_atualizacao():
    opcoes = [
        "Nome",
        "Responsavel",
        "Setor",
        "Tipo",
        "Descrição",
        "Canelar",
    ]
    print()
    for i, opcao in enumerate(opcoes, start=1):
        print(f"[{i}] {opcao}")
        
#funcao para atualziar o ativo:

def atualizar_ativo(ativos):
    print("\n--- ATUALIZAR ATIVO ---")
    id_att = ler_opcao("Digite o ID do ativo que você deseja atualizar: ", 1, 9999)

    for ativo in ativos:
        if ativo["id"] == id_att:
            exibir_ativo(ativo)
            break
    else:
        print("ID não encontrado")
        return
    
    exibir_menu_atualizacao()
    opcao = ler_opcao("Digite o que deseja realizar: ", 1, 5)

    if opcao == 1:
        ativo["nome"]  = ler_textos("Digite um novo nome: ")
    elif opcao == 2:
        ativo["responsavel"] = ler_textos("Digite o novo novo responsavel para ela: ")
    elif opcao == 3:
        ativo["setor"] = ler_textos("Qual o novo setor do ativo°? ") 
    elif opcao == 4:
        tipo_opcao = ler_opcao("Digite um niovo tipo: ", 1, 8)
        ativo["tipo"] = TipoAtivo(tipo_opcao).name
    elif opcao == 5:
        print("\nOperação cancelada")
        return
    
    salvar_ativos(ativos)
    print("\nAtivo atualizado com sucesso")
    