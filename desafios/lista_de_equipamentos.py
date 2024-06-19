#Lista de itens
itens = []

#solicita 3 itens ao usuário
contador = 0

while contador < 3:
    item = input("Informe um equipamento: ")
    itens.append(item)
    contador += 1

print(f"Lista de Equipamentos:")

for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")