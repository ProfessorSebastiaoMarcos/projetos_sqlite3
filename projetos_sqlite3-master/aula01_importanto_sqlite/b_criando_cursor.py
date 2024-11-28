import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect("meu_banco_de_dados.db")

# Para operações no banco de dados, você também precisará de um cursor,
# que é um objeto que permite executar comandos SQL.

cursor = conn.cursor()
