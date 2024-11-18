# main.py

from ticket_factory import TicketAdministrativoFactory, TicketManutencaoFactory, TicketTItiFactory
from ticket_handler import SuporteAdministrativo, SuporteManutencao, SuporteTI

class SistemaTickets:
    def __init__(self):
        self.tickets = []
        self.usuario_logado = None
        
        # Instanciando as fábricas para cada grupo de trabalho
        self.fabrica_administrativo = TicketAdministrativoFactory()
        self.fabrica_manutencao = TicketManutencaoFactory()
        self.fabrica_ti = TicketTItiFactory()

        # Instanciando os suportes (Chain of Responsibility)
        self.suporte_administrativo = SuporteAdministrativo()
        self.suporte_manutencao = SuporteManutencao()
        self.suporte_ti = SuporteTI()
        
        # Configuração da cadeia: Administrativo -> Manutenção -> TI
        self.suporte_administrativo.set_proximo(self.suporte_manutencao)
        self.suporte_manutencao.set_proximo(self.suporte_ti)

    def alterar_status_ticket(self):
        if not self.usuario_logado:
            print("É necessário fazer login para alterar o status dos tickets.")
            return

        # Solicitar número do ticket
        numero_ticket = input("Informe o número do ticket para alterar o status: ")
        ticket = next((t for t in self.tickets if str(t.numero) == numero_ticket and t.solicitante == self.usuario_logado), None)
        
        if not ticket:
            print("Ticket não encontrado ou você não é o solicitante.")
            return

        print(f"Ticket encontrado: {ticket.numero} - {ticket.titulo} - Status atual: {ticket.status}")
        
        # Exibir opções de alteração de status
        if ticket.status == "Aberto":
            print("1. Avançar para 'Em Processo'")
        elif ticket.status == "Em Processo":
            print("1. Avançar para 'Encerrado'")
        elif ticket.status == "Encerrado":
            print("1. Reabrir para 'Em Processo'")
        else:
            print("Status inválido.")
            return

        opcao = input("Escolha uma opção (1): ")
        
        if opcao == "1":
            if ticket.status == "Aberto":
                ticket.status = "Em Processo"
                print(f"Status do ticket {ticket.numero} alterado para 'Em Processo'.")
            elif ticket.status == "Em Processo":
                ticket.status = "Encerrado"
                print(f"Status do ticket {ticket.numero} alterado para 'Encerrado'.")
            elif ticket.status == "Encerrado":
                ticket.status = "Em Processo"
                print(f"Ticket {ticket.numero} reaberto para 'Em Processo'.")
        else:
            print("Opção inválida.")

    def login(self):
        # Sistema de login simples
        print("Sistema de Login")
        usuario = input("Nome de usuário: ")
        senha = input("Senha: ")

        # Verificação de login (usuário: admin, senha: admin)
        if usuario == "admin" and senha == "admin":
            self.usuario_logado = usuario
            print("Login bem-sucedido!")
        else:
            print("Usuário ou senha incorretos.")
            self.usuario_logado = None

    def criar_ticket(self):
        if not self.usuario_logado:
            print("É necessário fazer login para criar tickets.")
            return

        # Coletar título e descrição do ticket
        titulo = input("Informe o título do ticket (curto): ")
        descricao = input("Informe a descrição do ticket (mais longa): ")

        # Menu para o grupo de trabalho
        grupo = ""
        while grupo not in ["Administrativo", "Manutenção", "TI"]:
            print("Selecione o grupo de trabalho:")
            print("1. Administrativo\n2. Manutenção\n3. TI")
            grupo_opcao = input("Escolha uma opção (1-3): ")
            if grupo_opcao == "1":
                grupo = "Administrativo"
            elif grupo_opcao == "2":
                grupo = "Manutenção"
            elif grupo_opcao == "3":
                grupo = "TI"
            else:
                print("Insira uma das alternativas.")

        # Menu para a prioridade
        prioridade = ""
        while prioridade not in ["Baixa", "Média", "Alta", "Urgente"]:
            print("Selecione a prioridade:")
            print("1. Baixa\n2. Média\n3. Alta\n4. Urgente")
            prioridade_opcao = input("Escolha uma opção (1-4): ")
            if prioridade_opcao == "1":
                prioridade = "Baixa"
            elif prioridade_opcao == "2":
                prioridade = "Média"
            elif prioridade_opcao == "3":
                prioridade = "Alta"
            elif prioridade_opcao == "4":
                prioridade = "Urgente"
            else:
                print("Insira uma das alternativas.")

        # Criar o ticket com a fábrica correspondente ao grupo de trabalho
        if grupo == "Administrativo":
            ticket = self.fabrica_administrativo.criar_ticket(titulo, descricao, self.usuario_logado, grupo, prioridade)
        elif grupo == "Manutenção":
            ticket = self.fabrica_manutencao.criar_ticket(titulo, descricao, self.usuario_logado, grupo, prioridade)
        elif grupo == "TI":
            ticket = self.fabrica_ti.criar_ticket(titulo, descricao, self.usuario_logado, grupo, prioridade)

        self.tickets.append(ticket)
        print(f"Ticket criado: Número {ticket.numero} - {ticket.titulo}")

    def consultar_tickets_por_status(self):
        if not self.usuario_logado:
            print("É necessário fazer login para consultar tickets.")
            return

        # Menu para consulta por status
        status = ""
        while status not in ["Aberto", "Em Processo", "Encerrado"]:
            print("Selecione o status para consulta:")
            print("1. Aberto\n2. Em Processo\n3. Encerrado")
            status_opcao = input("Escolha uma opção (1-3): ")
            if status_opcao == "1":
                status = "Aberto"
            elif status_opcao == "2":
                status = "Em Processo"
            elif status_opcao == "3":
                status = "Encerrado"
            else:
                print("Insira uma das alternativas.")

        # Exibir os tickets que correspondem ao status selecionado
        encontrados = [ticket for ticket in self.tickets if ticket.status == status and ticket.solicitante == self.usuario_logado]
        
        if encontrados:
            print(f"Tickets com status {status}:")
            for ticket in encontrados:
                print(f"{ticket.numero} - {ticket.titulo}\n- Descrição: {ticket.descricao}")
        else:
            print(f"Não há tickets com o status {status}.")

    def consultar_tickets_por_numero(self):
        if not self.usuario_logado:
            print("É necessário fazer login para consultar tickets.")
            return
        
        # Consultar por número
        numero_ticket = input("Informe o número do ticket que deseja consultar: ")
        encontrado = next((ticket for ticket in self.tickets if str(ticket.numero) == numero_ticket and ticket.solicitante == self.usuario_logado), None)
        
        if encontrado:
            print(f"Ticket {encontrado.numero} - {encontrado.titulo} - Status: {encontrado.status}\n- Descrição: {encontrado.descricao}")
        else:
            print("Ticket não encontrado ou você não é o solicitante desse ticket.")

    def consultar_tickets_por_grupo(self):
        if not self.usuario_logado:
            print("É necessário fazer login para consultar tickets.")
            return
        
        # Consultar por grupo de trabalho
        grupo = ""
        while grupo not in ["Administrativo", "Manutenção", "TI"]:
            print("Selecione o grupo de trabalho para consulta:")
            print("1. Administrativo\n2. Manutenção\n3. TI")
            grupo_opcao = input("Escolha uma opção (1-3): ")
            if grupo_opcao == "1":
                grupo = "Administrativo"
            elif grupo_opcao == "2":
                grupo = "Manutenção"
            elif grupo_opcao == "3":
                grupo = "TI"
            else:
                print("Insira uma das alternativas.")

        encontrados = [ticket for ticket in self.tickets if ticket.grupo == grupo and ticket.solicitante == self.usuario_logado]
        
        if encontrados:
            print(f"Tickets no grupo {grupo}:")
            for ticket in encontrados:
                print(f"{ticket.numero} - {ticket.titulo}\n- Descrição: {encontrado.descricao}")
        else:
            print(f"Não há tickets no grupo {grupo}.")

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Criar ticket")
            print("2. Consultar ticket")
            print("3. Alterar status de ticket")
            print("4. Sair")
            opcao = input("Escolha uma opção (1-4): ")

            if opcao == "1":
                self.criar_ticket()
            elif opcao == "2":
                self.menu_consultar_ticket()
            elif opcao == "3":
                self.alterar_status_ticket()
            elif opcao == "4":
                break
            else:
                print("Insira uma das alternativas.")


        

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

def main():
    sistema = SistemaTickets()

    # Fazer login
    sistema.login()
    
    if sistema.usuario_logado:
        sistema.menu()

if __name__ == "__main__":
    main()
