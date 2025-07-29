dct = {"key 1": "abc",
       "key 2": "Valor 2",
       "key 3": "Valor 3"}

print(dct["key 1"])




"""
{
  "userId": 1,
  "id": 3,
  "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
  "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
}
"""
dct2 = {"key 1": "abc",
        "key 2": 123,
        "key 3": True,
        "key 4": 12.21 }

print(dct2)


dct3 = {"key 1": "abc",
        "key 2": 123,
        "key 3": True,
        "key 1": 12.21 }

print(dct3)

print("-----------------")

print(dct2["key 1"])
print(dct2.get("key 1"))


print("---")

# print(dct2["key 5"]) # key invalida -> erro
print(dct2.get("key 5")) # key invalida -> None -> null -> nil


dct2["Nova Key"] = 123


dct2["key 1"] = "Novo valor"
print(dct2)

dct2.update({"nova Key 2": "Novo valor 2"})

print(dct2)

dct2.update({"nova Key 2": "outro Novo valor 2"})

print(dct2)


d1 = {
    "nome":"Gonçalo",
    "idade": 39
}

d2 = {
    "centro":"Sabio do lago",
    "Ativo": True
}

print(d1)
d1.update(d2)

print(d1)

print(d1.keys())
print(d1.values())
print(d1.items())


"""
Criar
ler val
add val
juntar 2 dict
conjunto keys
conjunto values
conjunto pars

"""

print("---" * 10)

print(d1)

print(d1.pop("idade")) # remove o par com a chave indicada -> devolve o val

print(d1)

print(d1.popitem()) # remove o ultimo ultimo -> devolver o par removido

print(d1)

# print(d1.pop("idade")) # a chave tem de existir

del d1["centro"] # remove o par com a chave indicada ->

print(d1)

# del d1["centro"] # a chave tem de existir


d1 = {
    "nome":"Gonçalo",
    "idade": 39
}

d2 = {
    "centro":"Sabio do lago",
    "Ativo": True
}


d1.update(d2)

print(d1)

d1.clear()

print(d1)

d1["nome"] = "Gonçalo"


print("--rev listas--")
lst = [1,2,3,4]

for elm in lst:
    print(elm)

print("fim rev listas")


d1 = {
    "nome":"Gonçalo",
    "idade": 39
}

d2 = {
    "centro":"Sabio do lago",
    "Ativo": True
}


d1.update(d2)

print("\n\nfor elm in d1\n")
for elm in d1: # <=>  d1.keys():
    print(elm)

print("\n\nfor elm in d1.values()\n")
for elm in d1.values():
    print(elm)


print("\n\nfor elm in d1.items()\n")
for elm in d1.items():
    print(f"key: {elm[0]} val: {elm[1]}")
