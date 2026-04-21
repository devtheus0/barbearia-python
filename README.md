# Sistema de Gestão - Barbearia Império

Um sistema web profissional para donos de barbearia gerenciarem seus clientes, serviços e agendamentos.

## 🚀 Funcionalidades

- **Dashboard**: Visão geral com estatísticas e agendamentos do dia
- **Gerenciamento de Clientes**: Adicionar e visualizar clientes
- **Gerenciamento de Serviços**: Adicionar e visualizar serviços oferecidos
- **Agendamentos**: Criar, visualizar e cancelar agendamentos
- **Relatórios**: Faturamento mensal e ranking de serviços
- **Autenticação**: Sistema de login seguro para donos

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, Bootstrap 5, Font Awesome
- **Armazenamento**: JSON (dados.json)
- **Autenticação**: Flask Sessions

## 📋 Pré-requisitos

- Python 3.6+
- Flask instalado

## 🚀 Como Executar

1. **Instalar dependências**:
   ```bash
   pip install flask
   ```

2. **Executar o sistema**:
   ```bash
   python app.py
   ```

3. **Acessar no navegador**:
   ```
   http://127.0.0.1:5000
   ```

## 🔐 Login

- **Usuário**: admin
- **Senha**: barbearia123

## 📁 Estrutura do Projeto

```
barbearia-python/
├── app.py                 # Aplicação Flask principal
├── dados.json            # Arquivo de dados (criado automaticamente)
├── templates/            # Templates HTML
│   ├── login.html
│   ├── dashboard.html
│   ├── clientes.html
│   ├── adicionar_cliente.html
│   ├── servicos.html
│   ├── adicionar_servico.html
│   ├── agendamentos.html
│   ├── adicionar_agendamento.html
│   └── relatorios.html
└── README.md
```

## 🎯 Funcionalidades Detalhadas

### Dashboard
- Estatísticas rápidas (total de clientes, agendamentos, faturamento do dia)
- Lista de agendamentos do dia atual
- Navegação intuitiva

### Gerenciamento de Clientes
- Lista completa de clientes cadastrados
- Adição de novos clientes
- Validação para evitar duplicatas

### Gerenciamento de Serviços
- Lista de serviços com preços
- Adição de novos serviços
- Serviços padrão incluídos automaticamente

### Agendamentos
- Visualização de todos os agendamentos
- Criação de novos agendamentos com validação
- Cancelamento de agendamentos
- Verificação de horários disponíveis

### Relatórios
- Faturamento por mês
- Ranking de serviços mais realizados
- Estatísticas gerais

## 🔒 Segurança

- Sistema de autenticação baseado em sessão
- Proteção contra acesso não autorizado
- Validação de dados de entrada

## 📊 Dados

Os dados são armazenados em `dados.json` contendo:
- Lista de clientes
- Lista de serviços
- Lista de agendamentos

## 🎨 Design

Interface moderna e responsiva usando:
- Bootstrap 5 para layout responsivo
- Font Awesome para ícones
- Gradientes e sombras para aparência profissional
- Cores consistentes da marca

## 🔧 Personalização

### Alterar Credenciais de Login
No arquivo `app.py`, linha ~32:
```python
if username == 'admin' and password == 'barbearia123':
```

### Adicionar Serviços Padrão
No arquivo `app.py`, função `carregar_dados()`:
```python
servicos.extend([
    {'nome': 'Nome do Serviço', 'preco': 00.00},
    # ... mais serviços
])
```

### Modificar Horários Disponíveis
No arquivo `app.py`, lista `horarios`:
```python
horarios = [
    '08:00', '09:00', # ... mais horários
]
```

## 🚀 Próximos Passos

Para produção, considere:
- Banco de dados relacional (SQLite, PostgreSQL)
- Sistema de autenticação mais robusto
- Deploy em servidor WSGI (Gunicorn, uWSGI)
- HTTPS
- Backup automático de dados

## 📞 Suporte

Sistema desenvolvido para facilitar a gestão de barbearias, focado na experiência dos donos/proprietários.

- Python 3.6+
- Flask instalado

## 🚀 Como Executar

1. **Instalar dependências**:
   ```bash
   pip install flask
   ```

2. **Executar o sistema**:
   ```bash
   python app.py
   ```

3. **Acessar no navegador**:
   ```
   http://127.0.0.1:5000
   ```

## 🔐 Login

- **Usuário**: admin
- **Senha**: barbearia123

## 📁 Estrutura do Projeto

```
barbearia-python/
├── app.py                 # Aplicação Flask principal
├── dados.json            # Arquivo de dados (criado automaticamente)
├── templates/            # Templates HTML
│   ├── login.html
│   ├── dashboard.html
│   ├── clientes.html
│   ├── adicionar_cliente.html
│   ├── servicos.html
│   ├── adicionar_servico.html
│   ├── agendamentos.html
│   ├── adicionar_agendamento.html
│   └── relatorios.html
└── README.md
```

## 🎯 Funcionalidades Detalhadas

### Dashboard
- Estatísticas rápidas (total de clientes, agendamentos, faturamento do dia)
- Lista de agendamentos do dia atual
- Navegação intuitiva

### Gerenciamento de Clientes
- Lista completa de clientes cadastrados
- Adição de novos clientes
- Validação para evitar duplicatas

### Gerenciamento de Serviços
- Lista de serviços com preços
- Adição de novos serviços
- Serviços padrão incluídos automaticamente

### Agendamentos
- Visualização de todos os agendamentos
- Criação de novos agendamentos com validação
- Cancelamento de agendamentos
- Verificação de horários disponíveis

### Relatórios
- Faturamento por mês
- Ranking de serviços mais realizados
- Estatísticas gerais

## 🔒 Segurança

- Sistema de autenticação baseado em sessão
- Proteção contra acesso não autorizado
- Validação de dados de entrada

## 📊 Dados

Os dados são armazenados em `dados.json` contendo:
- Lista de clientes
- Lista de serviços
- Lista de agendamentos

## 🎨 Design

Interface moderna e responsiva usando:
- Bootstrap 5 para layout responsivo
- Font Awesome para ícones
- Gradientes e sombras para aparência profissional
- Cores consistentes da marca

## 🔧 Personalização

### Alterar Credenciais de Login
No arquivo `app.py`, linha ~32:
```python
if username == 'admin' and password == 'barbearia123':
```

### Adicionar Serviços Padrão
No arquivo `app.py`, função `carregar_dados()`:
```python
servicos.extend([
    {'nome': 'Nome do Serviço', 'preco': 00.00},
    # ... mais serviços
])
```

### Modificar Horários Disponíveis
No arquivo `app.py`, lista `horarios`:
```python
horarios = [
    '08:00', '09:00', # ... mais horários
]
```

## 🚀 Próximos Passos

Para produção, considere:
- Banco de dados relacional (SQLite, PostgreSQL)
- Sistema de autenticação mais robusto
- Deploy em servidor WSGI (Gunicorn, uWSGI)
- HTTPS
- Backup automático de dados

## 📞 Suporte

Sistema desenvolvido para facilitar a gestão de barbearias, focado na experiência dos donos/proprietários.
