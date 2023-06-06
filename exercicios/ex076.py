#LISTA DE PREÇOS COM TUPLA:
produtos = ('Lápis', 1.50,
            'Caderno', 27.00,
            'Lapiseira', 15.00,
            'Borracha', 2.50,
            'Calculadora', 75.90,
            'Estojo', 25.00,
            'Mochila', 120.00)
print('-' * 45)
print(f'{("LISTAGEM DE PREÇOS"):^44}')
print('-' * 45)
print(f'{produtos[0]}{("." * 30):<30}R$    {produtos[1]:.2f}',
      f'\n{produtos[2]}{("." * 28):<28}R$   {produtos[3]:.2f}',
      f'\n{produtos[4]}{("." * 26):<26}R$   {produtos[5]:.2f}',
      f'\n{produtos[6]}{("." * 27):<27}R$    {produtos[7]:.2f}',
      f'\n{produtos[8]}{("." * 24):<24}R$   {produtos[9]:.2f}',
      f'\n{produtos[10]}{("." * 29):<29}R$   {produtos[11]:.2f}',
      f'\n{produtos[12]}{("." * 28):<28}R$  {produtos[13]:.2f}')
print('-' * 45)
