
"""
Escala A-F (aproximada):
A: 17-20 (Excelente/Muito Bom).
B: 13-16 (Bom).
C: 10-12 (Suficiente/Satisfaz).
D: 7-9 (Insuficiente/Não Satisfaz).
E: 4-6 (Muito Insuficiente).
F: 0-3 (Muito Insuficiente/Reprovado).
"""

"""
nota = 10
if nota <= 3:
    print('F')
elif nota <= 6:
    print('E')
elif nota <= 9:
    print('D')
elif nota <= 12:
    print('C')
elif nota <= 16:
    print('B')
else:
    print('A')
     
"""


mes = 3

match mes:
    case 1:
        print('Janeiro')
    case 2:
        print('Fevereiro')
    case 3:
        print('Marco')
    case _:
        print('mes invalido')



"""
Escala A-F (aproximada):
A: 17-20 (Excelente/Muito Bom).
B: 13-16 (Bom).
C: 10-12 (Suficiente/Satisfaz).
D: 7-9 (Insuficiente/Não Satisfaz).
E: 4-6 (Muito Insuficiente).
F: 0-3 (Muito Insuficiente/Reprovado).
"""


nota = 0
match nota:
    case 17 | 18 | 19 | 20:
        print('A')
    case 13 | 14 | 15 | 16:
        print('B')
    case 10 | 11 | 12:
        print('C')
    case 7 | 8 | 9:
        print('D')
    case 4 | 5 | 6:
        print('E')
    case 0 | 1 | 2 | 3:
        print('F')
    case _:
        print('nota invalida')