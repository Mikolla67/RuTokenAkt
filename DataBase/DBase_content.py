import sqlite3
from DataBase.DbData import *

class DBContext:

    def __init__(self):
        self.conn = sqlite3.connect(PATH)
        self.cursor = self.conn.cursor()
        self.cursor.executescript(SQL_CREATE_DB)
        self.conn.commit()

    def FIND_TOKEN(self, ser_num):
        result_query = self.cursor.execute(SQL_Find_Token, ser_num)
        return (result_query)
