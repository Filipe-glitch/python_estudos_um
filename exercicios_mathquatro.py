# MATRIZES
#
#    ( 400 10 )
#F1 =( 480 12 )
#    ( 600 15 )
#              ( 31 11 )
#         F2 = ( 37 11 )
#              ( 48 11 )

# indústria de cadeiras gamer possui três modelos denominados de A, B e C, e possui duas fábricas chamadas de F1 e F2.
# fábrica F1, são produzidas as peças e, na fábrica F2, é feita a montagem das cadeiras.
# produção: A=400, B=480 e C=600 ; transporte: A=10, B=12, C=15
# Montagem: A=31, B=37 e C=48 ; transporte: A=11, B=11, C=11
# determine os custos totais de produção e de transporte referentes a cada modelo de cadeira gamer
import numpy as np
F1=np.array([[400, 10],[480, 12],[600, 15]])
F2=np.array([[31, 11],[37, 11],[48, 11]])
CustoTotal=F1+F2
print(CustoTotal)

#HOUVE AUMENTO DE 10% sobre os custos de fabricação das peças e sobre os respectivos custos de transporte.
# QUAIS serão os valores depois do aumento
F1=np.array([[400, 10],[480, 12],[600, 15]])
F1=1.1*F1
print(F1)
#MULTIPLICAÇÃO DE MATRIZES
A=np.array([[3, 1, 3],[6, 5, 5]])
B=np.array([[100, 50],[50, 100],[50, 50]])
C=np.matmul(A, B) # multiplicador de matrizes
print(C)

#FUNÇÕES
#Empresa que faz teclados, custo unitário da produção é 28 e mensalmente x unidades são produzidas
# custo mensal de produção C, C(x) = 28x
import matplotlib.pyplot as plt
# pyplot é usado para fazer gráficos.
# as plt cria um apelido: agora você chama as funções usando plt.
x=np.linspace(0, 10, 100) #Isso cria 100 números igualmente espaçados entre 0 e 10.
# incluindo os dois extremos. É como se você criasse [0.00, 0.10, 0.20, ..., 9.90, 10.00]
y=28*x
plt.plot(x,y) # desenha gráficos, recebe os pontos x e y
plt.show() #exibe o gráfico na tela, Abre a janela do gráfico

#se fosse produzida 2334. x = 2344, y = 28 * x , print(y)

#FUNÇÃO QUADRATICA
# lucro mensal de um determinado estacionamento com o preço cobrado por hora é L(x)=-340x2+5700x-9500
# x = preço por hora, L = lucro mensal. Contrua o gráfico
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 16, 100)
y = -340 * x ** 2 + 5700 * x - 9500
plt.plot(x, y)
plt.show()
# Preço ótimo: R$ 8,38  conceito de Xv = -b/2a
 # Lucro máximo: R$ 14.389,71 conceito de Yv= -delta/(4 * a)

