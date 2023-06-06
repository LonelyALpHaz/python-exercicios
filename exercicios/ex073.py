#LISTAS ORDENADAS SEM REPETIÇÃO:
numlist = list()
for c in range(0, 5):
    num = int(input('Digite um número: '))
    #PRIMEIRO NÚMERO:
    if numlist == []:
        numlist.insert(0, num)
        print('Primeiro número da lista, será adicionado na posição 0.')
        print(numlist)
    #MENOR NÚMERO:
    if num < min(numlist):
        numlist.insert(0, num)
        print('Número menor que o da posição 0, será adicionado na posição 0.')
        print(numlist)
    #MAIOR NÚMERO:
    if num > max(numlist):
        numlist.insert(len(numlist) + 1, num)
        print('Maior número até o momento, será adicionado na última posição.')
        print(numlist)
    #NÚMERO MAIOR QUE O DA POSIÇÃO 0:
    if num > numlist[0] and num < numlist[1]:
        numlist.insert(1, num)
        print('Número maior que o da posição 0, será adicionado na posição 1.')
        print(numlist)
    #NÚMERO ENTRE NÚMEROS:
    for pos, x in enumerate(numlist):
        if num in numlist:
            del(num)
        if num < x:
            numlist.insert(pos, num)
            print(numlist)
            break
print('\033[1;37m-\033[m' * 45)
print(f'\033[1;34mVocê digitou os números: {numlist}\033[m')
print('\033[1;37m-\033[m' * 45)
