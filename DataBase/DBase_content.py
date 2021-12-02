import sqlite3
from DataBase.DbData import *

class DBContext:

    def __init__(self):
        self.conn = sqlite3.connect(PATH)
        self.cursor = self.conn.cursor()
        self.cursor.executescript(CREATE_DB)
#        self.conn.commit()