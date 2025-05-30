# db/dbcontext.py
import mysql.connector
from mysql.connector import MySQLConnection
from typing import Optional

def get_connection() -> Optional[MySQLConnection]:
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='admin123',
            database='sakila'
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None
