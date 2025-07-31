def ola_mundo():
    print("ola mundo")


ola_mundo()
ola_mundo()
ola_mundo()


def ola_mundo_nome(nome):
    print(f"ola mundo {nome}")


ola_mundo_nome("Gonçalo")
ola_mundo_nome("João")
ola_mundo_nome("Ana")

def ola_mundo_nome2(nome, ano):
    print(f"ola mundo {nome} em {ano}")

ola_mundo_nome2("Gonçalo", 2001)
ola_mundo_nome2("João", 2012)
ola_mundo_nome2("Ana", 2025)


#type hint
def teste(nome: str):
    print(nome)

teste("ola mundo")
teste(324234)


"""
Funções sem param
Funções com 1 param
Funções com multiplos  param

type hint em funções
"""


"""
1 Faça uma função que receba um nome e mostre a mensagem: "Ola [nome]"
2 Faça uma função que receba 2 números e mostre a soma dos 2 números"
3 Faça uma função que receba 1 número e mostre a tabuada desse número"

"""

# 1 Faça uma função que receba um nome e mostre a mensagem: "Ola [nome]"
def msg(nome):
    print(f"Ola {nome}")

msg("Gonçalo")
msg("Rita")
msg("Luis")

# 2 Faça uma função que receba 2 números e mostre a soma dos 2 números

def soma(num1: float, num2: float):
    res = num1 + num2
    print(res)

soma(3.1,2)
soma(3,4.4)
soma(4,9)


# 3 Faça uma função que receba 1 número e mostre a tabuada desse número

def tabuada(num:int):
    for c in range(1,11):
        res = num * c
        print(f"{num} x {c} = {res}")

print("-- tabuada for---")
tabuada(3)
print("-----")
tabuada(6)


def tabuada2(num:int):
    c = 1
    while c <= 10:
        res = num * c
        print(f"{num} x {c} = {res}")
        c += 1

print("-- tabuada while---")
tabuada2(3)
print("-----")
tabuada2(6)