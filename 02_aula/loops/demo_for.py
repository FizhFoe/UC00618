range(5) # 0 a 4 # range(n) -> 0 a n -1

for elm in range(10):
    print(elm)

print("------")
for elm in range(4):
    print(elm)

print("------")

range(2, 5) # 2 a 4 # range(m,n) -> m a n - 1
for elm in range(5, 10):
    print(elm)

print("------")
for elm in range(8, 12, 4): # 8 # range(m,n,s) -> m a n - 1 com step s
    print(elm)

print("------")
for elm in range(8, 50, 2):
    if elm == 36:
        break
    if elm % 2 == 1:
        continue
    print(elm)