import random
n = int(input('Digite um número entre 1 e 5: '))
lista = [1, 2, 3, 4, 5]
nrandom = random.choice(lista)
print('O número selecionado foi {}.'.format(nrandom))
if n == nrandom:
    print('Parabéns! Você acertou.')
else:
    print('Que pena, você não acertou.')