#FICHA DO JOGADOR:
def ficha(jogador, gols):
    print('-' * 52)
    if jogador == '':
        jogador = '<desconhecido>'
    if jogador == '<desconhecido>':
        print(f'O jogador \033[1;31m{jogador}\033[m fez {gols} gol(s) no campeonato.')
    else:
        print(f'   O jogador \033[1;34m{jogador}\033[m fez {gols} gol(s) no campeonato.')
    print('-' * 52)


nome = str(input('Nome do jogador: '))
pontos = str(input(f'Quantidade de gols: '))
if pontos.isnumeric():
    pontos = int(pontos)
else:
    pontos = 0
ficha(nome, pontos)
