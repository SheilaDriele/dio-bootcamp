class Animal:
    def __init__(self, num_patas):
        self.num_patas = num_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(kw)

class Aves (Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(kw)
        self.cor_bico = cor_bico

class Cachorro (Mamifero):
    pass

class Gato (Mamifero):
    pass

class Leao (Mamifero):
    pass

class Ornitorrinco (Mamifero, Aves):
    def __init__(self, **kw):
        super().__init__(kw)
        print(Ornitorrinco.__mro__) #mostra sequencia por onde esta pegando as informacoes

cachorro = Cachorro(num_patas=4, cor_pelo= "branco")
print(cachorro)

ornitorrinco = Ornitorrinco(num_patas= 4, cor_pelo="azul", cor_bico="preto")
print(ornitorrinco)