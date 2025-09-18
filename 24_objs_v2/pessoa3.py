class Morada:
    def __init__(self, rua, porta, apt, cp, local):
        self.rua = rua
        self.porta = porta
        self.apt = apt
        self.cp = cp
        self.local = local

    def metodo_morada(self):
        pass

class Pessoa3:
    def __init__(self, nome, idade, morada:Morada):
        self.nome = nome
        self.idade = idade
        self.listaAmigos = []
        self.morada = morada

    def envelhecer(self):
        self.idade += 1

    def getInfo(self):
        print("|", "-|-|" * 3, sep="") # print com o sepeparador
        return f'nome :{self.nome}\nidade:{self.idade}\nlistaAmigos:{self.listaAmigos}'

    def addAmigo(self, amigo):
        # validar se o amigo ≠ self

        self.listaAmigos.append(amigo)
        print("Amigo adicionado com sucesso!")

    def mostrar_rua(self):
        print(self.morada.rua)

    def __str__(self):
           return  f'nome :{self.nome}\nidade:{self.idade}\nlistaAmigos:{self.listaAmigos}'

    def __repr__(self):
          return self.nome


nova_pessoa = Pessoa3('Gonçalo',22, Morada("Rua 1",
                                           "A1",
                                           "4C",
                                           "2785-123",
                                           "Sintra"))

addr  = Morada("Rua 2", "A1","4C", "2785-123", "Sintra")

nova_pessoa2 = Pessoa3('Gonçalo',22,addr)


print(nova_pessoa2.morada.rua)
print(nova_pessoa.morada.rua)


n = input("nome: ")
idd = int(input("idade: "))
addr2  = Morada("Rua 2", "A1","4C", "2785-123", "Sintra")

nova_pessoa5 = Pessoa3(n, idd, addr2)
print(nova_pessoa5)
