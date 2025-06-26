class Viagem:
    def __init__(self, nome):
        self.nome = nome
        self.destinos = ["Xique-Xique", "Ilheus", "Ibicarai", "Itapetinga", "Floresta"]

    def escolher_destino(self):
        for i, destino in enumerate(self.destinos, 1):
            print(f"{i} - {destino}")
        escolha = int(input("Escolha o número do destino: "))
        print(f"{self.nome} escolheu viajar para {self.destinos[escolha - 1]}")

if __name__ == "__main__":
    nome = input("Nome do viajante: ")
    viagem = Viagem(nome)
    viagem.escolher_destino()
