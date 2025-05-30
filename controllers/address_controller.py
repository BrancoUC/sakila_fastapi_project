import mysql.connector
from mysql.connector import Error
from db.dbcontext import get_connection
from entities.address import Address
from typing import List, Optional


class AddressController:
    def __init__(self):
        try:
            self.connection = get_connection()
        except Error as e:
            print("Error al conectar a la base de datos:", e)
            raise

    def list_addresses(self) -> List[Address]:
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM address")
            rows = cursor.fetchall()
            return [Address(**row) for row in rows]
        except Error as e:
            print("Error al listar direcciones:", e)
            raise
        finally:
            cursor.close()

    def get_address(self, address_id: int) -> Optional[Address]:
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM address WHERE address_id = %s", (address_id,))
            row = cursor.fetchone()
            return Address(**row) if row else None
        except Error as e:
            print("Error al obtener dirección:", e)
            raise
        finally:
            cursor.close()

    def add_address(self, data: dict):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                """
                INSERT INTO address (address, address2, district, city_id, postal_code, phone, last_update)
                VALUES (%s, %s, %s, %s, %s, %s, NOW())
                """,
                (
                    data['address'],
                    data.get('address2'),
                    data['district'],
                    data['city_id'],
                    data.get('postal_code'),
                    data['phone']
                )
            )
            self.connection.commit()
        except Error as e:
            print("Error al agregar dirección:", e)
            raise
        finally:
            cursor.close()

    def modify_address(self, address_id: int, data: dict):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                """
                UPDATE address
                SET address = %s, address2 = %s, district = %s,
                    city_id = %s, postal_code = %s, phone = %s, last_update = NOW()
                WHERE address_id = %s
                """,
                (
                    data['address'],
                    data.get('address2'),
                    data['district'],
                    data['city_id'],
                    data.get('postal_code'),
                    data['phone'],
                    address_id
                )
            )
            self.connection.commit()
        except Error as e:
            print("Error al modificar dirección:", e)
            raise
        finally:
            cursor.close()

    def remove_address(self, address_id: int):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM address WHERE address_id = %s", (address_id,))
            self.connection.commit()
        except Error as e:
            print("Error al eliminar dirección:", e)
            raise
        finally:
            cursor.close()

    def close(self):
        if self.connection.is_connected():
            self.connection.close()
