# lista = ["Ma", 23, "Ze", "Leiria", True]
#
# print(lista[3])
# lista[3] = "Lisboa"
# print(lista[3])
#
# lista.append("Joana")
# print(lista)
#
import random
import random as rand

qtd = 100000

lista = []
for i in range(qtd):
    numero = random.randint(1, qtd)
    lista.append(i)

lista.sort()
print(lista)