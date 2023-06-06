#ÍMPAR OU PAR?
n = int(input('Digite um número para saber se ele é par ou ímpar: '))
num = n % 2
if num == 1:
    print('O número {} é ímpar.'.format(n))
else:
    print('O número {} é par.'.format(n))
