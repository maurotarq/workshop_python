# Código que importa uma base de dados para análise

import pandas as pd
import plotly.express as px

# Importando e visualizando a base de dados
tabela = pd.read_csv('telecom_users.csv')
display(tabela)

# Fazendo uma limpeza inicial
tabela = tabela.drop('Unnamed: 0', axis=1)  # excluindo a coluna 'Unnamed: 0'
# o axis exclui a linha ou coluna(0 para linha 1 para coluna)
display(tabela)

# Tratando os dados
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')
tabela = tabela.dropna(how='all', axis=1)  # all é quando voce quer excluir colunas COMPLETAMENTE vazias
# any quando você quer excluir colunas que tem pelo menos 1 valor vazio
# linhas vazias
tabela = tabela.dropna(how='any', axis=0)
print(tabela.info())

# Análise dos dados
display(tabela['Churn'].value_counts())
display(tabela['Churn'].value_counts(normalize=True).map('{:.1%}'.format))

for coluna in tabela.columns:
        grafico = px.histogram(tabela, x=coluna, color='Churn')
        grafico.show()