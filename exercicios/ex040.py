#APOVADO, RECUPERAÇÃO E REPROVADO:
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('Com as notas {} e {} a média do aluno é igual a {:.1f}.\nCom essa média o aluno está REPROVADO!'.format(n1, n2, media))
elif media >= 5 and media < 7:
    print('Com as notas {} e {} a média do aluno é igual a {:.1f}.\nCom essa média o aluno está na RECUPERAÇÂO!'.format(n1, n2, media))
elif media >= 7:
    print('Com as notas {} e {} a média do aluno é igual a {:.1f}.\nCom essa média o aluno está APROVADO.'.format(n1, n2, media))
