fila_do_banco = []
adicionar_cliente = ""
opcao = ""

while(True):
        opcao = input(f"""\n\nOlá somos um banco, escolha uma das tres opcoes: 
            1- Adicionar cliente
            2- Atender cliente
            3- Finalizar
            \n Status da fila: {fila_do_banco}
            Digite aqui: """)


        if opcao == "1":
         adicionar_cliente = input("Bom dia, seja bem vindo ao nosso banco. Qual o seu nome? ")
         if adicionar_cliente.isdigit():
                print("Digite o NOME do próximo na fila")
         else:
                fila_do_banco.append(adicionar_cliente)
                print(f"{fila_do_banco[-1]} adicionado para a fila!!!!!")

        elif opcao == "2":
                # fila_do_banco.remove(fila_do_banco[0])
                if fila_do_banco:
                        print(f"{fila_do_banco[0]} atendido!!!!!")
                        fila_do_banco.pop(0)
                else:
                       print("!!!! Não existe pessoas na fila !!!!!!")
        
        elif opcao == "3":
                print(f"Fim!!")
                break

        else:
                print("Coloque um NÚMERO VÁLIDO")