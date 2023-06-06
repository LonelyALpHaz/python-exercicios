#NOMES RANDOMICOS:
import random
a = str(input(print('Digire o primeiro nome: ')))
b = str(input(print('Digite o segundo nome: ')))
c = str(input(print('Digite o terceiro nome: ')))
d = str(input(print('Digite o quarto nome: ')))
lista = [a, b, c, d]
r = random.choice(lista)
print('O nome sorteado foi: {}.'.format(r))
