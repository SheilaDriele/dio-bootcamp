def principal():
    print("executando a funcao principal")

    def funcao_interna():
        print("executando a funcao interna")

    def funcao_2():
        print("executando funcao 2")

    #chamando as funções internas dentro da funcão principal
    funcao_interna()
    funcao_2()

principal()