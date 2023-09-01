from questao1 import Animal
from questao2 import Peixe
from questao3 import Mamifero

class TestarAnimais:
    def main():
        camelo:Animal= Animal('Camelo',300,4,'Amarelo','Terra',2.0)
        tubarao:Peixe = Peixe('Tubarão',300,0,'Cinzento','Mar',1.5,'Barbatanas e cauda')
        ursocanada:Mamifero = Mamifero('Uso-do-canadá',180,4,'Vermelho','Terra',1.5, 'Mel')
        print('=======Dados Camelo========')
        camelo.dados()
        camelo.cor = 'Amarelo queimado'
        camelo.ambiente= 'Deserto'
        camelo.dados()
        print('=======Dados Tubarão========')
        tubarao.dados()
        tubarao.comprimento = 500
        tubarao.velocidade = 3.0 
        tubarao.dados()
        print('=======Dados Urso========')
        ursocanada.dados()
        ursocanada.comprimento = 2.0
        ursocanada.alimento = 'Peixe'
        ursocanada.dados()
    if __name__ == '__main__':
        main()
