"""
List Comprehension

for elm in lst:
    if elm % 2 == 0:
        nova_lista.append(elm * 2)

print(lst)
print(nova_lista)
"""
"""
import random

lst = []
for num in range(1000):
    numero = random.randint(1, 1000)
    lst.append(numero)
lst.sort()
nova_lista = [elm * 2 for elm in lst if elm % 2 == 0]

print(lst)
print(nova_lista)
"""

nomes = [
    "Ana", "João", "Maria", "Pedro", "Inês", "Miguel",
    "Catarina", "Tiago", "Sofia", "Diogo", "Beatriz",
    "Ricardo", "André", "Matilde", "Mariana", "Gonçalo",
    "Leonor", "Francisco", "Catarina", "Carolina", "Tomás",
    "Rita", "David", "Sara", "Luis", "Clara"
]

# print(len(nomes[0]))

# Crie uma lista com o num de letras de cada nome em nomes
contar_ltr = [len(nome) for nome in nomes]
print(contar_ltr)

# Crie uma lista com o num de letras de cada nome terminado em A na lista de nome
# conta_ltr2 = [len(nome) for nome in nomes if nome[-1] == "a"]
conta_ltr2 = [len(nome) for nome in nomes if nome[-1].lower() == "a"]
print(conta_ltr2)
print("------------------------------------")
# Crie uma lista com o nome e numero de letras correspondente de todos os nomes na lista nome com:
#   - mais de 4 letras
print("A")
lista_nome = [f"{nome} -> {len(nome)}" for nome in nomes if len(nome) > 7]
print(*lista_nome)

print("\nB")
lista_nome2 = [(nome, len(nome)) for nome in nomes if len(nome) > 4]
for elm in lista_nome2:
    nome, letras = elm
    print(nome, letras)

print("------------------------------------")

# encontre o maior num
lst = [1, 3, 45, 535, 33, 65767, 23, 323]

maior = lst[0] # só para igualar a um valor válido
for elm in lst:
    if elm > maior:
        maior = elm

print(maior)
print("------------------------------------")
# mostre o maior nome usando apenas a lista lista_nome sem usar o len
# caso A
max_name = lista_nome2[0]
# print(max_name)
for elm in lista_nome2:
    if elm[1] > max_name[1]:
        max_name = elm
print(max_name)

# mostre o menor nome usando apenas a lista lista_nome sem usar o len
# caso A
min_name = lista_nome2[0]
for elm in lista_nome2:
    if elm[1] < min_name[1]:
        min_name = elm
print(min_name)

