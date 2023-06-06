#CONTADOR COM FUNÇÕES:
from time import sleep
#CONTADOR DE 0 A 10:
def contador10():
    print('-' * 47)
    print(f'{"CONTADOR DE 0 A 10:":^47}\n{"A contagem vai de 0 a 10 com o passo de 1 em 1:":^47}')
    for cont in range(0, 11):
        print(f'  \033[1;34m{cont}\033[m', end=' ')
        sleep(0.5)
    print()


#CONTADOR DE 10 A 0:
def contador0():
    print('-' * 47)
    print(f'{"CONTAGEN DE 10 A 0:":^47}\n{"A contagem vai de 10 a 0 com o passo de 2 em 2:":^47}')
    for cont in range(10, -1, -2):
        print(f'     \033[1;34m{cont}\033[m', end=' ')
        sleep(0.5)
    print()


#CONTADOR PERSONALIZADO:
def contador(i, f, p):
    contlinha = 0
    print('-' * 47)
    print(f'{"CONTADOR PERSONALIZADO:":^47}\n{f"A contagem vai de {i} a {f} com passo de {p} em {p}:":^47}')
    if i > f and p > 0:
        p *= -1
    elif f > i and i > 0 and p < 0:
        f *= -1
    elif f > i and i < 0 and p < 0:
        print(f'\033[1;31m{"ERRO! O início e o passo são negativos!":^47}\n'
              f'{"Não há como chegar em um número positivo.":^47}\033[m')
    elif p == 0:
        p = 1
    c = i
    while c <= f:
        print(f'\033[1;34m  {c}\033[m', end=' ')
        c += p
        contlinha += 1
        if contlinha >= 10:
            contlinha = 0

            print('\n', end='')
        sleep(0.5)
    print()


#COMANDO PRINCIPAL:
i = int(input('- Início: '))
f = int(input('- Fim:    '))
p = int(input('- Passo:  '))
contador10()
contador0()
contador(i, f, p)
