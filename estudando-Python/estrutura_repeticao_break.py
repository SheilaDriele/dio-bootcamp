while True:
    numero = int(input("Informe um número:"))

    if numero == 10:
        break

    print(numero)

for impar in range(100):

    if impar % 2 == 0:
        continue

    print(impar, end=" ")