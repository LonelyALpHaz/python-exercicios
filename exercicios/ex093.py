#CADASTRO DE JOGADOR DE FUTEBOL V1.0:
contador = soma = 0
gols = []
jogador = {'nome': None, 'partidas': 0, 'gols': gols, 'total': 0}
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(1, jogador['partidas'] + 1):
        jogador['gols'] = int(input(f'Quantos gols {jogador["nome"]} fez na {c}ª partida? '))
        gols.append(jogador['gols'])
        print(gols)
        soma += jogador['gols']
        jogador['total'] = soma
        contador += 1
    if contador == jogador['partidas']:
        jogador['gols'] = gols
        #DICIONÁRIO 1.0:
        print('\033[1;36m-\033[m' * 65)
        print(jogador)
        print('\033[1;36m-\033[m' * 65)
        #DICIONÁRIO 2.0:
        print(f'Nome: \033[1;36m{jogador["nome"]}\033[m.\n'
              f'Gols: \033[1;36m{gols}\033[m.\n'
              f'Total de pontos: \033[1;36m{jogador["total"]}\033[m.')
        #DICIONÁRIO 3.0:
        print('\033[1;36m-\033[m' * 65)
        print(f'O jogador \033[1;36m{jogador["nome"]}\033[m jogou \033[1;36m{jogador["partidas"]}\033[m partidas:')
        for pos, x in enumerate(gols):
            print(f' -> Na \033[1;36m{pos + 1}ª\033[m partida ele fez \033[1;36m{gols[pos]}\033[m gols.')
        print(f' -> Total de pontos: \033[1;36m{jogador["total"]}\033[m')
        print('\033[1;36m-\033[m' * 65)
        break
