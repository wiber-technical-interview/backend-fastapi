
from fastapi import APIRouter
from typing import Text
from uuid import uuid4
from models.scriptModel import PostScript

#instancia de FastApi
router = APIRouter()


global_Identifier = 0
#POST --- CREATE SCRIPT    
postScript=[]
@router.post("/createScript")
async def create_Script(post:PostScript):
    post.id = str(uuid4()) #agregar id unico 
    #agregar un identificador para cada elemento 
    global global_Identifier
    global_Identifier += 1
    post.identifier = "Sc-00" + str(global_Identifier)
    postScript.append(post.model_dump()) # convertir a Json 
    return {"message": "Script created successfully"}


#GET --- READ ALL SCRIPT    
@router.get("/")
async def allScript():
    print(postScript)
    return postScript
