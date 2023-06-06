#GERENCIADOR DE PAGAMENTOS:
valor = float(input('Qual o valor da compra? '))
print('Escolha a forma de pagamento: ')
print('\033[1;33m=\033[m' * 33)
print('\033[1;34m[ 1 ] À vista [Dinheiro/Cheque]\n[ 2 ] À vista [Cartão]\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão\033[m')
print('\033[1;33m=\033[m' * 33)
escolha = int(input('Sua escolha: '))
desconto10 = (valor * 10) / 100
desconto5 = (valor * 5) / 100
desconto2x = valor / 2
if escolha == 1:
    print('\033[1;34mO valor da compra é R${:.2f}. Com a compra à vista no dinheiro/cheque você ganha 10% de desconto, sendo assim, o valor à pagar é R${:.2f}.\033[m'.format(valor, valor - desconto10))
elif escolha == 2:
    print('\033[1;34mO valor da compra é R${:.2f}. Com a compra à vista no cartão você ganha 5% de desconto, sendo assim, o valor à pagar é R${:.2f}.\033[m'.format(valor, valor - desconto5))
elif escolha == 3:
    print('\033[1;34mO valor da compra é R${:.2f}. Com a compra parcelada em 2x no cartão, cada parcela terá o valor de R${:.2f}.\033[m'.format(valor, desconto2x))
elif escolha == 4:
    parcela = int(input('\033[1;33mEm quantas vezes você deseja parcelar a compra?\033[m '))
    juros = (valor * 20) / 100
    total = (valor + juros) / parcela
    print('\033[1;34mO valor da compra é R${:.2f}. Com a compra parcelada em {}x no cartão você terá 20% de juros, sendo assim, cada parcela terá o valor de R${:.2f}.\033[m'.format(valor, parcela, total))
