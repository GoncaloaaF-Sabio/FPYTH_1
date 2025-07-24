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