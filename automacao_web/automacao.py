# Algoritmo para buscar a cotação do dólar, euro e ouro na internet e atualizar os preços de produtos baseados nisso

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd


navegador = webdriver.Chrome()
# Cotação do dólar
navegador.get('https://www.google.com/')
navegador.find_element_by_xpath(
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dólar')
navegador.find_element_by_xpath(
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_dolar = navegador.find_element_by_xpath(
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacao_dolar)

# Cotação do euro
navegador.get('https://www.google.com/')
navegador.find_element_by_xpath(
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação euro')
navegador.find_element_by_xpath(
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_euro = navegador.find_element_by_xpath(
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacao_euro)

# Cotação do ouro
navegador.get('https://www.melhorcambio.com/ouro-hoje')
cotacao_ouro = navegador.find_element_by_xpath('//*[@id="comercial"]').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(',', '.')
print(cotacao_ouro)

navegador.quit()

# Importar e atualizar a base de dados

tabela = pd.read_excel('Produtos.xlsx')
# caso quiser escolher de uma tabela específica do excel é só usar o parâmetro 'sheets'
display(tabela)

# atualizar as cotações
tabela.loc[tabela['Moeda'] == 'Dólar', 'Cotação'] = float(cotacao_dolar)
tabela.loc[tabela['Moeda'] == 'Euro', 'Cotação'] = float(cotacao_euro)
tabela.loc[tabela['Moeda'] == 'Ouro', 'Cotação'] = float(cotacao_ouro)

# atualizar o preço de compra
tabela['Preço Base Reais'] = tabela['Preço Base Original'] * tabela['Cotação']
# atualizar o preço de venda
tabela['Preço Final'] = tabela['Preço Base Reais'] * tabela['Margem']

# tabela['Preço Final'] = tabela['Preço Final'].map('{:.2f}'.format)
# tabela['Preço Base Reais'] = tabela['Preço Base Reais'].map('{:.2f}'.format)
# tabela['Cotação'] = tabela['Cotação'].map('{:.2f}'.format)
# Fazer formatação nos dados faz com que eles se tornem em uma string

display(tabela)

# Exportar a base de dados atualizada
tabela.to_excel('Produtos_Novo.xlsx', index=False)