import mysql.connector
from mysql.connector import Error
from db.dbcontext import get_connection
from entities.staff import Staff, StaffCreate
from datetime import datetime

class StaffController:
    def __init__(self):
        try:
            self.connection = get_connection()
        except Error as e:
            print("Error al conectar a la base de datos:", e)
            raise

    def list_staff(self):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM staff")
            rows = cursor.fetchall()
            cursor.close()
            return [Staff(**row) for row in rows]
        except Error as e:
            print(f"Error listing staff: {e}")
            return []

    def get_staff(self, staff_id: int):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM staff WHERE staff_id = %s", (staff_id,))
            row = cursor.fetchone()
            cursor.close()
            return Staff(**row) if row else None
        except Error as e:
            print(f"Error retrieving staff: {e}")
            return None

    def add_staff(self, data: dict):
        try:
            cursor = self.connection.cursor()
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute(
                """
                INSERT INTO staff (first_name, last_name, address_id, email, store_id, active, username, password, last_update)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    data["first_name"],
                    data["last_name"],
                    data["address_id"],
                    data.get("email"),
                    data["store_id"],
                    data["active"],
                    data["username"],
                    data["password"],
                    now
                )
            )
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error adding staff: {e}")
            return False

    def modify_staff(self, staff_id: int, data: dict):
        try:
            cursor = self.connection.cursor()
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute(
                """
                UPDATE staff SET first_name = %s, last_name = %s, address_id = %s, email = %s,
                store_id = %s, active = %s, username = %s, password = %s, last_update = %s
                WHERE staff_id = %s
                """,
                (
                    data["first_name"],
                    data["last_name"],
                    data["address_id"],
                    data.get("email"),
                    data["store_id"],
                    data["active"],
                    data["username"],
                    data["password"],
                    now,
                    staff_id
                )
            )
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error modifying staff: {e}")
            return False

    def remove_staff(self, staff_id: int):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM staff WHERE staff_id = %s", (staff_id,))
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error deleting staff: {e}")
            return False
