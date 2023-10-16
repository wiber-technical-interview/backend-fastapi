from pymongo import MongoClient

mongo_url = "mongodb://mongo:H5b6fm7cY0a4uQhSgmKN@containers-us-west-117.railway.app:6652"
 
# Configurar la conexión a MongoDB
connection = MongoClient(mongo_url)#"mongodb://database:27017/" # conectar a la base de datos
#Crear base de dato 
db = connection["DB_Scripts"]
#Crear coleccion 
collection = db["Scripts"]

#database

