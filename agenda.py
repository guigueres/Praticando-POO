class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, nome, telefone):
        self.contatos.append(Contato(nome, telefone))

    def mostrar_contatos(self):
        for contato in self.contatos:
            print(f"{contato.nome} - {contato.telefone}")

if __name__ == "__main__":
    agenda = Agenda()
    agenda.adicionar_contato("Tom", "73981-1001")
    agenda.adicionar_contato("Gui", "73981-4002")
    agenda.mostrar_contatos()
