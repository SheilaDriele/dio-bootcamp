import re
def menu():
    menu = """
    ======================
             MENU         
    ======================

        [1] Sacar
        [2] Depositar
        [3] Extrato
        [4] Novo Usuário
        [5] Nova Conta
        [6] Listar Contas
        [0] Sair

    ======================
    Escolha uma das opções: 
    =>  """

    agencia = "0001"
    saldo = 0
    extrato = ""
    limite = 500
    num_saque = 0
    maximo_saques = 3
    usuarios = []
    contas = []

    while True:
        opcao = int(input(menu))

        # SAQUE
        if opcao == 1:
           saldo,extrato, num_saque = sacar(saldo=saldo, extrato=extrato, limite=limite, num_saque=num_saque, maximo_saques=maximo_saques)
        elif opcao == 2:
            saldo, extrato= depositar(saldo, extrato)
        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == 4:
            cadastrar_usuario(usuarios)
        elif opcao == 5:
            num_conta = len(contas) + 1
            conta = cadastrar_conta(agencia, num_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 6:
            listar_contas(contas)
        elif opcao == 0:
            print("\nObrigado por utilizar o nosso banco.")
            break
        else:
            print("\nOpcão inválida.")


def sacar(*, saldo, extrato, limite, num_saque, maximo_saques):
    #Receber argumento apenas por nome *, (keyword only)

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
            extrato += f"\tSaque (-): R$ {valor:.2f}\n"
            print("Saque realizado com sucesso!")

    else:
        print("Limite de saques diário excedido!")

    return saldo, extrato, num_saque

def depositar(saldo, extrato, /):
    # Receber argumento apenas por posicao '/'(positional only)
    valor = float(input("Digite o valor do deposito: \n"))

    if valor > 0:
        saldo += valor
        extrato += f"\tDéposito (+): R$ {valor:.2f}\n"
        print("Deposito realizado com sucesso!")

    else:
        print("Valor inválido. Não foi possível realizar o deposito.")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    # Receber argumento apenas por nome *, e posicao ', /'
    print(f"""
    ======================
            EXTRATO         
    ======================""")
    print("\tNão foram realizadas movimentações." if not extrato else extrato)
    print(f"""
    Saldo Atual:      R$ {saldo:.2f}

    ======================""")

def cadastrar_usuario(usuarios):
    # Armazenar usuario em uma lista com nome, data de nascimento, cpf, endereço. Endereço em string: logradouro, numero, bairro, cidade/sigla estado
    cpf = input("Informe o CPF (Somente números): ")
    cpf_valido = validar_CPF(cpf)
    usuario = filtrar_usuario(cpf, usuarios)


    if cpf_valido:
        if usuario:
            print("Já existe usuário com esse CPF!")
            return
    else:
        print("CPF inválido. Digite apenas números")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")

def cadastrar_conta(agencia, num_conta, usuarios):
    cpf = input("Informe o CPF do usuário (Somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    #Cria a conta automaticamente a partir do usuário
    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": num_conta, "usuario": usuario}

    print("Operação não realizada! Usuário não encontrado.")

def validar_CPF(cpf):
    #CPF somente numeros. Apenas um usuario por CPF
    padrao = r"\d{11}"

    return re.match(padrao, cpf)

def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def listar_contas(contas):
    for conta in contas:
        linha_conta = f"""
\tAgência:\t{conta['agencia']}
\tNumero da Conta:\t{conta['numero_conta']}
\tTitular:\t{conta['usuario']['nome']}
"""
        print(linha_conta)

menu()


