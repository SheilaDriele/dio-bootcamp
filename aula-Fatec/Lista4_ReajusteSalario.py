#EXERCICIO 3 - REAJUSTE DE SALARIO
#A empresa Um programa que calcule o reajustes de aumento de salário.
#Deve receber o salário de um colaborador e fazer o reajuste seguindo os seguintes critérios, baseado no salário atual informado:
salario = float(input('Digite o salário do colaborador: '))

# salários até R$ 250,00: aumento de 20%
if salario <= 250:
    ajuste = salario * 0.2
    salarioReajustado = salario + ajuste
    print(f'\nSalario atual: R$ {salario:.2f} \tPercentual de 20% \tValor do aumento: R$ {ajuste:.2f} \tSalario com reajuste: R$ {salarioReajustado:.2f}')

# salários entre R$ 250,00 e R$ 900,00: aumento de 15%
elif salario > 250 and salario <= 900:
    ajuste = salario * 0.15
    salarioReajustado = salario + ajuste
    print(f'\nSalario atual: R$ {salario:.2f} \tPercentual de 15% \tValor do aumento: R$ {ajuste:.2f} \tSalario com reajuste: R$ {salarioReajustado:.2f}')

# salários entre R$ 900,00 e R$ 1500,00: aumento de 10%
elif salario > 900 and salario <= 1500:
    ajuste = salario * 0.1
    salarioReajustado = salario + ajuste
    print(f'\nSalario atual: R$ {salario:.2f} \tPercentual de 10% \tValor do aumento: R$ {ajuste:.2f} \tSalario com reajuste: R$ {salarioReajustado:.2f}')

# salários de R$ 1500,00 em diante: aumento de 5%
else:
    ajuste = salario * 0.05
    salarioReajustado = salario + ajuste
    print(f'\nSalario atual: R$ {salario:.2f} \tPercentual de 5% \tValor do aumento: R$ {ajuste:.2f} \tSalario com reajuste: R$ {salarioReajustado:.2f}')