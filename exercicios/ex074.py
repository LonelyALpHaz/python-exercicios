#MAIOR E MENOR VALOR EM TUPLA:
from random import choice
contador = maior = menor = 0
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print('Os valores sorteados foram: ', end='')
while contador < 5:
    nrandom = choice(numeros)
    contador += 1
    print(f'{nrandom}', end=' ')
    #MAIOR NÚMERO:
    numlist = [nrandom]
    for nrandom in numlist:
        if maior == 0 or nrandom > maior:
            maior = nrandom
        if menor == 0 or nrandom < menor:
            menor = nrandom
    if contador == 5:
        print(f'\nO maior número é {maior}.\nO menor número é {menor}.')
