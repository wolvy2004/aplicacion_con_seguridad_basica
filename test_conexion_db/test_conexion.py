import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

print("===== Diagnóstico de Conexión a MySQL =====")

# 1. Cargar .env y mostrar las variables
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

print(f"Host: {DB_HOST}")
print(f"User: {DB_USER}")
print(f"Password: {'*' * len(DB_PASSWORD) if DB_PASSWORD else None}")
print(f"Port: {DB_PORT}")
print(f"Database: {DB_NAME}")
print()

# 2. Probar conexión
try:
    config = {
        'host': DB_HOST,
        'user': DB_USER,
        'password': DB_PASSWORD,
        'port': int(DB_PORT),
        'raise_on_warnings': True,
        'connection_timeout': 5,
    }
    print("Intentando conectar con los siguientes datos:")
    print(config)
    connection = mysql.connector.connect(**config)
    print("✅ Conexión exitosa.")
    connection.close()
except Error as err:
    print("❌ Falló la conexión.")
    print("Tipo de error:", type(err))
    print("Mensaje:", err)
except Exception as ex:
    print("⚠️ Error inesperado:", type(ex), ex)

# 3. Verificación de la librería
try:
    import mysql.connector
    print("\n📦 Librería mysql.connector importada correctamente.")
except ImportError as ie:
    print("\n❌ Error al importar mysql.connector:", ie)
