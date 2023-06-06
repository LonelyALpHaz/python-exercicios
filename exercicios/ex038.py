#MAIOR, MENOR OU IGUAL?
n1 = int(input('\033[1;30mPrimeiro número:\033[m '))
n2 = int(input('\033[1;30mSegundo número:\033[m '))
print('\033[1;34mAnalisando esses dois números, podemos saber que...\033[m')
if n1 > n2:
    print('\033[1;30mO número\033[m \033[1;32m{}\033[m \033[1;30mé maior que o\033[m \033[1;31m{}\033[m\033[1;30m.\033[m'.format(n1, n2))
elif n2 > n1:
    print('\033[1;30mO número\033[m \033[1;32m{}\033[m \033[1;30mé maior que\033[m \033[1;31m{}\033[m\033[1;30m.\033[m'.format(n2, n1))
elif n1 == n2:
    print('\033[1;34mAmbos os números tem o mesmo valor.\033[m')
