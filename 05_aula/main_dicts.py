pessoa = {
    "nome": "Maria",
    "idade": 26,
    "escola": "IEFP",
}

print(pessoa)
print(pessoa["nome"])

pessoa["idade"] = 30
print(pessoa)
pessoa["Estado"] = True
print(pessoa)

print(pessoa.get("estado", "sem Estado"))

print(pessoa.pop("idade")) # 30
print(pessoa)

print(pessoa.popitem()) # ('Estado', True)
print(pessoa)

del pessoa["escola"]
del pessoa["nome"]
print(pessoa)

# del pessoa
# print(pessoa)

pessoa = {
    "nome": "Leo",
    "idade": 20,
    "escola": "IPL"
}

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

for elm in pessoa:
    print(elm)