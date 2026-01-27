# Cifra de César, a vira d, b vira e e assim por diante.
from string import ascii_uppercase #Importa a constante com todas as letras maiúsculas:

a = list(ascii_uppercase) #Transforma as letras em uma lista:['A', 'B', ..., 'Z']
m = input('Digite a mensagem: ')
m = m.upper() #Transforma tudo em maiúsculo, pois a cifra usa só letras maiúsculas.
mc = ""  # Cria a string onde será armazenada a mensagem criptografada.
#as próximas linhas servem para descobrir a posição numérica da letra no alfabeto e depois deslocá-la 3 posições
# Mesmo sendo letras, você ainda precisa saber: A = 0, B = 1 ...
for l in m: #Percorre letra por letra da mensagem.
  i=ord(l)-65 #ord(l) pega o código ASCII da letra. ord('B') = 66, 'B' = 66 - 65 = 1. converte a letra em (0 a 25)
  if l in a: #Verifica se a letra é do alfabeto (ignora números, acentos, espaços etc).
    mc+=a[(i+3)%26] #Aplica a Cifra de César (+3), com módulo para voltar ao A caso passe do Z.
  else:
    l
print(f'Mensagem criptografada: {mc}')
#CASO quisesse fazer o código invertido, digitar a mensagem criptografada e sair a origina.
#seria necessário trocar o que tá escrito nos prints e a linha m+=a[(i–3)%26]

import rsa #biblioteca RSA
chavepublica,chaveprivada=rsa.newkeys(512) #rsa.newkeys() gera as chaves pública e privada
m=input('Digite a mensagem: ') #mensagem a ser criptografada e em seguida descriptografada
mc=rsa.encrypt(m.encode(),chavepublica) #mensagem criptografada por meio da chave pública será armazenada em mc:
print("Mensagem original:", m) # mensagem original e a mensagem criptografada
print("Mensagem criptografada:", mc)
md=rsa.decrypt(mc,chaveprivada).decode() #mensagem descriptografada por meio da chave privada será armazenada em md:
print("Mensagem descriptografada:", md) #mensagem descriptografada

#Importar as funções necessárias:
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

#Gerar as chaves pública e privada nos arquivos "destinatario.pem" e "chavePrivada.pem", respectivamente:
chave=RSA.generate(2048)
chavePrivada=chave.export_key()
arquivoDeSaida=open("chavePrivada.pem", "wb")
arquivoDeSaida.write(chavePrivada)
arquivoDeSaida.close()
chavePublica=chave.publickey().export_key()
arquivoDeSaida=open("destinatario.pem", "wb")
arquivoDeSaida.write(chavePublica)
arquivoDeSaida.close()

#Cifrar o texto utilizando chave da sessão cifrada com chave pública RSA:
texto=input("Digite o texto a ser cifrado: ").encode("utf-8")
arquivoDeSaida=open("textoCifrado.bin", "wb")
chaveDoDestinatario=RSA.import_key(open("destinatario.pem").read())
chaveDaSessao=get_random_bytes(16)

#Cifrar a chave da sessão com a chave pública RSA
cifraRSA=PKCS1_OAEP.new(chaveDoDestinatario)
chaveEncaminhadaDaSessao=cifraRSA.encrypt(chaveDaSessao)

#Cifrar o texto com a chave da sessão:
cifraAES=AES.new(chaveDaSessao, AES.MODE_EAX)
textoCifrado, tag = cifraAES.encrypt_and_digest(texto)
[arquivoDeSaida.write(x) for x in (chaveEncaminhadaDaSessao, cifraAES.nonce, tag, textoCifrado)]
arquivoDeSaida.close()
print("Texto criptografado:", textoCifrado)

#Destinatário possui a chave privada RSA para ler o texto:
arquivoDeEntrada=open("textoCifrado.bin", "rb")
chavePrivada=RSA.import_key(open("chavePrivada.pem").read())
chaveEncaminhadaDaSessao, nonce, tag, textoCifrado = \
[arquivoDeEntrada.read(x) for x in (chavePrivada.size_in_bytes(), 16, 16, -1)]
arquivoDeEntrada.close()

#Decodificar a chave da sessão com a chave privada RSA:
cifraRSA=PKCS1_OAEP.new(chavePrivada)
chaveDaSessao=cifraRSA.decrypt(chaveEncaminhadaDaSessao)

#Decodificar o texto com a chave da sessão:
cifraAES=AES.new(chaveDaSessao, AES.MODE_EAX, nonce)
texto=cifraAES.decrypt_and_verify(textoCifrado, tag)
print("Texto descriptografado:", texto.decode("utf-8"))