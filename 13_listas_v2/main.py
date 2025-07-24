"""

criação
selc valor
add no fim
add sem ser no fim
remover (pop)



"""

"""
remove

list slice 
"""

nomes = [
    "Ana",       #0
    "Bruno",     #1
    "Carla",     #2
    "David",     #3
    "Eduarda",   #4
    "Fernando",  #5
    "Gabriela",  #6
    "Hugo",      #7
    "Inês",      #8
    "João"       #9
]

print(nomes[0])

print(nomes[3])


print(nomes)

nomes.append("Ana")
print(nomes)

nomes.insert(5, "Ana")
print(nomes)

nomes.append("Rui")
print(nomes)

nomes.pop()
print(nomes)


nomes.insert(6, "Rui")
print(nomes)

nomes.remove("Rui")
print(nomes)


nomes.insert(6, "Rui")
print(nomes)

nomes.insert(9, "Rui")
print(nomes)

nomes.remove("Rui") ## apaga a 1 vez q encontra o val
print(nomes)


# nomes.pop(x) -> o x tem de ser uma pos valida
# nomes.remove(x) -> o x tem de ser um valor valido
print("----"*10)
print(nomes)

print(nomes.count("Ana"))
print(nomes.count("Rui"))


print(nomes.__len__())
print(len(nomes))

print(nomes.index("David")) # nomes.index(x) -> o x tem de existir na lista

print(nomes.__contains__("David")) # <=> print("David" in nomes)
print(nomes.__contains__("david"))

print("David" in nomes)
print("david" in nomes)

nomes.sort() # ordena
print(nomes)

nomes.sort(reverse=True)
print(nomes)

nomes.clear() # remove todos os val da lista
print(nomes)

nomes = [
    "Ana",       #0
    "Bruno",     #1
    "Carla",     #2
    "David",     #3
    "Eduarda",   #4
    "Fernando",  #5
    "Gabriela",  #6
    "Hugo",      #7
    "Inês",      #8
    "João"       #9
]


nomes = ["Beatriz", "Rafael", "Luciana", "Carlos", "Marta",
         "Tiago", "Inês", "João", "Sofia", "Pedro"]

print(nomes)
nomes.reverse() # inverter a lista
print(nomes)

nomes.sort(reverse=True)
print(nomes)

print("---"*20)
nomes2 = nomes

print("nomes :", nomes)
print("nomes2:", nomes2)

print("---")
nomes2[0] = "Rita"

print("nomes2:", nomes2)
print("nomes :", nomes)


print("--copy-"*20)
nomes3 = nomes.copy() # criar uma nova list

print("nomes :", nomes)
print("nomes3:", nomes3)

print("---")
nomes3[0] = "Joana"

print("nomes3:", nomes3)
print("nomes :", nomes)


print("---"*20)


nomes2 = [
    "Ana",       #0
    "Bruno",     #1
    "Carla",     #2
    "David",     #3
    "Eduarda",   #4
    "Fernando",  #5
    "Gabriela",  #6
    "Hugo",      #7
    "Inês",      #8
    "João"       #9
]

print(nomes)
nomes.extend(nomes2)
print(nomes)