import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect("c:/projetos_sqlite3/BD/meu_banco_de_dados.db")

# Para operações no banco de dados, você também precisará de um cursor,
# que é um objeto que permite executar comandos SQL.

cursor = conn.cursor()

dados_cliente = ("João Silva", 30)
cursor.execute("INSERT INTO clientes (nome, idade) VALUES (?, ?)", dados_cliente)
conn.commit()  # Salva a transação no banco de dados

conn.close()

