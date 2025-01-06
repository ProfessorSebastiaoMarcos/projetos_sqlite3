import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect("c:/projetos_sqlite3/BD/meu_banco_de_dados.db")
# o cursosr serve para manipular o recursos do bd
cursor = conn.cursor()

