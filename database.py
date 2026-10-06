from pymongo import MongoClient

# Conexión con MongoDB local
client = MongoClient("mongodb://localhost:27017")

# Base de datos
db = client["biblioteca"]

# Colección de libros
libros = db["libros"]

# Comprobar conexión
try:
    client.admin.command("ping")
    print("Conexión con MongoDB exitosa.")
except Exception as e:
    print(f"Error de conexión con MongoDB: {e}")