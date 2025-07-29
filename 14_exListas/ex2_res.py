"""

peça ao utilizar quantos num ele quer adicionar, -> done
se o utilziador indicar um numero negativo deve voltar a pedir o numero de valroes a adicionar  -> done

deve pedir ao utilziar a quantidade de numeros indicada.

add os num a uma lista

no final:
    calcule a quantidade de valores positivos e nagativos
    mostre o dobro de todos os num inseridos
    calcule a quantidade de valores par e impar

"""

# var

lista_numeros = []

# peça ao utilizar quantos num ele quer adicionar,
while True:
    qt_num = int(input("Quantos numeros deseja adicionar? "))

    if qt_num > 0:
        break

    print(f"o {qt_num} é invalido, o valor tem de ser positivo")


print(f"Irá adicionar {qt_num} numeros")



for i in range(qt_num):
    numero = int(input(f"Digite um numero {i + 1}: "))
    lista_numeros.append(numero)



"""

    calcule a quantidade de valores positivos e nagativos
    mostre o dobro de todos os num inseridos
    calcule a quantidade de valores par e impar
    
"""

print(lista_numeros)

pos = 0
neg = 0
par = 0
impar = 0
lista_numeros_dobro = []


for numero in lista_numeros:
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1

    if numero < 0:
        neg += 1
    else:
        pos += 1

    #lista_numeros.append(numero * 2)
    #print(lista_numeros)
    lista_numeros_dobro.append(numero * 2)

print(f"pos: {pos}\nneg: {neg}\npar: {par}\nimpar: {impar}\nDobro: {lista_numeros_dobro}")