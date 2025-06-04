import mysql.connector
from mysql.connector import Error, errorcode

import os
from dotenv import load_dotenv

load_dotenv()
DB_NAME = os.getenv("DB_NAME")

DB_CONFIG = {
    'host': os.getenv("DB_HOST"),
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'port': os.getenv("DB_PORT"),
    'raise_on_warnings': True,
}
TABLES = {}
SEEDS = {}


TABLES['carreras'] = (
    "CREATE TABLE `carreras` ("
    "  `id` int NOT NULL AUTO_INCREMENT,"
    "  `nombre` varchar(50) NOT NULL,"
    " duracion int NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") "
)
TABLES['materias'] = (
    "CREATE TABLE `materias` ("
    "  `id` int NOT NULL AUTO_INCREMENT,"
    "  `nombre` varchar(150) NOT NULL,"
    "  `carrera_id` int NOT NULL,"
    "  PRIMARY KEY (`id`),"
    " FOREIGN KEY (`carrera_id`) references carreras(id)"
    ") "
)
TABLES['estudiantes'] = (
    "CREATE TABLE `estudiantes` ("
    "  `id` int NOT NULL AUTO_INCREMENT,"
    "  `nombre_y_apellido` varchar(150) NOT NULL,"
    "  `carrera_id` int NOT NULL,"
    "  PRIMARY KEY (`id`),"
    " FOREIGN KEY (`carrera_id`) references carreras(id)"
    ") "
)

TABLES["estudiantes_estudiantes"] = (
    "CREATE TABLE `estudiantes_materias` ("
    "id int NOT NULL AUTO_INCREMENT Primary Key,"
    "  `materia_id` int NOT NULL,"
    "  `estudiante_id` int NOT NULL,"
    " foreign key (`materia_id`) references materias(id),"
    " foreign key (`estudiante_id`) references estudiantes(id)"
    ") "
)


SEEDS['carreras'] = (
    "INSERT INTO carreras (nombre, duracion) "
    "VALUES (%s, %s)",
    [
        ('Ingeniería en Sistemas', 5),
        ('Licenciatura en Matemática', 4),
        ('Abogacía', 5)
    ])

SEEDS['materias'] = (
    "INSERT INTO materias (nombre, carrera_id) "
    "VALUES (%s, %s)",
    [
        ('Algoritmos y Estructuras de Datos', 1),
        ('Bases de Datos', 1),
        ('Álgebra Lineal', 2),
        ('Derecho Penal I', 3),
        ('Cálculo I', 2),
        ('Derecho Constitucional', 3)
    ])
SEEDS['estudiantes'] = (
    "INSERT INTO estudiantes (nombre_y_apellido, carrera_id ) "
    "VALUES (%s, %s)",
    [
        ('Edmundo Rivero', 1),
        ('Hugo del Carril', 1),
        ('Soledad Silveyra', 2),
        ('Alejandro Dolina', 2),
        ('Francisco Ibañez Menta', 3),
        ('Anibal Troilo', 2)
    ])

SEEDS['estudiantes_materias'] = (
    "INSERT INTO estudiantes_materias (estudiante_id, materia_id) "
    "VALUES (%s, %s)",
    [
        (1, 1),
        (1, 2),
        (2, 3),
        (2, 4),
        (3, 5),
        (3, 6)
    ])

def create_database(cursor):

    try:
        cursor.execute(
            f"CREATE DATABASE {DB_NAME} DEFAULT CHARACTER SET 'utf8'", )
    except Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database already exists")
        else:
            print(err)
    else:
        print(f"Database {DB_NAME} created successfully.")


def create_tables(tables, cursor):

    for table_name in tables:
        table_description = tables[table_name]
        try:
            print(f"Creating table {table_name}: ", end="")
            cursor.execute(table_description)
        except Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")


def seeds_tables(seed, cursor):
    for table_name in seed:
        seed_description = seed[table_name]
        try:
            print(f"Seeding table {table_name}: ", end="")
            cursor.executemany(seed_description[0], seed_description[1])
        except Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")


cxn = mysql.connector.connect(**DB_CONFIG)
cursor = cxn.cursor()
create_database(cursor)
CONF_DB = DB_CONFIG.copy()
CONF_DB['database'] = DB_NAME
cxn = mysql.connector.connect(**CONF_DB)
cursor = cxn.cursor()
create_tables(TABLES, cursor)
seeds_tables(SEEDS, cursor)
cxn.commit()
cursor.close()
cxn.close()
