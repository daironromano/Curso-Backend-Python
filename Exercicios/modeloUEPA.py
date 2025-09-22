class MembroUEPA:
    def __init__(self, nome, matricula, email):
        self.nome = nome
        self.matricula = matricula
        self.email = email

    def apresentar(self):
        print(f'Membro da UEPA')

class Aluno(MembroUEPA):
    def __init__(self, nome, matricula, email, curso, nota):
        super().__init__(nome, matricula, email)
        self.curso = curso
        self.nota = nota
    
    def verificar_notas(self):
        if self.nota < 5:
            print(f'Discente: {self.nome}\nMatrícula: {self.matricula}\nStatus: Reprovado')
        else:
            print(f'Discente: {self.nome}\nMatrícula: {self.matricula}\nStatus: Aprovado')

    def apresentar(self):
        super().apresentar()
        print(f'Discente: {self.nome}\nCurso: {self.curso}')

class Professor(MembroUEPA):
    def __init__(self, nome, matricula, email, departamento):
        super().__init__(nome, matricula, email)
        self.departamento = departamento
        self.frequencia = 0

    def lancar_frequencia(self, presente):
        if presente.lower() == 's':
            self.frequencia += 1
            print(f'Discente {self.nome} presente!\nFrequência: {self.frequencia}')
        else:
            print(f'Discente {self.nome} faltou!\nFrequência: {self.frequencia}')

    def apresentar(self):
        super().apresentar()
        print(f'Professor: {self.nome}\nDepartamento: {self.departamento}')

# Testando classe membro
Membro1 = MembroUEPA('dairon', 44005545, 'dr@gmail.com')
Membro1.apresentar()
print('\n')
# Testando classe aluno 
Aluno1 = Aluno('dairon', 44005545, 'dr@gmail.com', 'eng.comp', 7)
Aluno1.verificar_notas()
print('\n')
Aluno1.apresentar()
print('\n')
# Testando classe professor
Professor1 = Professor('dairon', 44005545, 'dr@gmail.com', 'Engenharia')
Professor1.lancar_frequencia('n')
print('\n')
Professor1.apresentar()