"""
list (Array) -> []


"""
lst = [19, 34, 14, 5, 1, 33, 13, 43, 3112]

print(lst)
print(lst[0])
print(lst[1])

print(lst[8])

# print(lst[9])

lst.append(123) # add no fim

print(lst[9])

print("-----------")
print(len(lst)) # num de elm na lista
print(lst.__len__())

"""

faça um programa que peça ao usr 10 num e add esses 10 num a lista ex1
no final deve mostrar a lista
"""
"""
ex1 = []
for i in range(10):
    num = input(f"Digite o {i+1}º numero : ")
    #validar num
    ex1.append(num)

print(ex1)

"""

"""
como criar listas
como aceder a um elemento
como add elm no fim
como saber qts elm tem uma lista


add elm sem ser no fim
remover elm
iterar pela lista

"""
print("----"*10)

lst = [19, 34, 14, 5, 1, 33, 13, 43, 3112]

print(lst)

lst.insert(0, 99)
"""
99 -> 0
[19, 34, 14, 5, 1, 33, 13, 43, 3112]

[-19-, 34, 14, 5, 1, 33, 13, 43, 3112]

[__ ,19, 34, 14, 5, 1, 33, 13, 43, 3112]

[99 ,19, 34, 14, 5, 1, 33, 13, 43, 3112]
"""

print(lst)



lst.insert(3, 88)
"""
[99 ,19, 34,  88,14, 5, 1, 33, 13, 43, 3112]
"""
print(lst)


"""

faça um programa que peça ao usr 10 num e add esses 10 no inicio da a lista ex1
no final deve mostrar a lista
"""

ex1 = []




