# Quant de notas, max(notas), min(notas), média da turma, situação (opc)
def notas(*nts, sit=False):
    """
    --------------------------------------------
    Utilidade: Fornecer informações com base nas
    notas dos alunos.
    --------------------------------------------
    :param nts: = Recebe as notas dos alunos.
    :param sit: = 'False' p/ não mostrar a
    situação do alunos, 'True' p/ mostrar a si-
    tuação.

    OBS: :param sit: predefinido no 'False'.
    --------------------------------------------
                  Criado por ADF
    --------------------------------------------
    """
    media = soma = 0
    for pos, x in enumerate(nts):
        soma += nts[pos]
    media = soma / len(nts)
    dicio = {'quant': len(nts), 'max': max(nts), 'min': min(nts), 'media': media}
    # Informações Dicio:
    print('-' * 51)
    print(dicio)
    # Informações:
    print('-' * 51)
    print(f' -> Foram cadastradas {dicio["quant"]} notas.')
    print(f' -> A maior nota foi {dicio["max"]}.')
    print(f' -> A menor nota foi {dicio["min"]}.')
    print(f' -> A média da turma é {dicio["media"]:.1f}.')
    print('-' * 51)
    # Sit == True:
    if sit:
        if dicio['media'] < 3:
            print(f'\033[1;31m{"Situação: Péssima.":^51}\033[m')
        if dicio['media'] >= 3 and dicio['media'] <= 6:
            print(f'\033[1;33m{"Situação: Ruim.":^51}\033[m')
        if dicio['media'] > 6 and dicio['media'] <= 8:
            print(f'\033[1;34m{"Situação: Boa.":^51}\033[m')
        if dicio['media'] > 8 and dicio['media'] <= 10:
            print(f'\033[1;32m{"Situação: Ótima.":^51}\033[m')
        print('-' * 51)


help(notas)
notas(7.5, 8, 8.5, 10, sit=True)
