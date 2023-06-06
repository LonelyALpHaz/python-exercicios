#CONTADOR DE LETRAS EM UMA STRING:
n = str((input('Digite uma frase: ').upper()).strip())
print('A letra "A" aparece na frase {} vezes.'.format(n.count('A')))
print('A letra "A" aparecfe pela primeira vez na posição {}.'.format(n.find('A')+1))
print('A última letra "A" aparece na posição {}.'.format(n.rfind('A')+1))
