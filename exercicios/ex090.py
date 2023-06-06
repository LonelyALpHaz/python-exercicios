#DICIONÁRIO EM PYTHON:
dados = {}
for d in range(0, 1):
    dados['nome'] = str(input('Nome: '))
    dados['media'] = float(input(f'Média de {dados["nome"]}: '))
if dados['media'] >= 7:
    dados['situação'] = '\033[1;32mAPROVADO\033[m'
if dados['media'] < 7 and dados['media'] >= 5:
    dados['situação'] = '\033[1;33mRECUPERAÇÂO\033[m'
if dados['media'] < 5:
    dados['situação'] = '\033[1;31mREPROVADO\033[m'
print('\033[1;36m-\033[m' * 30)
print(f'\033[1;37mNome do aluno: {dados["nome"]}')
print(f'Média do aluno: {dados["media"]}')
print(f'Situação do aluno:\033[m {dados["situação"]}\033[m')
print('\033[1;36m-\033[m' * 30)
