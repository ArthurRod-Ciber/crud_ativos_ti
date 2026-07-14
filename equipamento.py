from enums import TipoAtivo
from utilidades import ler_opcao, ler_textos
from exibicao import exibir_tipos, exibir_ativo, exibir_menu_atualizacao
from arquivo import salvar_ativos
from entidade import EntidadeBase
from vulnerabilidade import Vulnerabilidade

class Equipamentos(EntidadeBase):
    def __init__(self, id, nome, responsavel, tipo, setor):
        super().__init__(id)
        self.nome = nome 
        self.responsavel = responsavel
        self.tipo = tipo
        self.setor = setor
        self.vulnerabilidades = []
        

    def transformar_em_dict(self):
        dictbase = super().transformar_em_dict()
        dictbase["nome"] = self.nome
        dictbase["responsavel"] = self.responsavel
        dictbase["tipo"] = self.tipo
        dictbase["setor"] = self.setor
        dictbase["vulnerabilidades"] = [vulnerabilidade.transformar_em_dict() for vulnerabilidade in self.vulnerabilidades]
        return dictbase
    
    def adicionar_vulnerabilidade(self, vulnerabilidade):
        self.vulnerabilidades.append(vulnerabilidade)
    
    @classmethod
    def criar_a_partir_de_dict(cls, dados):
       novo_equipamento = cls(dados["id"], dados["nome"], dados["responsavel"], dados["tipo"], dados["setor"])
       for vulnerabilidade_dict in dados["vulnerabilidades"]:
           vulnerabilidade_objeto = Vulnerabilidade.criar_a_partir_de_dict(vulnerabilidade_dict)
           novo_equipamento.adicionar_vulnerabilidade(vulnerabilidade_objeto)
           return novo_equipamento

    



#funcao para gerar um id automaticamente
def gerar_id(ativos):
    if len(ativos) == 0:
        return 1
    return max(ativo.id for ativo in ativos) + 1

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

    novo_ativo = Equipamentos(id, nome, responsavel, tipo.name, setor)
    ativos.append(novo_ativo)
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
            if ativo.id == id_busca:
                exibir_ativo(ativo)
                return
        print("\nAtivo não encontrado.")

    elif metodo == 2:
        nome_busca = ler_textos("Digite o nome do ativo: ")
        encontrado = False
        for ativo in ativos:
            if ativo.nome.lower() == nome_busca.lower():
                exibir_ativo(ativo)
                encontrado = True
        if not encontrado:
            print("\nAtivo não encontrado.")

#funcao para atualizar um ativo
def atualizar_ativo(ativos):
    print("\n--- ATUALIZAR ATIVO ---")
    id_att = ler_opcao("Digite o ID do ativo que você deseja atualizar: ", 1, 9999)

    for ativo in ativos:
        if ativo.id == id_att:
            exibir_ativo(ativo)
            break
    else:
        print("\nID não encontrado.")
        return

    exibir_menu_atualizacao()
    opcao = ler_opcao("Digite o que deseja atualizar: ", 1, 5)

    if opcao == 1:
        ativo.nome = ler_textos("Digite o novo nome: ")
    elif opcao == 2:
        ativo.responsavel = ler_textos("Digite o novo responsavel: ")
    elif opcao == 3:
        ativo.setor = ler_textos("Qual o novo setor do ativo? ")
    elif opcao == 4:
        exibir_tipos()
        tipo_opcao = ler_opcao("Digite o novo tipo: ", 1, 8)
        ativo.tipo = TipoAtivo(tipo_opcao).name
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
        if ativo.id == id_deletar:
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