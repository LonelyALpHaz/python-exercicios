#JOGO DA ADIVINHAÇÃO V1.0:
from time import sleep
import random
print('\033[1;33m-=\033[m' * 36)
print('\033[1;34mVou pensar em um número entre 0 e 5, tente adivinhar qual é esse número.\033[m')
print('\033[1;33m-=\033[m' * 36)
n = int(input('\033[1;30mDigite um número entre 0 e 5: \033[m'))
lista = [0, 1, 2, 3, 4, 5]
nrandom = random.choice(lista)
print('\033[1;35mPROCESSANDO...\033[m')
sleep(3)
print('\033[30mO número selecionado foi \033[1;33m{}\033[m.\033[m'.format(nrandom))
if n == nrandom:
    print('\033[1;32mParabéns! Você conseguiu me vencer.\033[m'.format(nrandom))
else:
    print('\033[1;31mQue pena, você não acertou. Eu pensei no número {} e não no {}.\033[m'.format(nrandom, n))
