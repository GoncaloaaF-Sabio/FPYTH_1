valor1 = 10
valor2 = 20

print(valor1 + valor2)

soma = valor1 + valor2
print(soma)

multiplicar = valor1 * valor2
print(multiplicar)

dividir = valor1 / valor2
print(dividir)

subtrair = valor1 - valor2
print(subtrair)

valor3 = 7
"""
modulo -> Mod  - Resto da div int

0 1 2 3 4 5 

0 1 0 1 0 1
0 1 2 0 1 2

"""
modulo = valor3 % 3
print(modulo)

"""

7 // 3 --> 2
sobra - X

x = 7 % 3   

"""
div_inteiro = valor3 // 3
print(div_inteiro)



"""
op com string
str + str
str * int

"""


str1 = "Ola"
str2 = "Mundo"

sumString = str1 + str2
print(sumString)

print(str1 * 10)
print("---" * 10)

# print("---" * "12")

# print("Ola" - 10)

# print("Ola" - "Ola")

print(str1 + str(10))

print(str1 + "10")
print(str1 + f"{10}")

foo = 10
print(f"{str1}{foo}")