from dataclasses import dataclass

@dataclass(frozen=True) # Torna a classe imutável
class AlunoData:
    nome: str
    matricula: int
    ativo: bool = True

# Simulação 
aluno1 = AlunoData('Dairon',  202206840032)
aluno2 = AlunoData('Daniel',  202506840032)

print(aluno1) # Utiliza o método: __str__
print(aluno1 == aluno2) # Utiliza o método: __eq__
