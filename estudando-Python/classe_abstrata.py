from abc import ABC, abstractclassmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractclassmethod
    def ligar(self):
        pass
    @abstractclassmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Lingando a TV...")
        print("Ligada!")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!")

    def marca(self):
        print("Samsung")

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligado!")

    def desligar(self):
        print("Desligada!")

    def marca(self):
        print("LG")

controle = ControleTV()
controle.ligar()
controle.desligar()
controle.marca()

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
controle.marca()