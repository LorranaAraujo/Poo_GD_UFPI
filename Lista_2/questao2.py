from questao1 import Animal

def relatorio_peixe(metodo_dados):
    def adicionar_caracteristica(self):
        metodo_dados(self)
        print(self.nome)
        print(self.comprimento)
        print(self.patas)
        print(self.cor)
        print(self.ambiente)
        print(self.velocidade)
        print(self.caracteristica)
    return adicionar_caracteristica
        

class Peixe(Animal):
    def __init__(self, nome: str, comprimento: float, patas: int,
                  cor: str, ambiente: str, velocidade: float, caracteristica:str):
        super().__init__(nome, comprimento, patas, cor, 
                         ambiente, velocidade)
        self._caracteristica = caracteristica

    @property
    def caracteristica(self):
        return self._caracteristica
    @caracteristica.setter
    def caracteristica(self,valor):
        self._caracteristica = valor

    @relatorio_peixe
    def dados(self):
        ...

