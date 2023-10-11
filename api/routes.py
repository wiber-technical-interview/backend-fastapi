
from fastapi import APIRouter
from typing import Text
from uuid import uuid4
from models.scriptModel import Script
from config.db import collection
#instancia de FastApi
router = APIRouter()


global_Identifier = 0
#POST --- CREATE SCRIPT    
@router.post("/createScript")
async def create_Script(post:Script):
    post.id = str(uuid4()) # agregar id unico 
    #agregar un identificador para cada elemento 
    global global_Identifier
    global_Identifier += 1
    script_data = {
        "id": post.id,
        "identifier": "Sc-0" + str(global_Identifier),
        "name": post.name,
        "script": post.script,
        "updateDate":post.updateDate,
        "creationDate":post.creationDate
    }
    collection.insert_one(script_data )
    return {"message": "Script created successfully"}






#GET --- READ ALL SCRIPT    
@router.get("/")
async def getAllScript():
    dataScripts = list(collection.find({}, {"_id": 0})) #excluir _id automatico de mongo 
    return dataScripts
