import functools
import time
from dataclasses import dataclass
import requests
from requests.exceptions import RequestException
from typing import Dict, Any, Callable

@dataclass(frozen=True)
class ApiUser:
    id: int
    name_user: str
    email: str
    city: str

    @classmethod
    def from_json(cls, data: Dict[str, Any]) -> 'ApiUser':
        """Trata os dados de JSON recebido para instanciar corretamente a classe"""
        try:
            return cls(
                id=data['id'],
                name_user=data['username'],
                email=data['email'],
                city=data['address']['city']
            )
        except (KeyError, TypeError) as e:
            raise ValueError(f'Formato de JSON inesperado: {e}')

def retry_on_fail(tries: int, delay_sec: int) -> Callable:
    def decorador(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for _ in range(tries):
                try:
                    return func(*args, **kwargs)
                except RequestException as e:
                    last_exception = e
                    print(f"[RETRY] Falha da chamada {e.__class__.__name__}, tentando novamente...")
                    time.sleep(delay_sec)
            raise last_exception
        return wrapper
    return decorador

@functools.cache
@retry_on_fail(tries=3, delay_sec=2)
def fetch_user_by_id(user_id: int) -> ApiUser:
    """Busca de um usuário na API externa"""
    print(f'[API] Buscando dados na rede para ID {user_id}')
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}'

    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return ApiUser.from_json(response.json())

# Estrutura de execução de código
if __name__ == "__main__":
    start = time.perf_counter()
    user = fetch_user_by_id(1)
    print(user)
    print(f'Tempo: {time.perf_counter() - start:.2f}')

