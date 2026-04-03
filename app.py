import json

print('Bem-vindo à Império Barber!\n')

def mostrar_menu():
    print('\nO que deseja fazer?')
    print('1 - Cadastrar cliente')
    print('2 - Cadastrar serviço')
    print('3 - Agendar serviço')
    print('4 - Listar clientes')
    print('5 - Listar serviços')
    print('6 - Listar agendamentos')
    print('7 - Mostrar horários')
    print('8 - Cancelar agendamento')
    print('9 - Mostrar faturamento por dia')
    print('10 - Mostrar faturamento por mês')
    print('11 - Mostrar ranking de serviços')
    print('12 - agenda do dia')
    print('13 - agenda do mês')
    print('14 - Sair')


horarios = [
    '08:00', '09:00', '10:00', '11:00', '12:00',
    '13:00', '14:00', '15:00', '16:00', '17:00',
    '18:00', '19:00', '20:00', '21:00', '22:00'
]

clientes = []
servicos = []
agendamentos = []


# ================= JSON =================

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

    # 🔥 SERVIÇOS PADRÃO AUTOMÁTICOS
    if not servicos:
        servicos.extend([
            {'nome': 'corte de cabelo', 'preco': 50},
            {'nome': 'barba', 'preco': 30},
            {'nome': 'sobrancelha', 'preco': 20},
            {'nome': 'corte + barba', 'preco': 80}
        ])


carregar_dados()


# ================= FUNÇÕES =================

def mostrar_horarios():
    dia = input('Digite o dia: ')
    print(f'\nHorários para {dia}:\n')

    for h in horarios:
        ocupado = False
        for ag in agendamentos:
            if ag["horario"] == h and ag["dia"] == dia:
                ocupado = True
                break

        print(h, '- Ocupado' if ocupado else '- Livre')


def cadastrar_cliente():
    nome = input('Nome do cliente: ')
    clientes.append(nome)
    salvar_dados()
    print('Cliente cadastrado!')


def cadastrar_servico():
    nome = input('Nome do serviço: ')
    preco = float(input('Preço: R$ '))

    servicos.append({
        "nome": nome,
        "preco": preco
    })

    salvar_dados()
    print('Serviço cadastrado!')


def agendar_servico():
    if not clientes:
        print('Nenhum cliente cadastrado.')
        return

    if not servicos:
        print('Nenhum serviço cadastrado.')
        return

    cliente = input('Cliente: ')
    if cliente not in clientes:
        print('Cliente não encontrado.')
        return

    print('\nServiços disponíveis:')
    for s in servicos:
        print(f'- {s["nome"]} - R$ {s["preco"]}')

    nome_servico = input('Escolha o serviço: ')

    servico_encontrado = None
    for s in servicos:
        if s["nome"] == nome_servico:
            servico_encontrado = s
            break

    if not servico_encontrado:
        print('Serviço não encontrado.')
        return

    dia = input('Dia (ex: 20/03): ')

    print('\nHorários:')
    for h in horarios:
        ocupado = any(
            ag["horario"] == h and ag["dia"] == dia
            for ag in agendamentos
        )
        print(h, '- Ocupado' if ocupado else '- Livre')

    horario = input('Horário: ')

    for ag in agendamentos:
        if ag["horario"] == horario and ag["dia"] == dia:
            print('Horário ocupado.')
            return

    agendamentos.append({
        "cliente": cliente,
        "servico": servico_encontrado["nome"],
        "preco": servico_encontrado["preco"],
        "dia": dia,
        "horario": horario
    })

    salvar_dados()
    print('Agendamento realizado!')


def listar_clientes():
    print('\nClientes:')

    if not clientes:
        print('Nenhum cliente.')
        return

    for c in clientes:
        print('-', c)


def listar_servicos():
    print('\nServiços:')

    if not servicos:
        print('Nenhum serviço.')
        return

    for s in servicos:
        if isinstance(s, dict):
            print(f'- {s["nome"]} - R$ {s["preco"]}')
        else:
            print(f'- {s} (formato antigo)')


def listar_agendamentos():
    print('\nAgendamentos:')

    if not agendamentos:
        print('Nenhum.')
        return

    for ag in agendamentos:
        preco = ag.get("preco", 0)
        print(f'{ag["dia"]} - {ag["horario"]} - {ag["cliente"]} - {ag["servico"]} - R$ {preco}')


