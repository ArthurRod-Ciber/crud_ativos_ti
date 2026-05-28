#funcoes para organizar melhor o codigo

from enums import TipoAtivo

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
    
    for i, opcoes in enumerate(opcoes, start=1):
        print(f"[{i}] {opcoes}")

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


#exibir submenu do tipo de ativos

def exibir_tipos():
    for tipo in TipoAtivo:
        print(f"[{tipo.value}] {tipo.name.replace("_", " ")}")


#funcao para exibir o ativo

def exibir_ativo(campos):
    print(f"\nID: {campos[0]}")
    print(f"Nome: {campos[1]}")
    print(f"Responsavel: {campos[2]}")
    print(f"Setor: {campos[3]}")
    print(f"Tipo: {campos[4]}")
    print()

#funcao para carregar os ativos no .txt

def carregar_ativos():
    ativos = {}
    with open("ativos.txt", "r") as  arquivo:
        for linha in arquivo:
           campos = linha.strip().split("|")
           ativos[int(campos[0].strip())] = campos 
        return ativos

#funcao para exibir manu das atualizações

def exibir_menu_atualizacao():
    opcoes = [
        "Nome",
        "Responsavel",
        "Setor",
        "Tipo",
        "Descrição"
        "Canelar"

    ]

    print()
    for i in opcoes in enumerate(opcoes, start=1):
        print(f"[{i}] {opcoes}")
        
