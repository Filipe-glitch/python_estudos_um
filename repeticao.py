#WHILE(enquanto)
x = 1
while (x <= 5):
  print(x)
  x = x + 1 #não se esqueça da indentação
# caso o x = x + 1 fique de fora, ele vai imprimir o 1 infinitamente
# Variável de controle : Contagem do número de vezes que o laço está sendo executado.
# Contadoras : Acrescentam valores constantes em uma variável.
# Acumuladoras : acumulam totais como um somatório.

#Operadores especiais de atribuição
# +=, x += 1, x = x + 1
# -=, x -= 1, x = x - 1
# *=, x *= 1, x = x * 1
# /=, x /= 1, x = x / 1
# **=, x **= 1, x = x ** 1
# //=, x //= 1, x = x // 1

#break : serve para encerrar um laço de repetição abruptamente
#While True : a condição sempre é verdadeira, só para se tiver um break ou se o programa for interrompido
#Continue: retornar ao laço ao início a qualquer momento.
while True:
  nome = input('Qual o seu nome?')
  if (nome != 'Filipe' or 'filipe'):
    continue # volta para inicio do laço
  senha = input('Qual a sua senha?')
  if (senha == '1234abM'):
    break # encerra o laço
print('Acesso concedido.')

#Truthy e Falsey: dados não booleanos. String vazia e numero inteiro 0 são falsey.
# o Python precisa avaliar se esse valor é considerado verdadeiro ou falso mesmo que não sejam booleanos.
nome = ''
while not nome:
  # encerra o laço quando nome não estiver vazio
  nome = input('Digite seu nome:')
valor = int(input('Digite um número qualquer:'))
if valor: #Equivalente if valor != 0:
  print('Você digitou um valor diferente de zero.')
else:
  print('Você digitou zero.')

#FOR
# Estrutura : for <var> in range(<inicial>, <final>, <incremento/decremento>):
frase = "Lógica de Programação e Algoritmos"
for i in range(0, len(frase), 1):
  print(frase[i])

frase2 = "Lógica de Programação e Algoritmos"
for i in range(0, len(frase), 1):
  print(frase2[i], end="")
#o end faz com que ele fique na mesma linha tudo que for digitado

for i in range(10,0,-2):
  print(i)
# a contagem vai de 10 a 0 contando de -2 em -2

u = 1
for _ in range(3):
    for _ in range(3):
        print(i, end=' ')
        i+=1
    print() #matriz
