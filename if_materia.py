#Ifs separados, quando mais de uma condição pode ser verdadeira ao mesmo tempo e você quer que todas sejam verificadas.
idade = 25
salario = 4000
if idade >= 18:
    print("Maior de idade")
if salario > 3000:
    print("Ganha bem") #esse vai sair também mesmo que o primeiro já tenha saído

#If + elif + else, quando apenas uma condição deve ser executada.
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
if num1 > num2:
    print('O primeiro número é maior que o segundo')
elif(num1 == num2): #os parentêses são opcionais
    print('Os dois números são iguais') #equivale ao else if no C#
else:
    print('o segundo número é maior que o primeiro')

#Ifs aninhados, quando precisa checar uma condição dentro de outra(condições dependentes).
idade = 20
tem_carteira = True
if idade >= 18:
    if tem_carteira:
        print("Pode dirigir")
    else:
        print("Precisa ter carteira")
else:
    print("Menor de idade")

# not
x = True
y = False
print(not x) #not True = False
print(not y) #not False = True

# and
x = True
y = False
print(x and y)

if(min(12, 45, 32) < 30): #MMC
    print('É verdadeiro')
