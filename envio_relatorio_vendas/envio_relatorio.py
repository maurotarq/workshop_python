# Código para baixar uma base de dados de venda e mandar um relatório do faturamento para um email através do navegador

import pyautogui
import pyperclip
import time
import pandas as pd


def posicao_mouse():    # funcao para determinar a posicao do mouse
    time.sleep(5)
    pyautogui.position()


# Acessando um link de download através do navegador
pyautogui.PAUSE = 1
pyautogui.hotkey('ctrl', 't')
link = 'https://drive.google.com/drive/folders/1pJ3KqiOXmxLYHf7U4QdJ7dqVL9s9l2kF?usp=sharing'
pyperclip.copy(link)
pyautogui.hotkey('ctrl', 'v')  # o pyautogui nao consegue lidar com caracteres especiais, por isso o pyperclip
pyautogui.press('enter')

# Baixando o arquivo de vendas
time.sleep(2)
pyautogui.click(x=482, y=510)
pyautogui.click(x=1660, y=227)
pyautogui.click(x=1361, y=782)
time.sleep(3)
pyautogui.click(x=1135, y=844)
time.sleep(5)

# Calcular o faturamento
tabela = pd.read_excel(
    r'Vendas - Dez.xlsx')  # o r faz com que o python
# ignore caracters especiais, por exemplo \n
faturamento = tabela['Valor Final'].sum()
quantidade = tabela['Quantidade'].sum()
print(faturamento)
print(quantidade)

# Enviar um email com o relatório

link = 'https://mail.google.com/mail/u/0/#inbox'
pyautogui.hotkey('ctrl', 't')
pyperclip.copy(link)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

time.sleep(2)
pyautogui.click(x=93, y=255)
time.sleep(2)
pyautogui.write('algum_email@email.com')
pyautogui.press('tab')
pyautogui.press('tab')
assunto = 'Relatório de Vendas'
pyperclip.copy(assunto)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')
texto = f'''Prezados, bom dia.

O faturamento foi de R$ {faturamento:,.2f}.
A quantidade de produtos vendidos foi de {quantidade:,}.

Att. Nome'''
pyautogui.write(texto)
pyautogui.hotkey('ctrl', 'enter')
