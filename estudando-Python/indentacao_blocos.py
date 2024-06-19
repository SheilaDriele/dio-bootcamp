def sacar(valor):
    saldo = 500
    if saldo >= valor:
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa.")

    print("Obrigado por ser nosso cliente, tenha um bom dia")

def depositar(valor):
    saldo = 500
    saldo += valor

sacar(1000)


#TODO
# Para estudar melhor depois
numero = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]

print(numero)