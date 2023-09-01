from questao2 import Data
from typing import List
class Voo:
    assentos_ocupados:List[int] = []
    def __init__(self, numero:int, data:str, horario:str):
        self.numero = numero
        self.data = Data(data).data
        self.horario = horario
        self.quantidade_maxima = 100


    def proximo_Livre(self):
        for f in range(1,101):
            if f not in self.assentos_ocupados:
                escolha = f
                print(escolha)
                break

    def verifica(self,numero:int):
        if numero < 1 or numero >100:
            return 'Assento não existente'
        if numero in self.assentos_ocupados:
            return 'Asssento indisponivel.'
        return 'Assento disponivel.'
    
    def ocupa(self, numero:int):
        if numero < 1 or numero >100:
            return 'Assento não existente'
        if numero in self.assentos_ocupados:
            return 'Asssento indisponivel.'
        elif self.vagas() > 0:
            self.assentos_ocupados.append(numero)
            return 'Cadeira cadastrada'
        else:
            return ' Não há assentos disponiveis'

        

    def vagas(self):
        return self.quantidade_maxima - len(self.assentos_ocupados)
    

    def getVoo(self):
        return self.numero
    
    def getData(self):
        return self.data

    def clone(self):
        objeto_clonado_numero = Voo(self.data,self.horario,self.numero).numero
        objeto_clonado_data = Voo(self.data,self.horario,self.numero).data
        objeto_clonado_horario = Voo(self.data,self.horario,self.numero).horario
        return objeto_clonado_numero, objeto_clonado_data, objeto_clonado_horario
if __name__ == '__main__':
    voo1 = Voo(123,'26-09-2023','12:50')
    print(voo1.verifica(5))
    print(voo1.ocupa(5))
    print(voo1.vagas())
    print(voo1.assentos_ocupados)
    voo1.proximo_Livre()
    print(voo1.ocupa(1))
    voo1.proximo_Livre()
    print(voo1.getVoo())
    print(voo1.getData())
    print(voo1.clone())

