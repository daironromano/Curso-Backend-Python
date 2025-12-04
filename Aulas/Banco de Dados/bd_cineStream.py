import mysql.connector
from abc import ABC, abstractmethod

class DatabaseReceiver: # Receiver
    def __init__(self):
        self.config = {
            'host':'localhost',
            'user': 'root',
            'password': 'root',
            'database': 'cinestream_db',

        }

# Classes concretas ->
# Envoker ->

banco = DatabaseReceiver()