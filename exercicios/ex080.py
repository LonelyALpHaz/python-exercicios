#LISTAS ORDENADAS SEM SORT:
numlist = list()
for c in range(0, 5):
    num = int(input('Digite um número: '))
    if numlist == []:
        numlist.append(num)
        print('Primeiro número digitado, será adicionado na última posição.')
        print(numlist)
    for pos, x in enumerate(numlist):
        if num < x:
            numlist.insert(pos, num)
            print(f'Número adicionado na posição {pos}.')
            print(numlist)
            break
        if num > max(numlist):
            numlist.insert(len(numlist) + 1, num)
            print(f'Número adicionado na posição {pos}.')
            print(numlist)
            break
print('\033[1;37m-\033[m' * 45)
print(f'\033[1;34mVocê digitou os números: {numlist}\033[m')
print('\033[1;37m-\033[m' * 45)
