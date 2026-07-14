# ==================== FUNÇÕES DE VULNERABILIDADES ====================
# CRUD das vulnerabilidades associadas a cada ativo.

from enums import Severidade, Status
from utilidades import ler_opcao, ler_textos
from exibicao import exibir_severidades, exibir_status, exibir_menu_vulnerabilidades
from arquivo import salvar_ativos
from entidade import EntidadeBase

class Vulnerabilidade(EntidadeBase):
    def __init__(self, id, descricao, categoria, severidade, status):
        super().__init__(id)
        self.descricao = descricao
        self.categoria = categoria 
        self.severidade = severidade
        self.status = status

    def transformar_em_dict(self):
        dictbase =  super().transformar_em_dict()
        dictbase["descricao"] = self.descricao
        dictbase["categoria"] = self.categoria
        dictbase["severidade"] = self.severidade
        dictbase["status"] = self.status
        return dictbase
    
    @classmethod
    def criar_a_partir_de_dict(cls, dados):
        return cls(dados["id"], dados["descricao"], dados["categoria"], dados["severidade"], dados["status"] )


# funcao para cadastrar uma vulnerabilidade
def cadastrar_vulnerabilidade(ativos):
    print("\n--- CADASTRAR VULNERABILIDADE ---")
    id_ativo = ler_opcao("Digite o ID do ativo que deseja cadastrar a vulnerabilidade: ", 1, 9999)

    for ativo in ativos:
        if ativo.id == id_ativo:
            descricao = ler_textos("Digite a descrição da vulnerabilidade: ")
            categoria = ler_textos("Digite a categoria da vulnerabilidade: ")

            exibir_severidades()
            severidade_opcao = ler_opcao("Digite a severidade: ", 1, 4)
            severidade = Severidade(severidade_opcao)

            exibir_status()
            status_opcao = ler_opcao("Digite o status: ", 1, 4)
            status = Status(status_opcao)

            nova_vulnerabilidade = Vulnerabilidade(ativo.id, descricao, categoria, severidade.name, status.name)
            ativo.adicionar_vulnerabilidade(nova_vulnerabilidade)
            salvar_ativos(ativos)
            print("\nVulnerabilidade cadastrada com sucesso!")
            return

    print("\nAtivo não encontrado.")


# funcao para listar vulnerabilidades de um ativo
def listar_vulnerabilidades(ativos):
    print("\n--- VULNERABILIDADES ---")
    id_ativo = ler_opcao("Digite o ID do ativo: ", 1, 9999)

    for ativo in ativos:
        if ativo.id == id_ativo:
            if len(ativo.vulnerabilidades) == 0:
                print("\nEste ativo não possui vulnerabilidades registradas.")
                return
            for vulnerabilidade in ativo.vulnerabilidades:
                print(f"\nDescrição: {vulnerabilidade.descricao}")
                print(f"Categoria: {vulnerabilidade.categoria}")
                print(f"Severidade: {vulnerabilidade.severidade}")
                print(f"Status: {vulnerabilidade.status}")
                print("-" * 30)
            return

    print("\nAtivo não encontrado.")


# funcao para gerenciar vulnerabilidades
def gerenciar_vulnerabilidades(ativos):
    opcao_vul = 0
    while opcao_vul != 3:
        exibir_menu_vulnerabilidades()
        opcao_vul = ler_opcao("Digite a opção que deseja realizar: ", 1, 3)
        if opcao_vul == 1:
            cadastrar_vulnerabilidade(ativos)
        elif opcao_vul == 2:
            listar_vulnerabilidades(ativos)