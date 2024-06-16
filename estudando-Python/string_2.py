nome = "Sheila"
idade = 33
profissao = "Programadora"
linguagem = "Python"
saldo = 500.65854

#dicionario
dados = {"nome":nome, "idade": idade, "altura": "1,63"}

print("Nome: %s Idade: %d" % (nome,idade)) #formatação com %

#formatação com .format
print("Nome: {} Idade: {}" .format(nome,idade))
print("Nome: {1} Idade: {0}" .format(idade,nome)) #com indece
print("Nome: {1} Idade: {0}, idade da {1}" .format(idade,nome))
print("Nome: {nome} Idade: {idade}" .format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age}" .format(name=nome, age=idade)) #nome dareferencia pode ser diferente do nome da variavel
print("Nome: {nome} Idade: {idade} Altura: {altura}" .format(**dados))

#formatação f-string
print(f"Nome: {nome} Idade: {idade} Profissão: {profissao} Saldo: {saldo:.2f}")