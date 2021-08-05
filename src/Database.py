import sqlite3
from src.Singleton import Singleton

class DataBase(Singleton):
    def __init__(self) -> None:
        self.connection = sqlite3.connect("test.db")
        self.cursor = self.connection.cursor()
    
    def __del__(self):
        self.cursor.close()
        self.connection.commit()
        self.connection.close()

    def query(self, command):
        return self.cursor.execute(command)