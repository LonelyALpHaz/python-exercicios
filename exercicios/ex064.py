#TRATANDO VÁRIOS VALORES V1.0:
print('\033[1;33m--\033[m' * 45)
print('\033[1;34mDigite alguns valores, para finalizar digite "999" e ao final informarei a soma de todos.\033[m')
print('\033[1;33m--\033[m' * 45)
num = contador = soma = 0
num = int(input('Digite um valor: '))
while num != 999:
    contador += 1
    soma += num
    num = int(input('Digite um valor: '))
    if num == 999:
        print('\033[1;34mA soma dos {} números é igual a {}.\033[m'.format(contador, soma))
