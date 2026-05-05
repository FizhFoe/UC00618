"""
Nome: Emanuel Simão
Turma: TETPSI Leiria
"""
letra = input("Insira uma letra: ")

match letra:
    case 'F':
        print("Feminino")
    case 'M':
        print("Masculino")
    case _:
        print("Inválido")