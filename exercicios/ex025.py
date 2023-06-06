#ANALISADOR DE STRINGS (NOME PRÓPRIO):
n = str(input('Digite seu nome completo: ')).strip()
m = n.title()
p = m.count('Silva')
if p == True:
    print('Há "Silva" no seu nome.')
else:
    print('Não há "Silva" no seu nome.')
