import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import seaborn as sns

# Importando e visualizando os dados
tabela = pd.read_csv('advertising.csv')
display(tabela)

sns.heatmap(tabela.corr(), cmap='Wistia', annot=True)
plt.show()

sns.pairplot(tabela)
plt.show()


# Separando as informações em X e Y

y = tabela['Vendas']

x = tabela.drop('Vendas', axis=1) # 0 para linha e 1 para coluna

# aplicar o train test split
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)

modelo_regressaolinear = LinearRegression()
modelo_randomforest = RandomForestRegressor()

modelo_regressaolinear.fit(x_treino, y_treino)
modelo_randomforest.fit(x_treino, y_treino)

previsao_regressaolinear = modelo_regressaolinear.predict(x_teste)
previsao_randomforest = modelo_randomforest.predict(x_teste)

print(metrics.r2_score(y_teste, previsao_regressaolinear))
print(metrics.r2_score(y_teste, previsao_randomforest))
# RandomForest é o modelo vencedor

tabela_auxiliar = pd.DataFrame()
tabela_auxiliar['y_test'] = y_teste
tabela_auxiliar['regressao linear'] = previsao_regressaolinear
tabela_auxiliar['random forest'] = previsao_randomforest

plt.figure(figsize=(15, 5))
sns.lineplot(data=tabela_auxiliar)
plt.show()

sns.barplot(x=x_treino.columns, y=modelo_randomforest.feature_importances_)
plt.show()