#VALORES ÚNICOS EM UMA LISTA:
numlist = list()
while True:
    num = int(input('Digite um valor: '))
    if num in numlist:
        print('Valor já digitado, números repetidos não serão adicionados.')
    else:
        numlist.append(num)
    continuar = str(input('Deseja continuar [S/N]? ').upper()).strip()[0]
    #FINAL:
    if continuar == 'N':
        numlist.sort()
        print(f'Você digitou os números: {numlist}')
        break
