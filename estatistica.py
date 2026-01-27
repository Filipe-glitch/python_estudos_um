import pandas as pd  #usada para trabalhar com tabelas e dados.
x={'Pesos':[48.8, 48.9, 49.0, 49.1, 49.2, 49.3, 49.5, 49.7,
49.7, 49.7, 49.8, 50.0, 50.1, 50.1, 50.2, 50.2, 50.4, 50.6,
50.8, 50.9]} #criei um dicionário x com chave pesos. a chave guarda a lista com os valores
p=pd.DataFrame(x) # transforma o dicionário x em um DataFrame, que é uma tabela do pandas.
media=p['Pesos'].mean() # calcula a média dos valores usando .mean()
moda=p['Pesos'].mode() # .mode() retorna uma série (pode ter mais de uma moda).
mediana=p['Pesos'].median() #.median() calcula a mediana
print(f'Média: {media}')
print(f'Moda: {moda}')
print(f'Mediana: {mediana}')

# import io . Importa o módulo io, usado para manipular arquivos em memória.
# from google.colab import files . Importa a função files do Colab, que permite enviar arquivos para a sessão.
# uploaded=files.upload() . Abre uma janela para escolher arquivos do computador e fazer upload para o Colab.

# p=pd.read_excel(io.BytesIO(uploaded['ExemploAula05.xlsx']))
# estou importando o arquivo do excel para cá, pega o conteúdo bruto do arquivo Excel.
#  media=p['Pesos'].mean()
#  moda=p['Pesos'].mode()
#  mediana=p['Pesos'].median()
#  print(f'Média: {media}')
#  print(f'Moda: {moda}')
#  print(f'Mediana: {mediana}'}

#DESVIO PADRÃO: indica uma faixa de afastamento em relação à média que contém a maior parte dos dados, comando std().
# Variância por σ2: é a média dos quadrados dos desvios de cada dado em relação à média.
x={'Peso':[48.8, 48.9, 49.0, 49.1, 49.2, 49.3, 49.5, 49.7,
49.7, 49.7, 49.8, 50.0, 50.1, 50.1, 50.2, 50.2, 50.4, 50.6,
50.8, 50.9]}
p=pd.DataFrame(x)
desviopadrao=p['Peso'].std() #comando para ter o desvio padrão
print(f'Desvio padrão: {desviopadrao}')

#PROBABILIDADE:
#EXEMPLO: projetor com vida útil de 5000 horas com desvio padrão de 300 horas. probabilidade de
# que um projetor selecionado ao acaso tenha vida útil entre 5000 e 5500 horas.
import scipy.stats #funções de distribuições, probabilidades, testes estatísticos, etc.
media= 5000  # valor da média da sua distribuição normal.
desvio_padrao= 300  # desvio padrão da distribuição normal.
X= 5500 # valor para o qual você quer calcular a probabilidade acumulada.

# valores de X acima da média
p=scipy.stats.norm(media,desvio_padrao).cdf(X)-0.5
# scipy.stats.norm(media, desvio_padrao): Cria uma distribuição normal com aquela média e desvio padrão.
# .cdf(X): Qual a probabilidade de um valor ser menor ou igual a X?
# - 0.5: Isso subtrai 0.5, que é a probabilidade acumulada até a média.
print(p)

# valores de X abaixo da média
# p=0.5-scipy.stats.norm(media,desvio_padrao).cdf(X)

#ESTATISTICA: EXEMPLO: estudo realizado a 20000 pessoas e que apenas algumas delas fará parte de forma
#efetiva, qual é o tamanho da amostra considerando uma margem de erro de 2%?
from math import ceil #função ceil (teto), que arredonda qualquer número para cima.
N = 20000 
e = 0.02
n = ceil(N / (1 + N * e**2))
print(f'Tamanho da amostra: {n}')