#EXERCÍCIO IDADE
#Faça um algoritmo que retorne ao usuário a sua idade a partir da inserção da sua data de nascimento

import datetime

data_Nasc = input('Digite sua data de nascimento (ex.: 01/11/2000): ')
data_Convertida = datetime.datetime.strptime(data_Nasc, '%d/%m/%Y')
data_Atual = datetime.date.today()
idade = data_Atual.year - data_Convertida.year
mes = data_Atual.month - data_Convertida.month
dia = data_Atual.day - data_Convertida.day

if mes >= 0:
    if dia < 0:
        idade = idade - 1
        print(f'Idade igual a {idade} anos.')
    else:
        print(f'Idade igual a {idade} anos.')
else:
    idade = idade - 1
    print(f'Idade igual a {idade} anos.')
