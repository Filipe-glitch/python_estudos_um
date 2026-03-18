print('Bem-vindo a loja de Filipe Rocha')
valorDoPedido = int(input('Digite o valor do pedido: '))
quantidadeParcelas = int(input('Digite a quantidade de parcelas: '))
if quantidadeParcelas < 4:
    juros = 0
elif quantidadeParcelas >= 4 and quantidadeParcelas < 6:
    juros = 4
elif quantidadeParcelas >= 6 and quantidadeParcelas < 9:
    juros = 8
elif quantidadeParcelas >= 9 and quantidadeParcelas < 13:
    juros = 16
else:
    juros = 32

valorDaParcela = valorDoPedido * (1 + juros / 100) / quantidadeParcelas
valorTotalParcelado = valorDaParcela * quantidadeParcelas
print(f'O valor das parcelas é de: R${valorDaParcela:.2f}')
print(f'O valor total parcelado é de: R${valorTotalParcelado:.2f}')
