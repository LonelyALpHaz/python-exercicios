#JOGO DO ÍMPAR E PAR:
soma = resultado = contador = 0
from random import choice
while True:
    print('\033[1;36m-\033[m' * 47)
    jogador = int(input('\033[1;37mEscolha um número: \033[m'))
    escolha = str(input('\033[1;37mÍmpar ou Par? [I/P]: \033[m').upper())
    if escolha != 'P' and escolha != 'I':
        print('\033[1;31mComando inválido. Utilize apenas "P" ou "I".\033[m')
        break
    print('\033[1;36m-\033[m' * 47)
    lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    computador = choice(lista)
    soma = jogador + computador
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    print(f'\033[1;37mVocê jogou {jogador} e o computador {computador}.\nA soma entre esses dois números é igual a {soma}.\033[m')
    if escolha == 'P' and resultado == 'PAR':
        print(f'\033[1;32m{soma} é {resultado} e a sua escolha foi PAR. Você GANHOU!\033[m')
        contador += 1
    elif escolha == 'P' and resultado == 'ÍMPAR':
        print(f'\033[1;31m{soma} é {resultado} e a sua escolha foi PAR. Você PERDEU!\033[m')
        print(f'\033[1;37mVocê ganhou {contador} vezes.\033[m')
        print('\033[1;36m-\033[m' * 47)
        break
    elif escolha == 'I' and resultado == 'PAR':
        print(f'\033[1;31m{soma} é {resultado} e a sua escolha foi ÍMPAR. Você PERDEU!\033[m')
        print(f'\033[1;37mVocê ganhou {contador} vezes.\033[m')
        print('\033[1;36m-\033[m' * 47)
        break
    elif escolha == 'I' and resultado == 'ÍMPAR':
        print(f'\033[1;32m{soma} é {resultado} e a sua escolha foi ÍMPAR. Você GANHOU!\033[m')
        contador += 1
