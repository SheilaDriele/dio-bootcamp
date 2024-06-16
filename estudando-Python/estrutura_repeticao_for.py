vogais = "AEIOU"

#Solicitar texto para usuário
texto = input("Informe um texto: ")

#Repeticao para separar vogais do texto
for letra in texto:
    if letra.upper() in vogais: #transforma letras em maiusculas e verifica se tem vogais
        print(letra, end="")
else:
    print() #adiciona uma quebra de linha
    print("Obrigado pela participação.")

#Exemplo com built-in range
#tabuada do 5
for numero in range(0, 51, 5):
    print(numero, end=" ")