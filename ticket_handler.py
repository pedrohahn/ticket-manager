# ticket_handler.py

from abc import ABC, abstractmethod
from ticket import Ticket

class Handler(ABC):
    def __init__(self):
        self.proximo = None

    def set_proximo(self, handler):
        self.proximo = handler

    @abstractmethod
    def tratar(self, ticket):
        pass


class SuporteAdministrativo:
    def set_proximo(self, proximo):
        self.proximo = proximo

    def tratar(self, ticket):
        if ticket.grupo == "Administrativo":
            print(f"Ticket {ticket.numero} tratado pelo Suporte Administrativo.")
            ticket.status = "Em Processo"
        elif self.proximo:
            self.proximo.tratar(ticket)

class SuporteManutencao:
    def set_proximo(self, proximo):
        self.proximo = proximo

    def tratar(self, ticket):
        if ticket.grupo == "Manutenção":
            print(f"Ticket {ticket.numero} tratado pelo Suporte Manutenção.")
            ticket.status = "Em Processo"
        elif self.proximo:
            self.proximo.tratar(ticket)

class SuporteTI:
    def set_proximo(self, proximo):
        self.proximo = proximo

    def tratar(self, ticket):
        if ticket.grupo == "TI":
            print(f"Ticket {ticket.numero} tratado pelo Suporte TI.")
            ticket.status = "Em Processo"
        elif self.proximo:
            self.proximo.tratar(ticket)

