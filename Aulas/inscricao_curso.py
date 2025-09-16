class InscricaoCurso:
    def __init__(self, aluno: str, curso: str):
        self.aluno = aluno
        self.curso = curso
        self.status = 'Pendente' #RF01

    def confirmar_matricula(self):
        if self.status == 'Pendente':
            if self.status == 'Confirmado':
                print('A matrícula está já confirmada! ')
            else:
                self.status = 'Confirmado'
                print(f'Matrícula confirmada!')
        else:
            print(f'[ERRO]: A matrícula de {self.aluno} não pode ser confirmada!')
    
    def cancelar_matricula(self):
        if self.status == 'Cancelada':
            print('Matrícula já está cancelada!')
        else:
            self.status = 'Cancelada'
            print(f'Matrícula de {self.aluno} cancelada!')

    def consulta_status(self):
        print(f'[Consulta] {self.aluno}: {self.status}')

inscricao = InscricaoCurso('Dairon', 'Backend Python')
inscricao.consulta_status()
inscricao.confirmar_matricula()
inscricao.consulta_status()
inscricao.cancelar_matricula()
inscricao.consulta_status()