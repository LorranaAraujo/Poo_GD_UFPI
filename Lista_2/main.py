from questao4 import TestarAnimais

def main():
    while True: 
        print('Digite 1 para testar animais ou 2 para encerrar.')
        x = int(input('Digite a opção desejada:'))
        if x == 1:
            TestarAnimais.main()
        elif x == 2:
            print('Programa encerrado')
            break
        else:
            print('Opção Inválida')

main()