class carro:
    def __init__(self, cor: str, motor:float):
        self.cor = cor
        self.motor = motor
        self.em_movimento = False

    def acelarar(self):
        self.em_movimento = True
        print(f"O carro {self.cor} está a acelerar")

    def travar(self):
        self.em_movimento = False
        print(f"O carro {self.cor} está a travar")

    def trocaCor(self, nova_cor:str):
        self.cor = nova_cor

    def mostraCor(self):
        print(f"Carro com cor {self.cor}")