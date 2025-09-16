"""

Crie uma class aluno
    nome
    email
    turma
    lista notas com um valor pre-definido de []


crie um aluno onde adiciona a lista de notas
crie um aluno onde sem adicionar a lista de notas

mostre as informações dos 2 alunos


"""

class Aluno:
    def __init__(self, nome:str, email:str, turma:str, notas = []):
        self.nome = nome
        self.email = email
        self.turma = turma
        self.notas = notas


al = Aluno("aluno1", "email1", "turma1")
print(f"aluno1: {al.nome}, email1: {al.email}, turma1: {al.turma}\nNotas do aluno1: {al.notas} ")

print("---" * 10)
al2 = Aluno("aluno2", "email1", "turma1", [12,14,18,20])
print(f"aluno1: {al2.nome}, email1: {al2.email}, turma1: {al2.turma}\nNotas do aluno1: {al2.notas} ")
