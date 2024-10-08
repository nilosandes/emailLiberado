import pyautogui as pyg
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
import pytz

# Alterna para a última janela aberta (deve ser o email)
pyg.hotkey('alt', 'tab')

pyg.hotkey('ctrl', 'f')
pyg.write('De:')
pyg.press('enter')
pyg.press('esc')
pyg.press('right')
pyg.press('right')
pyg.hotkey('ctrl', 'shiftleft', 'shiftright', 'right')
pyg.PAUSE = 0.4
pyg.hotkey('ctrl', 'c')
pyg.PAUSE = 0.4
pyg.hotkey('ctrl', 'home')

# Obtém a hora atual e converter para INT
timezone = pytz.timezone('America/Sao_Paulo')
now = datetime.now(timezone)
horaAtual = int(now.strftime("%H"))
print (type(horaAtual))

# Confere se é manhã ou tarde
saudacao = ""
if horaAtual<12:
  saudacao = "Bom dia, "
else:
  saudacao = "Boa tarde, "

#Comandos para responder o e-mail
pyg.write(f'{saudacao}')
pyg.hotkey('ctrl', 'v')
pyg.write('!\n\nEmail liberado.', interval=0.02)
pyg.hotkey('ctrl', 'enter')
pyg.press('enter')