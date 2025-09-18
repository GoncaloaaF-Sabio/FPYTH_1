class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.listaAmigos = []

    def envelhecer(self):
        self.idade += 1

    def getInfo(self):
        print("|", "-|-|" * 3, sep="") # print com o sepeparador
        return f'nome :{self.nome}\nidade:{self.idade}\nlistaAmigos:{self.listaAmigos}'

    def addAmigo(self, amigo):
        # validar se o amigo ≠ self

        self.listaAmigos.append(amigo)
        print("Amigo adicionado com sucesso!")

    def __str__(self):
           return  f'nome :{self.nome}\nidade:{self.idade}\nlistaAmigos:{self.listaAmigos}'

    def __repr__(self):
          return self.nome

p = Pessoa("Carlos", 22)
p2 = Pessoa("Maria", 25)
p3 = Pessoa("Rui", 30)

p.addAmigo(p2)
p.addAmigo(p3)


print(p.getInfo())
print("-------")
print(p)
print("-------")
print(p2)
print("-------")
print(p3)
print("-------")