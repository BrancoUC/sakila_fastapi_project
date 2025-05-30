import mysql.connector
from mysql.connector import Error
from db.dbcontext import get_connection
from entities.city import City
from typing import List, Optional

class CityController:
    def __init__(self):
        try:
            self.connection = get_connection()
        except Error as e:
            print("Error al conectar a la base de datos:", e)
            raise

    def list_cities(self) -> List[City]:
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT city_id, city, country_id, last_update FROM city")
            rows = cursor.fetchall()
            return [City(**row) for row in rows]
        except Error as e:
            print("Error al listar ciudades:", e)
            raise
        finally:
            cursor.close()

    def get_city(self, city_id: int) -> Optional[City]:
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT city_id, city, country_id, last_update FROM city WHERE city_id = %s", (city_id,))
            row = cursor.fetchone()
            return City(**row) if row else None
        except Error as e:
            print("Error al obtener ciudad:", e)
            raise
        finally:
            cursor.close()

    def add_city(self, data: dict):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO city (city, country_id, last_update) VALUES (%s, %s, NOW())",
                (data['city'], data['country_id'])
            )
            self.connection.commit()
        except Error as e:
            print("Error al agregar ciudad:", e)
            raise
        finally:
            cursor.close()

    def modify_city(self, city_id: int, data: dict):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "UPDATE city SET city = %s, country_id = %s, last_update = NOW() WHERE city_id = %s",
                (data['city'], data['country_id'], city_id)
            )
            self.connection.commit()
        except Error as e:
            print("Error al modificar ciudad:", e)
            raise
        finally:
            cursor.close()

    def remove_city(self, city_id: int):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM city WHERE city_id = %s", (city_id,))
            self.connection.commit()
        except Error as e:
            print("Error al eliminar ciudad:", e)
            raise
        finally:
            cursor.close()

    def close(self):
        if self.connection.is_connected():
            self.connection.close()
