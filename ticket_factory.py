# ticket_factory.py

from ticket import Ticket

class TicketAdministrativoFactory:
    def criar_ticket(self, titulo, descricao, solicitante, grupo, prioridade):
        return Ticket(titulo, descricao, "Administrativo", solicitante, grupo, prioridade)

class TicketManutencaoFactory:
    def criar_ticket(self, titulo, descricao, solicitante, grupo, prioridade):
        return Ticket(titulo, descricao, "Manutenção", solicitante, grupo, prioridade)

class TicketTItiFactory:
    def criar_ticket(self, titulo, descricao, solicitante, grupo, prioridade):
        return Ticket(titulo, descricao, "TI", solicitante, grupo, prioridade)
