import sqlite3
from Singleton import Singleton

class DataBase(Singleton):
    def __init__(self) -> None:
        if not self.sourceFile:
            self.sourceFile = "default"

        self.connection = sqlite3.connect(self.sourceFile+".db")
        self.cursor = self.connection.cursor()

    @classmethod
    def setSourceFile(cls, file):
        self.sourceFile = file

    def __del__(self):
        self.cursor.close()
        self.connection.commit()
        self.connection.close()

    def query(self, command):
        return self.cursor.execute(command)
