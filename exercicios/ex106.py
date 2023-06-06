def pyhelp():
    resp = 0
    while resp != 'FIM':
        print('\033[1m-\033[m' * 57)
        print(f'\033[1;36m{"Sistema Interativo PyHelp":^57}\033[m')
        print('\033[1m-\033[m' * 57)
        resp = str(input('\033[1;36mDigite um comando para ver seu manual ("fim" para parar): \033[m').upper())
        if resp == 'FIM':
            print('\033[1;31mFinalizando PyHelp...\n'
                  '   Volte sempre!\033[m')
            break
        else:
            resp = resp.lower()
        print('\033[1m-\033[m' * 57)
        print(f'{help(resp)}')


pyhelp()
