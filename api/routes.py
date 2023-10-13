
from fastapi import APIRouter
from typing import Text
from uuid import uuid4
from models.scriptModel import Script
from config.db import collection
from models.scriptModel import DescriptionScript
from datetime import datetime
from fastapi import Query
from bson import ObjectId
from fastapi import HTTPException
from models.scriptModel import UpdateScript


#instancia de FastApi
router = APIRouter()


#POST --- CREATE SCRIPT    
@router.post("/createScript")
def create_Script(post: DescriptionScript):
    try:
        script_data = {
            "name": post.name,
            "script": [{
                "updateDate": str(datetime.now().strftime("%d-%m-%Y")),
                "description": post.script
            }],
            "creationDate": str(datetime.now().strftime("%d-%m-%Y"))
        }
        result = collection.insert_one(script_data)
    
        if result.inserted_id is not None:
            return {"message": "Script creado exitosamente"}
        else:
            return {"error": "Script no se pudo crear"}
    except Exception as error:
        return {"error": "Error en el servidor"}



#GET --- READ ALL SCRIPT    
@router.get("/")
def get_all_script():
    try:
        dataScripts = list(collection.find())  # Excluir _id automático de MongoDB
        for docs in dataScripts:
            docs["_id"] = str(docs["_id"])
        return dataScripts
    except Exception as e:
        return {"error": "Error en el servidor"}




#GET --- READ Script by ID   
@router.get("/updateScript/{id}")
def get_script_by_id(id:str):
    object_id = ObjectId(id)
    dataScript = (collection.find_one({"_id": object_id})) #excluir _id automatico de mongo 
    dataScript["_id"] = str(dataScript["_id"])
    return dataScript






@router.put("/updateScript/{id}")
def update_script(id: str, put: UpdateScript):
    try:
        object_id_update = ObjectId(id)
        update_data = {
            "updateDate": str(datetime.now().strftime("%d-%m-%Y")),
            "description": put.description
        }
        result = collection.update_one({"_id": object_id_update}, {"$push": {"script": update_data}})
        if result.modified_count == 1:
            return {"message": "Script actualizado exitosamente"}
        else:
            return {"error": "Script no se pudo actualizar"}
    except Exception as e:
        return {"error": "Error en el servidor"}
    


#Delete ---  delete script by ID 
@router.delete("/updateScript/{id}")
def delete_script(id: str):
    try:
        object_id = ObjectId(id)
        result = collection.delete_one({"_id": object_id})
        if result.deleted_count == 1:
            return {"message": "Script eliminado exitosamente"}
        else:
            return {"error": "Script no se pudo eliminar exitosamente"}
    except Exception as error:
        return {"error": "Error en el servidor"}
