# file: crud_tkinter.py

import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox


# Conexão com o banco de dados SQLite
def connect_db():
    return sqlite3.connect("usuarios.db")

# Criar tabela no banco de dados
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

# Inserir novo usuário
def insert_user(nome, email):
    try:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
            conn.commit()
            return True
    except sqlite3.IntegrityError:
        return False

# Listar usuários
def fetch_users():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        return cursor.fetchall()

# Atualizar usuário
def update_user(user_id, nome, email):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE usuarios SET nome = ?, email = ? WHERE id = ?", (nome, email, user_id))
        return cursor.rowcount > 0

# Remover usuário
def delete_user(user_id):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (user_id,))
        return cursor.rowcount > 0


# Funções da Interface Gráfica
def refresh_table():
    for row in tree.get_children():
        tree.delete(row)
    for user in fetch_users():
        tree.insert("", "end", values=user)

def add_user():
    nome = entry_nome.get()
    email = entry_email.get()
    if nome and email:
        if insert_user(nome, email):
            messagebox.showinfo("Sucesso", "Usuário adicionado com sucesso!")
            refresh_table()
            entry_nome.delete(0, tk.END)
            entry_email.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Email já cadastrado!")
    else:
        messagebox.showwarning("Atenção", "Preencha todos os campos!")

def edit_user():
    try:
        selected_item = tree.selection()[0]
        user_id = tree.item(selected_item)["values"][0]
        nome = entry_nome.get()
        email = entry_email.get()
        if nome and email:
            if update_user(user_id, nome, email):
                messagebox.showinfo("Sucesso", "Usuário atualizado com sucesso!")
                refresh_table()
                entry_nome.delete(0, tk.END)
                entry_email.delete(0, tk.END)
            else:
                messagebox.showerror("Erro", "Erro ao atualizar o usuário.")
        else:
            messagebox.showwarning("Atenção", "Preencha todos os campos!")
    except IndexError:
        messagebox.showwarning("Atenção", "Selecione um usuário para editar.")

def delete_selected_user():
    try:
        selected_item = tree.selection()[0]
        user_id = tree.item(selected_item)["values"][0]
        if messagebox.askyesno("Confirmação", "Deseja realmente remover o usuário?"):
            if delete_user(user_id):
                messagebox.showinfo("Sucesso", "Usuário removido com sucesso!")
                refresh_table()
            else:
                messagebox.showerror("Erro", "Erro ao remover o usuário.")
    except IndexError:
        messagebox.showwarning("Atenção", "Selecione um usuário para remover.")


# Criar a Interface Gráfica
app = tk.Tk()
app.title("CRUD com Tkinter e SQLite")
app.geometry("600x400")

# Widgets
frame_form = tk.Frame(app)
frame_form.pack(pady=10)

tk.Label(frame_form, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
entry_nome = tk.Entry(frame_form, width=30)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Email:").grid(row=1, column=0, padx=5, pady=5)
entry_email = tk.Entry(frame_form, width=30)
entry_email.grid(row=1, column=1, padx=5, pady=5)

frame_buttons = tk.Frame(app)
frame_buttons.pack(pady=10)

btn_add = tk.Button(frame_buttons, text="Adicionar", command=add_user)
btn_add.grid(row=0, column=0, padx=5)

btn_edit = tk.Button(frame_buttons, text="Editar", command=edit_user)
btn_edit.grid(row=0, column=1, padx=5)

btn_delete = tk.Button(frame_buttons, text="Remover", command=delete_selected_user)
btn_delete.grid(row=0, column=2, padx=5)

# Tabela de usuários
frame_table = tk.Frame(app)
frame_table.pack(pady=10)

columns = ("ID", "Nome", "Email")
tree = ttk.Treeview(frame_table, columns=columns, show="headings")
tree.heading("ID", text="ID")
tree.heading("Nome", text="Nome")
tree.heading("Email", text="Email")
tree.column("ID", width=50, anchor="center")
tree.column("Nome", width=200, anchor="w")
tree.column("Email", width=250, anchor="w")
tree.pack()

refresh_table()

# Inicializar
create_table()
app.mainloop()
