num_max = 10
curr = 0

while curr < num_max:
    print(curr)
    curr += 1 # curr = curr + 1

# TODO: Contador de 10 a 0
# curr = 0
while num_max >= curr:
    print(num_max)
    num_max -= 1

print("---------------------")

num_max = 100
print("Linha 1")

while num_max > 0:
    print(num_max)
    num_max -= 10

    if num_max == 50:
        break   # termina o loop

print("\nLinha 2\n")

# TODO: loop que mostre os num pares entre 1 e 50, e usar inc de a cada volta
num_par = 1
while num_par <= 50:
    if num_par % 2 == 0:
        print(num_par)
    num_par+=1
# while


# for
