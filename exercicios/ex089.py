#BOLETIM COM LISTAS COMPOSTAS:
from time import sleep
alunos = list()
dados = list()
while True:
    #DADOS:
    nome = str(input('Nome: '))
    dados.append(nome[:])
    nota1 = float(input('1ª Nota: '))
    dados.append(nota1)
    nota2 = float(input('2ª Nota: '))
    dados.append(nota2)
    #MÉDIA:
    media = (nota1 + nota2) / 2
    dados.append(media)
    alunos.append(dados[:])
    dados.clear()
    #CONTINUAR:
    continuar = str(input('Deseja continuar [S/N]? ').upper()).strip()[0]
    if continuar == 'N':
       break
print('-' * 30)
print('N° | Nome          | Média')
for pos, x in enumerate(alunos):
    print(f'{pos:<4}  {alunos[pos][0]:<9} {alunos[pos][3]:>8.1f}')
print('-' * 30)
while True:
    for pos, x in enumerate(alunos):
        escolha = int(input(('Para saber os dados de um aluno digite o N° (999 interrompe): ')))
        if escolha == pos:
            print(f'Aluno(a): {alunos[pos][0]}; Notas: ({alunos[pos][1]}), ({alunos[pos][2]}) ')
        if escolha == 999:
            print('Finalizando programa...')
            sleep(2)
            print('Volte sempre.')
            break
