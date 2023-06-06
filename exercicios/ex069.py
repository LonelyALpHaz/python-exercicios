#ANÁLISE DE DADOS DE UM GRUPO:
maioridade = menoridade = homemcadas = mulhermenor = 0
while True:
    print('-' * 35)
    print('      CADASTRE UMA PESSOA:')
    print('-' * 35)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ').upper()).strip()[0]
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]? ').upper()).strip()[0]
    #MAIOR E MENOR IDADE:
    if idade < 20:
        menoridade += 1
    if idade >= 20:
        maioridade += 1
    #HOMENS CADASTRADOS:
    if sexo == 'M':
        homemcadas += 1
    #MULHERS COM MENOS DE 20 ANOS:
    if sexo == 'F' and idade < 20:
        mulhermenor += 1
    #CONTINUA?
    if continuar == 'N':
        print('-' * 42)
        print(f'Total de pessoas com mais de 20 anos: {maioridade}')
        print(f'Total de homens cadastrados: {homemcadas}')
        print(f'Total de mulheres com menos de 20 anos: {mulhermenor}')
        print('-' * 42)
        break
