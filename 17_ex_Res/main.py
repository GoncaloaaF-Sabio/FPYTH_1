"""

assuma que tem uma lista de numeros inteiros diferentes e não ordenados e um valor inteiro

ache os dois numeros da lista que somados dao o valor inteiro

deve indicar os numeros e as suas posições

pode assumir que existe sempre uma e so uma solução

exp:
lista - [3,5,1,6]
num - 7

saida:

num = [1,6]
pos = [2, 3]

"""

lst = [3,5,1,9,7,4]
target = 4
num = []
pos = []

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        soma = lst[i] + lst[j]
        print(f"{lst[i]} + {lst[j]}= {soma}")

        if soma == target:
            #opt 1
            # num.append(lst[i])
            # num.append(lst[j])
            
            # opt 2
            # num.extend([lst[i], lst[j]])

            # opt 3
            num = [lst[i], lst[j]]

            pos.extend([i,j])
            break


print(num)
print(pos)


"""

e se a lista estver ordenada?

exp:
lista - [1,3,5,6]
num - 7

saida:

num = [1,6]
pos = [2, 3]

"""

lst = [1, 3, 4, 5, 7, 9]

target = 4
num = []
pos = []

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        soma = lst[i] + lst[j]
        print(f"{lst[i]} + {lst[j]}= {soma}")

        if soma == target:
            # opt 1
            # num.append(lst[i])
            # num.append(lst[j])

            # opt 2
            # num.extend([lst[i], lst[j]])

            # opt 3
            num = [lst[i], lst[j]]

            pos.extend([i, j])
            break

print(num)
print(pos)
