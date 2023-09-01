from questao1 import Animal

def relatorio_mamifero(metodo_dados):
    def adicionar_alimento(self):
        metodo_dados(self)
        print(self.nome)
        print(self.comprimento)
        print(self.patas)
        print(self.cor)
        print(self.ambiente)
        print(self.velocidade)
        print(self.alimento)
    return adicionar_alimento


class Mamifero(Animal):
    def __init__(self, nome: str, comprimento: float, patas: int, cor: str, ambiente: str, velocidade: float, alimento:str):
        super().__init__(nome, comprimento, patas, cor, ambiente, velocidade)
        self._alimento = alimento

    @property
    def alimento(self):
        return self._alimento
    @alimento.setter
    def alimento(self,valor):
        self._alimento = valor

    @relatorio_mamifero
    def dados(self):
        ...



