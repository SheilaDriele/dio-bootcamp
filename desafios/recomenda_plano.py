def recomendar_plano(media_consumo):
    if media_consumo <= 10:
        return "Plano Essencial Fibra - 50Mbps."
    elif 10 < media_consumo <= 20:
        return "Plano Prata Fibra - 100Mbps."
    else:
        return "Plano Premium Fibra - 300Mbps."

try:

    # Solicita ao usuário que insira o consumo médio mensal de dados:
    consumo = float(input("Olá, informe sua media de consumo mensal em GB: \n"))

    # Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
    print(recomendar_plano(consumo))

except ValueError as e:
    print("Não foi possível realizar sua consulta. Por favor, insira apenas valores válidos.")