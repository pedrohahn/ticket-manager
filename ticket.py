# ticket.py

from datetime import datetime, timedelta

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
        self.sla = None
        self.data_limite = None

    def __str__(self):
        return (f"{self.numero} - {self.titulo} \n"
                f"Status: {self.status}, Grupo: {self.grupo}, "
                f"Prioridade: {self.prioridade}, "
                f"Executor: {self.executor}, "
                f"SLA: {self.sla}, Data Limite: {self.data_limite}\n"
                f"Descrição: {self.descricao} ")


