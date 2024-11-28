# file: crud_sqlite3_prettytable.py

import sqlite3
from prettytable import PrettyTable

# Criar ou conectar ao banco de dados
def connect_db():
    return sqlite3.connect("usuarios.db")

# Criar a tabela se não existir
def create_table():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        """)
        conn.commit()

# Create: Inserir um novo usuário
def create_user(nome, email):
    try:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
            conn.commit()
            print("Usuário inserido com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: Email já cadastrado.")

# Read: Listar todos os usuários
def list_users():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        users = cursor.fetchall()
        
        if users:
            # Configurar tabela com PrettyTable
            table = PrettyTable()
            table.field_names = ["ID", "Nome", "Email"]
            for user in users:
                table.add_row(user)
            print(table)
        else:
            print("Nenhum usuário encontrado.")

# Update: Atualizar usuário pelo ID
def update_user(user_id, nome, email):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE usuarios SET nome = ?, email = ? WHERE id = ?", (nome, email, user_id))
        if cursor.rowcount > 0:
            conn.commit()
            print("Usuário atualizado com sucesso!")
        else:
            print("Usuário não encontrado.")

# Delete: Remover usuário pelo ID
def delete_user(user_id):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (user_id,))
        if cursor.rowcount > 0:
            conn.commit()
            print("Usuário removido com sucesso!")
        else:
            print("Usuário não encontrado.")

# Menu interativo
def menu():
    create_table()  # Garantir que a tabela existe
    while True:
        print("\n=== MENU CRUD ===")
        print("1. Inserir usuário")
        print("2. Listar usuários")
        print("3. Atualizar usuário")
        print("4. Remover usuário")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            create_user(nome, email)
        elif escolha == "2":
            list_users()
        elif escolha == "3":
            user_id = int(input("ID do usuário: "))
            nome = input("Novo nome: ")
            email = input("Novo email: ")
            update_user(user_id, nome, email)
        elif escolha == "4":
            user_id = int(input("ID do usuário: "))
            delete_user(user_id)
        elif escolha == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
