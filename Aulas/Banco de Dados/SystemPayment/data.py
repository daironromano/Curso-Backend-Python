import sqlite3
import os

DB_NAME = "ecomerce_db"

def criar_banco():

    # Conexão com o banco de dados (local)
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Habilitar chaves estrangeiras
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Criar tabelas 
    cursor.execute("""
    CREATE TABLE pedidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_nome TEXT,
        valor_produto REAL NOT NULL,
        status TEXT DEFAULT 'PENDENTE'
    );             
    """)

    cursor.execute("""
    CREATE TABLE pagamentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        metodo TEXT,
        valor_final REAL,
        pedido_id INTEGER,
        FOREIGN KEY(pedido_id) REFENCES pedidos(id)     
    );             
    """)

    pedidos = [
        ('Dairon Romano', 1000.00),
        ('Maria Joana', 500.00), 
        ('Carlos', 2000.00)
    ]

    cursor.executemany(
        "INSERT INTO pedidos (cliente_nome, valor_bruto) VALUES (?, ?);",
        pedidos
    )

    conn.commit()
    print('Banco de dados gerado!')
    conn.close()

if __name__ == "__main__":
    criar_banco()