from funcoes import (pega_numero)

def main():

    mensagem = "Digite um numero: "
    mensagem_erro = "Digite um NUMERO INTEIRO para que seja válido"
    menor_valor = 10
    maior_valor = 50
   
    pega_numero(mensagem, mensagem_erro, menor_valor, maior_valor)


if __name__ == "__main__":
    main()
 
