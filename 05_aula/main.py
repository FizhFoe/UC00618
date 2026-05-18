myset = {"alho", "cebola", "aveia", "chocolate", "leite"}


myset.add("ovos")
myset.remove("alho")
print(myset)
print(len(myset))

print(myset.pop()) # remove um elm random
myset.add("Ovos")
myset2 = {"Farinha", "Oleo", "Ovos", "Açucar", "Iogurte"}

print(myset.union(myset2))
print(myset | myset2)
print(myset.intersection(myset2))
print(myset & myset2)

print(myset.difference(myset2))
print(myset - myset2)

print(myset.symmetric_difference((myset2)))
print(myset ^ myset2)

set1 = {i for i in range(1, 11)}
set2 = {i for i in range(0, 12, 2)}
set3 = {i for i in range(10, 21)}
print(set1)
print(set2)
print(set3)

