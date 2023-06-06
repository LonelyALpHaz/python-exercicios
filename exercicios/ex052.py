#NÚMEROS PRIMOS:
num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1;32m{}\033[m'.format(c), end=' ')
        total += 1
    else:
        print('\033[1;31m{}\033[m'.format(c), end=' ')
print('\nO número \033[1;34m{}\033[m é divisível por \033[1;34m{}\033[m números.'.format(num, total))
if total == 2:
    print('O número {} \033[1;32mÉ\033[m primo.'.format(num))
else:
    print('O número \033[1;34m{}\033[m \033[1;31mNÃO É\033[m primo.'.format(num))
