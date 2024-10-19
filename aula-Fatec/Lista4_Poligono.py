## EXERCICIO 1 - POLIGONO
#Ler o número de lados de um polígono regular e a medida do lado (em cm)
print('Será um polígono?\n')
num_Lados = int(input('Digite o número de lado: '))

#Se o número de lados for inferior a 3, escrever NÃO É UM POLÍGONO
if num_Lados < 3:
    print('NÃO É UM POLÍGONO')

#Se o número de lados for igual a 3 escrever TRIÂNGULO e o valor da área
elif num_Lados == 3:
    base = float(input('Digite o valor da base (em cm): '))
    altura = float(input('Digite o valor da altura (em cm): '))
    area = (base * altura)/2

    print('TRIÂNGULO\nA área do triangulo é ', area)

#Se o número de lados for igual a 4 e todos os lados forem iguais, escrever QUADRADO e o valor da sua área.
elif num_Lados == 4:
    base = float(input('Digite o valor da base (em cm): '))
    altura = float(input('Digite o valor da altura (em cm): '))

    if base == altura:
        area = base * altura
        print('QUADRADO\nA área do quadrado é ', area)

# Se os números de lados forem iguais a 4 porém 2 lados (bases) são iguais e os outros 2 lados (altura) forem iguais, escrever RETÂNGULO e o valor da sua área.
    else:
        area = base * altura
        print('RETÂNGULO\nA área do retângulo é ', area)

#Se o número de lados for superior a 4, escrever POLÍGONO NÃO IDENTIFICADO.
else:
    print('POLÍGONO NÃO IDENTIFICADO')