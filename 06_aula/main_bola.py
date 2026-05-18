from bola import Bola
"""
Classe Bola:
    Crie uma classe que modele uma bola:
    atributos: cor, circuferencia e material
"""

b1 = Bola("verde", 10.6, "carbono")
b2 = Bola("vermelha", 3.7, "plastico")
b3 = Bola("preta", 34.7, "silicone")

for bola in (b1, b2, b3):
    print(f"{bola.cor} {bola.material}")

"""
Lista com as bolas e mostrar a cor e o material de todas as bolas na lista
"""
bolas = [b1, b2, b3]
print("--------")
for bola in bolas:
    print(f"{bola.cor} - {bola.material}")