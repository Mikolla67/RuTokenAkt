import sqlite3
from DataBase.DbData import *

class DBContext:

    def __init__(self):
        self.conn = sqlite3.connect(PATH)
        self.cursor = self.conn.cursor()
        self.cursor.executescript(SQL_CREATE_DB)
        self.conn.commit()

    def find_token(self, sn_string):
        result_query = self.cursor.execute(SQL_FIND_TOKEN, [sn_string]).fetchall()
        return (result_query)
