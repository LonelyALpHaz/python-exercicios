#EMBARALHADOR RANDOMICO:
from random import shuffle
a = str(input('Digite o primeiro nome: '))
b = str(input('Digite o segundo nome: '))
c = str(input('Digite o terceiro nome: '))
d = str(input('Digite o quarto nome: '))
lista = [a, b, c, d]
r = shuffle(lista)
print('A ordem sorteada é: ')
print(lista)
