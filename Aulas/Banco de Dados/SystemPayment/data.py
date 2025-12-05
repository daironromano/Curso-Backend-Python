import sqlite3
import os

DB_NAME = "ecomerce_db"

def criar_banco():

    # Conexão com o banco de dados (local)
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Habilitar chaves estrangeiras
    cursor.execute("PROGMA foreign_key = ON;")

    # Criar tabelas 
    cursor.execute("""
    CREATE TABLE Pedidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_nome TEXT,
        valor_produto REAL NOT NULL,
        status TEXT DEFAULT 'PENDENTE'
    );             
    """)
    


