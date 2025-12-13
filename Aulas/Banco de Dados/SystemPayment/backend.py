from abc import ABC, abstractmethod
import sqlite3
from typing import Dict, Any

# Strategy Pattern (lógica de negócio)
class PagamentoStrategy(ABC):
    @abstractmethod
    def calcular(self, valor_bruto: float) -> float:
        pass

class PixStrategy(PagamentoStrategy):
    def calcular(self, valor_bruto: float) -> float:
        return valor_bruto * 0.90 #aplica 10% de descontro

class CartaoStrategy(PagamentoStrategy):
    def calcular(self, valor_bruto: float) -> float:
        return valor_bruto * 1.05 # aplica 5% de juros
# Database Services (código para sqlite)
class PedidoService: 
    def __init__(self, db_name='ecomerce_db'):
        self.db_name = db_name

    def get_connection(self):
        conn = sqlite3.connect(self.db_name)
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn
    
    def buscar_valor_pedido(self, pedido_id: int ) -> float:
        conn = self.get_connection()
        cursor = conn.cursor()
        
        sql = "SELECT valor_produto FROM pedidos WHERE id = ? AND status = 'PENDENTE'"
        cursor.execute(sql, (pedido_id,))
        resultado = cursor.fetchone()

        cursor.close()
        conn.close()

        if resultado:
            return float(resultado[0])
        return None

    def processar_pagamento_db(self, pedido_id: int, metodo: str, valor_final: float):
        conn = self.get_connection()
        cursor = conn.cursor()

        try:
            # Registrar pagamento
            sql_insert = 'INSERT INTO pagamentos(pedido_id, metodo, valor_final) VALUES(?, ?, ?)'
            cursor.execute(sql_insert, (pedido_id, metodo, valor_final))
            # Atualizar status do pedido
            sql_update = 'UPDATE pedidos SET status = "PAGO" WHERE id = ?'
            cursor.execute(sql_update, (pedido_id))
            # Realizar commit no banco de dados
            conn.commit()
            print('[DB] Transação realizada com sucesso!')
        except Exception as e:
            conn.rollback()
            print(f'[DB] erro de transação: {e}')
        finally:
            cursor.close()
            conn.close()

# Controller (orquestrador)

class CheckoutController:
    def __init__(self):
        self.strategies = {
            "PIX": PixStrategy(),
            "CARTAO": CartaoStrategy()
            }
        self.services = PedidoService()

    def handler_request(self, request: Dict[str, Any]):
        # Resgatar o produto e o método no DB - Processar requisição
            #Valor esperado: request: {'pedido': x, 'metodo': y}
        pedido_id = request.get('pedido_id')
        metodo = request.get('metodo')
        print(f'------------- PROCESSANDO PEDIDO #{pedido_id}  -------------')
        # Validar dados
        valor_bruto = self.services.buscar_valor_pedido(pedido_id)
        if valor_bruto is None:
            return {"status": 404, "error": 'Pedido não encontrado ou já pago'}
        # Estratégia de pagamento

        if metodo not in self.strategies:
            return {'status': 404, 'error': "metodo de pagamento inválid"}

        strategy = self.strategies[metodo]
        valor_final = strategy.calcular(valor_bruto)

        print(f'Valor original: R$ {valor_bruto:.2f}')
        print(f'Valor Final: R$ {valor_final:.2f}')
        # Garantir a persistencia
        self.services.processar_pagamento_db(pedido_id, metodo, valor_final)
        return {"status": 200, "msg": "Pagamento aprovado!"}
    
#Simulação

if __name__ == "__main__":

    controller = CheckoutController()
    # Cenário 1: Pagamento do pedido 1 com PIX
    req1 = {"pedido_id": 1, "metodo": "PIX"}
    print(controller.handler_request(req1))
    # Cenário 2: Pagamento do pedido 2 com CARTÃO
    req2 = {"pedido_id": 2, "metodo": "CARTAO"}
    print(controller.handler_request(req2))
    # Cenário 3: Pagamento do pedido 1 com PIX: Tem que falhar
    req3 = {"pedido_id": 1, "metodo": "PIX"}
    print(controller.handler_request(req3))