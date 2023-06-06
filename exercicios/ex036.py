#EMPRÉSTIMO IMOBILIÁRIO:
valorcasa = int(input('\033[1;36mValor do imóvel: R$\033[m '))
salario = int(input('\033[1;36mValor do seu salário:\033[m '))
anos = int(input('\033[1;36mEm quantos anos você deseja pagar?\033[m '))
salario30 = (salario * 30) / 100
prestacao = valorcasa / (anos * 12)
if prestacao > salario30:
    print('\033[1;30mEmpréstimo\033[m \033[1;31mNEGADO\033[m\033[1;30m! Pois as prestações não podem exceder o valor de R${:.2f} (30% do seu salário) e o valor das prestações é igual a R${:.2f}.\033[m'.format(salario30 ,prestacao))
else:
    print('\033[1;32mPARABÉNS\033[m\033[1;30m! O impréstimo foi aceito, você levará {} anos para pagar e o valor das prestações será de R${:.2f}.\033[m'.format(anos, prestacao))
