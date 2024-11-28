import os
import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect("c:/projetos_sqlite3/BD/meu_banco_de_dados.db")

# Para operações no banco de dados, você também precisará de um cursor,
# que é um objeto que permite executar comandos SQL.

cursor = conn.cursor()

# ? = Placeholder
# (25,) = O execute precisa de uma tupla com um valor no segundo parâmetro
cursor.execute("SELECT * FROM clientes WHERE idade > ?", (25,)) 
resultados = cursor.fetchall()

os.system('cls')
for row in resultados:
    print(row)

conn.close()





