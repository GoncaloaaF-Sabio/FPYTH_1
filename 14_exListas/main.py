"""

peça ao utilizador 10 num e guarde esses 10 num numa lista, -> done
deve guardar o 1º e ultimo num a serem adiciodos para os utilizar mais tarde

mostre ao utilizar:
    a lista pela ordem que foi criada
    a lista invertida
    a lista ordenada
    o index do 1º a ser adicionado

remover o ultimo elemento a ser adicionado

"""

num_elm = 10

lista = []

# peça ao utilizador 10 num e guarde esses 10 num numa lista, -> done
for i in range(num_elm):

    num = int(input(f"Digite um numero {i}: "))
    lista.append(num)
    #if lista.__len__() == 1:
    #    p = num
    #elif lista.__len__() == num_elm:
    #    u = num

# deve guardar o 1º e ultimo num a serem adiciodos para os utilizar mais tarde
p = lista[0]
u = lista[num_elm-1]

#   a lista pela ordem que foi criada
print(lista)

for i in lista:
    print(i, end=" ")

print()
#   a lista invertida

lista.reverse() # inverte a lista

print(lista)

for i in lista:
    print(i, end=" ")

print()

#    a lista ordenada


lista.sort()

print(lista)

for i in lista:
    print(i, end=" ")

print()



#    o index do 1º a ser adicionado

idx = lista.index(p)
print(f"o idx do 1º val a ser adicionado: {idx} ")

# remover o ultimo elemento a ser adicionado


lista.remove(u)

print(lista)
