#LISTA COMPOSTA E ANÁLISE DE DADOS:
contador = maior = menor = 0
dados = list()
pessoas = list()
while True:
#DADOS:
    nome = str(input('Nome: '))
    dados.append(nome[:])
    peso = float(input('Peso: '))
    dados.append(peso)
    pessoas.append(dados[:])
    dados.clear()
    contador += 1
    continuar = str(input('Deseja continuar [S/N]? ').upper()).strip()[0]
#MAIOR E MENOR PESO:
    pesolist = [peso]
    for peso in pesolist:
        if maior == 0 or peso > maior:
            maior = peso
        if menor == 0 or peso < menor:
            menor = peso
        if maior == peso:
            maiorpeso = nome
        if menor == peso:
            menorpeso = nome
#FINAL:
    if continuar == 'N':
        print(f'Você cadastrou {contador} pessoas.')
        print(f'A pessoa com maior peso é {maiorpeso} e ele(a) pesa {maior}Kg.')
        print(f'A pessoa com o menor peso é {menorpeso} e ele(a) pesa {menor}Kg.')
        break
