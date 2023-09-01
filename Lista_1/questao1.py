class Aluno:
    def __init__(self,matricula,nome,nota1,nota2,notaT) -> None:
        self.matricula = matricula
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.notaT = notaT


    def media(self):
        media = ((self.nota1 * 2.5) + (self.nota2 * 2.5 ) + (self.notaT * 2))/(2.5+2.5+2)
        m_float = f'{media:.1f}'
        return float(m_float)
    
    def final(self):
        m = self.media()
        if m >= 7 :
            return 0
        else: 
            nota_necessaria = 7 - m
            return nota_necessaria




if __name__ == '__main__':
    aluno1 = Aluno(2123,'Blabla',2,3,4)
    print(aluno1.media()) 
    print(f'É necessário {aluno1.final()} para ser aprovado' )