##Exercício 1 - Maior ou Igual
#Num1 = float(input("Insira um número: "))
#Num2 = float(input("Insira outro número:"))

#if Num1 > Num2:
#    print("O maior é ", Num1)
#elif Num1 < Num2:
#    print("O maior é ", Num2)
#else:
#    print("Números iguais")


##Exercício 2 - Acima da velocidade
#velocidade = float(input("Insira a velocidade do automóvel: "))

#if velocidade <= 80:
 #   print("Dentro da velocidade permitida.")
#else:
#    valor = 5.00
 #   multa = (velocidade - 80) * valor
#
#    print("Você foi multado!\nSua multa é de R$ ", multa)

##Exercício 3 - Maior e menor
#num1 = float(input("Insira um número: "))
#num2 = float(input("Insira outro número:"))
#num3 = float(input("Insira mais um número:"))

#if num1 > num2 > num3:
#    print("O maior é ", num1, " e o menor é ", num3)
#elif num1 > num3 > num2:
#    print("O maior é ", num1, " e o menor é ", num2)
#elif num2 > num1 > num3:
# #   print("O maior é ", num2, " e o menor é ", num3)
#elif num2 > num3 > num1:
#    print("O maior é ", num2, " e o menor é ", num1)
#elif num3 > num1 > num2:
# #   print("O maior é ", num3, " e o menor é ", num2)
#else:
#    print("O maior é ", num3, " e o menor é ", num1)

##Exercício 4 - Aumento de salário
#sal_Atual = float(input('Digite o valor do sálario atual: '))

#if sal_Atual > 1250:
#    aumento = sal_Atual * 0.1
#    sal_Novo = sal_Atual + aumento
#    print('O aumento foi de R$ ', aumento, '. O novo salario é R$ ', sal_Novo)
#else:
#    aumento = sal_Atual * 0.15
#    sal_Novo = sal_Atual + aumento
#    print('O aumento foi de R$ ', aumento, '. O novo salario é R$ ', sal_Novo)

##Exercício 5 - Carro novo/velho
#idade_carro = int(input('Insira a idade do seu carro: '))

#if idade_carro > 3:
#    input("Seu carro é velho.")
#else:
#    input("Seu carro é novo.")

##Exercício 6 - Valor da viagem
#distancia = float(input('Digite a distância a ser percorrida em km: '))

#if distancia > 200:
#    vl_viagem = distancia * 0.45
#    print("O valor da viagem é de R$ ", vl_viagem)
#else:
#    vl_viagem = distancia * 0.5
#    print("O valor da viagem é de R$ ", vl_viagem)

##Exercício 7 - Preço por categoria
#categoria = int(input('Digite o numero da categoria: '))

#if categoria == 1:
#    print("Preço é R$ 10,00.")
#elif categoria == 2:
#    print("Preço é R$ 15,00.")
#elif categoria == 3:
#    print("Preço é R$ 19,00.")
#elif categoria == 4:
#    print("Preço é R$ 23,00.")
#elif categoria == 5:
#    print("Preço é R$ 27,00.")
#else:
#    print('Categoria não existe.')

##Exercício 7 - Calcular
#num1 = float(input('Digite um número: '))
#num2 = float(input('Digite outro número: '))
#operador = int(input('''Escolha uma opção:
#[1] Soma
#[2] Subtração
#[3] Multiplicação
#[4] Divisão
#-> '''))

#if operador == 1:
#    resultado = num1 + num2
#    print('Resultado: ', resultado)
#elif operador == 2:
#    resultado = num1 - num2
#    print('Resultado: ', resultado)
#elif operador == 3:
#    resultado = num1 * num2
#    print('Resultado: ', resultado)
#elif operador == 4:
#    resultado = num1 / num2
#    print('Resultado: ', resultado)
#else:
#    print('Operação invalida')