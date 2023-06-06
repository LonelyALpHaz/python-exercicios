#PALPITES PARA A MEGA-SENA:
resultado = []
cont = 0
from time import sleep
from random import randint
resp = int(input('Quantos jogos eu devo sortear? '))
for s in range(0, resp):
    for n in range(0, 6):
        nrandom = randint(0, 60)
        cont += 1
        print(nrandom, end=' ')
        if cont >= 6:
            cont = 0
            print('\n', end='')
