#UNINDO DICIONÁRIOS E LISTAS:
soma = contador = 0
dados = {}
pessoas = []
while True:
    dados['nome'] = str(input('Nome: '))
    dados['idade'] = int(input('Idade: '))
    dados['sexo'] = str(input('Sexo [M/F]: ').upper()).strip()[0]
    soma += dados['idade']
    contador += 1
    #TRANSFORMANDO DICIONÁRIO EM LISTA:
    pessoas.append(dados.copy())
    #SEXO INCORRETO:
    if dados['sexo'] != 'M' and dados['sexo'] != 'F':
        print('Comando inválido, utilize apenas "M" ou "F".')
    #CONTINUAR:
    continuar = str(input('Deseja continuar [S/N]? ').upper()).strip()[0]
    #CONTINUAR INCORRETO:
    if continuar != 'S' and continuar != 'N':
        print('Comando inválido, utilize apenas "S" ou "N".')
        continuar = str(input('Deseja continuar [S/N]? ').upper()).strip()[0]
    #MÉDIA E PESSOAS ACIMA DA MÉDIA:
    media = soma / contador
    #CONTINUAR = N:
    if continuar == 'N':
        break
print('-' * 50)
print(f'          Foram cadastradas \033[1;36m{contador}\033[m pessoas:\n')
print(f' - A média de idade é igual a \033[1;36m{media:.2f}\033[m anos.')
print(f' - As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] in 'Ff':
        print(f'\033[1;36m{p["nome"]}\033[m', end='; ')
print()
print(f' - Pessoas que estão acima da média: ')
for i in pessoas:
    if i['idade'] > media:
        print(f'   - Nome: \033[1;36m{i["nome"]}\033[m; Idade: \033[1;36m{i["idade"]}\033[m; Sexo: \033[1;36m{i["sexo"]}\033[m;')
print('-' * 50)
