#PEDRA, PAPEL E TESOURA:
from time import sleep
from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('=' * 32)
print('Escolha uma das opções abaixo:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA')
print('=' * 32)
jogador = int(input('Qual a sua escolha? '))
print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Pô!!!')
sleep(0.5)
print('O jogador jogou {}.\nO computador jogou {}.'.format(itens[jogador], itens[computador]))
if computador == 0:
    if jogador == 0:
        print('Não houve vencedor, pois deu EMPATE.')
    elif jogador == 1:
        print('Você VENCEU! Parabéns.')
    elif jogador == 2:
        print('Você PERDEU, tente novamente.')
if computador == 1:
    if jogador == 0:
        print('Você PERDEU, tente novamente.')
    elif jogador == 1:
        print('Não houve vencedor, pois deu EMPATE.')
    elif jogador == 2:
        print('Você VENCEU! Parabéns.')
if computador == 2:
    if jogador == 0:
        print('Você VENCEU! Parabéns.')
    elif jogador == 1:
        print('Você PERDEU, tente novamente.')
    elif jogador == 2:
        print('Não houve vencedor, pois deu EMPATE.')
