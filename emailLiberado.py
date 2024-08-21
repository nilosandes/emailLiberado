import pyautogui as pyg
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
import pytz

# Alterna para a última janela aberta (deve ser o email)
pyg.hotkey('alt', 'tab')

# Obtém a hora atual e converter para INT
timezone = pytz.timezone('America/Sao_Paulo')
now = datetime.now(timezone)
horaAtual = int(now.strftime("%H"))
print (type(horaAtual))

# Confere se é manhã ou tarde
saudacao = ""
if horaAtual<12:
  saudacao = "Bom dia!"
else:
  saudacao = "Boa tarde!"

#Comandos para responder o e-mail
pyg.write(f'{saudacao}\n\nEmail liberado.', interval=0.02)
pyg.hotkey('ctrl', 'enter')
pyg.press('enter')