# ticket.py

class Ticket:
    _contador = 0

    def __init__(self, titulo, descricao, solicitante, grupo, prioridade):
        Ticket._contador += 1
        self.numero = Ticket._contador
        self.titulo = titulo
        self.descricao = descricao
        self.solicitante = solicitante
        self.grupo = grupo
        self.prioridade = prioridade
        self.status = "Aberto"

    def __str__(self):
        return (f"{self.numero} - {self.titulo} \n"
                f"Status: {self.status}, Grupo: {self.grupo},"
                f"Prioridade: {self.prioridade} \n"
                f"Descrição: {self.descricao} ")

    def encerrar(self):
        self.status = "Encerrado"
        print(f"Ticket encerrado: {self.numero} - {self.titulo}")

    def reabrir(self):
        self.status = "Aberto"
        print(f"Ticket reaberto: {self.numero} - {self.titulo}")

    def encerrar(self):
        self.status = "Encerrado"
        print(f"Ticket encerrado: {self.descricao}")

    def reabrir(self):
        self.status = "Aberto"
        print(f"Ticket reaberto: {self.descricao}")
