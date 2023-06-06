#ANALISADOR COMPLETO:
nomehomemmvelho = None
mm20 = hmvelho = media = maioridade = menoridade = 0
masculino = 'Masculino'
feminino = 'Feminino'
#ANALISADOR GERAL:
for dados in range(1, 5):
    print('------ {}ª Pessoa ------'.format(dados))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
#ANALISADOR DE IDADES:
    idadedados = [idade]
    for idade in idadedados:
        if maioridade == 0 or idade > maioridade:
            maioridade = idade
        if menoridade == 0 or idade < menoridade:
            menoridade = idade
#ANALISADOR DE MÉDIA DE IDADE:
    media += idade / 4
#ANALISADOR DO SEXO [M/F]:
    if sexo == 'M':
        sexo = masculino
    elif sexo == 'F':
        sexo = feminino
    elif sexo != 'M' and sexo != 'F':
        print('Informação inválida. Utilize apenas "M" ou "F".')
        break
#HOMEM MAIS VELHO:
    if maioridade == idade and sexo == masculino:
        hmvelho = idade
        nomehomemmvelho = nome
#MULHERS < 20 ANOS:
    if menoridade <= 19 and sexo == feminino:
        mm20 += 1
#CONCLUSÃO:
print('A média de idade entre as 4 pessoas é igual a {:.2f}'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridade, nomehomemmvelho))
print('Há {} mulheres com menos de 20 anos.'.format(mm20))
