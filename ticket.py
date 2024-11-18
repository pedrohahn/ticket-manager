# ticket.py

class Ticket:
    _contador = 0  # Contador de tickets para atribuir número único

    def __init__(self, descricao, tipo):
        Ticket._contador += 1
        self.numero = Ticket._contador  # Número único do ticket
        self.descricao = descricao
        self.tipo = tipo
        self.status = "Aberto"  # status pode ser 'Aberto', 'Em Processo', 'Encerrado'
# ticket.py

class Ticket:
    _contador = 0  # Contador de tickets para atribuir número único

    def __init__(self, titulo, descricao, tipo, solicitante, grupo, prioridade):
        Ticket._contador += 1
        self.numero = Ticket._contador  # Número único do ticket
        self.titulo = titulo
        self.descricao = descricao
        self.tipo = tipo
        self.solicitante = solicitante
        self.grupo = grupo
        self.prioridade = prioridade
        self.status = "Aberto"  # status pode ser 'Aberto', 'Em Processo', 'Encerrado'

    def __str__(self):
        return f"{self.numero} - {self.titulo} (Tipo: {self.tipo}, Status: {self.status}, Solicitante: {self.solicitante}, Grupo: {self.grupo}, Prioridade: {self.prioridade})"

    def encerrar(self):
        self.status = "Encerrado"
        print(f"Ticket encerrado: {self.numero} - {self.titulo}")

    def reabrir(self):
        self.status = "Aberto"
        print(f"Ticket reaberto: {self.numero} - {self.titulo}")

    def __str__(self):
        return f"{self.numero} - {self.descricao} (Tipo: {self.tipo}, Status: {self.status})"

    def encerrar(self):
        self.status = "Encerrado"
        print(f"Ticket encerrado: {self.descricao}")

    def reabrir(self):
        self.status = "Aberto"
        print(f"Ticket reaberto: {self.descricao}")
