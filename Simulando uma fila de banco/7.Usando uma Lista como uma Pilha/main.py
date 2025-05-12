fila_do_banco_pilha = []



while(True):
        opcao = input(f"""\n\nOlá somos um banco, escolha uma das tres opcoes: 
            1- Adicionar cliente
            2- Atender cliente
            3- Finalizar
            \n Status da fila: {fila_do_banco_pilha}
            Digite aqui: """)


        if opcao == "1":
         adicionar_cliente = str(input("Bom dia, seja bem vindo ao nosso banco. Qual o seu nome? "))
         if adicionar_cliente.isdigit():
                print("Digite o NOME do próximo na fila (pilha)")
         else:
                fila_do_banco_pilha.append(adicionar_cliente)
                print(f"{fila_do_banco_pilha[-1]} adicionado para a fila (pilha)!!!!!")

        elif opcao == "2":
                if fila_do_banco_pilha:
                        print(f"{fila_do_banco_pilha[-1]} atendido!!!!!")
                        fila_do_banco_pilha.pop()
                else:
                       print("!!!! Não existe pessoas na fila (pilha) !!!!!!")
        
        elif opcao == "3":
                print(f"Fim!!")
                break

        else:
                print("Coloque um NÚMERO VÁLIDO")