# Biblioteca Personal - MongoDB y PyMongo

## Descripción

Este proyecto consiste en una aplicación de consola para administrar una biblioteca personal utilizando Python y MongoDB.

La aplicación permite registrar libros y realizar diferentes operaciones sobre ellos utilizando documentos de MongoDB.

## Funciones principales

La aplicación permite:

1. Agregar libros.
2. Actualizar información de libros.
3. Eliminar libros.
4. Mostrar todos los libros.
5. Buscar libros por título, autor o género.
6. Salir del programa.

## Tecnologías utilizadas

- Python 3
- MongoDB
- PyMongo
- MongoDB Compass
- Visual Studio Code

## Estructura del proyecto

```text
biblioteca-mongodb/
│
├── app.py
├── crud.py
├── database.py
├── requirements.txt
└── README.md

Instalación de MongoDB
Para ejecutar este proyecto se necesita tener MongoDB instalado en el equipo.
Se utilizó MongoDB Community Server de forma local.
También se puede utilizar MongoDB Atlas modificando la cadena de conexión del archivo database.py.
Después de instalar MongoDB, se puede comprobar la conexión utilizando MongoDB Compass.
La conexión local utilizada en este proyecto es:
mongodb://localhost:27017

Instalación de PyMongo
Desde la terminal, dentro de la carpeta del proyecto, ejecutar:
pip install -r requirements.txt

También se puede instalar directamente con:
pip install pymongo

Configuración de la base de datos
El archivo database.py contiene la conexión con MongoDB:
from pymongo import MongoClientclient = MongoClient("mongodb://localhost:27017")db = client["biblioteca"]libros = db["libros"]


La base de datos utilizada es:
biblioteca

Y la colección utilizada es:
libros

Estructura de los documentos
Cada libro se almacena como un documento BSON en MongoDB.
Ejemplo:
{
    "id": 1,
    "titulo": "El Principito",
    "autor": "Antoine de Saint-Exupéry",
    "genero": "Novela",
    "estado": "Pendiente"
}

MongoDB también agrega automáticamente un campo _id para identificar cada documento.
Estados de lectura
Los estados disponibles son:
- Pendiente
- Leyendo
- Terminado


Ejecución del programa
Desde la terminal de VS Code ejecutar:
python app.py

Aparecerá un menú como el siguiente:
===== BIBLIOTECA PERSONAL =====
1. Agregar libro
2. Actualizar libro
3. Eliminar libro
4. Mostrar todos los libros
5. Buscar libro
6. Salir

Búsqueda
La búsqueda permite encontrar libros utilizando:
- Título
- Autor
- Género
Por ejemplo, si se busca:
Principito

la aplicación mostrará los libros que coincidan con ese texto.
La búsqueda no distingue entre mayúsculas y minúsculas.
Manejo de errores
El programa utiliza bloques try/except para manejar errores relacionados con la conexión y las operaciones de MongoDB.
También valida los datos ingresados por el usuario y verifica que:
- El título no esté vacío.
- El autor no esté vacío.
- El género no esté vacío.
- El estado sea válido.
- El ID utilizado para actualizar o eliminar exista.
¿Qué es MongoDB?
MongoDB es una base de datos NoSQL orientada a documentos.
A diferencia de una base de datos relacional, MongoDB no organiza la información principalmente en tablas y filas.
MongoDB almacena la información en documentos BSON, que tienen una estructura similar a JSON.
En este proyecto, cada libro representa un documento dentro de la colección libros.
¿Qué es PyMongo?
PyMongo es el controlador oficial de Python para trabajar con MongoDB.
Permite realizar operaciones como:
- insert_one() para insertar documentos.
- find() para consultar documentos.
- update_one() para actualizar documentos.
- delete_one() para eliminar documentos.
Diferencia con la versión anterior
En la versión anterior del proyecto se utilizó MariaDB junto con SQLAlchemy ORM.
En esta versión se reemplazó la base de datos relacional por MongoDB y se utiliza PyMongo para trabajar directamente con documentos.
Esto permite que la aplicación trabaje con una estructura NoSQL basada en documentos.



