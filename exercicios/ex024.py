#ANALISADOR DE STRINGS (CIDADE):
n = str(input('Em que cidade você nasceu? ')).strip()
m = n.title()
p = m.count('Santo')
if p == False:
    print('A sua cidade não possui "Santo" no nome.')
else:
    print('A sua cidade possui "Santo" no nome.')
