import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect("c:/projetos_sqlite3/BD/meu_banco_de_dados.db")

# Para operações no banco de dados, você também precisará de um cursor,
# que é um objeto que permite executar comandos SQL.

cursor = conn.cursor()

# ? = Placeholder - será substituído pelos valores da tupla
# (25,) = O execute precisa de uma tupla com um valor no segundo parâmetro
cursor.execute("UPDATE clientes SET idade = ? WHERE nome = ?",
               (32, "João Silva"))
conn.commit()

conn.close()