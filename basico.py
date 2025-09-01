# atalho para deixar em comentário, marque o que quiser comentar e aperte control + /
print('Hello World !')
print('2*9 = ')
print(2*9)

print('2'+ '3')
print('olá, ' + 'mundo') #ou print('olá,','mundo ')
print(2 + 3 * 3)
print(4**2 / 3) #será feito da esquerda para a direita(mesma ordem de prioridade)
print(( 9 ** 2 + 2 ) * 6 - 1)

#operações aritméticas
# soma(+), subtração(-)	,Divisão(/), (//)Divisão inteira,(%,resto da divisão),(**)Exponenciação

#operações de comparação
# (==) Igual, (!=) Diferente de, (>) Maior que, (<)	Menor que,(>=) Maior ou igual a,(<=) Menor ou igual a.

# Dicas para nomes de variáveis
# 2nota(não iniciar com número ou caracteres especiais, não use acentos e letras maiusculas, inicie com letra ou _)
#não colocar espaços entre a variavel

a = 1 # a recebe 1
b = 3
resposta = a == b
print(resposta)

resposta_2 = a != b
print (resposta_2)

#tamanho( quantidade de caracteres)
s8 = 'logica de programacao e algoritmos'
tamanho = len(s8)
print(tamanho)

nome = 'filipe'
boll = len(nome) <= 15 # len determina o número de itens em um objeto
print(nome)

# Quando queremos o valor absoluto de uma conta
print(abs(54 - 57)) # abs faz o valor ficar positivo, terá 3 como resultado ao invés de -3
print(min(12, 36, 847)) #min pega o menor valor dos números entre parentêses.
