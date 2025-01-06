import os
import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect("c:/projetos_sqlite3/BD/meu_banco_de_dados.db")

# Para operações no banco de dados, você também precisará de um cursor,
# que é um objeto que permite executar comandos SQL.

cursor = conn.cursor()

# ? = Placeholder
# (25,) = O execute precisa de uma tupla
cursor.execute("SELECT * FROM clientes WHERE idade > ?", (25,)) 
resultados = cursor.fetchall()


os.system('cls')
# Cabeçalho
print("-" * 40)
print(f"{'ID':<5} {'Nome':<20} {'Idade':<5}")
print("=" * 40)

# Dados
for row in resultados:
    id_cliente, nome, idade = row
    print(f"{id_cliente:<5} {nome:<20} {idade:<5}")

print("-" * 40)
conn.close()





