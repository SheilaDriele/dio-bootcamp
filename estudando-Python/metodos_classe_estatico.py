class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)

    @staticmethod
    def maior_idade(idade):
        return idade >= 18

#Forma antiga
#p = Pessoa("Sheila", 33)
#print(p.nome, p.idade)

#Forma mais comum
p = Pessoa.criar_apartir_data_nascimento(1990, 10, 1, "Sheila")
print(p.nome, p.idade)

print(Pessoa.maior_idade(18))
print(Pessoa.maior_idade(10))
print(Pessoa.maior_idade(p.idade))