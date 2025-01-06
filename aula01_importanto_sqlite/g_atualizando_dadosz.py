import os
import sqlite3

conn = sqlite3.connect("c:/projetos_sqlite3/BD/meu_banco_de_dados.db")

cursor = conn.cursor()

os.system('cls')
nome_cliente = input("Digite o nome do cliente: ")
nova_idade = int(input("Digite a nova idade: "))

# Atualiza a idade com base no nome fornecido pelo usuário
cursor.execute("UPDATE clientes SET idade = ? WHERE nome = ?",
               (nova_idade, nome_cliente))

# Salva as alterações no banco de dados
conn.commit()
print("Dados atualizados com sucesso!")
conn.close()

