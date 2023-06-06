#ESTATÍSTICAS EW PRODUTOS:
soma = maior = menor = total = caro = barato = 0
print('-' * 35)
print('{:^34}'.format('MERCADO BOM PREÇO'))
print('-' * 35)
while True:
    #ANALISADOR GERAL:
    produto = str(input('Nome do produto: '))
    valor = int(input('Valor do produto: R$').strip())
    continuar = str(input('Deseja continuar [S/N]? ').upper()).strip()[0]
    print('-' * 35)
    #SOMA DOS PREÇOS:
    soma += valor
    #MAIOR E MENOR PREÇO:
    listavalor = [valor]
    for valor in listavalor:
        if maior == 0 or valor > maior:
            maior = valor
        if menor == 0 or valor < menor:
            menor = valor
    if valor > 1000:
        caro += 1
    if menor == valor:
        barato = produto
    #FINAL:
    if continuar == 'N':
        print(f'{"FIM DA COMPRA!":^35}')
        print(f'O preço total da compra é R${soma:.2f}.')
        print(f'Temos {caro} produtos custando mais de R$1000.00.')
        print(f'O produto mais barato foi {barato} que custa R${menor:.2f}.')
        break
