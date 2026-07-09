# ==================== FUNÇÕES DE UTILIDADE ====================

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
