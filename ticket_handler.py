class Handler:
    def __init__(self):
        self.proximo = None

    def set_proximo(self, handler):
        self.proximo = handler

    def tratar(self, ticket):
        if self.pode_tratar(ticket):
            print(f"Ticket {ticket.numero} tratado pelo Suporte {ticket.grupo}.")
            ticket.status = "Em Processo"
        elif self.proximo:
            self.proximo.tratar(ticket)

    def pode_tratar(self, ticket):
        return False


class SuporteAdministrativo(Handler):
    def pode_tratar(self, ticket):
        return ticket.grupo == "Administrativo"


class SuporteManutencao(Handler):
    def pode_tratar(self, ticket):
        return ticket.grupo == "Manutenção"


class SuporteTI(Handler):
    def pode_tratar(self, ticket):
        return ticket.grupo == "TI"
