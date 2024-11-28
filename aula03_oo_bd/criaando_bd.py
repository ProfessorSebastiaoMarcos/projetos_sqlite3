import sqlite3

class BancoDeDados:
    def __init__(self, banco_de_dados):
        """
        Inicializa a conexão com o banco de dados.

        Args:
            banco_de_dados (str): Nome do arquivo do banco de dados.
        """
        self.conexao = sqlite3.connect(banco_de_dados)
        self.cursor = self.conexao.cursor()

    def executar_consulta(self, consulta):
        """
        Executa uma consulta SQL.

        Args:
            consulta (str): Consulta SQL a ser executada.

        Returns:
            list: Lista de tuplas com os resultados da consulta.
        """
        self.cursor.execute(consulta)
        return self.cursor.fetchall()

    def inserir_dados(self, tabela, dados):
        """
        Insere dados em uma tabela.

        Args:
            tabela (str): Nome da tabela.
            dados (tuple): Tupla com os dados a serem inseridos.
        """
        campos = ', '.join(dados.keys())
        valores = ', '.join(['?' for _ in dados.values()])
        consulta = f"INSERT INTO {tabela} ({campos}) VALUES ({valores})"
        self.cursor.execute(consulta, tuple(dados.values()))
        self.conexao.commit()

    def fechar_conexao(self):
        """
        Fecha a conexão com o banco de dados.
        """
        self.conexao.close()
    
# programa principal
# Criando uma instância da classe BancoDeDados
banco = BancoDeDados('c:/projetos_sqlite3/BD/bd_oo.db')

# Criando uma tabela (se não existir)
banco.executar_consulta('CREATE TABLE IF NOT EXISTS pessoas (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER)')

# Inserindo dados
banco.inserir_dados('pessoas', {'nome': 'João', 'idade': 30})

# Consultando dados
resultado = banco.executar_consulta('SELECT * FROM pessoas')
print(resultado)

# Fechando a conexão
banco.fechar_conexao()