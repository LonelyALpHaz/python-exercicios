#CONTADOR DE UNIDADES, DEZENAS, CENTENAS E MILHARES:
n = int(input('Digite um número: '))
uni = n // 1 % 10
dez = n // 10 % 10
cen = n // 100 % 10
mil = n // 1000 % 10
print('Analisando o número {}, podemos saber que nele há:'.format(n))
print('Unidades: {}'.format(uni))
print('Dezenas: {}'.format(dez))
print('Centenas: {}'.format(cen))
print('Milhares: {}'.format(mil))
