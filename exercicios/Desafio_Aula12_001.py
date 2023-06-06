#DADOS DO USUÁRIO:
valorcasa = int(input('Valor do imóvel: R$ '))
salario = int(input('Valor do seu salário: '))
anos = int(input('Em quantos anos você deseja pagar? '))
#CONTAS:
salario30 = (salario * 30) / 100
prestacao = valorcasa / (anos * 12)
if prestacao > salario30:
    print('Empréstimo NEGADO! Pois as prestações não podem exceder o valor de R${:.2f} (30% do seu salário) e o valor das prestações é igual a R${:.2f}.'.format(salario30 ,prestacao))
else:
    print('PARABÉNS! O impréstimo foi aceito, você levará {} anos para pagar e o valor das prestações será de R${:.2f}.'.format(anos, prestacao))
