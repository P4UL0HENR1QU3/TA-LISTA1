def pega_numero(mensagem: str, mensagem_erro: str, menor_valor: int, maior_valor: int) -> int:

    while True:
        variavel = input(mensagem)
        try:
            numero = int(variavel)
            print("É um número inteiro")

            if(menor_valor <= numero <= maior_valor):
                print("Ele cumpre o menor e maior valor")
                return numero
            else:
                print("Ela não cumpre o menor e maior valor")

        except ValueError:
            print(mensagem_erro)