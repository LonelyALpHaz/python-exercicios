#CONVERSOR DE BASES NUMÉRICAS:
n = int(input('Digite um número inteiro: '))
print('_' * 32)
print('Escolha a base de conversão:\n[ 1 ] Converter para BINÁRIO\n[ 2 ] Converter para OCTAL\n[ 3 ] Converter para HEXADECIMAL')
print('_' * 32)
escolha = int(input('Qual a sua escolha? '))
bin = bin(n)
oct = oct(n)
hexa = hex(n)
if escolha == 1:
    print('A conversão de {} para BINÁRIO é igual a: {}.'.format(escolha, bin[2:]))
elif escolha == 2:
    print('A conversão de {} para OCTAL é igual a: {}'.format(escolha, oct[2:]))
elif escolha == 3:
    print('A conversão de {} para HEXADECIMAL é igual a: {}'.format(escolha, hexa[2:]))
elif escolha != 1 and escolha != 2 and escolha != 3:
    print('Comando inválido, você deve escolher um número entre 1 e 3 de acordo com a base de conversão.')
