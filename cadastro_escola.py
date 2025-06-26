class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Aluno(Pessoa):
    pass

class Professor(Pessoa):
    pass

class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = set()
        self.professores = set()

    def adicionar_aluno(self, aluno):
        self.alunos.add(aluno.nome)

    def adicionar_professor(self, professor):
        self.professores.add(professor.nome)

    def exibir_info(self):
        print(f"Curso: {self.nome}")
        print("Alunos:", self.alunos)
        print("Professores:", self.professores)

if __name__ == "__main__":
    curso = Curso("Matemática")
    aluno1 = Aluno("Vanim")
    aluno2 = Aluno("Kiko")
    prof = Professor("Carlos Victor")
    curso.adicionar_aluno(aluno1)
    curso.adicionar_aluno(aluno2)
    curso.adicionar_professor(prof)
    curso.exibir_info()
