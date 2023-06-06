#DISSECANDO UMA STRING:
n = input(print("digite algo: "))
print('O tipo primitivo da palavra {} é {}.'.format(n, type(n)))
print('A palavra é alfanumérica? {}.', n.isalnum)
print('A palavra é numérica? {}.', n.isnumeric)
print('A palavra tem somente espaços? {}.', n.isspace)
