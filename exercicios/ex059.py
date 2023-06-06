#MENU DE OPÇÕES:
from time import sleep
escolha = 0
num1 = int(input('\033[1;30mPrimeiro número: '))
num2 = int(input('Segundo número: \033[m'))
while escolha != 7:
    print('\033[1;30m=\033[m' * 28)
    print('\033[1;30mSuas opções:\033[m\n\033[1;36m[ 1 ] Adição\n[ 2 ] Subtração\n[ 3 ] Multiplicação\n[ 4 ] Divisão\n[ 5 ] Maior número\n[ 6 ] Novos números\n[ 7 ] Fechar programa\033[m')
    print('\033[1;30m=\033[m' * 28)
    escolha = int(input('\033[1;30mSua escolha: \033[m'))
    if escolha == 1:
        adicao = num1 + num2
        print('\033[1;36mA adição de {} + {} é igual a {}.\033[m'.format(num1, num2, adicao))
        sleep(2)
    elif escolha == 2:
        subtracao = num1 - num2
        print('\033[1;36mA subtração de {} - {} é igual a {}.\033[m'.format(num1, num2, subtracao))
        sleep(2)
    elif escolha == 3:
        multiplicacao = num1 * num2
        print('\033[1;36mA multiplicação de {} * {} é igual a {}.\033[m'.format(num1, num2, multiplicacao))
        sleep(2)
    elif escolha == 4:
        divisao = num1 / num2
        print('\033[1;36mA divisão de {} por {} é igual a {}\033[m'.format(num1, num2, divisao))
        sleep(2)
    elif escolha == 5:
        if num1 > num2:
            print('\033[1;36mO maior número entre {} e {} é o {}.\033[m'.format(num1, num2, num1))
            sleep(2)
        elif num2 > num1:
            print('\033[1;36mO maior número entre {} e {} é o {}.\033[m'.format(num1, num2, num2))
            sleep(2)
        else:
            print('\033[1;36mOs dois números tem o mesmo valor.\033[m')
            sleep(2)
    elif escolha == 6:
        print('\033[1;30mInforme os novos valores:\033[m')
        num1 = int(input('\033[1;30mPrimeiro número: '))
        num2 = int(input('Segundo número: \033[m'))
    elif escolha == 7:
        print('\033[1;31mFinalizando programa.... Volte sempre.\033[m')
        sleep(2)
        break
    elif escolha > 6:
        print('\033[1;31mNúmero inválido, tente outra vez.\033[m')
        sleep(2)
