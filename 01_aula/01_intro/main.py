idade = 20
if idade > 18:
    print("Adulto")

if idade == 20:
    print("20 anos")

idade = 14
if idade > 18:
    print("Adulto")
else:
    print("menos idade")

# # TODO: Crie uma app que receba 2 numeros e diga qual o maior
# num1 = int(input("Numero 1: "))
# num2 = int(input("Numero 2: "))
#
# if num1 > num2:
#     print("o maior num é: ", num1)
# elif num1 == num2:
#     print("Numeros iguais")
# else:
#     print(f"o maior num é: {num2}")
#

num = 9
match num:
    case 1:
        print("1")
    case 2:
        print("2")
    case 10:
        print("10")
    case _: # default
        print("Outro Valor")