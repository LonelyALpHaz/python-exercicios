#ANÁLISE DE DADOS EM TUPLA:
contador = nove = tres = 0
num = (int((input('Digite um número: '))),
        int((input('Digite um número: '))),
        int((input('Digite um número: '))),
        int((input('Digite um número: '))))
print(f'Você digitou: {num}')
if num.count(9) == 1:
        print('O número nove foi digitado 1 vez.')
else:
        print(f'O número nove foi digitado {num.count(9)} vezes.')
if 3 in num:
        print(f'O número três apareceu pela primeira vez na {num.index(3) + 1}ª posição.')
else:
        print('O número três não foi digitado.')
print('Os números pares digitados foram: ',end='')
for n in num:
        if n % 2 == 0:
                print(n, end=' ')
