class Feira:
    def __init__(self, nome):
        self.nome = nome
        self.frutas = ["Maçã", "Banana", "Laranja", "Manga", "Uva", "Melancia", "Pera", "Morango", "Kiwi", "Abacaxi"]

    def escolher_fruta(self):
        for i, fruta in enumerate(self.frutas, 1):
            print(f"{i} - {fruta}")
        escolha = int(input("Escolha o número da fruta: "))
        print(f"{self.nome} escolheu a fruta '{self.frutas[escolha - 1]}'")

if __name__ == "__main__":
    nome = input("Nome: ").title()
    feira = Feira(nome)
    feira.escolher_fruta()
