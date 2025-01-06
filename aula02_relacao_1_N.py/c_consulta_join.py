import os
import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect("c:/projetos_sqlite3/BD/bd_rel_1_n.db")
cursor = conn.cursor()

# Consulta com JOIN para combinar informações de clientes e pedidos
consulta = '''
    SELECT clientes.nome AS Cliente, clientes.idade AS Idade, 
           pedidos.descricao AS Pedido, pedidos.valor AS Valor
    FROM clientes
    LEFT JOIN pedidos ON clientes.id = pedidos.cliente_id
    ORDER BY clientes.nome
'''

cursor.execute(consulta)

os.system('cls')
# Formatação dos registros com tabulação
print(f"{'Cliente':<20} {'Idade':<6} {'Pedido':<30} {'Valor':<10}")
print("-" * 66)

# Iterando sobre os resultados e imprimindo cada registro
for cliente, idade, pedido, valor in cursor.fetchall():
    print(f"{cliente:<20} {idade:<6} {pedido or 'Nenhum':<30} {valor or '0.00':<10}")

# Fechando a conexão
conn.close()
