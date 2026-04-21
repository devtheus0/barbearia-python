from flask import Flask, render_template, request, redirect, url_for, flash, session
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'barbearia_imperio_secret_key'

# Dados globais
clientes = []
servicos = []
agendamentos = []

horarios = [
    '08:00', '09:00', '10:00', '11:00', '12:00',
    '13:00', '14:00', '15:00', '16:00', '17:00',
    '18:00', '19:00', '20:00', '21:00', '22:00'
]

# ================= FUNÇÕES DE DADOS =================

def salvar_dados():
    dados = {
        "clientes": clientes,
        "servicos": servicos,
        "agendamentos": agendamentos
    }
    with open("dados.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

def carregar_dados():
    global clientes, servicos, agendamentos
    try:
        with open("dados.json", "r") as arquivo:
            dados = json.load(arquivo)
            clientes = dados.get("clientes", [])
            servicos = dados.get("servicos", [])
            agendamentos = dados.get("agendamentos", [])
    except:
        clientes = []
        servicos = []
        agendamentos = []

    # Serviços padrão se vazio
    if not servicos:
        servicos.extend([
            {'nome': 'Corte de Cabelo', 'preco': 50},
            {'nome': 'Barba', 'preco': 30},
            {'nome': 'Sobrancelha', 'preco': 20},
            {'nome': 'Corte + Barba', 'preco': 80}
        ])

carregar_dados()

# ================= ROTAS =================

@app.route('/')
def index():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    return redirect(url_for('dashboard'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Login simples - em produção, use hash de senha
        if username == 'admin' and password == 'barbearia123':
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        flash('Credenciais inválidas!')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'logged_in' not in session:
        return redirect(url_for('login'))

    hoje = datetime.now().strftime('%d/%m')
    agendamentos_hoje = [ag for ag in agendamentos if ag['dia'] == hoje]

    # Estatísticas rápidas
    total_clientes = len(clientes)
    total_agendamentos = len(agendamentos)
    faturamento_hoje = sum(ag.get('preco', 0) for ag in agendamentos_hoje)

    return render_template('dashboard.html',
                         agendamentos_hoje=agendamentos_hoje,
                         total_clientes=total_clientes,
                         total_agendamentos=total_agendamentos,
                         faturamento_hoje=faturamento_hoje,
                         hoje=hoje)

@app.route('/clientes')
def listar_clientes():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    return render_template('clientes.html', clientes=clientes)

@app.route('/clientes/adicionar', methods=['GET', 'POST'])
def adicionar_cliente():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        nome = request.form['nome']
        if nome and nome not in clientes:
            clientes.append(nome)
            salvar_dados()
            flash('Cliente adicionado com sucesso!')
            return redirect(url_for('listar_clientes'))
        flash('Nome inválido ou cliente já existe!')
    return render_template('adicionar_cliente.html')

@app.route('/servicos')
def listar_servicos():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    return render_template('servicos.html', servicos=servicos)

@app.route('/servicos/adicionar', methods=['GET', 'POST'])
def adicionar_servico():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        nome = request.form['nome']
        preco = float(request.form['preco'])
        if nome and preco > 0:
            servicos.append({'nome': nome, 'preco': preco})
            salvar_dados()
            flash('Serviço adicionado com sucesso!')
            return redirect(url_for('listar_servicos'))
        flash('Dados inválidos!')
    return render_template('adicionar_servico.html')

@app.route('/agendamentos')
def listar_agendamentos():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    return render_template('agendamentos.html', agendamentos=agendamentos)

@app.route('/agendamentos/adicionar', methods=['GET', 'POST'])
def adicionar_agendamento():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        cliente = request.form['cliente']
        servico_nome = request.form['servico']
        dia = request.form['dia']
        horario = request.form['horario']

        # Validar cliente
        if cliente not in clientes:
            flash('Cliente não encontrado!')
            return redirect(url_for('adicionar_agendamento'))

        # Encontrar serviço
        servico = next((s for s in servicos if s['nome'] == servico_nome), None)
        if not servico:
            flash('Serviço não encontrado!')
            return redirect(url_for('adicionar_agendamento'))

        # Verificar horário disponível
        if any(ag['dia'] == dia and ag['horario'] == horario for ag in agendamentos):
            flash('Horário ocupado!')
            return redirect(url_for('adicionar_agendamento'))

        agendamentos.append({
            'cliente': cliente,
            'servico': servico['nome'],
            'preco': servico['preco'],
            'dia': dia,
            'horario': horario
        })
        salvar_dados()
        flash('Agendamento realizado com sucesso!')
        return redirect(url_for('listar_agendamentos'))

    return render_template('adicionar_agendamento.html', clientes=clientes, servicos=servicos, horarios=horarios)

@app.route('/agendamentos/cancelar/<int:index>')
def cancelar_agendamento(index):
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    if 0 <= index < len(agendamentos):
        agendamentos.pop(index)
        salvar_dados()
        flash('Agendamento cancelado!')
    return redirect(url_for('listar_agendamentos'))

@app.route('/relatorios')
def relatorios():
    if 'logged_in' not in session:
        return redirect(url_for('login'))

    # Faturamento por mês
    faturamento_mensal = {}
    for ag in agendamentos:
        if '/' in ag['dia']:
            mes = ag['dia'].split('/')[1]
            faturamento_mensal[mes] = faturamento_mensal.get(mes, 0) + ag.get('preco', 0)

    # Ranking de serviços
    ranking = {}
    for ag in agendamentos:
        servico = ag.get('servico', '')
        ranking[servico] = ranking.get(servico, 0) + 1
    ranking = sorted(ranking.items(), key=lambda x: x[1], reverse=True)

    return render_template('relatorios.html',
                         faturamento_mensal=faturamento_mensal,
                         ranking=ranking)

if __name__ == '__main__':
    app.run(debug=True)