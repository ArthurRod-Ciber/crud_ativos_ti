import json

ARQUIVO = "ativos.json"

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
        ativos_em_dict = [ativo.transformar_em_dict() for ativo in ativos]
        json.dump(ativos_em_dict, arquivo, indent=4)