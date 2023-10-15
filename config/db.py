from pymongo import MongoClient

mongo_url = "mongodb://mongo:eGGE5a+G2FhD3dbHg2Eg1CCg3EC36DEH@mongodb.railway.internal:27017"


# Configurar la conexión a MongoDB
connection = MongoClient(mongo_url)#"mongodb://database:27017/" # conectar a la base de datos
#Crear base de dato 
db = connection["DB_Scripts"]
#Crear coleccion 
collection = db["Scripts"]

#database

