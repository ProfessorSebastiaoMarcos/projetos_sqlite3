import os
import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect("c:/projetos_sqlite3/BD/bd_rel_1_n.db")
cursor = conn.cursor()


# Função para listar pedidos de forma tabulada
def listar_pedidos():
    cursor.execute('''
        SELECT clientes.nome, pedidos.descricao, pedidos.valor
        FROM pedidos
        JOIN clientes ON pedidos.cliente_id = clientes.id
    ''')
    pedidos = cursor.fetchall()

    # Exibindo de forma tabulada
    print(f"{'Cliente':<20} {'Pedido':<30} {'Valor':>10}")
    print("-" * 60)  # Linha de separação
    for pedido in pedidos:
        print(f"{pedido[0]:<20} {pedido[1]:<30} {pedido[2]:>10.2f}")


# Função para excluir pedidos de um cliente pelo nome
def excluir_pedidos_por_nome(nome_cliente):
    # Buscar o id do cliente pelo nome
    cursor.execute("SELECT id FROM clientes WHERE nome = ?", (nome_cliente,))
    cliente_id = cursor.fetchone()

    if cliente_id:
        cliente_id = cliente_id[0]
        # Excluir os pedidos associados ao cliente
        cursor.execute(
            "DELETE FROM pedidos WHERE cliente_id = ?", (cliente_id,))
        conn.commit()
        print(f"Pedidos do cliente {nome_cliente} excluídos com sucesso!")
    else:
        print(f"Cliente {nome_cliente} não encontrado.")


# Exemplo de uso
os.system('cls')
# Listar todos os pedidos
listar_pedidos()

# Excluir pedidos de um cliente com base no nome
nome_cliente = input("Digite o nome do cliente para excluir os pedidos: ")
excluir_pedidos_por_nome(nome_cliente)

# Fechar a conexão
conn.close()
