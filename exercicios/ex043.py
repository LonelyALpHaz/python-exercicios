#ÍNDICE DE MASSA CORPÓREA (IMC):
peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura ** 2)
if imc <= 18.5:
    print('Seu IMC é {:.1f}. Você está ABAIXO DO PESO!'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Seu IMC é {:.1f}. Você está no PESO IDEAL!'.format(imc))
elif imc >= 25 and imc <= 30:
    print('Seu IMC é {:.1f}. Você está com SOBREPESO.'.format(imc))
elif imc >= 30 and imc <= 40:
    print('Seu IMC é {:.1f}. Você esta com OBESIDADE.'.format(imc))
elif imc >= 40:
    print('Seu IMC é {:.1f}. Você está com OBESIDADE MÓRBIDA.'.format(imc))
