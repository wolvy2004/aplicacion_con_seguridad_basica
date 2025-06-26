import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()
database_name = os.getenv("DB_NAME")

database_config = {
    'host': os.getenv("DB_HOST"),
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'port': os.getenv("DB_PORT"),
    'raise_on_warnings': True,
    "database": database_name
}

DROPPED_TB = {}
DROPPED_TB[" Auto Increment = 1 estudiantes_materias"] ="ALTER TABLE estudiantes_materias AUTO_INCREMENT = 1;";
DROPPED_TB[" Auto Increment = 1 estudiantes"] ="ALTER TABLE estudiantes AUTO_INCREMENT = 1;";
DROPPED_TB[" Auto Increment = 1 materias"] ="ALTER TABLE materias AUTO_INCREMENT = 1;";
DROPPED_TB[" Auto Increment = 1 carreras"] ="ALTER TABLE carreras AUTO_INCREMENT = 1;";
DROPPED_TB["estudiantes_materias"] = "DROP TABLE IF EXISTS estudiantes_materias;"
DROPPED_TB["materias"] = "DROP TABLE IF EXISTS materias;"
DROPPED_TB["estudiantes"] = "DROP TABLE IF EXISTS estudiantes;"
DROPPED_TB["carreras"] = "DROP TABLE IF EXISTS carreras;"



def rollback_db():
    cxn = mysql.connector.connect(**database_config)
    cursor = cxn.cursor()
    for table in DROPPED_TB:
        print(f"Dropped table: {table}", end=" ")
        try:
            cursor.execute(DROPPED_TB[table])
            print('ok')
            cxn.commit()
        except Error as e:
            print(f"{e}")
    
    cursor.close()
    cxn.close()

rollback_db()
