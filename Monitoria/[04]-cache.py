import functools
import time

_cache_simples = {} # [chave]: valor

# decorador manual
def cachear (func_original):
    @functools.wraps(func_original)
    def wrapper(*args, **kwargs):
        chave_cache = (func_original.__name__, args, tuple(sorted(kwargs.items())))

        if chave_cache in _cache_simples:
            print(f'Cache HIT para {chave_cache}')
            return _cache_simples[chave_cache]
        else:
            print(f'Cache MISS para {chave_cache}')
            resultado = func_original(*args, **kwargs)
            _cache_simples[chave_cache] = resultado
            return resultado
    return wrapper

@cachear
def consulta_db(query: str):
    print(f'Executando consulta no DB: {query}')
    time.sleep(2)
    return f'Resultado para {query}'

# Simulações 
consulta_1 = consulta_db("SELECT * from usuarios")
print(consulta_1)

consulta_2 = consulta_db("SELECT * from usuarios")
print(consulta_2)