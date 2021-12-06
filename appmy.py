from DataBase.DBase_content import DBContext
from fastapi import FastAPI, Request
import datetime

app = FastAPI(title="Comon everybody !")
db = DBContext()

#Ищем в базе токен с указанным номером (очень точно)
@app.get("/findtoken")
async def get_find_token(sn: str):
    returnlst = db.find_token(sn)
    return returnlst

# Добавляем запись в БД
##jrn (sn, type_device, id_adm)
@app.post("/addrec")
async def post_add_rec(sn, type_device, id_adm: str, request: Request):
    client_ip = request.client.host
    date_reg = datetime.datetime.now()
    addList = [sn, date_reg, type_device, id_adm]
    db.add_rec(addList)
    return {'Logs added to the database'}


