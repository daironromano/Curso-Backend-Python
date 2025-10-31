import time
import requests

def dec_medir_tempo(funcao_original_decorada):
    def wrapper():
        inicio = time.time() # TEMPO INICIO
        r = funcao_original_decorada()
        final = time.time() # TEMPO FINAL
        duracao = final - inicio
        print(f'Tempo de duração: {duracao}')
        return r
    return wrapper

@dec_medir_tempo
def buscar_API():
    url = 'https://webhook.site/77dfbd8d-0874-46e9-8d89-5688dcecac26'
    print('Realizando GET')
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status() # ERRO: 400
        return response.json
    except requests.exceptions.RequestException:
        print('--- [ERRO AO BUSCAR DADOS] --- ')
        return None
    
buscar_API()