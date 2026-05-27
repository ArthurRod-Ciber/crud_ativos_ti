from enum import Enum   


class TipoAtivo(Enum):
    NOTEBOOK = 1
    SERVIDOR = 2
    ROTEADOR = 3
    SOFTWARE_LICENCIADO = 4
    APLICACOES_WEB = 5
    IMPRESSORA_DE_REDE = 6
    ESTACAO_DE_TRABALHO = 7
    BANCO_DE_DADOS = 8

class Severidade(Enum):
    BAIXA = 1
    MEDIA = 2
    ALTA = 3
    CRITICA = 4

class Status(Enum):
    ABERTA = 1
    EM_TRATAMENTO = 2
    CORRIGIDA = 3
    ACEITA = 4
