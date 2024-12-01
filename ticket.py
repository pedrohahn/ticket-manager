# ticket.py

class Ticket:
    _contador = 0

    def __init__(self, titulo, descricao, solicitante, grupo, executor, prioridade):
        Ticket._contador += 1
        self.numero = Ticket._contador
        self.titulo = titulo
        self.descricao = descricao
        self.solicitante = solicitante
        self.grupo = grupo
        self.prioridade = prioridade
        self.executor = executor
        self.status = "Aberto"

    def __str__(self):
        return (f"{self.numero} - {self.titulo} \n"
                f"Status: {self.status}, Grupo: {self.grupo}, "
                f"Prioridade: {self.prioridade}, "
                f"Executor: {self.executor} \n"
                f"Descrição: {self.descricao} ")


