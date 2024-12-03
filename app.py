from flask import Flask, render_template, request, redirect, url_for, session
from ticket import Ticket
from ticket_factory import TicketAdministrativoFactory, TicketManutencaoFactory, TicketTItiFactory
from datetime import datetime, timedelta
from ticket_handler import SuporteAdministrativo, SuporteManutencao, SuporteTI


suporte_administrativo = SuporteAdministrativo()
suporte_manutencao = SuporteManutencao()
suporte_ti = SuporteTI()

suporte_administrativo.set_proximo(suporte_manutencao)
suporte_manutencao.set_proximo(suporte_ti)

app = Flask(__name__)
app.secret_key = 'alguma_chave' 

tickets = []
usuario_logado = None

fabricas = {
    "Administrativo": TicketAdministrativoFactory(),
    "Manutenção": TicketManutencaoFactory(),
    "TI": TicketTItiFactory(),
}


usuarios_validos = {
    'admin': 'admin',  # Username: password
    'usuario': 'usuario123',
}

@app.route('/')
def index():
    if 'usuario_logado' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'usuario_logado' in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        
        if usuarios_validos.get(usuario) == senha:
            session['usuario_logado'] = usuario
            return redirect(url_for('index'))
        else:
            return render_template('login.html', erro="Usuário ou senha inválidos")
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('usuario_logado', None)
    return redirect(url_for('login'))

@app.route('/criar_ticket', methods=['GET', 'POST'])
def criar_ticket():
    if 'usuario_logado' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        grupo = request.form['grupo']
        prioridade = request.form['prioridade']
        
        fabrica = fabricas.get(grupo)
        ticket = fabrica.criar_ticket(titulo, descricao, session['usuario_logado'], grupo, prioridade)
        tickets.append(ticket)
        
        return redirect(url_for('consultar_ticket'))
    
    return render_template('criar_ticket.html')

@app.route('/consultar_ticket')
def consultar_ticket():
    if 'usuario_logado' not in session:
        return redirect(url_for('login'))
    return render_template('consultar_ticket.html', tickets=tickets)

@app.route('/alterar_status/<int:numero>', methods=['GET', 'POST'])
def alterar_status(numero):
    if 'usuario_logado' not in session:
        return redirect(url_for('login'))

    ticket = next((t for t in tickets if t.numero == numero), None)
    if ticket:
        if request.method == 'POST':
            novo_status = request.form['status']
            ticket.status = novo_status
            ticket.data_limite = datetime.now() + timedelta(hours=48)  # Exemplo de alteração do prazo
            return redirect(url_for('consultar_ticket'))
        
        return render_template('alterar_status.html', ticket=ticket)

    return redirect(url_for('consultar_ticket'))

if __name__ == '__main__':
    app.run(debug=True)
