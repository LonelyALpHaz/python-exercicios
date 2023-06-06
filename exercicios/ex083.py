#VALIDANDO EXPRESSÕES MATEMÁTICAS:
exp = list(input('Digite um expressão: '))
abrep = exp.count('(')
fechap = exp.count(')')
if abrep == fechap:
    print('Essa equação É VÁLIDA.')
else:
    print('Essa equação NÃO É VÁLIDA.')

