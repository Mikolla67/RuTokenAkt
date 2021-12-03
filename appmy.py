from DataBase.DBase_content import DBContext
from fastapi import FastAPI

app = FastAPI(title="Ну что, ёпта?!")
db = DBContext()

@app.get("/findtoken")
async def get_find_token(substring: str):
#Ищем в базе токен с указанным номером
    returnlst = db.FIND_TOKEN(substring)
    return returnlst