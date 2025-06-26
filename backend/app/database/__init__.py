import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()


class Connect:

    @staticmethod
    def get_connect():
        try:
            cxn = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                database=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                port=os.getenv("DB_PORT"),
                raise_on_warnings=True,
                charset='utf8mb4'
            )
            return cxn
        except Error as e:
            print(f'error as happend {e}')
        finally:
            print('The try except is finished')

    def  read(sql: str, params: tuple = None):
        cxn = Connect.get_connect()
        with cxn.cursor(dictionary=True) as cursor:
            try:
                cursor.execute(sql, params)
                result = cursor.fetchall()
                return result if result else None
            except Error as e:
                print(f'Error {e}')
            finally:
                cxn.close()

    @staticmethod
    def write(sql: str, params: tuple):
        cxn = Connect.get_connect()
        with cxn.cursor() as cursor:
            try:
                cursor.execute(sql, params)
                cxn.commit()
                if cursor.lastrowid:
                    return cursor.lastrowid
                count = cursor.rowcount
                return True if count > 0 else False
            except Error as e:
                print(f'Something went wrong {e}')
            finally:
                cxn.close()
