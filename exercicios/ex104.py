def leiaint(*num):
    while True:
        n = str(input('Digite um número: '))
        while not n.isnumeric():
            print('-' * 35)
            print('\033[1;31mComando inválido, digite um número.\033[m')
            n = str(input('Digite um número: '))
        if n.isnumeric():
            print('-' * 35)
            print(f'     \033[1;34mVocê digitou o número {n}.\033[m')
            print('-' * 35)
            break


leiaint()
