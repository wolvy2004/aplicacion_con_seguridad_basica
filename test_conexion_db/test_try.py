import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()
print("Archivo .env cargado")

DB_NAME = os.getenv("DB_NAME")
config = {
    'host': os.getenv("DB_HOST"),
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'port': int(os.getenv("DB_PORT")),
}

print("Intentando conectar con los siguientes datos:")
print(config)
try:
    cxn = mysql.connector.connect(**config)
    print("Conexión establecida correctamente.")
except mysql.connector.Error as err:
    print("Ocurrió un error al intentar conectar:")
    print(err)
    import traceback
    traceback.print_exc()
    exit(1)
