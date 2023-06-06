#EXTRAÍNDO VALORES DE UMA LISTA:
numlist = list()
contador = 0
while True:
    num = int(input('Digite um número: '))
    numlist.append(num)
    continuar = str(input('Deseja continuar [S/N]? ').upper()).strip()[0]
    contador += 1
    if continuar == 'N':
        numlist.sort(reverse=True)
        print('-' * 50)
        print(f'Você digitou {contador} números.')
        print(f'Os valores em ordem decreescente são: {numlist}')
        if 5 in numlist:
            print('O número 5 está na lista.')
        else:
            print('O número 5 não está na lista.')
        print('-' * 50)
        break
