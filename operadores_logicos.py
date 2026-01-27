#proposição p, sua negação é preposição ~p ou p'
#proposição verdadeira: representado por V ou 1
#Proposição falsa: representado por F ou 0
print('--------- Cadastro de notas ---------')
rg=input('RG (s/n): ')
cpf=input('CPF (s/n): ')
if rg=='s' or cpf=='s': #proposições p e q. conectivo ou = OR, representado por p v q ou p + q. DISJUNÇÃO
  print('Entrada liberada.')
else:
  print('Entrada não autorizada.')

idadeAna = 32
idadeBeatriz = 29
print(idadeAna >= idadeBeatriz)
print(idadeAna < idadeBeatriz)
print( not(idadeAna<idadeBeatriz))
p = True
print(p)
print(not p)
M=float(input('Média obtida: '))
F=float(input('Total de faltas: '))
if M>=70 and F<=20: #proposições p e q. conectivo e = AND, representado por p ^ q ou p.q. CONJUNÇÃO
  print('Aprovado')
else:
  print('Reprovado')
# NAND (Not AND): É o oposto da operação E (AND). Tudo que for verdadeiro no AND será falso no NAND. A↑B=¬(A∧B)
# NOR (Not OR): É o oposto da operação OU (OR). Tudo que for verdadeiro será falso no NOR. A↓B=¬(A∨B)
# XOR (Exclusive OR): verdadeiro apenas quando uma das entradas é verdadeira, mas não ambas. A⊕B=(A∨B)∧¬(A∧B)
#Representa isso “ou um ou outro, mas não os dois”. Verdadeiro quando A e B são diferentes e falso quando for iguais.
# CONDICIONAL (→): A→B, A condicional só é falsa quando a primeira proposição (A) é verdadeira e a segunda (B) é falsa.
# Em todos os outros casos, ela é verdadeira.
# BICONDICIONAL (↔): A↔B, A bicondicional é verdadeira quando A e B têm o mesmo valor lógico
#(ambos verdadeiros ou ambos falsos). Se forem diferentes, é falsa.

