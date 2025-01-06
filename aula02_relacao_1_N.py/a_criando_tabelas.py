import sqlite3

# Conexão e criação do banco de dados
conn = sqlite3.connect("bd_rel_1_n.db")
cursor = conn.cursor()

# Criação da tabela de clientes
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER
    )
''')

# Criação da tabela de pedidos com chave estrangeira referenciando clientes
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pedidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL,
        valor REAL,
        cliente_id INTEGER,
        FOREIGN KEY (cliente_id) REFERENCES clientes (id)
    )
''')

# Inserção de dados na tabela clientes
dados_cliente = ("João Silva", 30)
cursor.execute(
    "INSERT INTO clientes (nome, idade) VALUES (?, ?)", dados_cliente)

dados_varios_clientes = [
    ("Maria Souza", 25),
    ("Carlos Pereira", 35),
    ("Ana Costa", 28)
]
cursor.executemany(
    "INSERT INTO clientes \
    (nome, idade) VALUES (?, ?)", dados_varios_clientes)
conn.commit()

# Inserção de dados na tabela pedidos associados a um cliente
dados_pedidos = [
    # Associado ao cliente com id 1 (João Silva)
    ("Compra de eletrodoméstico", 1200.50, 1),
    ("Compra de móveis", 750.00, 1),
    # Associado ao cliente com id 2 (Maria Souza)
    ("Serviço de instalação", 150.00, 2)
]
cursor.executemany(
    "INSERT INTO pedidos \
        (descricao, valor, cliente_id) VALUES (?, ?, ?)", dados_pedidos)
conn.commit()

# Fechando a conexão
conn.close()
