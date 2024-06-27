def meu_decorador(funcao):
    def envelope():
        print("faz algo antes de executar")
        funcao()
        print("faz algo depois de executar")

    return envelope

def ola_mundo():
    print("Olá mundo!")

#para decorar um funcao, atribui à funcão um novo valor
#passa a funcao que desseja decorar como argumento

ola_mundo = meu_decorador(ola_mundo)
ola_mundo()