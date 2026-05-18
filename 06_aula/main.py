from Carro import carro
from bola import Bola

c1 = carro("Amarelo", 1.6)

print(c1.cor)
print(c1.motor)

c2 = carro("Rosa", 2.0)

print(f"c2 {c2.cor}")
print(f"c2 {c2.motor}")

c3 = c1
print(f"c3 {c3.cor}")
print(f"c3 {c3.motor}")

c3.motor = 1.8
print("c3", c3.motor)
print("c1", c1.motor)

c1.acelarar()
c2.travar()

print("-------------")
c1.trocaCor("Azul")
c1.mostraCor()

