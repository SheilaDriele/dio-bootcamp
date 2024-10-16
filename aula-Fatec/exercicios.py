##Exercício 1 | Nome e idade
#nome = input('Digite seu nome: ')
#idade = input('Digite sua idade: ')
#
#print("Seu nome é ", nome, " e você tem ", idade, " anos.")
#
##Exercício 2 | Calculadora
#num1 = 5
#num2 = 2
#adicao = num1 + num2
#subtracao = num1 - num2
#multiplicacao = num1 * num2
#divisao = num1 / num2
#
#print("Resultados entre {} e {}: \n" .format(num1,num2), 'Adição = {}, Subtração = {}, Multiplicação = {}, Divisão = {}'.format(adicao,subtracao,multiplicacao,divisao))

##Exercício 3 | Concatenar
#doce = "Suspiro"
#valor = 0.55
#
#print('O {} custa R$ {}'.format(doce,valor))
#
##Exercício 4 | Not True
#ligado = True
#
#print(not ligado)

##Exercício 5 | Area do circulo
#raio = float(input('Digite o valor do raio: '))
#area = 3.1416 * (raio ** 2)
#
#print(area)

##Exercício 6 | Frutas
#fruta1 = input('Digite uma fruta: ')
#fruta2 = input('Digite outra fruta: ')
#
#fruta1 = 'Jaca'
#fruta2 = 'Carambola'
#
#print(fruta1, fruta2)

##Exercício 7 | Kilo para Libra
#pesoKG = float(input('Digite o seu peso em kg: '))
#pesoLB = pesoKG * 2.2046
#
#print('Seu peso em libra é de {}lb'.format(pesoLB))

##Exercício 8 | Calcular idade
#anoNasc = int(input('Digite o ano de nascimento: '))
#anoAtual = 2024
#idade = anoAtual - anoNasc
#
#print("A idade é {} anos.".format(idade))

##Exercício 9 | Contar caracteres
#frase = input("Digite uma frase: ")
#
#print(f'A frase tem {len(frase)} caracteres.')

#Exercício 10
#num1 = int(input('Digite um numero inteiro: '))
#num2 = int(input('Digite mais um numero inteiro: '))

#if num1 > num2:
 #   print(f'{num1} é maior do que {num2}.')
#elif num1 < num2:
#    print(f'{num1} é menor do que {num2}.')
#else:
# #   print('Os números são iguais.')


#TESTE
#A = input("insira valor: ")
#B = input("insira valor: ")

#x = int(A) + int(B)

#if x > 10:
#    print("Soma dos valores é: ", x, " é maior que 10.")
#else:
#    print("soma dos valores é ", x," valor não é maior que 10. ")

##ORDENADOR
A = int(input("Insira valor: "))
B = int(input("Insira outro valor: "))
C = int(input("Insira mais um valor: "))

print("Exibindo em ordem crescente:\n")
if A < B < C:
    print(A, " - ", B, " - ", C)
elif A < C < B:
    print(A, " - ", C, " - ", B)
elif B < A < C:
    print(B, " - ", A, " - ", C)
elif B < C < A:
    print(B, " - ", C, " - ", A)
elif C < A < B:
    print(C, " - ", A, " - ", B)
else:
    print(C, " - ", B, " - ", A)