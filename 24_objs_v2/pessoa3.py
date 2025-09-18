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

    def __str__(self):
           return  f'nome :{self.nome}\nidade:{self.idade}\nlistaAmigos:{self.listaAmigos}'

    def __repr__(self):
          return self.nome


nova_pessoa = Pessoa3('Gonçalo',22, Morada("Rua 1",
                                           "A1",
                                           "4C",
                                           "2785-123",
                                           "Sintra"))

addr  = Morada("Rua 1", "A1","4C", "2785-123", "Sintra")

nova_pessoa = Pessoa3('Gonçalo',22,addr)