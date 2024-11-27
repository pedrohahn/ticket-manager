from ticket import Ticket


class TicketFactory:
    def criar_ticket(self, titulo, descricao, solicitante, grupo, prioridade):
        return Ticket(titulo, descricao, solicitante, grupo, prioridade)


class TicketAdministrativoFactory(TicketFactory):
    tipo = "Administrativo"


class TicketManutencaoFactory(TicketFactory):
    tipo = "Manutenção"


class TicketTItiFactory(TicketFactory):
    tipo = "TI"
