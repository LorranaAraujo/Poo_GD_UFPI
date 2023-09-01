from datetime import datetime

class Data:
    def __init__(self, data: str) -> None:
        self.data = data
        self.data_atual = datetime.today().strftime('%d-%m-%Y')
    
    def data_correta(self):
        if self.data != self.data_atual:
            self.data = '01-01-0001'
            return self.data
        else:
            return 'data correta'
        
    def compara(self, objeto):
        transformar_objeto= datetime.strptime(objeto.data, '%d-%m-%Y').date()
        transformar_data_atual = datetime.strptime(self.data_atual,'%d-%m-%Y').date()
        if  transformar_data_atual == transformar_objeto:
            return 0
        elif transformar_data_atual > transformar_objeto:
            return 1 
        elif transformar_data_atual < transformar_objeto:
            return -1 
       #data_atual = self.data_atual
    
    def getDia(self):
        data_objeto = self.data
        dia = data_objeto.split('-')
        return dia[0]
    
    def getMes(self):
        data_objeto = self.data
        mes = data_objeto.split('-')
        return mes[1]

    def getMesExtenso(self):
        data_objeto = self.data
        mes = data_objeto.split('-')[1]
        mes_extenso = ['Janeiro','Fevereiro','Março','Abril','Maio',
                       'Junho','Julho','Agosto','Setembro','Outubro',
                       'Novembro','Dezembro']
        meses = mes_extenso[int(mes)-1]
        return meses
        
    def getAno(self):
        data_objeto = self.data
        ano = data_objeto.split('-')[2]
        return ano
    
    def isBissexto(self):
        v_ano = int(self.getAno())
        if v_ano % 4 == 0 or v_ano % 400 == 0:
            return True
        return False


    def clone(self):
        data = Data(self.data).data
        return data
if __name__ == '__main__':
    teste1 = Data('30-08-2023')
    print(teste1.data)
    print(teste1.data_atual)
    print(teste1.data_correta())
    print(teste1.getDia())
    print(teste1.getMes())
    print(teste1.getMesExtenso())
    print(teste1.getAno())
    print(teste1.isBissexto())
    print(teste1.clone())

    teste2 = Data('30-08-2023')
    print(teste1.compara(teste2))