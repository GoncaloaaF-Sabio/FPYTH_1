
r = range(10) # 0 a 9 <-> range(m)  -> 0 ate m-1
r2 = range(2, 10) # 2 a 9 <-> range(n, m)  -> n ate m-1 -> 2 3 4 5 6 7 8 9
r3 = range(5, 50, 5) # 5 a 49 de 5 em 5 <-> range(n, m, s)  -> n ate m-1 com um step de s
                     # 5 10 15 20 25 30 35 40 45

nota = 4
match nota:
    case range(10):
        print("case1")
    case range(10, 20):
        print("case2")
    case _:
        print("case3")



print(4 in range(10)) # val in conjunto_valores

nota = 10
if nota in range(10, 21):
    print("Aluno Aporvado")
elif nota in range(0, 10):
    print("Aluno não Aporvado")
else:
    print("Nota invalida")