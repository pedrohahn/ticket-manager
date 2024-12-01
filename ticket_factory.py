from ticket import Ticket


class TicketFactory:
    def criar_ticket(self, titulo, descricao, solicitante, grupo, prioridade):
        return Ticket(titulo, descricao, solicitante, grupo, self.executor, prioridade )


class TicketAdministrativoFactory(TicketFactory):
    executor = "João"


class TicketManutencaoFactory(TicketFactory):
    executor = "Rafael"


class TicketTItiFactory(TicketFactory):
    executor = "Rodrigo"

