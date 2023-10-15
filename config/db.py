from pymongo import MongoClient


# Configurar la conexión a MongoDB
connection = MongoClient("mongodb://database:27017/") # conectar a la base de datos
#Crear base de dato 
db = connection["DB_Scripts"]
#Crear coleccion 
collection = db["Scripts"]

#database