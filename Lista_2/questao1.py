class Animal: 
    def __init__(self,nome:str,comprimento:float,patas:int,
                 cor:str,ambiente:str,velocidade:float):
        self._nome = nome
        self._comprimento = comprimento
        self._patas = patas
        self._cor = cor
        self._ambiente = ambiente
        self._velocidade = velocidade

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,valor):
        self._nome = valor
    @property
    def comprimento(self):
        return self._comprimento
    @comprimento.setter
    def comprimento(self,valor):
        self._comprimento = valor
    @property
    def patas(self):
        return self._patas
    @patas.setter
    def patas(self,valor):
        self._patas = valor
    @property
    def cor(self):
        return self._cor
    @cor.setter
    def cor(self,valor):
        self._cor = valor

    @property
    def ambiente(self):
        return self._ambiente
    @ambiente.setter
    def ambiente(self,valor):
        self._ambiente = valor
    @property
    def velocidade(self):
        return self._velocidade
    @velocidade.setter
    def velocidade(self,valor):
        self._velocidade = valor
        

    def dados(self):
        print(self.nome)
        print(self.comprimento)
        print(self.patas)
        print(self.cor)
        print(self.ambiente)
        print(self.velocidade)
    
