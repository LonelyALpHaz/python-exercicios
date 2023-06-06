#DIVIDINDO VALORES EM VÁRIAS LISTAS:
par = list()
impar = list()
numlist = list()
while True:
    num = int(input('Digite um número: '))
    numlist.append(num)
    continuar = str(input('Deseja continuar [S/N]? ').upper()).strip()[0]
    #NÚMEROS PARES:
    if num % 2 == 0:
        par.append(num)
    if num % 2 != 0:
        impar.append(num)
    #CONCLUSÃO:
    if continuar == 'N':
        print('-' * 45)
        print(f'Você digitou os números: {numlist}.')
        print(f'Os números pares digitados foram: {par}.')
        print(f'Os números ímpares digitados foram: {impar}.')
        print('-' * 45)
        break
