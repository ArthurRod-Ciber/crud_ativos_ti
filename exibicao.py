# ==================== FUNÇÕES DE EXIBIÇÃO ====================
from enums import TipoAtivo, Severidade, Status

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

#funcao para exibir o menu de gerenciar as vulnerabilidades
def exibir_menu_vulnerabilidades():
    print("\n--- GERENCIAR VULNERABILIDADES ---")
    opcoes = [
        "Cadastrar Vulnerabilidades",
        "Listar Vulnerabilidades",
        "Voltar"
    ]
    for i, opcao in enumerate(opcoes, start=1):
        print(f"[{i}] {opcao}")

#exibir submenu do tipo de ativos
def exibir_tipos():
    for tipo in TipoAtivo:
        print(f"[{tipo.value}] {tipo.name.replace('_', ' ')}")

#funcao para exibir severidades
def exibir_severidades():
    for severidade in Severidade:
        print(f"[{severidade.value}] {severidade.name.replace('_', ' ')}")

#funcao para exibir opcoes de status
def exibir_status():
    for status in Status:
        print(f"[{status.value}] {status.name.replace('_', ' ')}")

#funcao para exibir o ativo
def exibir_ativo(ativo):
    print(f"\nID: {ativo['id']}")
    print(f"Nome: {ativo['nome']}")
    print(f"Responsavel: {ativo['responsavel']}")
    print(f"Setor: {ativo['setor']}")
    print(f"Tipo: {ativo['tipo'].replace('_', ' ')}")
    print()
