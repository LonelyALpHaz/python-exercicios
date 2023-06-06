#SIMULADOR DE CAIXA ELETRÔNICO:
contador50 = contador20 = contador10 = contador1 = final = 0
print('-' * 26)
print('{:^25}'.format('BANCO ADF'))
print('-' * 26)
valor = int(input('Valor do saque: '))
while valor != 0:
    #DIVISÃO POR 50:
    divisao = valor // 50
    total = valor - (divisao * 50)
    contador50 = divisao
    #DIVISAO POR 20:
    if total % 50 != 0:
        divisao = total // 20
        total = total - (divisao * 20)
        contador20 = divisao
    #DIVISAO POR 10:
    if total % 20 != 0:
        divisao = total // 10
        total = total - (divisao * 10)
        contador10 = divisao
    #DIVISÃO POR 1:
    if total % 10 != 0:
        divisao = total // 1
        total = total - (divisao * 1)
        contador1 = divisao
    print('-' * 26)
    print(f'Você irá receber:\n[{contador50}] cédulas de R$50,00\n[{contador20}] cédulas de R$20,00\n[{contador10}] cédulas de R$10,00\n[{contador1}] cédulas de R$1,00')
    print('-' * 26)
    break
