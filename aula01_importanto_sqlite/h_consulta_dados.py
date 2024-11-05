import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect("c:/projetos_sqlite3/BD/meu_banco_de_dados.db")

# Para operações no banco de dados, você também precisará de um cursor,
# que é um objeto que permite executar comandos SQL.

cursor = conn.cursor()


cursor.execute("SELECT * FROM clientes")
resultados = cursor.fetchall()

for row in resultados:
    print(row)
conn.close()




