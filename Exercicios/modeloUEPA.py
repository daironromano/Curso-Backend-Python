class MembroUEPA:
    def __init__(self, nome, matricula, email):
        self.nome = nome
        self.matricula = matricula
        self.email = email

    def apresentar(self):
        print(f'Membro da UFPA')

class Aluno(MembroUEPA):
    def __init__(self, nome, matricula, email, curso, nota):
        super().__init__(nome, matricula, email)
        self.curso = curso
        self.nota = nota
    
    def verificar_notas(self, nome, matricula, nota):
        if self.nota < 5:
            print(f'Aluno: {self.nome}\nMatrícula: {self.matricula}\nStatus: Reprovado')
        else:
            print(f'Aluno: {self.nome}\nMatrícula: {self.matricula}\nStatus: Aprovado')

    def apresentar(self, nome, curso):
        print(f'{super().apresentar()}\nNome: {self.nome}\nCurso: {self.curso}')

class Professor(MembroUEPA):
    def __init__(self, nome, matricula, email, departamento):
        super().__init__(nome, matricula, email)
        self.departamento = departamento
        self.frequencia = 0

    def lancar_frequencia(self, frequencia):
        pass

    def apresentar(self):
        pass

# Testando classe membro
Membro1 = MembroUEPA('dairon', 44005545, 'dr@gmail.com')
Membro1.apresentar()

# Testando classe aluno 
Aluno1 = Aluno('dairon', 44005545, 'dr@gmail.com', 'eng.comp', 7)
Aluno1.verificar_notas('dairon', '44005545', 7)
Aluno1.apresentar('dairon', 'eng.comp')