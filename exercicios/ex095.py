#CADASTRO DE JOGADOR DE FUTEBOL V2.0:
from time import sleep
soma = 0
jogador = dict()
gols = list()
time = list()
while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for p in range(1, jogador['partidas'] + 1):
        gols.append(int(input(f' - Quantos gols {jogador["nome"]} fez na {p}ª partida? ')))
        jogador['gols'] = gols.copy()
        soma = sum(gols)
        jogador['total'] = soma
    time.append(jogador.copy())
    continuar = str(input('Deseja continuar [S/N]? ').upper()).strip()[0]
    if continuar == 'N':
        break
print('\033[1;37m-\033[m' * 50)
print('\033[1;36mN° |     NOME     |     GOLS     |     TOTAL     |\033[m')
for pos, x in enumerate(time):
    print(f'\033[1;37m{pos:<2} \033[1;36m{time[pos]["nome"]:^7}', end='')
    print(f'          {time[pos]["gols"]} {time[pos]["total"]:>13}\033[m')
print('\033[1;37m-\033[m' * 50)
while True:
    for pos, x in enumerate(time):
        escolha = int(input('Digite o N° do jogador para saber seus dados (999 para interromper): '))
        if escolha == pos:
            print('\033[1;36m-\033[m' * 60)
            print(f'Jogador: \033[1;36m{time[pos]["nome"]}\033[m; Partidas: \033[1;36m{time[pos]["partidas"]}\033[m;'
                  f' Gols: \033[1;36m{time[pos]["gols"]}\033[m; Total: \033[1;36m{time[pos]["total"]}\033[m')
            print('\033[1;36m-\033[m' * 60)
            sleep(3)
        if escolha == 999:
            break
    print('\033[1;31mFinalizando programa...\033[m')
    sleep(3)
    print('Volte sempre.')
    break

