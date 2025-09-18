
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.listaAmigos = []

    def envelhecer(self):
        self.idade += 1


    def getInfo(self):
        """
        funcao que retorna as informações da pessoa

        :return: string com os dados da pessoa
        :rtype: str

        """
        print("|", "-|-|" * 3, sep="") # print com o sepeparador
        return f'nome :{self.nome}\nidade:{self.idade}\nlistaAmigos:{self.listaAmigos}'

    def addAmigo(self, nome_amigo):
        self.listaAmigos.append(nome_amigo)
        print("Amigo adicionado com sucesso!")


#print("----")
pessoa = Pessoa('João', 22)
print(pessoa.getInfo())

#print("----")
pessoa2 = Pessoa('Rui', 64)
print(pessoa2.getInfo())
#print("----")


pessoa.envelhecer()
#print("----")
print(pessoa.getInfo())

#print("----")
pessoa2.envelhecer()
pessoa2.envelhecer()
pessoa2.envelhecer()
print(pessoa2.getInfo())
#print("----")