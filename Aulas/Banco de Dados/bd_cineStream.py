import mysql.connector
from abc import ABC, abstractmethod
from typing import List, Tuple

# 1. Receiver 

class DatabaseReceiver: # Receiver
    def __init__(self):
        self.config = {
            'host':'localhost',
            'user': 'root',
            'password': 'admin',
            'database': 'cinestream_db',
        }

    def execute_query(self, query: str, params: tuple = None) -> List[Tuple]:
      # Comando SQL -> List (Consulta no banco de dados)
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor()
            cursor.execute(query, params)
            result = cursor.fetchall()
            cursor.close()
            return result
        except mysql.connector.Error as err:
            print(f'[Erro de leitura MySQL: {err}]')
            return []
        
    def execute_command(self, query: str, params: tuple = None):
        # Modificações no banco de dados
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit() #Salva as alterações
            cursor.close()
            conn.close()
            print('Operação realizada com sucesso')
        except mysql.connector.Error as err:
            print(f'[Erro de leitura MySQL: {err}]')


# 2. Command Interface (Contrato)
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# 3. Concrete Commands (Funcionalidades)
class ListarCatalagoCommand(Command):
    def __init__(self, db: DatabaseReceiver):
        self.db = db
        
    def execute(self):
        print('--- Catálogo de Filmes ---')
        sql = 'SELECT * FROM filme ORDER BY visualizacoes DESC'
        filmes = self.db.execute_query(sql)

        for filme in filmes:
            print(f'{filme[0]} | {filme[1]} | {filme[2]} | {filme[3]}')

class AssistirFilmeCommand(Command):
    def __init__(self, db: DatabaseReceiver):
        self.db = db

    def execute(self):
        try:
            filme_id = input('Qual filme você quer assistir? Responda com: [ID]')
            # SQL 1: Atualizar o DB:
            sql_up = 'UPDATE filmes SET visualizacoes = visualizacoes + 1 WHERE id = %s'
            self.db.execute_command(sql_up, (filme_id))
            # SQL 2: Registrar histórico (INSERT)
            sql_ins = 'INSERT INTO historico_views (filme_id) VALUES (%s)'
            self.db.execute_command(sql_ins, (filme_id))
            print(f'Divirta-se! Filme ID {filme_id} iniciado')

        except Exception as e:
            print(f'Erro ao procesar filme: {e}')

class SairCommando(Command):
    def execute(self):
        print('Fechando CineStream')
        exit()

# 4. Envoker

class MenuApp:
    def __init__(self):
        self.comandos = {}

    def registrar(self, tecla, comando: Command):
        self.comandos[tecla] = comando
    
    def rodar(self):
        while True:
            print('====== CINESTREAM ======')
            print('1. Ver Catálogo')
            print('2. Assistir filme')
            print('0. Sair')

            opcao = input('oPÇÃO: ')
            if opcao in self.comandos:
                self.comandos[opcao].execute()
            else:
                print('Opção inválida')

if __name__ == "__main__":
    banco = DatabaseReceiver()

    cmd_listar = ListarCatalagoCommand(banco)
    cmd_assistir = AssistirFilmeCommand(banco)
    cmd_sair = SairCommando(banco)

    app = MenuApp()
    app.registrar('1', cmd_listar)
    app.registrar('2', cmd_assistir)
    app.registrar('3', cmd_sair)

    app.rodar()


# Classes concretas ->
# Envoker ->

banco = DatabaseReceiver()