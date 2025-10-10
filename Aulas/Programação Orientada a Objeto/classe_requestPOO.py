import requests #REQUISIÇÃO
from abc import ABC, abstractmethod #CONTRATO
import datetime #HORA SISTEMA

#Interfaces - Classes Abstratas
class IVerificador(ABC):

    @abstractmethod
    def verificar(self) -> bool: 
        pass

class IAlerta(ABC):

    @abstractmethod
    def enviar_alerta(self, mensagem: str):
        pass

# Classes Concretas
class VerificadorAPI(IVerificador):
    def __init__(self, URL: str):
        self.__URL = URL
    
    def verificar(self) -> bool:
        try: 
            response = requests.get(self.__URL, timeout=5)
            if response.status_code == 200:
                print(f'--> STATUS: OK [200]')
                return True
        except requests.exceptions.RequestException as e:
            print(f'--> ERRO DE CONEXÃO: {e}')
            return False

class AlertaSlack(IAlerta):
    def __init__(self, webhook_URL: str):
        self.__webhook_URL = webhook_URL

    def enviar_alerta(self, mensagem: str):

        payload = {"text:" f'ALERTAURGENTE \n{mensagem}'}

        try:
            print('[ALERTA] Enviando para o slack')
            requests.post(self.__webhook_URL, json=payload, timeout=5).raise_for_status()
            print(f'Alerta enviado com sucesso!')
        except requests.exceptions.RequestException as e:
            print(f'[ERRO] - Alerta não enviado: {e}')

class AlertaEmail(IAlerta):
    def __init__(self, destinatario: str):
        self._destinatario = destinatario
    
    def enviar_alerta(self, mensagem: str):
        print(f'[ALERTA] - Gerando e-mail para: {self._destinatario}')

class Monitor:
    def __init__(self, verificador: IVerificador, alerta: IAlerta):
        self.__verificador = verificador
        self._alerta = alerta

    def rodar_ciclo(self):
        print('--- INICIANDO NOVO CICLO --- ')
        if not self.__verificador.verificar():
            self._alerta.enviar_alerta('Serviço offline')
        else:
            print('--- SERVIÇO FUNCIONANDO ---')

URL_WEBHOOK = 'https://webhook.site/851778c3-b39a-4503-a9c9-fd6b89e192d0'
URL_REAL = 'https://ufpa.br/'
URL_FAKE = 'https://urlfake.com/'


alerta_para_slack = AlertaSlack(URL_WEBHOOK)
alerta_para_email = AlertaEmail('daironromano@gmail.com')

verificador_ok = VerificadorAPI(URL=URL_REAL)
verificador_not_ok = VerificadorAPI(URL=URL_FAKE)

# SERVIÇO FUNCIONANDO
monitor_principal = Monitor(verificador_ok, alerta_para_email)
monitor_principal.rodar_ciclo()

# SERVIÇO FALHA
monitor_secundario = Monitor(verificador_not_ok, alerta_para_email)
monitor_secundario.rodar_ciclo()