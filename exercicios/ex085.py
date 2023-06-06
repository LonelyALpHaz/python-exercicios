#LISTA ÚNICA COM PARES E ÍMPARES:
numeros = [[], [], []]
for n in range(0, 7):
    num = int(input('Digite um número: '))
    numeros[2].append(num)
#PARES:
    if num % 2 == 0:
        numeros[0].append(num)
        numeros[0].sort()
#ÍMPARES:
    if num % 2 != 0:
        numeros[1].append(num)
        numeros[1].sort()
#FINAL:
print('-' * 53)
print(f'Você digitou os números: \033[1;36m{numeros[2]}\033[m.')
print(f'Os números pares digitados são: \033[1;36m{numeros[0]}\033[m.')
print(f'Os números ímpares digitados são: \033[1;36m{numeros[1]}\033[m.')
print('-' * 53)
