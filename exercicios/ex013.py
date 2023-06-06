#CÁLCULO DO AUMENTO DE SALÁRIO:
s = float(input(print('Digite o valor do seu salário: R$ ')))
a = int(input(print('Digite o valor do aumento: % ')))
aumento = (s * a) / 100
total = s + aumento
print('O valor do seu novo salário com um aumento de {}% é igual a {:.2f}.'.format(a, total))
