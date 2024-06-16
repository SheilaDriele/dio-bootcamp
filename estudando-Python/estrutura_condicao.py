maior_idade = 18
idade_especial = 17

idade = int(input("Informe a sua idade:"))

#Condicao com Apenas IF
if idade >= maior_idade:
    print("Maior de idade, pode tirar a CNH.")

if idade < maior_idade:
    print("Ainda não pode tirar a CNH.")

#Condicao com IF e Else
if idade >= maior_idade:
    print("Maior de idade, pode tirar a CNH.")
else:
    print("Ainda não pode tirar a CNH.")

#Condicao com IF, ELIF e ELSE
if idade >= maior_idade:
    print("Maior de idade, pode tirar a CNH.")
elif idade == idade_especial:
    print("Pode fazer aulas teoricas, mas não pode fazer aulas praticas.")
else:
    print("Ainda não pode tirar a CNH.")