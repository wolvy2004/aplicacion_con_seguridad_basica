import mysql.connector
from mysql.connector import Error

try:
    print("Intentando conectar...")
    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="password",
        port=3306,
        connect_timeout=5
    )
    if connection.is_connected():
        print("✅ ¡Conectado con éxito!")
        connection.close()
    else:
        print("❌ No se pudo conectar.")
except Error as e:
    print("❗ Error de conexión:", e)
