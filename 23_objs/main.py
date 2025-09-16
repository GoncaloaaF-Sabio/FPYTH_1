from Carro import Carro



c = Carro("BMW", "C3", 2023)

c1 = Carro("BMW", "C1")



print(f"o carro c e: {c.marca} {c.modelo} e é do ano {c.ano}")
print(f"o carro c1 e: {c1.marca} {c1.modelo} e é do ano {c1.ano}")

c1.ano = 3000
print(f"o carro c1 e: {c1.marca} {c1.modelo} e é do ano {c1.ano}")