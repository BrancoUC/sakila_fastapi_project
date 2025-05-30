import mysql.connector
from mysql.connector import Error
from db.dbcontext import get_connection
from entities.rental import Rental, RentalCreate
from datetime import datetime

class RentalController:
    def __init__(self):
        try:
            self.connection = get_connection()
        except Error as e:
            print("Error al conectar a la base de datos:", e)
            raise

    def list_rentals(self):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM rental")
            rows = cursor.fetchall()
            cursor.close()
            return [Rental(**row) for row in rows]
        except Error as e:
            print(f"Error listing rentals: {e}")
            return []

    def get_rental(self, rental_id: int):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM rental WHERE rental_id = %s", (rental_id,))
            row = cursor.fetchone()
            cursor.close()
            return Rental(**row) if row else None
        except Error as e:
            print(f"Error retrieving rental: {e}")
            return None

    def add_rental(self, data: dict):
        try:
            cursor = self.connection.cursor()
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute(
                """
                INSERT INTO rental (rental_date, inventory_id, customer_id, return_date, staff_id, last_update)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (
                    data["rental_date"],
                    data["inventory_id"],
                    data["customer_id"],
                    data.get("return_date"),
                    data["staff_id"],
                    now
                )
            )
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error adding rental: {e}")
            return False

    def modify_rental(self, rental_id: int, data: dict):
        try:
            cursor = self.connection.cursor()
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute(
                """
                UPDATE rental
                SET rental_date = %s, inventory_id = %s, customer_id = %s,
                    return_date = %s, staff_id = %s, last_update = %s
                WHERE rental_id = %s
                """,
                (
                    data["rental_date"],
                    data["inventory_id"],
                    data["customer_id"],
                    data.get("return_date"),
                    data["staff_id"],
                    now,
                    rental_id
                )
            )
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error modifying rental: {e}")
            return False

    def remove_rental(self, rental_id: int):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM rental WHERE rental_id = %s", (rental_id,))
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error deleting rental: {e}")
            return False
