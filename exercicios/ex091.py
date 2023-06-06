#JOGANDO DADOS EM PYTHON:
from random import randint
from time import sleep
from operator import itemgetter
pos = contador = 0
dados = {}
ranking = []
#SORTEANDO NÚMEROS:
dados['jogador 1'] = randint(1, 6)
ranking.append(dados['jogador 1'])
dados['jogador 2'] = randint(1, 6)
ranking.append(dados['jogador 2'])
dados['jogador 3'] = randint(1, 6)
ranking.append(dados['jogador 3'])
dados['jogador 4'] = randint(1, 6)
ranking.append(dados['jogador 4'])
#MAIOR NÚMERO EM ORDEM:
print('\033[1;36m-\033[m' * 35)
for k, v in dados.items():
    print(f'   O \033[1;36m{k}\033[m tirou {v} no dado.')
    sleep(0.8)
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print('\033[1;36m-\033[m' * 35)
for i, v in enumerate(ranking):
    print(f' {contador + 1}° Lugar: \033[1;36m{v[0]}\033[m com {v[1]} pontos.')
    contador += 1
    sleep(0.8)
print('\033[1;36m-\033[m' * 35)
