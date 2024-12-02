#ticket_handler.py

from datetime import datetime, timedelta

class Handler:
    def __init__(self):
        self.proximo = None

    def set_proximo(self, handler):
        self.proximo = handler

    def tratar(self, ticket):
        # Só deve tratar tickets com status "Aberto"
        if ticket.status == "Aberto":
            if self.pode_tratar(ticket):
                print(f"Ticket {ticket.numero} tratado pelo Suporte {ticket.grupo}.")
                ticket.status = "Em Processo"  # Avança para "Em Processo"
            elif self.proximo:
                self.proximo.tratar(ticket)

    def pode_tratar(self, ticket):
        return False


class SuporteAdministrativo(Handler):
    def pode_tratar(self, ticket):
        return ticket.grupo == "Administrativo"

    def tratar(self, ticket):
        if self.pode_tratar(ticket):
            sla_horas = 72
            self.definir_sla(ticket, sla_horas)
        elif self.proximo:
            self.proximo.tratar(ticket)

    def definir_sla(self, ticket, horas):
        ticket.sla = f"{horas} horas"
        ticket.data_limite = datetime.now() + timedelta(hours=horas)


class SuporteManutencao(Handler):
    def pode_tratar(self, ticket):
        return ticket.grupo == "Manutenção"

    def tratar(self, ticket):
        if self.pode_tratar(ticket):
            sla_horas = 24
            self.definir_sla(ticket, sla_horas)
        elif self.proximo:
            self.proximo.tratar(ticket)

    def definir_sla(self, ticket, horas):
        ticket.sla = f"{horas} horas"
        ticket.data_limite = datetime.now() + timedelta(hours=horas)

class SuporteTI(Handler):
    def pode_tratar(self, ticket):
        return ticket.grupo == "TI"

    def tratar(self, ticket):
        if self.pode_tratar(ticket):
            # SLA para TI (exemplo: 1 dia)
            sla_horas = 120
            self.definir_sla(ticket, sla_horas)
        elif self.proximo:
            self.proximo.tratar(ticket)

    def definir_sla(self, ticket, horas):
        ticket.sla = f"{horas} horas"
        ticket.data_limite = datetime.now() + timedelta(hours=horas)