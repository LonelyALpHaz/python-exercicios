def fatorial(num=1, show=False):
    """
    --------------------------------------------
    Utilidade: Calcular o fatorial de um número.
    --------------------------------------------
    :param num: = Número que será utilizado;
    :param show: = 'False' p/ não mostrar o
    cálculo, 'True' p/ mostrar o cálculo;

    OBS: :param show: predefinido no 'False'.
         :param num: predefinido em '1'.
    --------------------------------------------
                 Criado por ADF.
    --------------------------------------------
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
    if show:
        print('\033[1;34m-\033[m' * 35)
        for cont in range(num, 0, -1):
            print(cont, end='')
            if cont > 1:
                print('  x  ', end='')
            else:
                print('  =  ', end='')
        print(f'{f}')
        print('\033[1;34m-\033[m' * 35)
    if not show:
        print('\033[1;34m-\033[m' * 35)
    print(f'   O fatorial de {num} é igual a {f}')
    print('\033[1;34m-\033[m' * 35)


fatorial(5, True)
