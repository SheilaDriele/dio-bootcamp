#pytz e uma biblioteca de terceiro para facilitar o trabalho com timezone
from datetime import datetime
import pytz

#nome e fuso horario sao padrao no utc
timezone = pytz.timezone('America/Sao_Paulo')
data = datetime.now(timezone)

print(data)

#  TODO não colocar o nome do  arquivo igual do import
