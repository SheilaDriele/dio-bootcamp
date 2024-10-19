##EXERCICIO 6
#Faça um algoritmo investigador criminal. Ele deve fazer 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# ⦁ "Telefonou para a vítima?" ⦁ "Esteve no local do crime?" ⦁ "Mora perto da vítima?" ⦁ "Devia para a vítima?" ⦁ "Já trabalhou com a vítima?"

afirmacao = 0
print('\t\tO INVESTIGADOR')
print('Responda as perguntas com "Sim" ou "Não"\n')

resp = input("Telefonou para a vítima?[Sim/Não]\n-> ")
if resp == 'Sim' or resp == 'sim':
    afirmacao += 1

resp = input("Esteve no local do crime?[Sim/Não]\n-> ")
if resp == 'Sim' or resp == 'sim':
    afirmacao += 1

resp = input("Mora perto da vítima?[Sim/Não]\n-> ")
if resp == 'Sim' or resp == 'sim':
    afirmacao += 1

resp = input("Devia para a vítima?[Sim/Não]\n-> ")
if resp == 'Sim' or resp == 'sim':
    afirmacao += 1

resp = input("Já trabalhou com a vítima?[Sim/Não]\n-> ")
if resp == 'Sim' or resp == 'sim':
    afirmacao += 1

# O algoritmo deve emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a
print('\n\t\tRESULTADO')
# 2 questões ela deve ser classificada como "Suspeita",
if afirmacao == 2:
    print('Suspeito')
# entre 3 e 4 como "Cúmplice" e
elif afirmacao == 3 or afirmacao == 4:
    print('Cumplice')
# 5 como "Assassino".
elif afirmacao == 5:
    print('Assassino')
# Caso contrário, ele será classificado como "Inocente".
else:
    print('Inocente')
