def ola_mundo():
    print("ola mundo")

ola_mundo()
ola_mundo()

def ola_mundo2():
    return "ola mundo2"


def idade():
    return 20

i = idade()

idade()

print(idade())

r = ola_mundo2()
r2 = r.upper()
print(r2)
print(r2.find("MUNDO2"))


print("------------------")
def somar(a,b):
    soma = a+b
    return soma

r = somar(10,20)
print(r)


novo = somar(30,60)
print(novo)


novo2 = somar(novo,r)
print(novo2)


print("------------------")
def somar(a,b,c):
    soma = a + b + c
    return soma




def somar2(a, b=10, c=5):
    soma = a + b + c
    return soma



print(somar2(10))
print(somar2(10, 1))
print(somar2(10, 1, 40))

print(somar2(12, c=12))