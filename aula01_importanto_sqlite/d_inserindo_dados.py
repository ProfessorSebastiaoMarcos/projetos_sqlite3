import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect("c:/projetos_sqlite3/BD/meu_banco_de_dados.db")

cursor = conn.cursor()

# Definição de uma tupla com os dados
dados_cliente = ("João Silva", 30)

# Placeholders (?, ?): Os pontos de interrogação são usados como 
# "espaços reservados". Eles serão substituídos pelos valores da 
# tupla dados_cliente (ou seja, "João Silva" e 30).
# Por quê: Usar placeholders é uma prática recomendada, 
# pois previne ataques de injeção de SQL.
cursor.execute("INSERT INTO clientes (nome, idade) VALUES (?, ?)", dados_cliente)

conn.commit()  # Salva a transação no banco de dados
conn.close() # fecha conexão

