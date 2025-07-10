"""

    faça um programa que receba 2 num e indique:

    qual o maior (1º ou 2º)
    se forem iguais deve dar essa informação


"""


# num1 = int(input("informe o primeiro numero: "))
# num2 = int(input("informe o segundo numero: "))

num1 = 42
num2 = 42

if num1 > num2:
    print(f"o maior e {num1}")

elif num2 == num1:
    print(f"os numeros iguais")

elif num1 == 42:
    print(f"num1 é 42")

else:
    print(f"o maior e {num2}")

print("depois do if")
