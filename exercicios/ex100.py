from random import randint
numeros = list()


def numsort():
    for c in range(0, 5):
       numeros.append(randint(1, 10))
    print(numeros)


def somapar():
    soma = 0
    for pos, x in enumerate(numeros):
        if numeros[pos] % 2 == 0:
            soma += numeros[pos]
            pares = numeros[pos]
    print(soma)


#PRINCIPAL:
print('-' * 52)
print('Os números sorteados foram:\033[1;34m ', end='')
numsort()
print('\033[mSomando os números \033[1;32mPARES\033[m temos o seguinte valor:\033[1;34m ', end='')
somapar()
print('\033[m-' * 52)
