
from fastapi import APIRouter
from typing import Text
from uuid import uuid4
from models.scriptModel import Script
from config.db import collection
from models.scriptModel import DescriptionScript
from datetime import datetime
from fastapi import Query
from bson import ObjectId


#instancia de FastApi
router = APIRouter()


global_Identifier = 0
#POST --- CREATE SCRIPT    
@router.post("/createScript")
async def create_Script(post:DescriptionScript):
    #agregar un identificador para cada elemento 
    global global_Identifier
    global_Identifier += 1
    script_data = {
        "identifier": "Sc-0" + str(global_Identifier),
        "name": post.name,
        "script":[{
            "updateDate":str( datetime.now()),
            "description":post.script
            }],
        "creationDate":str( datetime.now())
    }
    result = collection.insert_one(script_data )
    if result.inserted_id:
        return {"message": "Script creado exitosamente"}
    else:
        return {"message": "Script no se pudo crear"}
    


#GET --- READ ALL SCRIPT    
@router.get("/")
async def getAllScript():
    dataScripts = list(collection.find()) #excluir _id automatico de mongo 
    for docs in dataScripts:
        docs["_id"] = str(docs["_id"])
    return dataScripts



@router.delete("/updateScript/{id}")
async def delete_Script(id:str):
    id = ObjectId(id)
    result = collection.delete_one({"_id": id})
    if result.deleted_count == 1:
        return {"message": "Script eliminado exitosamente"}
    else:
        return {"message": "Script no encontrado o no se pudo eliminar"}
    
