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

"""
ex1 = []

for i in range(10):
    num = input(f"Digite o {i + 1}º numero : ")
    ex1.insert(0, num)



print(ex1)
"""






# in_data = int(input("idade: "))

#print(in_data * 2)

#in_data2 = input("idade 2: ")

#in_data2_int = int(in_data2)

#print(in_data2_int * 2)

#print(11 % 2 == 0)
#print(10 % 2 == 0)


"""
faça um programa que peça ao usr 10 num e:
    se o num for par add no inicio
    se o num for impar add no fim

no final deve mostrar a lista
"""

ex1 = []

"""
for i in range(10):
    num = int(input(f"Digite o {i + 1}º numero : "))

    if num % 2 == 0:
        ex1.insert(0, num)

    else:
        ex1.append(num)



print(ex1)

"""
"""
contador = 0
lst = []

while contador <= 10:
    num = int(input(f"Digite um numero {contador}: "))

    if num % 2 == 0:
        lst.insert(0, num)
    else:
        lst.append(num)

    contador += 1 # contador =  contador + 1

print(lst)

"""

print("---" * 10)

print(lst)

lst.pop()
print(lst)

lst.pop()
print(lst)


lst.pop(0)
print(lst)



"""
faça um programa que peça ao usr 10 num e:
    se o num for par add no inicio
    se o num for impar add no fim
    se num for 5 remover o ultimo elem da lista
    se num for 7 remover o primeiro elem da lista


no final deve mostrar a lista
"""

ex = []


for i in range(10):
    num = int(input(f"Digite o {i + 1}º numero : "))

    if num % 2 == 0:
        ex.insert(0, num)

    else:
        ex.append(num)

    if num == 5:
        ex.pop()

    elif num == 7:
        ex.pop(0)


print(ex)


# ==
# !=
# and
# or