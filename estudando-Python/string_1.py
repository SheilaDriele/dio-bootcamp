#MAIUSCULA E MINUSCULA
nome = "sHeiLA"

print(nome.upper()) #transforma tudo em maiuscula
print(nome.lower()) #transforma tudo em minuscula
print(nome.title()) #deixa apenas a primeira letra como maiuscula

#ELIMINAÇÃO DOS ESPAÇOS
texto = "  Belo dia. "

print(texto + ".")
print(texto.strip() + ".") #remove todos os espaços antes e depois na string
print(texto.lstrip() + ".") #remove todos os espaços a esquerda da string
print(texto.rstrip() + ".") #remove todos os espaços a direitaa string

#CENTRALIZAÇÃO
menu = "Python"

print("###" + menu + "###") #centralização manual
print(menu.center(14)) #centralização automatica
print(menu.center(14, "#")) #centralização com segundo parametro

#JUNÇÃO
print("P-y-t-h-o-n") #manual
print("-".join(menu)) #resultado com join