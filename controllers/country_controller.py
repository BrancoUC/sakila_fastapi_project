import mysql.connector
from mysql.connector import Error
from db.dbcontext import get_connection
from entities.country import Country
from typing import List, Optional


class CountryController:
    def __init__(self):
        try:
            self.connection = get_connection()
        except Error as e:
            print("Error al conectar a la base de datos:", e)
            raise

    def list_countries(self) -> List[Country]:
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT country_id, country, last_update FROM country")
            rows = cursor.fetchall()
            return [Country(**row) for row in rows]
        except Error as e:
            print("Error al listar países:", e)
            raise
        finally:
            cursor.close()

    def get_country(self, country_id: int) -> Optional[Country]:
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT country_id, country, last_update FROM country WHERE country_id = %s", (country_id,))
            row = cursor.fetchone()
            return Country(**row) if row else None
        except Error as e:
            print("Error al obtener país:", e)
            raise
        finally:
            cursor.close()

    def add_country(self, data: dict):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO country (country, last_update) VALUES (%s, NOW())",
                (data['country'],)
            )
            self.connection.commit()
        except Error as e:
            print("Error al agregar país:", e)
            raise
        finally:
            cursor.close()

    def modify_country(self, country_id: int, data: dict):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "UPDATE country SET country = %s, last_update = NOW() WHERE country_id = %s",
                (data['country'], country_id)
            )
            self.connection.commit()
        except Error as e:
            print("Error al modificar país:", e)
            raise
        finally:
            cursor.close()

    def remove_country(self, country_id: int):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM country WHERE country_id = %s", (country_id,))
            self.connection.commit()
        except Error as e:
            print("Error al eliminar país:", e)
            raise
        finally:
            cursor.close()

    def close(self):
        if self.connection.is_connected():
            self.connection.close()
