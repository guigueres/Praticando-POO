class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = [
            "Gênesis", "Êxodo", "Eclesiátes", "Números", "Deuteronômio",
            "Salmos", "Provérbios", "Isaías", "Mateus", "Apocalipse"
        ]

    def emprestar_livro(self):
        for i, livro in enumerate(self.livros, 1):
            print(f"{i} - {livro}")
        escolha = int(input("Escolha o número do livro: "))
        print(f"{self.nome} escolheu o livro '{self.livros[escolha - 1]}'")

if __name__ == "__main__":
    nome = input("Nome: ").title()
    biblioteca = Biblioteca(nome)
    biblioteca.emprestar_livro()
