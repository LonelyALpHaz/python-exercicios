#TABUADA V3.0:
mult = num = 0
while True:
    print('\033[1;30 m-\033[m' * 40)
    num = int(input('\033[1;36mDigite um número para ver sua tabuada: \033[m'))
    print('\033[1;30m-\033[m' * 40)
    if num < 0:
        print('\033[1;31mNúmero inválido... Finalizando programa.\033[m')
        print('\033[1;30m-\033[m' * 40)
        break
    for m in range(1, 11):
        mult = m * num
        print(f'\033[1;30m{num} * {m} = {mult}\033[m')
