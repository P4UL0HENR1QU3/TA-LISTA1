fila_do_banco = []
adicionar_cliente = ""


while adicionar_cliente.lower() != "finalizar":
    adicionar_cliente = str(input("Bom dia, seja bem vindo ao nosso banco. Qual o seu nome? "))

    if adicionar_cliente.isdigit():
        print("Digite o NOME do próximo na fila")

    elif adicionar_cliente.lower() != "finalizar":
        print(f"Pode se dirigir para a fila, {adicionar_cliente}")
        fila_do_banco.append(adicionar_cliente)
        print(f"""{fila_do_banco} está na fila
              1...
              2...
              3...
              Cliente atendido!!""")
        print("Próximo da fila!!!")
        fila_do_banco.remove(adicionar_cliente)
    else:
        print("Fila encerrada!!")

