class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("ligando o motor")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self,carregado, cor, placa, numero_rodas):
        self.carregado = carregado
        super().__init__(cor, placa, numero_rodas)

    def esta_carregado(self):
        print(f"{'Sim,' if self.carregado else 'Não'} estou carregado")

moto = Motocicleta("vermelha", "ad-1204", 2)
print(moto)
moto.ligar_motor()

carro = Carro("roxo", "abece - 1230", 4)
print(carro
      )
caminhao = Caminhao(False,"branco", "bca 1245", 6)
print(caminhao)
caminhao.ligar_motor()
caminhao.esta_carregado()