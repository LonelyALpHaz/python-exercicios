#CONTANDO VOGAIS EM TUPLA:
from time import sleep
palavras = ('PROGRAMAR', 'PYTHON', 'PRATICAR', 'VARIAVEIS', 'MODULOS', 'TUPLAS', 'LISTAS', 'DICIONARIOS',
            'STRINGS', 'CONDIÇOES', 'TERMINAL', 'REPETIÇAO', 'CODIGOS', 'SCRIPTS')
for c in range(0, len(palavras)):
    a = palavras[c].find("A")
    e = palavras[c].find("E")
    i = palavras[c].find("I")
    o = palavras[c].find("O")
    u = palavras[c].find("U")
    palavrasc = palavras[c]
    print(f'Na palavra \033[1;34m{palavrasc}\033[m temos as vogais: ')
    if a > -1:
        print(palavrasc[a])
    if e > -1:
        print(palavrasc[e])
    if i > -1:
        print(palavrasc[i])
    if o > -1:
        print(palavrasc[o])
    if u > -1:
        print(palavrasc[u])
