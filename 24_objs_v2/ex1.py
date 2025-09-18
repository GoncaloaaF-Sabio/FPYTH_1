"""
crie a Classe Bola: Crie uma classe que modele uma bola:
    Atributos: Cor, circunferência, material
    Métodos: trocaCor e mostraCor

instancie duas bolas com dados recebidos do utilizador (input)
"""

class Bola:
    def __init__(self, cor:str, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        print(self.cor)


cor = input("Digite o cor: ")
circunferencia = float(input("Digite o circunferencia: "))
material = input("Digite o material: ")

b1 = Bola(cor, circunferencia, material)

cor = input("Digite o cor: ")
circunferencia = float(input("Digite o circunferencia: "))
material = input("Digite o material: ")

b2 = Bola("azul", 31, "borracha")

nova_cor = input("Digite a nova cor: ")
b2.trocaCor(nova_cor)
