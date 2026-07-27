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
# funcao para ler estritamente textos (sem ser apenas números)
def ler_textos(mensagem):
  while True:
    valor = input(mensagem).strip()

    if not valor:
      print("\nCampo não pode ser vazio, tente novamente!\n")
      continue

    if valor.isdigit():
      print("\nO campo não pode conter apenas números, tente novamente!\n")
      continue

    return valor

