import sqlite3  # Biblioteca para trabalhar com bancos de dados SQLite
from prettytable import PrettyTable  # Biblioteca para exibir tabelas formatadas

# Conexão com o banco de dados (arquivo será criado se não existir)
conn = sqlite3.connect('c:/projetos_sqlite3/BD/bd_rel_1_n.db')
cursor = conn.cursor()

# Criação da tabela 'Clientes' (Tabela principal)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Clientes (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT, -- ID único para o cliente
    nome TEXT NOT NULL,                          -- Nome do cliente
    email TEXT UNIQUE NOT NULL,                  -- Email único
    telefone TEXT,                               -- Telefone do cliente
    cidade TEXT                                  -- Cidade onde mora
)
''')

# Criação da tabela 'Pedidos' (Tabela relacionada)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Pedidos (
    id_pedido INTEGER PRIMARY KEY AUTOINCREMENT, -- ID único para o pedido
    id_cliente INTEGER NOT NULL,                -- Relacionamento com a tabela Clientes
    produto TEXT NOT NULL,                      -- Nome do produto pedido
    quantidade INTEGER NOT NULL,                -- Quantidade do produto
    data TEXT NOT NULL,                         -- Data do pedido
    valor_total REAL NOT NULL,                  -- Valor total do pedido
    FOREIGN KEY (id_cliente) REFERENCES Clientes (id_cliente) -- Chave estrangeira
)
''')

# Função para verificar se um cliente existe no banco de dados
def cliente_existe(id_cliente):
    cursor.execute('SELECT 1 FROM Clientes WHERE id_cliente = ?', (id_cliente,))
    # Retorna True se o cliente existir, False caso contrário
    return cursor.fetchone() is not None  

# Função para inserir dados na tabela Clientes
def inserir_cliente():
    nome = input('Digite o nome do cliente: ')
    email = input('Digite o email do cliente: ')
    telefone = input('Digite o telefone do cliente: ')
    cidade = input('Digite a cidade do cliente: ')
    cursor.execute('''
    INSERT INTO Clientes (nome, email, telefone, cidade)
    VALUES (?, ?, ?, ?)
    ''', (nome, email, telefone, cidade))
    conn.commit()
    print('Cliente inserido com sucesso!')

# Função para inserir dados na tabela Pedidos
def inserir_pedido():
    try:
        # Garantir que o ID seja um número inteiro
        id_cliente = int(input('Digite o ID do cliente: '))  
        
        # Verificar se o cliente existe antes de prosseguir
        if not cliente_existe(id_cliente):
            print('-'*70)
            print(f'Erro: Cliente com ID {id_cliente} não encontrado!')
            print('Por favor, cadastre o cliente primeiro.')
            print('-'*70)
            # Retorna ao menu se o cliente não existir
            return  

        # Solicitar os dados do pedido
        produto = input('Digite o nome do produto: ')
        quantidade = int(input('Digite a quantidade: '))
        #  ISO 8601 (YYYY-MM-DD)
        data = input('Digite a data do pedido (YYYY-MM-DD): ')
        valor_total = float(input('Digite o valor total: '))

        # Inserir o pedido no banco de dados
        cursor.execute('''
        INSERT INTO Pedidos (id_cliente, produto, quantidade, data, valor_total)
        VALUES (?, ?, ?, ?, ?)
        ''', (id_cliente, produto, quantidade, data, valor_total))
        conn.commit()
        print('Pedido inserido com sucesso!')
    except ValueError:
        print('-'*70)
        print('Erro: ID do cliente deve ser um número inteiro.')
        print('-'*70)

# Função para realizar uma consulta com JOIN e exibir resultados
def consultar_dados():
    cursor.execute('''
    SELECT 
        Clientes.nome, Clientes.email, Clientes.cidade, -- Campos da tabela Clientes
        Pedidos.produto, Pedidos.quantidade, Pedidos.valor_total -- Campos da tabela Pedidos
    FROM 
        Clientes
    JOIN 
        Pedidos ON Clientes.id_cliente = Pedidos.id_cliente
    ''')
    resultados = cursor.fetchall()

    # Criar e formatar a tabela para exibição
    tabela = PrettyTable(['Nome', 'Email', 'Cidade', 'Produto', 'Quantidade', 'Valor Total'])
    for linha in resultados:
        tabela.add_row(linha)
    print(tabela)

# Menu interativo
while True:
    print('\nMenu:')
    print('1. Inserir Cliente')
    print('2. Inserir Pedido')
    print('3. Consultar Dados')
    print('4. Sair')
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        inserir_cliente()
    elif opcao == '2':
        inserir_pedido()
    elif opcao == '3':
        consultar_dados()
    elif opcao == '4':
        print('Saindo...')
        break
    else:
        print('-'*70)
        print('Opção inválida. Tente novamente.')
        print('-'*70)

# Fechar a conexão com o banco de dados
conn.close()
