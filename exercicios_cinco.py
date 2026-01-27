import pandas as pd
x ={'pesos':[35, 34, 26, 32, 37, 28, 27, 33, 36, 32.]}
p = pd.DataFrame(x)
media=p['pesos'].mean()
moda=p['pesos'].mode()
mediana=p['pesos'].median()
print(f'Moda: {moda}')
print(f'Média: {media}')
print(f'Mediana: {mediana}')
p=pd.DataFrame(x)
desviopadrao = p['pesos'].std()
print(f'Desvio padrão: {desviopadrao}')

from math import ceil
N=200000
e=0.04
n=ceil(N/(1+N*e**2))
print(f'Tamanho da amostra: {n}')