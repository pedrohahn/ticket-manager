# main.py

from ticket_factory import TicketAdministrativoFactory, TicketManutencaoFactory, TicketTItiFactory
from ticket_handler import SuporteAdministrativo, SuporteManutencao, SuporteTI


class SistemaTickets:
    def __init__(self):
        self.tickets = []
        self.usuario_logado = None

        # Instanciando fábricas e handlers
        self.fabricas = {
            "Administrativo": TicketAdministrativoFactory(),
            "Manutenção": TicketManutencaoFactory(),
            "TI": TicketTItiFactory(),
        }

        self.handlers = self.configurar_handlers()

    def configurar_handlers(self):
        suporte_administrativo = SuporteAdministrativo()
        suporte_manutencao = SuporteManutencao()
        suporte_ti = SuporteTI()

        # Configurar cadeia
        suporte_administrativo.set_proximo(suporte_manutencao)
        suporte_manutencao.set_proximo(suporte_ti)
        return suporte_administrativo

    def login(self):
        print("Sistema de Login")
        usuario = input("Nome de usuário: ")
        senha = input("Senha: ")

        # Login fixo para simplificação
        if usuario == "admin" and senha == "admin":
            self.usuario_logado = usuario
            print("Login bem-sucedido!")
        else:
            print("Usuário ou senha incorretos.")

    def criar_ticket(self):
        if not self.usuario_logado:
            print("É necessário fazer login para criar tickets.")
            return

        titulo = input("Título do ticket: ")
        descricao = input("Descrição do ticket: ")
        grupo = self.selecionar_opcao("grupo", ["Administrativo", "Manutenção", "TI"])
        prioridade = self.selecionar_opcao("prioridade", ["Baixa", "Média", "Alta", "Urgente"])

        fabrica = self.fabricas.get(grupo)
        ticket = fabrica.criar_ticket(titulo, descricao, self.usuario_logado, grupo, prioridade)
        self.tickets.append(ticket)

        print(f"Ticket criado com sucesso! Número: {ticket.numero} - {ticket.titulo}")

    def alterar_status_ticket(self):
        if not self.usuario_logado:
            print("É necessário fazer login para alterar status de tickets.")
            return

        numero_ticket = input("Número do ticket: ")
        ticket = next((t for t in self.tickets if t.numero == int(numero_ticket) and t.solicitante == self.usuario_logado), None)

        if not ticket:
            print("Ticket não encontrado ou você não é o solicitante.")
            return

        novo_status = self.definir_novo_status(ticket)
        if novo_status:
            ticket.status = novo_status
            print(f"Status do ticket {ticket.numero} alterado para {novo_status}.")

    def menu(self):
        opcoes = {
            "1": ("Criar ticket", self.criar_ticket),
            "2": ("Consultar tickets", self.menu_consultar_ticket),
            "3": ("Alterar status de ticket", self.alterar_status_ticket),
            "4": ("Sair", exit),
        }
        while True:
            print("\nMenu:")
            for k, (desc, _) in opcoes.items():
                print(f"{k}. {desc}")
            opcao = input("Escolha uma opção: ")
            _, acao = opcoes.get(opcao, (None, lambda: print("Opção inválida.")))
            acao()

    def menu_consultar_ticket(self):
        while True:
            print("\nConsultar Ticket:")
            print("1. Por status")
            print("2. Por número")
            print("3. Por grupo de trabalho")
            print("4. Voltar")
            opcao = input("Escolha uma opção (1-4): ")

            if opcao == "1":
                self.consultar_tickets_por_status()
            elif opcao == "2":
                self.consultar_tickets_por_numero()
            elif opcao == "3":
                self.consultar_tickets_por_grupo()
            elif opcao == "4":
                break
            else:
                print("Insira uma das alternativas.")

    def consultar_tickets_por_status(self):
        if not self.usuario_logado:
            print("É necessário fazer login para consultar tickets.")
            return

        # Menu para consulta por status
        print("\nConsultar Tickets por Status:")
        status_opcoes = {
            "1": "Aberto",
            "2": "Em Processo",
            "3": "Encerrado"
        }

        print("1. Aberto\n2. Em Processo\n3. Encerrado")
        status_opcao = input("Escolha uma opção (1-3): ")
        status = status_opcoes.get(status_opcao)

        if not status:
            print("Opção inválida.")
            return

        encontrados = [ticket for ticket in self.tickets if ticket.status == status and ticket.solicitante == self.usuario_logado]

        if encontrados:
            print(f"\nTickets com status '{status}':")
            for ticket in encontrados:
                print(ticket)
        else:
            print(f"\nNão há tickets com o status '{status}'.")

    def consultar_tickets_por_numero(self):
        if not self.usuario_logado:
            print("É necessário fazer login para consultar tickets.")
            return

        # Consultar por número
        print("\nConsultar Tickets por Número:")
        numero_ticket = input("Informe o número do ticket que deseja consultar: ")
        encontrado = next((ticket for ticket in self.tickets if str(ticket.numero) == numero_ticket and ticket.solicitante == self.usuario_logado), None)

        if encontrado:
            print("\nDetalhes do Ticket Encontrado:")
            print(encontrado)
        else:
            print("\nTicket não encontrado ou você não é o solicitante.")

    def consultar_tickets_por_grupo(self):
        if not self.usuario_logado:
            print("É necessário fazer login para consultar tickets.")
            return

        # Consultar por grupo de trabalho
        print("\nConsultar Tickets por Grupo:")
        grupo_opcoes = {
            "1": "Administrativo",
            "2": "Manutenção",
            "3": "TI"
        }

        print("1. Administrativo\n2. Manutenção\n3. TI")
        grupo_opcao = input("Escolha uma opção (1-3): ")
        grupo = grupo_opcoes.get(grupo_opcao)

        if not grupo:
            print("Opção inválida.")
            return

        encontrados = [ticket for ticket in self.tickets if ticket.grupo == grupo and ticket.solicitante == self.usuario_logado]

        if encontrados:
            print(f"\nTickets no grupo '{grupo}':")
            for ticket in encontrados:
                print(ticket)
        else:
            print(f"\nNão há tickets no grupo '{grupo}'.")


    def selecionar_opcao(self, campo, opcoes):
        print(f"Selecione uma {campo}:")
        for i, opcao in enumerate(opcoes, 1):
            print(f"{i}. {opcao}")
        while True:
            escolha = input("Escolha uma opção: ")
            if escolha.isdigit() and 1 <= int(escolha) <= len(opcoes):
                return opcoes[int(escolha) - 1]
            print("Escolha inválida.")

    def definir_novo_status(self, ticket):
        status_map = {
            "Aberto": "Em Processo",
            "Em Processo": "Encerrado",
            "Encerrado": "Em Processo",
        }
        proximo_status = status_map.get(ticket.status)
        if not proximo_status:
            print("Status inválido.")
            return None

        print(f"Alterar status de '{ticket.status}' para '{proximo_status}'? (s/n)")
        return proximo_status if input().lower() == "s" else None


def main():
    sistema = SistemaTickets()
    sistema.login()
    if sistema.usuario_logado:
        sistema.menu()


if __name__ == "__main__":
    main()
