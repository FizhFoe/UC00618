class Quadrado:
    def __init__(self, tam_lado: float):
        self.tamanho = tam_lado

    def mudaLado(self, novo_valor: float):
        self.tamanho = novo_valor

    def mostraValor(self):
        print(f"Tamanho lateral do quadrado {self.tamanho}")

    def calculaArea(self):
        lado = self.tamanho
        area_quadrado = lado * lado
        print(f"Área do Quadrado: {area_quadrado}")