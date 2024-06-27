def calculadora(operacao):
    def soma(a,b):
        return a + b
    def sub(a,b):
        return a - b
    def multi(a,b):
        return a * b
    def divi(a,b):
        return a / b


    #match operacao: #MATCH NÃO DISPONIVEL
    #    case "+":
    #        return soma
    #    case "-":
    #        return sub
    #    case "*":
    #        return multi
    #    case "/":
    #        return divi

    if operacao == "+":
        return soma
    elif operacao == "-":
        return sub
    elif operacao == "*":
        return multi
    elif operacao == "/":
        return divi
    else:
        "operação inválida"

#Pegar a referencia da funcao
print(calculadora("+"))

print(calculadora("+")(2,3))

#Guardar em uma variável
op = calculadora("+")
print(op(5,5))
op = calculadora("-")
print(op(5,5))
op = calculadora("*")
print(op(5,5))
op = calculadora("/")
print(op(5,5))
