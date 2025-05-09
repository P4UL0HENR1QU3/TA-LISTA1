def main():

    try: #permite que o codigo rode mesmo que ocorra um valor incorreto inserido de inicio
        ano = int(input("Insira o ano: "))


        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            print(f"o ano {ano} é bissexto")
        else:
            print(f"o ano {ano} NÃO é bissexto")

    except ValueError: #pular erro inicial
        print("Digite um ano (número) INTEIRO")

main()