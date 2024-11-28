import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect("c:/projetos_sqlite3/BD/meu_banco_de_dados.db")

# Para operações no banco de dados, você também precisará de um cursor,
# que é um objeto que permite executar comandos SQL.

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER
    )
''')
