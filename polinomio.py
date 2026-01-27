from scipy.interpolate import *
x=[]
y=[]
p=lagrange(x, y)
print(p)

#polinômio que interpola os pontos A(4, 2), B(7, -1), C(10, 12) e D(11,15)
from scipy.interpolate import *
x=[4, 7, 10, 11]
y=[2, -1, 12, 15]
p=lagrange(x, y)
print(p) #-0.1746 x3 + 4.556 x2 - 34.87 x + 79.78

#concentração de partículas de um poluente em uma região está se alterando com o passar do tempo.
#Dados: 1 ano - 80, 2 ano - 95, 3 ano - 110, 4 ano - 122
from scipy.interpolate import *
x=[1, 2, 3, 4] # polinômio que interpola esses dados
y=[80, 95, 110, 122]
p=lagrange(x, y)
print(p) #p(x)=-0,5x3 + 3x2 + 9,5x + 68.

#Aritmetica modular:
n = (3 + 4) % 5 # % é o resto da divisão 7 / 5
# trabalhamos com um número finito de números ou de letras

#aritmetica modular relacionada as letras do alfabeto é mod 26 pois há 26 letras no alfabeto

#considere os números 0, 1, 2, 3, 4, temos um conjunto com 5 elementos, operações são mod 5.
# (3+4) mod 5 = 7 mod 5 = 2 , 2 pois é como se desse uma volta 3 + 2 = 5, reinicio 0 + 2 = 2.
#note que 7 % 5 = 2