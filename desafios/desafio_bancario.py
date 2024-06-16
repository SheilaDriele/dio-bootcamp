menu = """
======================
         MENU         
======================

    [1] Sacar
    [2] Depositar
    [3] Extrato
    [0] Sair

======================
Escolha uma das opções
======================
"""

saldo = 0
limite = 500
num_saque = 0
maximo_saques = 3
extrato = ""

while True:
    opcao = int(input(menu))

    # SAQUE
    if opcao == 1:
        if num_saque < maximo_saques:
            valor = float(input("Digite o valor do saque: \n"))

            if valor < 0:
                print("Não é possivel realizar esta operação. Valor Inválido.")

            elif valor > saldo:
                print("Operação falhou. Saldo insuficiente!")

            elif valor > limite:
                print("Operação falhou. O valor excede o limite por saque.")
            else:
                saldo -= valor
                num_saque += 1
                extrato += f"Saque (-): R$ {valor:.2f}\n"
                print("Saque realizado com sucesso!")

        else:
            print("Limite de saques diário excedido!")


    # DEPOSITO
    elif opcao == 2:
        valor = float(input("Digite o valor do deposito: \n"))

        if valor > 0:
            saldo += valor
            extrato += f"Déposito (+): R$ {valor:.2f}\n"
            print("Deposito realizado com sucesso!")

        else:
            print("Valor inválido. Não foi possível realizar o deposito.")

    # EXTRATO
    elif opcao == 3:
        print(f"""
======================
        EXTRATO         
======================

{extrato}
Saldo Atual: R$ {saldo:.2f}

======================""")

    elif opcao == 0:
        print("\nObrigado por utilizar o nosso banco.")
        break
    else:
        print("\nOpcão inválida.")