def cancelar_agendamento():
    dia = input('Dia: ')
    horario = input('Horário: ')

    for ag in agendamentos:
        if ag["dia"] == dia and ag["horario"] == horario:
            agendamentos.remove(ag)
            salvar_dados()
            print('Cancelado!')
            return

    print('Não encontrado.')


def agenda_do_dia():
    dia = input('digite o dia do mes para ver a agenda:') 
    
    print(f'\n📅 agenda do dia {dia}:\n')
    
    for h in horarios:
        agendamento_encontrado = None
        
        for ag in agendamentos:
            if ag['dia'] == dia and ag['horario'] == h:
                agendamento_encontrado = ag
                break
            
        if agendamento_encontrado:
            print(f'{h} - {agendamento_encontrado['cliente']} - {agendamento_encontrado['servico']}')
        else:
            print(f'{h} - Livre')    
            
    
def mostrar_faturamento_por_dia():
        dia = input('Digite o dia e o mes para ver o faturamento: ')
        
        total = 0 
        quantidade = 0
        for ag in agendamentos:
            if ag["dia"] == dia:
                total += ag.get("preco", 0)
                quantidade += 1
                
        print(f'\n💰 faturamento do dia {dia}: R$ {total}')
        print(f'📊 Total de atendimentos: {quantidade}')
        
        if quantidade > 0:
            media = total / quantidade
            print(f'📈 Ticket médio: R$ {media:.2f}')
            
                
def agenda_do_mes():
    mes = input('digite o mes:')
    
    print(f'\n📅 agenda do mes {mes}:\n')
    
    dias = {}
    
    #organizar por dia 
    for ag in agendamentos:
        if "/" in ag['dia']:
            partes = ag['dia'].split("/")
            
        if len(partes) == 2:
            mes_ag = partes[1]
            
            if mes_ag == mes:
                if ag['dia']not in dias:
                    dias[ag['dia']] = []
                    
                dias[ag['dia']].append(ag)
                
    if not dias:
         print('nenhum agendamento esse mes.')
         return
     
     #ordenar por dia
    for dia in sorted(dias.keys()):
        print(f'\n📅 {dia}:\n')
         
        #ordenar por horario
        ags_ordenados = sorted(dias[dia], key=lambda x: x['horario'])
         
        for ag in ags_ordenados:
             print(f'{ag["horario"]} - {ag["cliente"]} - {ag["servico"]}')
             

def faturamento_por_mes():
    mes = input('digite o mes : ')
    
    total = 0
    quantidade = 0
    
    for ag in agendamentos:
        if "/" in ag["dia"]:
            dia_agendamento = ag["dia"].split("/")
            
            if len(dia_agendamento) == 2:
                mes_ag = dia_agendamento[1] 
                
                if mes_ag == mes:
                    total += ag.get("preco", 0)
                    quantidade += 1 
    
    print(f'\n💰 Faturamento do mês {mes}: R$ {total}')
    print(f'📊 Total de atendimentos: {quantidade}')
    
    if quantidade > 0:
        media = total / quantidade
        print(f'📈 Ticket médio: R$ {media:.2f}')
    
    
def ranking_servicos():
    print('\nRanking de serviços:\n')
    
    if not agendamentos:
        print('nenhum agendamento.')
        return
    
    contador = {} 
    
    for ag in agendamentos:
        servicos = ag.get('servico')
        
        if servicos:
            contador[servicos] = contador.get(servicos, 0) + 1
            
    #ordem do maior para o menor
    ranking = sorted(contador.items(), key=lambda x: x[1], reverse=True)
            
    for servicos, quantidade in ranking:
        print(f'{servicos} - {quantidade} x')
                
                
# ================= LOOP =================

while True:
    mostrar_menu()
    op = input('Opção: ')

    if op == '1':
        cadastrar_cliente()
    elif op == '2':
        cadastrar_servico()
    elif op == '3':
        agendar_servico()
    elif op == '4':
        listar_clientes()
    elif op == '5':
        listar_servicos()
    elif op == '6':
        listar_agendamentos()
    elif op == '7':
        mostrar_horarios()
    elif op == '8':
        cancelar_agendamento()
    elif op == '9':
        mostrar_faturamento_por_dia()
    elif op == '10':
            faturamento_por_mes()
    elif op == '11':
        ranking_servicos()
    elif op == '12':
        agenda_do_dia()
    elif op == '13':
        agenda_do_mes()
    elif op == '14':
        print('Encerrando...')
        break 
    else:
        print('Opção inválida.')
        
        print('obrigado por usar o sistema da Império Barber!\n')
