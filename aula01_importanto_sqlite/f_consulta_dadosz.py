import os
import sqlite3
from prettytable import PrettyTable # no terminal: pip install prettytable

conn = sqlite3.connect("c:/projetos_sqlite3/BD/meu_banco_de_dados.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM clientes")
resultados = cursor.fetchall()

os.system('cls')

# Cria a tabela PrettyTable e define os nomes das colunas
tabela = PrettyTable()
# Obtém os nomes das colunas a partir de cursor.description
colunas = [descricao[0] for descricao in cursor.description]
# Define os nomes das colunas na tabela PrettyTable
tabela.field_names = colunas

# Adiciona as linhas à tabela
for row in resultados:
    tabela.add_row(row)

print(tabela)
conn.close()

