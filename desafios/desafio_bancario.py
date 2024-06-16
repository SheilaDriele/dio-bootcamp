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
opcao = -1
saldo = 500


while  opcao != 0:
    opção = input(print(menu))
    if opcao == 1:
        print("Digite o valor do saque: \n")
    elif opcao == 2:
        print("Digite o valor do deposito: \n")
    elif opcao == 3:
        print("""
======================
        EXTRATO         
======================""")
    else:
        print("Opcão inválida.\n")
else:
    print("Obrigado por utilizar o nosso banco.")


