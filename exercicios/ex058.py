#JOGO DA ADIVINHAÇÃO V2.0:
from time import sleep
import random
contador = 0
jogador = 0
print('\033[1;33m-\033[m' * 70)
print('\033[1;34mVou pensar em um número entre 1 e 10 e você terá que acertar qual foi.\nAo final informarei o número de tentativas.\033[m')
print('\033[1;33m-\033[m' * 70)
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = random.choice(numeros)
while jogador != num:
    contador += 1
    jogador = int(input('Digite um número: '))
    print('\033[1;35mPROCESSANDO...\033[m')
    sleep(1)
    if jogador < num:
      print('Um pouco mais... Tente mais uma vez.')
    elif jogador > num:
        print('Um pouco menos... Tente mais uma vez.')
    elif jogador == num:
        print('\033[1;32mVocê acertou! O número que eu pensei foi {}. Você tentou {} vezes até acertar.\033[m'.format(num, contador))
        break
