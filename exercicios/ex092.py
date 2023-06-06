#CADASTRO DE TRABALHADOR:
from datetime import date
dados = dict()
while True:
    dados['nome'] = str(input('Nome: '))
    dados['nascimento'] = int(input('Ano de nascimento: '))
    dados['ctps'] = int(input('N° da Carteira de Trabalho ("0" se não tiver): '))
    #CÁLCULO DA IDADE:
    anoatual = date.today().year
    idade = anoatual - dados['nascimento']
    #CARTEIRA = 0:
    if dados['ctps'] == 0:
        print('-' * 48)
        print(f'Nome Cadastrado: {dados["nome"]}\n'
              f'Idade: {idade}\n'
              f'CTPS: N/A')
        print('-' * 48)
        break
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = int(input('Valor do salário: '))
    #APOSENTADORIA:
    dados['aposentadoria'] = (dados['contratação'] + 35) - dados['nascimento']
    #FINAL:
    if dados['ctps'] != 0:
        print('-' * 48)
        print(f'Nome Cadastrado: {dados["nome"]}\n'
              f'Idade: {idade}\n'
              f'CTPS: {dados["ctps"]}\n'
              f'Ano de contratação: {dados["contratação"]}\n'
              f'Salário: {dados["salario"]:.2f}\n'
              f'Idade da Aposentadoria: {dados["aposentadoria"]}')
        print('-' * 48)
        break
