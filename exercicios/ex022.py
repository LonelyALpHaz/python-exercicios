#ANALISADOR DE NOMES:
n = str((input('Digite seu nome completo: '))).strip()
m = n.split()
print('Analisando seu nome...\nSeu nome completo tem {} letras.\nSeu nome em maiúsculo é {}.\nSeu nome em minúsculo é {}.\nSeu primeiro nome é {} e ele possui {} letras.'.format(len(n)-n.count(' '), n.upper(), n.lower(), m[0], len(m[0])))
