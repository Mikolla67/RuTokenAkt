from DataBase.DBase_content import DBContext
from fastapi import FastAPI

app = FastAPI(title="Ну что, ёпта?!")
db = DBContext()