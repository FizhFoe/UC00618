"""
# Listas 2

# criação lista vazia
lst = ["elm1", "elm2", "elm3", "elm4", "elm5"]
print(lst[2])
lst[2] = "nome"

print(lst[2])

lst = [1, 2, 3, 4, 5]
count = 0
# sempre que o ciclo de fora executa, o de dentro tbm executa 5 vezes, ou seja complexidade O(n^2)
for i in lst:
    for j in lst:
        count += 1
        print(f"{count}: {i} {j}")

# pouca eficiencia
lst.insert(2, "elm7")
lst.insert(2, "elm7")
lst.insert(2, "elm7")
print(lst)

print(lst.count("elm7")) # ocurrências dp elemento
print(lst.__len__())
print(len(lst))

lst.remove(4) # remove o valor do array, não o index/posição
print(lst)

lst.pop(2)
print(lst)

print(lst.index("elm7"))

"""

nomes = [
    "Ana", "João", "Maria", "Pedro", "Inês", "Miguel",
    "Catarina", "Tiago", "Sofia", "Diogo", "Beatriz",
    "Ricardo", "André", "Matilde", "Mariana", "Gonçalo",
    "Leonor", "Francisco", "Catarina"
]

print(nomes[-6])