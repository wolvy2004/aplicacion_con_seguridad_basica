import socket
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

print("Cargando variables de entorno...")
load_dotenv()

DB_CONFIG = {
    'host': os.getenv("DB_HOST"),
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'port': int(os.getenv("DB_PORT")),
}

print("Configuración leída del entorno:")
print(DB_CONFIG)

try:
    print("Intentando conectar...")
    cxn = mysql.connector.connect(**DB_CONFIG)
    print("✅ Conectado correctamente")
    cxn.close()
except Error as e:
    print("❌ Error al conectar:")
    print(e)
except Exception as e:
    print("❌ Excepción general:")
    print(e)


host = "localhost"
port = 3306

print(f"Probando conexión TCP a {host}:{port}...")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.settimeout(3)  # timeout de 3 segundos
    result = sock.connect_ex((host, port))

    if result == 0:
        print("✅ El puerto está abierto y accesible.")
    else:
        print(f"❌ No se puede conectar al puerto {port}. Código: {result}")
