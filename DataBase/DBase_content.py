import sqlite3
from DataBase.DbData import *

class DBContext:

    def __init__(self):
        self.conn = sqlite3.connect(PATH)
        self.cursor = self.conn.cursor()
        self.cursor.executescript(SQL_CREATE_DB)
        self.conn.commit()

    def find_token(self, sn):
        id = self.cursor.execute(SQL_FIND_TOKEN, [sn]).fetchone()
        if id is None:
            result_query = ['Нет такого токена, надо писать !']
        else:
            result_query = ['А уже есть такой номер - ',sn]
#            result_query = self.cursor.execute(SQL_FIND_TOKEN_ALL, id).fetchall()
        return result_query

    def add_rec(self, addList):
        self.cursor.execute(SQL_INSERT_REC, addList)
        self.conn.commit()
