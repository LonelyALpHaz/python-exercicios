#AUMENTO DE SALÁRIO EM 10% E 15%:
salario = int(input('Qual o salário do funcionário? R$ '))
aumen10 = (salario * 10) / 100
aumen15 = (salario * 15) / 100
if salario > 1250:
    print('Com um aumento de 10% o valor do seu novo salário é R${:.2f}.'.format(salario + aumen10))
if salario <= 1250:
    print('Com um aumento de 15% o valor do seu novo salário é R${:.2f}.'.format(salario + aumen15))
