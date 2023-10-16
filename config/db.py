from pymongo import MongoClient

mongo_url = "mongodb://mongo:ix8JghczLKvF6e0ZNtpl@containers-us-west-94.railway.app:6437"
 
# Configurar la conexión a MongoDB
connection = MongoClient(mongo_url)#"mongodb://database:27017/" # conectar a la base de datos
#Crear base de dato 
db = connection["DB_Scripts"]
#Crear coleccion 
collection = db["Scripts"]

#database

