def pega_numero(mensagem: str, mensagem_erro: str) -> int:

    while True:
        variavel = input(mensagem)
        try:
            numero = int(variavel)
            print("É um número inteiro")
            return numero
        except ValueError:
            print(mensagem_erro)