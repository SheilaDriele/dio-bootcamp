from datetime import datetime, timedelta, timezone

#trabalhando com fuso horarios de Oslo/Noruega e Sao Paulo/Brasil
data_oslo = datetime.now(timezone(timedelta(hours=2)))
#nome opcional, será retornado apenas se solicidado
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3), "BRL"))

print(data_oslo)
print(data_sao_paulo)